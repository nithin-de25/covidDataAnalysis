import json
from src.pipeline.extract import fetch_weather_data
from src.pipeline.transform import transform_weather_data
from src.pipeline.load import to_csv

with open("data/config/config.json") as f:
    config = json.load(f)

raw_data = fetch_weather_data(config["default_city"], config["api_key"])
clean_data = transform_weather_data(raw_data)
file = to_csv(clean_data)

print(f"Weather data saved to {file}")
