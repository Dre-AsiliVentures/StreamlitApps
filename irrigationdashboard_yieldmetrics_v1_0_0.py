import streamlit as st
import numpy as np
import pandas as pd

# Set up the app title and sidebar options
st.set_page_config(page_title='Data Manipulation App', layout='wide')
st.sidebar.title('Options')
st.sidebar.markdown('Select your data parameters:')

# Set up the data generation parameters
num_rows = st.sidebar.slider('Number of Rows', min_value=100, max_value=1000, step=100, value=500)
num_cols = st.sidebar.slider('Number of Columns', min_value=2, max_value=10, step=1, value=5)
min_val = st.sidebar.number_input('Minimum Value', value=0)
max_val = st.sidebar.number_input('Maximum Value', value=100)
random_seed = st.sidebar.number_input('Random Seed', value=42)

# Generate the random data using NumPy
np.random.seed(random_seed)
data = np.random.randint(low=min_val, high=max_val, size=(num_rows, num_cols))

# Convert the NumPy array to a Pandas DataFrame
df = pd.DataFrame(data, columns=[f'Column {i+1}' for i in range(num_cols)])

# Set up the app layout and display the data
st.title('Data Manipulation App')
st.write(f'Generated {num_rows} rows and {num_cols} columns of data:')
st.write(df)

# Allow the user to manipulate the data using Pandas
st.markdown('---')
st.write('Data Manipulation')
col_select = st.selectbox('Select a Column to Manipulate:', df.columns)
col_data = df[col_select]
st.write('Selected Column Data:')
st.write(col_data)

col_mean = col_data.mean()
st.write(f'Mean Value: {col_mean}')

col_median = col_data.median()
st.write(f'Median Value: {col_median}')

st.write('Sorted Column Data:')
st.write(col_data.sort_values())

st.markdown('---')
st.write('Data Distribution')
st.write('Histogram of Selected Column:')
st.hist(col_data, bins=20)
