import requests

def get_name_country_probability(name, country_id):
    url = f"https://api.nationalize.io?name={name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        countries_data = data.get('country', [])
        
        # Check if the specified country is in the predicted nationalities
        for country in countries_data:
            if country['country_id'] == country_id.upper():
                return True, country['probability'], countries_data
        
        # If the specified country was not found, return False but with the data found
        return False, 0, countries_data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None, None, None

# Get user input for the name and country
name = input("Enter a name: ")
country_id = input("Enter a country ID (e.g., US for United States): ")

found, probability, countries_data = get_name_country_probability(name, country_id)
if found is not None:
    if found:
        print(f"The name {name} is likely from {country_id.upper()} with a probability of {probability:.2f}.")
    else:
        print(f"The name {name} does not seem to be from {country_id.upper()}. Here are the results I found:")
        for country in countries_data:
            print(f"- Country ID: {country['country_id']}, Probability: {country['probability']:.2f}")
else:
    print("There was an error processing the request.")
