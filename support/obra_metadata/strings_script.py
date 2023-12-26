import pandas as pd
import re

def extract_img_str(input_string):
    matches = re.findall(r'(\d+\.\d+)', input_string)
    return matches[0]

def extract_cfg_scale(input_string):
    matches = input_string.split(':')
    return matches[2].strip()

def generate_script(id, frequency, metadata):

    # UPLOAD CLIMATE INFORMATION
    if frequency == "monthly":
        features = pd.read_csv('obra_metadata/cmip6_monthly.csv')
    else:
        features = pd.read_csv('obra_metadata/cmip6_yearly.csv')
    
    # JOIN DATAFRAMES
    df = pd.merge(features, metadata, on='time_bounds')

    # CREATE NEW DATAFRAME
    # data = pd.DataFrame(columns=[["date", "iteration", "cfg_scale", "img_str", "seed", "model", "pr", "tas", "sfcWind", "psl", "rldscs"]])
    data = pd.DataFrame(columns=[["date", "iteration", "cfg_scale", "img_str", "model", "pr", "tas", "sfcWind", "psl", "rldscs"]])

    data["date"]       = df["time_bounds"].apply(lambda x: str(x))
    data["iteration"]  = df['filename'].str.split('_').str[-1].str.split('.').str[0]

    data["pr"]      = df["pr"].apply(lambda x: str(x))  
    data["tas"]     = df["tas"].apply(lambda x: str(x))  
    data["sfcWind"] = df["sfcWind"].apply(lambda x: str(x))   
    data["psl"]     = df["psl"].apply(lambda x: str(x))   
    data["rldscs"]  = df["rldscs"].apply(lambda x: str(x))  

    # data["cfg_scale"]  = df['parameters'].apply(extract_cfg_scale)
    # data["img_str"]    = df["parameters"].apply(extract_img_str)
    # data["seed"]       = df["seed"].apply(lambda x: str(x))   
    # data["model"]      = df["model"]
    data["cfg_scale"]  = "7"
    data["img_str"]    = "0.75"
    data["model"]      = "stable-diffusion-v1-5"
    
    data.to_csv(f"website_script_{id}.csv", index=False)
    print(f"Done")

metadata_folder = ['/Volumes/Seagate/Estudos/Unicamp/PFG/video/s1_full/video_20y_v4_75/metadata_video.csv']

for folder in metadata_folder:

    id = "01_004"

    # UPLOAD MODEL INFORMATION
    metadata = pd.read_csv(folder)

    # FORMAT MODEL_DATA DATE
    metadata.rename(columns={'date': 'time_bounds'}, inplace=True)
    metadata["time_bounds"] = metadata["time_bounds"].str.slice(stop=7)

    # GENERATE SCRIPT
    generate_script(id, "monthly", metadata)