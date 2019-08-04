# Load and identify users by pretrained model

def get_user_data(user_id, model_features, cat_features):
    # Load data from DB for specific user_id, split cat_features to dummies and fill absented categorical features' values by zeros to create complete dataset with model_features
    import numpy as np
    import pandas as pd
    import psycopg2
    # Create connection to DB
    connection = psycopg2.connect(
        host='localhost',
        port=54320,
        dbname='ht_db',
        user='postgres',
    )
    # open cursor
    c = connection.cursor()
    # load dataset for specific user_id
    c.execute(f"SELECT * FROM dataset t1, dataset_time t2 where t1.USER_ID = t2.USER_ID and t1.USER_ID = '{user_id}';")
    # get all rows from opened cursor
    result = c.fetchall()
    # check that we have one or more rows
    assert len(result) > 0, f"We don't have data for user_id={user_id}!"
    # get column' names from cursor to create dataframe
    colnames = [desc[0].upper() for desc in c.description]
    # close cursor
    c.close()
    # create dataframe
    result = pd.DataFrame(result, columns = colnames)
    # split categorical features from dataset to dummies
    result = pd.get_dummies(result, columns = cat_features)
    # absented fields with categorical features' values fill with zeros and concat with loaded dataset to create complete dataset with model_features
    result = pd.concat([result,pd.DataFrame(0, index=np.arange(len(result)), columns=[x for x in model_features if x not in result.columns])], axis = 1)[model_features]
    # Close connection to DB
    connection.close()
    return result

def check_alert(y_predicted):
    # Return the most important (heaviest by weight) flag as a result
    '''
    Rules:
        If percent is more than first level (50% for example) we need ALERT (weight=1) because it's suspicious transaction.
        If percent is more than second level (75% for example) we need LOCK and ALERT (weight=2) because it's very suspicious transaction and it's better to lock user and send alert signal to work with this user.
        If percent is more than max level (90% for example) we need LOCK (weight=3) because it's fraudster.
    '''
    
    # dictionary of alerts
    dict_of_alerts = {0: ['PASS'],
                      1: ['ALERT_AGENT'],
                      2: ['LOCK_USER', 'ALERT_AGENT'],
                      3: ['LOCK_USER']
                     }
    # for each prediction in y_prediction check the rules, get the max weight and apply dictionary to get the alert
    return dict_of_alerts[max([{       y >= .9: 3,
                                .75 <= y <  .9: 2,
                                .5  <= y < .75: 1,
                                       y <  .5: 0}[True] for y in y_predicted])]

def load_model(model_path):
    # Load pickled model from artifact
    from sklearn.externals import joblib
    rf = joblib.load(model_path)
    return rf


def patrol(user_id):
    # Main function
    cat_features = ['ENTRY_METHOD','TYPE','SOURCE','STATE','MERCHANT_CATEGORY','TERMS_VERSION','KYC']
    
    # get list of features from the model
    try:
        col_list = rf.feature_names
    except NameError:
        # if model is not loaded yet => load our pretrained model
        rf = load_model(model_path = '../artifacts/model.pkl')
        col_list = rf.feature_names

    # load data for user_id
    X = get_user_data(user_id = user_id, model_features = col_list, cat_features = cat_features)

    # get prediction of model
    y_pred = rf.predict_proba(X)[:,1]

    # apply rules and return solution
    return check_alert(y_pred)