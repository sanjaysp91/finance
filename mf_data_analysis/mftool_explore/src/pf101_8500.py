from mftool import Mftool
import json

# Initialize Mftool
mf = Mftool()

# Get all mutual fund schemes
schemes = mf.get_scheme_codes()
# print(schemes)
# print(json.dumps(schemes, indent=4))

# # Fetch latest NAV for each scheme
# for scheme_name, scheme_code in list(schemes.items())[:10]:  # Limiting to 10 for readability
#     nav_data = mf.get_scheme_quote(scheme_code)
#     if nav_data:
#         print(f"{scheme_name}: {nav_data['nav']}")
#     else:
#         print(f"{scheme_name}: NAV data not available")

# Create a dictionary to store fund names with NAV
funds_with_nav = {}

# Fetch NAV for each scheme code
for scheme_code, scheme_name in list(schemes.items())[:10]:
    print(f"{scheme_code}: {scheme_name}")
    nav_data = mf.get_scheme_quote(scheme_code)  # Get NAV details
    if nav_data:  # Check if data is available
        funds_with_nav[scheme_code] = {
            "name": scheme_name,
            "nav": nav_data.get("nav")  # Extract NAV value
        }


# Print the first few results
for code, details in list(funds_with_nav.items())[:10]:  # Display first 10 for preview
    print(f"{code}: {details['name']} - NAV: {details['nav']}")

import csv
input_csv = "data/pf101_8500.csv"  # Original CSV with Scheme Code and Scheme Name
output_csv = "data/pf101_8500_output.csv"  # New CSV with NAV included

# Read the CSV file and create a dictionary
with open(input_csv, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Reads CSV as a list of dictionaries
    pf101_8500_data_dict = {row["Scheme Code"]: row["Scheme Name"] for row in reader}

# Print the dictionary
# print(data_dict)
# print(json.dumps(pf101_8500_data_dict, indent=4))


# Create a dictionary to store fund names with NAV
pf101_8500_funds_with_nav = {}
# Fetch NAV for each scheme code
for scheme_code, scheme_name in pf101_8500_data_dict.items():
    print(f"{scheme_code}: {scheme_name}")
    nav_data = mf.get_scheme_quote(scheme_code)  # Get NAV details
    if nav_data:  # Check if data is available
        pf101_8500_funds_with_nav[scheme_code] = {
            "name": scheme_name,
            "nav": nav_data.get("nav")  # Extract NAV value
        }

print(f"############################################################")
print(pf101_8500_funds_with_nav)
print(f"############################################################")

# Print the first few results
for code, details in pf101_8500_funds_with_nav.items():  # Display all
    print(f"{code}: {details['name']} - NAV: {details['nav']}")

#
#
#
#
nav_dict = pf101_8500_funds_with_nav
# Read the original CSV and add NAV values
with open(input_csv, newline="", encoding="utf-8") as infile, open(output_csv, "w", newline="", encoding="utf-8") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["NAV"]  # Add NAV column to headers

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        scheme_code = row["Scheme Code"]
        row["NAV"] = nav_dict.get(scheme_code, {}).get("nav", "N/A")  # Extract NAV safely
        writer.writerow(row)

print(f"Updated NAVs written to {output_csv}")

