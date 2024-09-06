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
    if not city.strip():
        print("City name cannot be empty.")
        return
    data = load_weather_data()
    weather = generate_weather(city)
    data.append(weather)
    save_weather_data(data)
    print(f"Weather data for {city} added successfully.")

def list_all_weather():
    """Lists all stored weather data."""
    data = load_weather_data()
    if not data:
        print("No weather data available.")
        return
    print("\nStored Weather Data:")
    for index, weather in enumerate(data, start=1):
        print(f"{index}. {weather['city']} - {weather['temperature']}°C - {weather['condition']}")

def update_weather():
    """Updates weather data for an existing city."""
    data = load_weather_data()
    if not data:
        print("No weather data available to update.")
        return
    list_all_weather()
    try:
        index = int(input("Enter the number of the city to update: ")) - 1
        if index < 0 or index >= len(data):
            print("Invalid city number.")
            return
        updated_weather = generate_weather(data[index]['city'])
        data[index] = updated_weather
        save_weather_data(data)
        print(f"Weather data for {data[index]['city']} updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

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
