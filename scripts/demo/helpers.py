import os
from urllib.parse import urlparse
import requests
from tqdm import tqdm
import streamlit as st
from pathlib import Path

@st.cache_resource()
def download_model(url):
    parsed_url = urlparse(url)
    file_path = (Path("checkpoints") / os.path.basename(parsed_url.path)).resolve()
    print(f"file_path = {file_path}")
    if not os.path.exists(file_path):
        Path("checkpoints").mkdir(parents=True, exist_ok=True)
        print(f"Downloading file from {url}...")
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        with open(file_path, 'wb') as file, tqdm(
                desc=str(file_path),
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                bar.update(len(data))
                file.write(data)
        print(f"File downloaded successfully to {file_path}")
    else:
        print(f"File already exists at {file_path}")
    return file_path
