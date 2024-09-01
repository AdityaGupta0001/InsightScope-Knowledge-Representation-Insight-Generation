import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def plot_correlation_heatmap(data):
    try:
        plt.figure(figsize=(16, 9))
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        return plt.gcf()
    except Exception as e:
        return None

def plot_distributions(data):
    try:
        distribution_figs = []
        for column in data.select_dtypes(include=['float64', 'int64']).columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(data[column], kde=True)
            plt.title(f'Distribution of {column}')
            plt.tight_layout()
            fig = plt.gcf()
            distribution_figs.append((column, fig))
            plt.close()
        return distribution_figs
    except Exception as e:
        return None

def plot_pca(data):
    try:
        pca = PCA(n_components=2)
        scaled_data = StandardScaler().fit_transform(data.select_dtypes(include=['float64', 'int64']))
        pca_result = pca.fit_transform(scaled_data)
        pca_df = pd.DataFrame(data=pca_result, columns=['PCA1', 'PCA2'])
        
        fig = px.scatter(pca_df, x='PCA1', y='PCA2', title='PCA of Numerical Features')
        return fig
    except Exception as e:
        return None
    
def plot_pca_3d(data):
    try:
        if data.select_dtypes(include=['float64', 'int64']).shape[1] > 2:
            pca_3d = PCA(n_components=3).fit_transform(StandardScaler().fit_transform(data.select_dtypes(include=['float64', 'int64'])))
            pca_3d_df = pd.DataFrame(data=pca_3d, columns=['PCA1', 'PCA2', 'PCA3'])
            
            fig = px.scatter_3d(pca_3d_df, x='PCA1', y='PCA2', z='PCA3', title='3D PCA Scatter Plot')
            return fig
    except Exception as e:
        return None

def load_and_prepare_data(file_path):
    data = pd.read_csv(file_path)
    
    data.columns = data.columns.str.strip().str.replace(' ', '_')

    for column in data.columns:
        if data[column].dtype == 'object':  # Categorical data
            data[column].fillna(data[column].mode()[0], inplace=True)
        else:  # Numerical data
            data[column].fillna(data[column].mean(), inplace=True)

    # One-hot encode categorical data
    data = pd.get_dummies(data, drop_first=True)

    # Normalize numerical columns
    scaler = StandardScaler()
    data[data.select_dtypes(include=['float64', 'int64']).columns] = scaler.fit_transform(data.select_dtypes(include=['float64', 'int64']))

    return data
