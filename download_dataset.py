import os
import kaggle

# Download BirdCLEF 2026 dataset
kaggle.api.competition_download_files('birdclef-2026', path='./data', quiet=False)

# Unzip the dataset
import zipfile
with zipfile.ZipFile('./data/birdclef-2026.zip', 'r') as zip_ref:
    zip_ref.extractall('./data')

print("Dataset downloaded and extracted to ./data/")
