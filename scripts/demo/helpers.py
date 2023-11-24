import os
from urllib.parse import urlparse
import requests
def download(url):
    parsed_url = urlparse(url)
    file_path = os.path.basename(parsed_url)
    if not os.path.exists(file_path):
        print(f"Downloading file from {url}...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded successfully to {file_path}")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
    else:
        print(f"File already exists at {file_path}")
