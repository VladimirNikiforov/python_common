# create features and store them in the DB

import psycopg2 as pg
import yaml
from pathlib import Path
import os
import pandas as pd
from datetime import datetime
import dateutil


def prepare_user_features(users_file_name):
    user_df = pd.read_csv(users_file_name)
    # There are NaN in TERMS_VERSION - fill it by "Undefined" version
    user_df['TERMS_VERSION'] = user_df['TERMS_VERSION'].fillna("Undefined")
    user_df.drop('STATE', axis=1, inplace=True)
    # Create AGE variable as age on CREATED_DATE date of profile in system
    user_df['AGE'] = user_df.apply(lambda x: datetime.strptime(x['CREATED_DATE'], '%Y-%m-%d %H:%M:%S.%f').year-x['BIRTH_YEAR'], axis=1)
    # We don't need BIRTH_YEAR anymore - drop it
    user_df.drop('BIRTH_YEAR', axis=1, inplace=True)
    return user_df


def prepare_transactions_features(user_df, transactions_file_name):
    trn_df = pd.read_csv(transactions_file_name)
    df = trn_df.drop('ID', axis=1).merge(user_df, left_on="USER_ID", right_on="ID").drop(['ID'],axis=1)
    # Replace NaN to 'Undefined' in MERCHANT_CATEGORY and MERCHANT_COUNTRY
    df = df.fillna('Undefined')
    # Create AGE variable as age on CREATED_DATE date of profile in system
    df['PROFILE_AGE'] = df.apply(lambda x: (datetime.strptime(x['CREATED_DATE_x']+('000' if '.' in x['CREATED_DATE_x'] else '.000000'), '%Y-%m-%d %H:%M:%S.%f')-datetime.strptime(x['CREATED_DATE_y'], '%Y-%m-%d %H:%M:%S.%f')).days, axis=1)
    df['CREATED_DATE_x'] = df['CREATED_DATE_x'].apply(lambda x: (datetime.strptime(x+('000' if '.' in x else '.000000'), '%Y-%m-%d %H:%M:%S.%f').strftime("%Y-%m-%d %H:%M:%S")))
    # No needs of CREATED_DATE_y anymore, drop them
    df.drop(['CREATED_DATE_y'], axis=1, inplace=True)
    # Transform boolean variable IS_FRAUDSTER to binary
    df['IS_FRAUDSTER'] = df['IS_FRAUDSTER'].astype(int)
    return df
    
    
def prepare_country_features(df, countries_file_name):
    cntr_df = pd.read_csv(countries_file_name)
    df['COUNTRY'] = df['COUNTRY'].map({c[0]: c[1] for c in cntr_df[['CODE','CODE3']].values})
    # Trying to replace country code to CODE3
    df['MERCHANT_COUNTRY'] = df['MERCHANT_COUNTRY'].apply(lambda x: (cntr_df[cntr_df['NUMCODE']==int(x)]['CODE3'].values[0] if len(cntr_df[cntr_df['NUMCODE']==int(x)]['CODE3'].values)>0 else x) if x.isdigit() else x)
    # Trying to replace country code to CODE3
    # Add "C" to the missing countries
    df['MERCHANT_COUNTRY'] = df['MERCHANT_COUNTRY'].apply(lambda x: (cntr_df[cntr_df['PHONECODE']==int(x)]['CODE3'].values[0] if len(cntr_df[cntr_df['PHONECODE']==int(x)]['CODE3'].values)>0 else 'C'+x) if x.isdigit() else x)
    # Fill NaN to Undefined and create binary variable HOMELAND to identify than transaction is made in country of user
    df['COUNTRY'] = df['COUNTRY'].fillna('Undefined')
    df['HOMELAND'] = df.apply(lambda x: 1 if x['COUNTRY'].upper() == x['MERCHANT_COUNTRY'].upper() else 0, axis=1)
    return df


