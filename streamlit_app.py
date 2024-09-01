import streamlit as st
import pandas as pd
import time
from preprocessor import preprocess_data
import visualizer as viz
import os
import datetime
import glob2
import insight_generator
import uuid

# Generate a unique session ID for each user
data_folder = 'data'

def delete_old_folders(data_folder):
    current_time = time.time()

    for subfolder in os.listdir(data_folder):
        subfolder_path = os.path.join(data_folder, subfolder)

        if os.path.isdir(subfolder_path):
            timestamp_file = os.path.join(subfolder_path, 'session_init.txt')

            if os.path.exists(timestamp_file):
                with open(timestamp_file, 'r') as file:
                    folder_time = float(file.read().strip())

                if current_time - folder_time > 3600:
                    for root, dirs, files in os.walk(subfolder_path, topdown=False):
                        for name in files:
                            os.remove(os.path.join(root, name))
                        os.rmdir(root)
            #         # print(f"Deleted folder: {subfolder_path}")
            # else:
            #     print(f"No timestamp file found in {subfolder_path}, skipping.")

delete_old_folders(data_folder=data_folder)

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

saved_directory = f"data/{st.session_state.session_id}"
if not os.path.exists(saved_directory):
    os.makedirs(saved_directory)

last_activity_file = os.path.join(saved_directory, 'session_init.txt')
with open(last_activity_file, 'w') as f:
    f.write(str(datetime.datetime.now().timestamp()))

if "button" not in st.session_state:
    st.session_state.button = False

if "generated" not in st.session_state:
    st.session_state.generated = ""

if "regenerate" not in st.session_state:
    st.session_state.regenerate = False

