import csv
import json


# Open the CSV
f = open('/Users/sowmya/python/output.csv', 'rU')
# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader(f, fieldnames=(
    "Name", "Tel", "Address", "City", "State", "Zip Code", "Latitude", "Longitude"))
# Parse the CSV into JSON
out = json.dumps([row for row in reader])
print("JSON parsed!")
# Save the JSON
f = open('/Users/sowmya/python/parsed.json', 'w')
f.write(out)
print("JSON saved!")
