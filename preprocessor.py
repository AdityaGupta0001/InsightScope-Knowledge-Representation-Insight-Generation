import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer

def preprocess_data(file_path, threshold=0.5, scaling_method='standard', encode_method='onehot'):
    data = pd.read_csv(file_path,encoding='ISO-8859-1')
    
    data.columns = data.columns.str.strip().str.replace(' ', '_')

    for column in data.columns:
        if data[column].dtype in ['int64', 'float64']:
            data[column] = pd.to_numeric(data[column], errors='coerce')
            imputer = SimpleImputer(strategy='mean')
            data[column] = imputer.fit_transform(data[[column]])
        else:
            # Drop columns with too many missing or null values
            missing_percentage = data[column].isnull().mean()
            if missing_percentage > threshold:
                data.drop(column, axis=1, inplace=True)
            else:
                data[column] = data[column].fillna(data[column].mode()[0])
    
    for column in data.select_dtypes(include=['object', 'category']).columns:
        if encode_method == 'onehot':
            encoded_df = pd.get_dummies(data[column], prefix=column)
            data = pd.concat([data, encoded_df], axis=1)
            data.drop(column, axis=1, inplace=True)
        elif encode_method == 'label':
            encoder = LabelEncoder()
            data[column] = encoder.fit_transform(data[column])
        else:
            raise ValueError("encode_method must be either 'onehot' or 'label'")
    
    numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
    if scaling_method == 'standard':
        scaler = StandardScaler()
    elif scaling_method == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise ValueError("scaling_method must be either 'standard' or 'minmax'")
    
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])
    
    variance_threshold = 0.01
    low_variance_cols = data.var() < variance_threshold
    data = data.drop(columns=low_variance_cols[low_variance_cols].index)
    
    data.to_csv(file_path, index=False)
    
    return data