if st.session_state.button == False:

    st.set_page_config(initial_sidebar_state="collapsed", layout='wide', page_title='InsightScope', page_icon=':mag:')
    st.markdown(
        """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
            .stApp {
                background: rgb(161,98,0);
                background: linear-gradient(338deg, rgba(161,98,0,1) 0%, rgba(9,9,121,1) 49%, rgba(2,2,51,1) 100%);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("InsightScope :mag:")
    st.subheader("Unlock the Power of Your Data - Discover Insights, Visualize Trends, and Make Informed Decisions.")
    st.write("Upload your CSV files to effortlessly analyze and visualize data trends. Generate insightful reports and explore your data with interactive charts, all in one place.")
    st.write(" ")
    st.write(" ")

    with st.form("my_form", clear_on_submit=True):
        upload_file = st.file_uploader("Upload a structured dataset (.csv)", accept_multiple_files=False, type=['csv'])
        submitted = st.form_submit_button("Submit", use_container_width=True, type='secondary')
        if submitted:
            if upload_file is not None:
                with st.spinner("Loading..."):
                    time.sleep(5)

                date = datetime.datetime.now()
                tim = datetime.datetime.now().ctime().split(" ")[3]
                file_path = os.path.join(saved_directory,upload_file.name[0:len(upload_file.name)-4]+f"_{int(date.timestamp())  }_"+".csv") #+f"_{date.day}-{date.month}-{date.year}_{tim}"
                with open(file_path, "wb") as f:
                    f.write(upload_file.getbuffer())

                st.success(f"File uploaded successfully")

    def generate():
        st.session_state.button = True

    st.write(" ")
    st.write(" ")
    st.button("Visualize data and generate insights", use_container_width=True, type='primary', on_click=generate)

    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: black;
            color: white;   
            text-align: center;
            padding: 10px;
        }
        
        .footer img {
            border-radius: 50%;
            width: 50px;
            height: 50px;
            margin-right: 15px;
        }

        .footer a {
            color: white;
            margin: 0 10px;
            text-decoration: none;
        }

        .footer a:hover {
            color: #0000ff; /* Optional: Add a hover effect */
        }
        </style>
        
        <div class="footer">
            <a href="https://github.com/AdityaGupta0001" target="_blank">GitHub</a>
            <a href="https://www.linkedin.com/in/aditya-gupta-475328252/" target="_blank">LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    st.set_page_config(initial_sidebar_state="collapsed", layout='wide', page_title='InsightScope', page_icon=':mag:')
    st.markdown(
        """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
            .stApp {
                background: rgb(161,98,0);
                background: linear-gradient(338deg, rgba(161,98,0,1) 0%, rgba(9,9,121,1) 49%, rgba(2,2,51,1) 100%);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    def stream_data(message):
        text = message
        for word in text.split(" "):
            for i in word:
                yield i
                time.sleep(0.005)
            yield " "
            time.sleep(0.02)

    st.title("InsightScope :mag:")
    st.subheader("Unlock the Power of Your Data - Discover Insights, Visualize Trends, and Make Informed Decisions.")
    st.write(" ")
    st.write(" ")

    data_folder_path = os.path.join("data", st.session_state.session_id)

    file_pattern = os.path.join(data_folder_path, "*.csv")
    files = glob2.glob(file_pattern)

    file_dict = {}

    for file in files:
        file_name = os.path.basename(file)
    
        try:
            name, timestamp, _ = file_name.rsplit('_', 2)
            timestamp = float(timestamp)
            file_dict[file] = timestamp
        except ValueError:
            # print(f"Skipping file with unexpected name format: {file_name}")
            pass

    if file_dict:
        most_recent_file = max(file_dict, key=file_dict.get)

        for file in files:
            if file != most_recent_file:
                os.remove(file)
                # print(f"Removed file: {file}")
        # print(f"Kept file: {most_recent_file}")
    else:
        # print("No valid files found to process.")
        pass

    data_contents = os.listdir(data_folder_path)
    if len(data_contents) == 0:
        st.error("No file uploaded")
    else:
        for item in data_contents:
            if item.endswith('.csv'):
                item_path = os.path.join(data_folder_path, item)
                df = pd.read_csv(item_path, encoding='ISO-8859-1')
                st.subheader('Preprocessed Data')
                st.dataframe(df, use_container_width=True)
                preprocess_data(item_path, threshold=0.4, scaling_method='minmax', encode_method='onehot')

                st.write("")
                st.write("")
                st.write("")
                st.write("")

                with st.form(key='insight_form'):
                    st.subheader("Dataset Insights")
                    if st.session_state.generated == "":
                        insights = insight_generator.generate_insights(item_path)
                        st.session_state.generated = insights
                        st.write_stream(stream_data(st.session_state.generated))
                    elif st.session_state.generated != "" and st.session_state.regenerate:
                        insights = insight_generator.generate_insights(item_path)
                        st.session_state.generated = insights
                        st.write_stream(stream_data(st.session_state.generated))
                        st.session_state.regenerate = False
                    else:
                        st.write(st.session_state.generated)
                    
                    def change_state():
                        st.session_state.regenerate = True
                    st.form_submit_button(label="Regenerate Insights", use_container_width=True, on_click=change_state, type='primary')

                data = viz.load_and_prepare_data(item_path)

                st.write("")
                st.write("")
                st.write("")
                st.write("")

                with st.form(key='correlation_heatmap_form'):
                    st.subheader('Correlation Heatmap')
                    try:
                        heatmap_fig = viz.plot_correlation_heatmap(data)
                        st.pyplot(heatmap_fig, use_container_width=True)
                    except:
                        st.info("Correlation Heatmap could not be generated for this dataset")
                    st.form_submit_button(label='Update Correlation Heatmap', use_container_width=True)

                st.write("")
                st.write("")
                st.write("")
                st.write("")

                st.subheader('Distributions of Numerical Features')
                for column, fig in viz.plot_distributions(data):
                    with st.form(key=f'distribution_form_{column}'):
                        st.write(f'Distribution of {column}')
                        try:
                            st.plotly_chart(fig, use_container_width=True)
                        except:
                            st.info(f"Distribution plot could not be generated for this {column} of this dataset")
                        st.form_submit_button(label=f'Update Distribution of {column}', use_container_width=True)
                        
                st.write("")
                st.write("")
                st.write("")
                st.write("")

                with st.form(key='pca_form'):
                    st.subheader('PCA')
                    try:
                        pca_fig = viz.plot_pca(data)
                        st.plotly_chart(pca_fig, use_container_width=True, theme=None)
                    except:
                        st.info("PCA Plot could not be generated for this dataset")
                    st.form_submit_button(label='Update PCA Plot', use_container_width=True)      

                st.write("")
                st.write("")
                st.write("")
                st.write("")

                with st.form(key='pca_3d_form'):
                    st.subheader('3D PCA Scatter Plot')
                    try:
                        pca_3d_fig = viz.plot_pca_3d(data)
                        if pca_3d_fig:
                            st.plotly_chart(pca_3d_fig, use_container_width=True, theme=None)
                    except:
                        st.info("PCA 3D Plot could not be generated for this dataset")
                    st.form_submit_button(label='Update 3D PCA Plot', use_container_width=True)
    
    def generate():
        st.session_state.button = False
        st.session_state.generated = ""
        st.session_state.regenerate = False
    
    st.write("")
    st.write("")
    st.write("")
    st.button("Upload Another File", use_container_width=True, type='primary', on_click=generate)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: black;
            color: white;   
            text-align: center;
            padding: 10px;
        }
        
        .footer img {
            border-radius: 50%;
            width: 50px;
            height: 50px;
            margin-right: 15px;
        }

        .footer a {
            color: white;
            margin: 0 10px;
            text-decoration: none;
        }

        .footer a:hover {
            color: #0000ff; /* Optional: Add a hover effect */
        }
        </style>
        
        <div class="footer">
            <a href="https://github.com/AdityaGupta0001" target="_blank">GitHub</a>
            <a href="https://www.linkedin.com/in/aditya-gupta-475328252/" target="_blank">LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True
    )
