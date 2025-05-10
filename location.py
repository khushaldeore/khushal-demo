import random

# Simulated mobile number location database
mock_location_data = {
    "9623985911": {"city": "New York", "state": "NY", "country": "USA"},
    "0987654321": {"city": "Los Angeles", "state": "CA", "country": "USA"},
    "5555555555": {"city": "Chicago", "state": "IL", "country": "USA"},
    # Add more simulated numbers and locations as needed
}

def get_location_for_number(phone_number):
    """
    Simulates querying a geolocation service to get the location based on a phone number.
    """
    # Look up the phone number in the mock database
    location = mock_location_data.get(phone_number)
    if location:
        return location
    else:
        raise ValueError("Location not found for the given phone number.")

# Example usage
if __name__ == "__main__":
    phone_number = input("Enter the mobile number to find location (e.g., 9623985911): ")
    
    try:
        location = get_location_for_number(phone_number)
        print(f"Location for {phone_number}:")
        print(f"City: {location['city']}")
        print(f"State: {location['state']}")
        print(f"Country: {location['country']}")
    except ValueError as e:
        print(e)
