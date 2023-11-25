import json

# Define the range of indices
start_index = 0
end_index = 256

# Generate a list of dictionaries with index and text
data = [{"index": i, "text": f'VIGILANTE_{i:04}'} for i in range(start_index, end_index + 1)]

# Specify the file name
json_file = 'vigilante_data.json'

# Write the data to a JSON file
with open(json_file, 'w') as file:
    json.dump(data, file, indent=2)

print(f'The JSON file "{json_file}" has been created.')
