import time

# Step 1: Initializing NUD
print("Initializing NUD...")
time.sleep(2)

# Step 2: Ask for Service Number and Password
service_number = input("Enter your Service Number: ")
password = input("Enter your NUD password: ")

# Step 3: Display user information
print("\nVerifying credentials...")
time.sleep(2)
print("Name: Jayandra Babu Pilla")
time.sleep(1)
print("Rank: Ex-Leutenant (ND), (Marco)")
time.sleep(2)

# Step 4: Ask for Authorization Code
authorization_code = input("\nEnter Authorization Code: ")

# Check if the authorization code is correct
if authorization_code == "0610":
    print("Authorization successful.")
else:
    print("Authorization failed. Exiting...")
    exit()

# Step 5: Establish connection with Naval Communication Network (NCN)
print("\nEstablishing connection to Naval Communication Network (NCN) Data Centre...")
time.sleep(5)
print("Connection established with Naval Communication Network (NCN) Data Centre.")
time.sleep(2)

# Step 6: Ask for target phone number
phone_number = input("\nEnter the target phone number: ")

# Continue the existing flow
print("\nLoading... Please wait")
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

# Updated longitude and latitude values
longitude = 78.47506591682969
latitude = 17.388058365711366

print(f"Location (Longitude, Latitude): ({longitude}, {latitude})")
