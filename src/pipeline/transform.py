def transform_weather_data(raw_data):
    """
    Transforms the raw weather data into a more usable format.

    Args:
        raw_data (dict): The raw weather data from the API.

    Returns:
        dict: Transformed weather data with relevant fields.
    """
    transformed_data = {
        "city": raw_data.get("name"),
        "temperature": raw_data["main"].get("temp"),
        "humidity": raw_data["main"].get("humidity"),
        "weather": raw_data["weather"][0].get("description"),
        "wind_speed": raw_data["wind"].get("speed"),
    }
    return transformed_data
