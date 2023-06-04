import pandas as pd
import requests
import os

# Read the Excel file from the URL
excel_url = 'https://asiliventures.com/wp-content/uploads/2023/06/Seedways-Products-to-be-Processed-test-case.xlsx'
excel_file = pd.read_excel(excel_url, sheet_name='Seedways')

# Read the file names from "Sheet 1"
file_names = pd.read_excel(excel_url, sheet_name='Sheet 1', usecols='C', nrows=184)

# Specify the folder path to save the images
folder_path = r'W:\IoT Remote Consultant\Gig 2 Work\Data Scraping & Data Entry\Images_with_Description'

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Iterate over the rows to download and save the images
for index, row in excel_file.iterrows():
    if index < 2 or index > 185:
        continue
    
    image_url = row['Photo (Weblink)']
    image_filename = file_names.iloc[index - 2, 0]

    # Download the image
    response = requests.get(image_url)
    image_path = os.path.join(folder_path, image_filename)

    # Save the image to the specified folder
    with open(image_path, 'wb') as file:
        file.write(response.content)

    print(f'Saved image: {image_filename}')

print('Image saving completed.')
