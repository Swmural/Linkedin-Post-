from seleniumwire import webdriver
import time
from seleniumwire.utils import decode as sw_decode
import json
import pandas as pd

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the specified URL
driver.get('https://www.zooniverse.org/projects/brbcornell/nest-quest-go-tanagers-and-blackbirds/talk/5359')
# Sleep to allow the request to go through
time.sleep(5)

# Access and print requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        if "api/users" in request.url:
            print(request.response.body)

            # Decode the response body and convert it to JSON
            data = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
            data = data.decode("utf-8")
            json_data = json.loads(data)

            # Extract the "users" part of the JSON data
            users_data = json_data['users']

            # Convert the users_data to a pandas DataFrame
            new_df = pd.DataFrame(users_data)

            # Read the existing Excel file into a DataFrame
            file_path = "C:\\Users\\srina\\OneDrive\\Desktop\\zooniverse\\Book1.xlsx"
            existing_df = pd.read_excel(file_path)

            # Concatenate the new DataFrame with the existing one
            updated_df = pd.concat([existing_df, new_df], ignore_index=True)

            # Save the updated DataFrame to the same Excel file
            updated_df.to_excel(file_path, index=False)

# Must always be called to clean up after ourselves
driver.quit()