def prepare_time_features(df, dataset_time_file_name):
    # Functions to calculate day and hour of transactions of users
    def transaction_by_day_count(dataset):
        dataset['DAY_OF_TRANSACTION'] = dataset['CREATED_DATE_x'].apply(
            lambda x: int((datetime.strptime(x, '%Y-%m-%d %H:%M:%S')).strftime('%w'))
        ) 
        tmp_df = dataset.groupby(
            ['USER_ID','DAY_OF_TRANSACTION']
        )['DAY_OF_TRANSACTION'].size().unstack().fillna(0).reset_index()
        old_columns = [
            old_col for old_col in tmp_df.columns.tolist()
            if old_col in dataset['DAY_OF_TRANSACTION'].unique()
        ]
        tmp_df.rename(
            columns={old_col: 'DAY_' + str(old_col) for old_col in old_columns},
            inplace=True
        )
        return tmp_df

    def transaction_by_hour_count(dataset):
        dataset['HOUR_OF_TRANSACTION'] = dataset['CREATED_DATE_x'].apply(
            lambda x: int((datetime.strptime(x, '%Y-%m-%d %H:%M:%S')).strftime('%H'))
        ) 
        tmp_df = dataset.groupby(
            ['USER_ID','HOUR_OF_TRANSACTION']
        )['HOUR_OF_TRANSACTION'].size().unstack().fillna(0).reset_index()
        old_columns = [
            old_col for old_col in tmp_df.columns.tolist()
            if old_col in dataset['HOUR_OF_TRANSACTION'].unique()
        ]
        tmp_df.rename(
            columns={old_col: 'H_' + str(old_col) for old_col in old_columns},
            inplace=True
        )
        return tmp_df

    transaction_by_day = transaction_by_day_count(df)
    transaction_by_day = transaction_by_day.set_index('USER_ID')

    transaction_by_hour = transaction_by_hour_count(df)
    transaction_by_hour = transaction_by_hour.set_index('USER_ID')

    # Join datasets
    df_time = pd.merge(
        transaction_by_day,
        transaction_by_hour,
        left_index=True,
        right_index=True,)

    df_time = df_time.reset_index()
    # we will store time-features separetely from main dataset to minimize space on disk and database
    df_time.to_csv(dataset_time_file_name)
    return df


def prepare_currency_features(df, currencies_file_name):
    cur_df = pd.read_csv(currencies_file_name)
    df = pd.merge(df, cur_df, left_on="CURRENCY", right_on="CCY")
    df['IS_CRYPTO'] = df['IS_CRYPTO'].astype(int)
    df['AMOUNT'] = df['AMOUNT'] * 10**df['EXPONENT']
    return df


def collect_all_features(df, dataset_file_name):
    cols_to_select = ['USER_ID', 'AMOUNT',
           'STATE', 'MERCHANT_CATEGORY', 'ENTRY_METHOD', 'TYPE', 'SOURCE', 'HAS_EMAIL', 
           'IS_FRAUDSTER', 'TERMS_VERSION', 'KYC', 'FAILED_SIGN_IN_ATTEMPTS', 'AGE', 'PROFILE_AGE', 'HOMELAND',
           'DAY_OF_TRANSACTION', 'HOUR_OF_TRANSACTION', 'IS_CRYPTO']
    df = df[cols_to_select]
    df.to_csv(dataset_file_name)
    

def create_tables(config, connection):
    cur = connection.cursor()
    for table in config:
        name = table.get('name')
        schema = table.get('schema')
        ddl = f"""CREATE TABLE IF NOT EXISTS {name} ({schema})"""
        cur.execute(ddl)
    connection.commit()
    cur.close()

    
def transform_tables(config, data_path = "../data/"):
    for table in config:
        table_name = table.get('name')
        table_source = os.path.join(data_path,f"{table_name}.csv")
        table_cols = []
        for i in table.get('columns'):
            table_cols.append(str.upper(i))
        df = pd.read_csv(table_source)
        df_reorder = df[table_cols]  # rearrange column here
        df_reorder.to_csv(table_source, index=False)

        
def load_tables(config, connection, data_path = "../data/"):
    # iterate and load
    cur = connection.cursor()
    for table in config:
        table_name = table.get('name')
        table_source = os.path.join(data_path,f"{table_name}.csv")
        with open(table_source, 'r') as f:
            next(f)
            cur.copy_expert(f"COPY {table_name} FROM STDIN CSV NULL AS ''", f)
        connection.commit()
    cur.close()

    
def store_features_to_db(yaml_file, host, port, dbname, user):
    # open connection
    connection = pg.connect(
        host = host,
        port = port,
        dbname = dbname,
        user = user
    )
    # open config file and store files to the DB
    with open(yaml_file) as schema_file:
        config = yaml.load(schema_file)
    create_tables(config, connection)
    transform_tables(config)
    load_tables(config, connection)
    # close connection
    connection.close()

    
if __name__ == "__main__":
    user_df = prepare_user_features(users_file_name = '../data/users.csv')
    df = prepare_transactions_features(user_df, transactions_file_name = '../data/transactions.csv')
    df = prepare_country_features(df, countries_file_name = '../data/countries.csv')
    df = prepare_time_features(df, dataset_time_file_name = '../data/dataset_time.csv')
    df = prepare_currency_features(df, currencies_file_name = '../data/currency_details.csv')
    df = collect_all_features(df, dataset_file_name = '../data/dataset.csv')

    store_features_to_db(yaml_file = "../misc/schemas_features.yaml",
                         host='localhost',
                         port=54320,
                         dbname='ht_db',
                         user='postgres')