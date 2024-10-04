import time

# Ask for target phone number
phone_number = input("Enter the target phone number: ")

# Show loading messages
print("Loading... Please wait")
time.sleep(2)

print("Activating Geo Tagger...")
time.sleep(3)

print("Obtaining Operator Details...")
time.sleep(10)

# Simulate operator info
print("Operator: Airtel-IN")
time.sleep(2)

# Simulate SIM holder info
print("Obtaining SIM Holder Info...")
time.sleep(5)
print("SIM Holder: Bhavesh Harish Ondhiya")
print("Source of Info: TRAI DATABASE")
time.sleep(3)

# Show final message with longitude and latitude
print("Enabling APIs and Webhooks...")
time.sleep(2)

# Default longitude and latitude values
longitude = 102.44
latitude = 17.82

print(f"Location (Longitude, Latitude): ({longitude}, {latitude})")
