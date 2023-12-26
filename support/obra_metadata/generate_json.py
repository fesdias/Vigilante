import pandas as pd
import json

def generate_html(id, data):
    
    json_array_desktop = []
    json_array_mobile = []

    for i in range(len(data)):

        # WITH SEED
        # text_en_desktop = f"<div id=\"left-container\">\n<h2>RIO DE JANEIRO - GUANABARA BAY</h1>\n<p>Precipitation Rate = {data['pr'].values[i]} Kg m-2 s-1<br>\nTemperature = {data['tas'].values[i]} K<br>\nSurface Pressure = {data['psl'].values[i]} Pa<br>\nWind Speed = {data['sfcWind'].values[i]} m s-1<br>\nSolar Radiation = {data['rldscs'].values[i]} W m-2</p>\n</div>\n<div id=\"right-container\">\n<h1>{data['date'].values[i]}</h1>\n<p>Iteration = {data['iteration'].values[i]}<br>\nSeed = {data['seed'].values[i]}<br>\nModel = {data['model'].values[i]}<br>\nimg_str = {data['img_str'].values[i]}<br>\ncfg_scale = {data['cfg_scale'].values[i]}</p>\n</div>"
        # text_en_mobile = f"<div id=\"left-container\">\n<p>Precipitation Rate = {data['pr'].values[i]} Kg m-2 s-1<br>\nTemperature = {data['tas'].values[i]} K<br>\nSurface Pressure = {data['psl'].values[i]} Pa<br>\nWind Speed = {data['sfcWind'].values[i]} m s-1<br>\nSolar Radiation = {data['rldscs'].values[i]} W m-2</p>\n</div>\n<h1>{data['date'].values[i]}</h1>\n<h2>RIO DE JANEIRO<br>GUANABARA BAY</h1>\n<div id=\"right-container\">\n<p>Iteration = {data['iteration'].values[i]}<br>\nSeed = {data['seed'].values[i]}<br>\nModel = {data['model'].values[i]}<br>\nimg_str = {data['img_str'].values[i]}<br>\ncfg_scale = {data['cfg_scale'].values[i]}</p>\n</div>"
        
        # WITHOUT SEED
        text_en_desktop = f"<div id=\"left-container\">\n<h2>RIO DE JANEIRO - GUANABARA BAY</h1>\n<p>Precipitation Rate = {data['pr'].values[i]} Kg m-2 s-1<br>\nTemperature = {data['tas'].values[i]} K<br>\nSurface Pressure = {data['psl'].values[i]} Pa<br>\nWind Speed = {data['sfcWind'].values[i]} m s-1<br>\nSolar Radiation = {data['rldscs'].values[i]} W m-2</p>\n</div>\n<div id=\"right-container\">\n<h1>{data['date'].values[i]}</h1>\n<p>Iteration = {data['iteration'].values[i]}<br>\nModel = {data['model'].values[i]}<br>\nimg_str = {data['img_str'].values[i]}<br>\ncfg_scale = {data['cfg_scale'].values[i]}</p>\n</div>"
        text_en_mobile = f"<div id=\"left-container\">\n<p>Precipitation Rate = {data['pr'].values[i]} Kg m-2 s-1<br>\nTemperature = {data['tas'].values[i]} K<br>\nSurface Pressure = {data['psl'].values[i]} Pa<br>\nWind Speed = {data['sfcWind'].values[i]} m s-1<br>\nSolar Radiation = {data['rldscs'].values[i]} W m-2</p>\n</div>\n<h1>{data['date'].values[i]}</h1>\n<h2>RIO DE JANEIRO<br>GUANABARA BAY</h1>\n<div id=\"right-container\">\n<p>Iteration = {data['iteration'].values[i]}<br>\nModel = {data['model'].values[i]}<br>\nimg_str = {data['img_str'].values[i]}<br>\ncfg_scale = {data['cfg_scale'].values[i]}</p>\n</div>"

        json_array_desktop.append({"index": i, "text": text_en_desktop})
        json_array_mobile.append({"index": i, "text": text_en_mobile})

    # Specify the file name
    json_file_desktop_url = f'../../assets/gallery/vigilante_{id}/vigilante_data_en_desktop_{id}.json'
    json_file_mobile_url  = f'../../assets/gallery/vigilante_{id}/vigilante_data_en_mobile_{id}.json'

    # Write the data to a JSON file
    with open(json_file_desktop_url, 'w') as file:
        json.dump(json_array_desktop, file, indent=2)

    with open(json_file_mobile_url, 'w') as file:
        json.dump(json_array_mobile, file, indent=2)

    print(f'The JSON file "{json_file_desktop_url}" has been created.')
    print(f'The JSON file "{json_file_mobile_url}" has been created.')

id = "01_004"
script = pd.read_csv(f'website_script_{id}.csv')
generate_html(id, script)