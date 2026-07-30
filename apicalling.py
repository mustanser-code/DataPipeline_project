import pandas as pd
import requests
# Now, first i have request server to give me data
# using request.get() it is HTTP module
# URL
url = 'https://dummyjson.com/products'
# print that url
print(url)
# important thing now i will add params certain data to fetch 
# from that url 
query = {'limit' : 10}
# response from the server 
# if it code_status 200 means successful
response = requests.get(url,params=query)
# Response json data stored!
json_data = response.json()
# now i wanna fetch the product inside from that json_data
product_list = json_data['products']
# now load product into pandas dataframe
df = pd.DataFrame(product_list)
print(df.info())
# now i have all the product data into 'df'
# checking the response from server 
print(response.status_code)
# print the first few line of the dataset
print(df.head())
# Save that dataset into the csv file
df.to_csv('product_data.csv',index = False)