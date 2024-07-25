import pandas as pd
from pymongo import MongoClient

# Read the CSV file
file_path = "World Energy Consumption.csv"  # Replace with the actual file path
df = pd.read_csv(file_path)

df = df.iloc[1:]

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["kaggle"]
collection = db["world_energy_consumption"]

data = df.to_dict(orient="records")

collection.insert_many(data)

print(f"Data from {file_path} has been successfully inserted into the 'world_energy_consumption' collection in MongoDB.")