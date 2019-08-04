# generates the fitted model artifact

def load_datasets(dataset_file_name, dataset_time_file_name):
    # Load and merge prepared datasets to the final dataset
    
    import pandas as pd

    # We don't need CURRENCY as a feature because FRAUDSTER is not identified by CURRENCY
    df = pd.read_csv(dataset_file_name)
    df_time = pd.read_csv(dataset_time_file_name)

    # Let's create dummy columns for categorical variables
    df = pd.get_dummies(df, columns=['ENTRY_METHOD','TYPE','SOURCE','STATE','MERCHANT_CATEGORY','TERMS_VERSION','KYC'])
    # and collect final dataset with time-features from dataset_time
    df = df.merge(df_time, left_on="USER_ID", right_on="USER_ID")
    del df_time
    return df


def oversampling_dataset(df):
    # Do oversampling of unbalanced class
    
    import numpy as np
    # split dataset to features and predicted value
    X, y = df.drop('IS_FRAUDSTER',axis=1), df['IS_FRAUDSTER']

    # balancing classes
    classes_count = y.value_counts()
    max_class_count = classes_count.max()

    X_over = X.copy()
    y_over = y.copy()

    for cls in zip(classes_count,classes_count.index):
        if cls[0] != max_class_count:
            idx = np.random.choice(y[y==cls[1]].index,size = max_class_count-cls[0])
            X_add = X.iloc[idx]
            y_add = y.iloc[idx]
            X_over = X_over.append(X_add)
            y_over = y_over.append(y_add)

    del X,y
    return X_over, y_over


def train_and_save_model(X_over, y_over, model_file_name, test_users_file_name, N_FOLDS, RANDOM_STATE):
    # Train and save model to the file
    
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split, KFold
    
    # split to train and test datasets
    X_train_over,X_test_over,y_train_over,_ = train_test_split(X_over,y_over,test_size=.2, random_state=RANDOM_STATE)

    # store user_id of untrained users to check model
    users_to_check = list(set(X_test_over['USER_ID'].values).difference(set(X_train_over['USER_ID'].values)))
    X_train_over.drop('USER_ID', axis=1, inplace=True)
    # train simple randomforest with KFold
    rf = RandomForestClassifier(n_jobs=-1,random_state=RANDOM_STATE)
    rf.fit(X_train_over,y_train_over)
    # store list of features to the model parameter
    rf.feature_names = list(X_train_over.columns.values)
    
    # save model to artifact
    from sklearn.externals import joblib
    joblib.dump(rf, model_file_name)
    # save list of untrained users to check the model
    joblib.dump(users_to_check, test_users_file_name)
    del rf


if __name__ == "__main__":
    # load datasets from files
    df = load_datasets(dataset_file_name = '../data/dataset.csv', dataset_time_file_name = '../data/dataset_time.csv')
    # oversampling fraudsters' class for better performance
    X_over, y_over = oversampling_dataset(df)
    # train and save model to the file
    train_and_save_model(X_over, y_over, model_file_name = '../artifacts/model.pkl', test_users_file_name = '../data/test_users.pkl', N_FOLDS = 3, RANDOM_STATE = 7)    