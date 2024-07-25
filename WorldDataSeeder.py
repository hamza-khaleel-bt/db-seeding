from json import load
from pymongo import MongoClient

# Read data from worldmap.json (replace with the actual file path)
file_path = "WorldData.json" 
with open(file_path, "r") as json_file:
    world_data = load(json_file)["features"]

for feature in world_data:
    if "id" in feature:
        feature["iso_code"] = feature.pop("id")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["kaggle"]  # Replace with your database name
collection = db["world_data_countries"]  # Replace with your collection name

# Insert data into the collection
collection.insert_many(world_data)

print("Data inserted successfully!")

# Close the connection
client.close()