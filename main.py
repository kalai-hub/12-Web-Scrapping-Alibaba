from AlibabaData import AlibabaData
import pandas as pd

# Getting necessary details from Alibaba site
alibaba_data = AlibabaData()

data = alibaba_data.get_data()
name = data[0]
price = data[1]
min_qty = data[2]
link = data[3]

# Creating dictionary with product lists
product_dict = {"Product Name": name, "Product Price": price, "Order Quantity": min_qty, "URL": link}

# Converting dictionary to CSV
df = pd.DataFrame(product_dict)
df.to_csv("Product_Details.csv")