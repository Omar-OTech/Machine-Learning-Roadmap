# Creating a dictionary to map country codes to country names
countries = {
    "US": "United States",
    "CA": "Canada",
    "GB": "United Kingdom",
}

print("Dictionary of Countries:", countries)

# Accessing values by keys
print("Country for CA:", countries["CA"])

# Adding a new key-value pair
countries['FR'] = 'France'
print("After Adding France:", countries)

# Updating a value
countries["US"] = "USA"
print("After Updating United States:", countries)

# Iterating over dictionary keys and values
print("\nIterating over dictionary:")
for code, name in countries.items():
    print(f"Country Code: {code}, Country Name: {name}")


# Checking for key existence
if "GB" in countries:
    print("GB exists in the dictionary.")