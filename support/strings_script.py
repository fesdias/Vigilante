import pandas as pd
import re

def extract_img_str(input_string):
    matches = re.findall(r'(\d+\.\d+)', input_string)
    return matches[0]

def extract_cfg_scale(input_string):
    matches = input_string.split(':')
    return matches[2].strip()

features_url = '/Volumes/Seagate/Estudos/Unicamp/PFG/Data/cmip6/predictions/features_dataset_yearly.csv'
features     = pd.read_csv(features_url)

metadata_folder = ['/Volumes/Seagate/Estudos/Unicamp/PFG/video/s2_yearly/2023-08-v10']

for folder in metadata_folder:
    metadata = pd.read_csv(f'{folder}/metadata_video.csv')
    metadata.rename(columns={'date': 'time_bounds'}, inplace=True)
    
    df = pd.merge(features, metadata, on='time_bounds')
    
    data = pd.DataFrame(columns=[["date", "iteration", "cfg_scale", "img_str", "seed", "model", "pr", "tas", "sfcWind", "psl", "rldscs"]])

    data["iteration"]  = df['filename'].str.split('_').str[-1].str.split('.').str[0]
    data["cfg_scale"]  = df['parameters'].apply(extract_cfg_scale)
    data["img_str"]    = df["parameters"].apply(extract_img_str)
    #data['img_str'], data['cfg_scale'] = zip(*df['parameters'].apply(extract_values))
    data["seed"]       = df["seed"].apply(lambda x: str(x))   
    data["model"]      = df["model"]
    data["date"]       = df["time_bounds"].apply(lambda x: str(x))

    data["pr"]      = df["pr"].apply(lambda x: str(x))  
    data["tas"]     = df["tas"].apply(lambda x: str(x))  
    data["sfcWind"] = df["sfcWind"].apply(lambda x: str(x))   
    data["psl"]     = df["psl"].apply(lambda x: str(x))   
    data["rldscs"]  = df["rldscs"].apply(lambda x: str(x))  
    
    data.to_csv(f"website_script.csv", index=False)
    print(f"Done")