import pandas as pd
import json

start_index = 0
end_index = 256

data = pd.read_csv('website_data.csv')
json_array = []

for i in range(start_index, end_index + 1):
    text = f"<div id=\"left-container\">\n<h2>RIO DE JANEIRO - GUANABARA BAY</h1>\n<p>Precipitation Rate = {data['pr'].values[i]} Kg m-2 s-1<br>\nTemperature = {data['tas'].values[i]} K<br>\nSurface Pressure = {data['psl'].values[i]} Pa<br>\nWind Speed = {data['sfcWind'].values[i]} m s-1<br>\nSolar Radiation = {data['rldscs'].values[i]} W m-2</p>\n</div>\n<div id=\"right-container\">\n<h1>{data['date'].values[i]}</h1>\n<p>Iteration = {data['iteration'].values[i]}<br>\nSeed = {data['seed'].values[i]}<br>\nModel = {data['model'].values[i]}<br>\nimg_str = {data['img_str'].values[i]}<br>\ncfg_scale = {data['cfg_scale'].values[i]}</p>\n</div>"
    json_array.append({"index": i, "text": text})

# Specify the file name
json_file = 'vigilante_data_v2.json'

# Write the data to a JSON file
with open(json_file, 'w') as file:
    json.dump(json_array, file, indent=2)

print(f'The JSON file "{json_file}" has been created.')