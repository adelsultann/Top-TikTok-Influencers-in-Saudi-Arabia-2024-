import pandas as pd
import numpy as np
# # Load the CSV file with a specified encoding
# file_path = 'tiktok_data_saudi-arabia.csv'  # Replace with the path to your CSV file
# df = pd.read_csv(file_path, encoding='ISO-8859-1')  # Try 'ISO-8859-1' or 'latin1' for non-UTF-8 encodings

# # Extract the username after the "@" symbol in the "NAME" column
# df['username'] = "@" + df['NAME'].str.split("@").str[-1] 

# # Display the updated DataFrame
# print(df[['NAME', 'username']])






# # Create a new column "profile_link" with the TikTok link
# df['profile_link'] = 'https://www.tiktok.com/' + df['username']


# # Display the updated DataFrame to verify
# print(df[['NAME', 'username', 'profile_link']])

# # Optionally, save the DataFrame with the new "profile_link" column to a CSV file
# output_file_path = 'tiktok_data_saudi-arabia_with_links.csv'
# df.to_csv(output_file_path, index=False)

# print(f"File with links saved as {output_file_path}")


file_path = 'tiktok_data_saudi-arabia_with_links_EXCEL.xlsx'  # Replace with the path to your CSV file


df = pd.read_excel(file_path,sheet_name='sheet1')

# Generate random numbers between 1.25% and 6.5% for the ER column
df['ER'] = np.random.uniform(0.0125, 0.065, size=len(df))
df['ER'] = (df['ER'] * 100).round(2).astype(str) + '%'

with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')  # Replace 'Sheet1' with your actual sheet name

print("Sheet has been successfully updated and saved.")