# weather_app.py
import random
import json

WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Windy', 'Stormy']
DATA_FILE = 'weather_data.json'

def generate_weather(city):
    """Generates random weather data for a given city."""
    temperature = random.randint(-10, 40)
    condition = random.choice(WEATHER_CONDITIONS)
    return {
        'city': city,
        'temperature': temperature,
        'condition': condition
    }

def save_weather_data(data):
    """Saves weather data to a JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def load_weather_data():
    """Loads weather data from a JSON file."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_city_weather():
    """Adds a new city's weather data."""
    city = input("Enter the city name: ")
    data = load_weather_data()
    weather = generate_weather(city)
    data.append(weather)
    save_weather_data(data)
    print(f"Weather data for {city} added successfully.")

def list_all_weather():
    """Lists weather data for all cities."""
    data = load_weather_data()
    if not data:
        print("No weather data available.")
        return
    for item in data:
        print(f"City: {item['city']}, Temperature: {item['temperature']}°C, Condition: {item['condition']}")

def update_weather():
    """Updates the weather data for a specific city."""
    city = input("Enter the city name to update: ")
    data = load_weather_data()
    for item in data:
        if item['city'].lower() == city.lower():
            updated_weather = generate_weather(city)
            item.update(updated_weather)
            save_weather_data(data)
            print(f"Weather data for {city} updated successfully.")
            return
    print(f"No data found for city: {city}")

def main():
    while True:
        print("\nWeather Application")
        print("1. Add City Weather")
        print("2. List All Weather")
        print("3. Update Weather")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_city_weather()
        elif choice == '2':
            list_all_weather()
        elif choice == '3':
            update_weather()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()