#!/usr/bin/env python3
import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import mimetypes
import re

def download_file(url, local_path):
    try:
        # Add headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, stream=True, headers=headers)
        response.raise_for_status()
        
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Successfully downloaded: {url}")
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

def extract_image_urls(html_content):
    """Extract image URLs from HTML content including those in style attributes and background images"""
    urls = set()
    
    # Find all img tags
    for img in html_content.find_all('img'):
        src = img.get('src')
        if src:
            urls.add(src)
            
        # Check data-src attribute (common for lazy loading)
        data_src = img.get('data-src')
        if data_src:
            urls.add(data_src)
    
    # Find background images in style attributes
    for tag in html_content.find_all(style=True):
        style = tag['style']
        bg_urls = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', style)
        urls.update(bg_urls)
    
    # Find background images in style tags
    for style in html_content.find_all('style'):
        if style.string:
            bg_urls = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', style.string)
            urls.update(bg_urls)
    
    return urls

def main():
    base_url = 'https://brooksfloorcovering.com'
    pages_to_check = [
        '/photo-gallery',
        '/about-us',
        '/flooring-services-in-maricopa-county-arizona',
        '/',
    ]
    assets_dir = 'src/assets'
    gallery_dir = os.path.join(assets_dir, 'gallery')
    
    # Create assets directory if it doesn't exist
    os.makedirs(gallery_dir, exist_ok=True)
    
    # Store all unique image URLs
    all_image_urls = set()
    
    # Headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Check each page for images
    for page in pages_to_check:
        page_url = urljoin(base_url, page)
        print(f"Checking page: {page_url}")
        
        try:
            response = requests.get(page_url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract image URLs from the page
            image_urls = extract_image_urls(soup)
            
            # Add valid URLs to our set
            for url in image_urls:
                full_url = urljoin(page_url, url)
                if is_valid_file(full_url):
                    all_image_urls.add(full_url)
            
            # Small delay to be nice to the server
            time.sleep(1)
            
        except Exception as e:
            print(f"Error processing {page_url}: {e}")
    
    # Download all unique images
    print(f"Found {len(all_image_urls)} unique images")
    for url in all_image_urls:
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            continue
            
        # Determine if this should go in the gallery directory
        is_gallery_image = 'gallery' in url.lower() or 'project' in url.lower()
        target_dir = gallery_dir if is_gallery_image else os.path.join(assets_dir, 'images')
        local_path = os.path.join(target_dir, filename)
        
        # Skip if file already exists
        if os.path.exists(local_path):
            print(f"File already exists: {local_path}")
            continue
            
        print(f"Downloading {url} to {local_path}")
        download_file(url, local_path)
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
