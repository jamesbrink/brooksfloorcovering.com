#!/usr/bin/env python3
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import mimetypes

def download_file(url, local_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def is_valid_file(url):
    parsed = urlparse(url)
    ext = os.path.splitext(parsed.path)[1].lower()
    mime_type = mimetypes.guess_type(url)[0]
    
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.css', '.js']
    valid_mimes = ['image/', 'text/css', 'application/javascript']
    
    return ext in valid_extensions or any(mime_type.startswith(t) for mime_type in valid_mimes if mime_type)

def main():
    base_url = 'https://brooksfloorcovering.com'
    assets_dir = 'assets/original'
    
    # Create assets directory if it doesn't exist
    os.makedirs(assets_dir, exist_ok=True)
    
    # Get the main page
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all images, stylesheets, and scripts
    assets = []
    assets.extend([(img.get('src'), 'images') for img in soup.find_all('img')])
    assets.extend([(link.get('href'), 'css') for link in soup.find_all('link', rel='stylesheet')])
    assets.extend([(script.get('src'), 'js') for script in soup.find_all('script', src=True)])
    
    # Download each asset
    for asset_url, asset_type in assets:
        if not asset_url:
            continue
            
        full_url = urljoin(base_url, asset_url)
        if not is_valid_file(full_url):
            continue
            
        filename = os.path.basename(urlparse(full_url).path)
        if not filename:
            continue
            
        local_path = os.path.join(assets_dir, asset_type, filename)
        
        print(f"Downloading {full_url} to {local_path}")
        if download_file(full_url, local_path):
            print(f"Successfully downloaded {filename}")
        else:
            print(f"Failed to download {filename}")

if __name__ == '__main__':
    main()
