# 🔍 InsightScope

## Introduction
InsightScope is an AI-based solution designed to effectively represent knowledge and generate insights from structured datasets. In the era of big data, organizations produce massive amounts of structured data daily. This data holds valuable insights that can significantly improve decision-making processes if processed and analyzed correctly. InsightScope addresses this challenge by providing a comprehensive platform that preprocesses data, visualizes key patterns, and generates meaningful insights, making the data easy to understand and actionable.

## Dataset Description
InsightScope focuses on structured datasets, which are collections of data organized into rows and columns with well-defined features. These datasets typically include numerical, categorical, and text data, making them suitable for various analytical tasks. The project is designed to be versatile, allowing users to upload any structured dataset in CSV format, which is then processed and analyzed to uncover hidden patterns and insights.

## Data Preprocessing
Data preprocessing is a crucial step in transforming raw data into a format suitable for analysis. The following preprocessing techniques are applied in InsightScope:

- 🧹 **Handling Missing Values**: Columns with missing or null values are either filled with the mean/mode or dropped if the missing values exceed a certain threshold.
- 🛠️ **Data Cleaning**: Column names are stripped of whitespace and replaced with underscores for consistency.
- 🧮 **Data Imputation**: Missing numerical data is imputed using the mean, while categorical data is filled with the most frequent value.
- 🔄 **Encoding**: Categorical data is encoded using either One-Hot Encoding or Label Encoding, depending on the user's choice.
- 📏 **Data Scaling**: Numerical data is scaled using StandardScaler or MinMaxScaler, based on the selected method.
- ❌ **Low Variance Filter**: Columns with variance below a certain threshold are removed to reduce noise in the data.

## Methodology
InsightScope uses a combination of statistical analysis, machine learning, and data visualization techniques to uncover patterns and generate insights.

### Data Visualization
- 📊 **Correlation Heatmaps**: To visualize the relationships between numerical features in the dataset.
- 📈 **Distribution Plots**: To display the distribution of values for each column, helping to identify skewness and outliers.
- 🌐 **PCA Plots**: Principal Component Analysis (PCA) is used to reduce the dimensionality of the dataset and visualize it in 2D and 3D space, revealing the underlying structure of the data.

### Insight Generation
The insight generation process leverages the Groq API to create human-readable insights from the processed data. The platform uses a pre-trained model (e.g., LLaMA) to summarize the statistical properties of the dataset and provide key insights that are relevant to decision-making.

## Results
InsightScope provides users with a comprehensive view of their data through various visualizations and insights:

- 🔍 **Correlation Heatmaps**: Reveals the strength and direction of relationships between numerical features.
- 📉 **Distribution Plots**: Helps in understanding the spread and central tendency of the data.
- 🌐 **PCA Plots**: Offers a simplified view of the data, making it easier to identify clusters and trends.
- 📝 **Generated Insights**: Provides key takeaways from the data, summarizing the most important aspects that can aid in decision-making.

## Tech Stack Used
<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python" width="100" height="40"/>
  <img src="https://pandas.pydata.org/static/img/pandas_white.svg" alt="Pandas" width="100" height="40"/>
  <img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" alt="Scikit-learn" width="120" height="40"/>
  <img src="https://matplotlib.org/_static/images/logo2.svg" alt="Matplotlib" width="100" height="40"/>
  <img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="100" height="40"/>
  <img src="https://images.plot.ly/logo/new-branding/plotly-logomark.png" alt="Plotly" width="100" height="40"/>
  <img src="https://groq.com/wp-content/uploads/2024/08/groq-logo-1-2.png" alt="Groq" width="100" height="40"/>
  <img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" alt="Streamlit" width="100" height="40"/>
</p>

## Libraries Used
- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `plotly`
- `groq`
- `os`
- `glob2`
- `uuid`
- `time`
- `streamlit`

## How to Run the Project Locally

### 1. Setup a Virtual Environment
To isolate project dependencies, it's recommended to use a virtual environment.

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows
.\env\Scripts\activate

# On macOS/Linux
source env/bin/activate

```

### 2. Install the dependencies
After setting up the virtual environment, install the required libraries using the requirements.txt file.

```bash
# Install the dependencies
pip install -r requirements.txt
```
### 3. Update the .streamlit/secrets.toml File
Make sure to update your .streamlit/secrets.toml file with the required GROQ_API_KEY to enable insight generation.

```bash
# Update the .streamlit/secrets.toml File
GROQ_API_KEY=your_api_key_here
```

### 4. Run the Streamlit App
Finally, run the Streamlit application using the following command:

```bash
# Run streamlit file
python -m streamlit run streamlit_app.py
```

## Conclusion
InsightScope is a powerful tool for analyzing structured datasets, offering a user-friendly interface that simplifies the process of data preprocessing, visualization, and insight generation. By integrating advanced AI and machine learning techniques, the platform helps users unlock the full potential of their data, making informed decisions based on actionable insights.
