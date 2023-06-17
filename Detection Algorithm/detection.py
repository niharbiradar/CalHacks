import os
import kaggle

kaggle_json_path = 'Detection Algorithm/kaggle.json'
destination_dir = 'Detection Algorithm/kaggle.json'  

kaggle_username = 'niharbiradar'  
kaggle_key = '7f8eca90f81e91f22e674f18db85112e'  

dataset_name = 'deepfake_faces'  
kaggle.api.authenticate(username=kaggle_username, key=kaggle_key)

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

kaggle.api.dataset_download_files(dataset_name, path=destination_dir, unzip=True)

print('Dataset downloaded successfully.')
