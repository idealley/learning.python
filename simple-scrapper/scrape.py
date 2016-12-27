import argparse
import base64
import json
import os
from bs4 import BeautifulSoup
import requests

def scrape(url, format_, type_):
    try:
        page = requests.get(url)
    except requests.RequestException as rex:
        print(str(rex))
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        images = _fetch_images(soup, url)
        images = _filter_images(images, type_)
        _save(images, format_)

def _fetch_images(soup, base_url):
    images = []
    for img in soup.findAll('img'):
        src = img.get('src')
        img_url = src
        if src.split('/')[0] != 'http:':
            img_url = (
                '{base_url}/{src}'.format(
                    base_url=base_url, src=src))
        path = img_url.split('/')        
        name = img_url.split('/')[-1]
        if '?' in name:
            name = name.split('?')[0]
        images.append(dict(name=name, url=img_url))
    return images

def _filter_images(images, type_):
    ext_map = {
        'png': ['.png'],
        'jpg': ['.jpg', '.jpeg'],
        'all': ['.jpg', '.jpeg', '.png']
    }
    return [
        img for img in images
        if _matches_extension(img['name'], ext_map[type_])
    ]

def _matches_extension(filename, extension_list):
    name, extension = os.path.splitext(filename.lower())
    return extension in extension_list

def _save(images, format_):
    if images:
        if format_ == 'img':
            _save_images(images)
        else:
            _save_json(images)
        print('Done')
    else:
        print('No images to save.')

def _save_images(images):
    for img in images:
        img_data = requests.get(img['url']).content   
        file_ = path('scrapped/images', img['name'])
        with open(file_, 'wb') as f:
            f.write(img_data)

def _save_json(images):
    data = {}
    for img in images:
        img_data = requests.get(img['url']).content
        b64_img_data = base64.b64encode(img_data)
        str_img_data = b64_img_data.decode('utf-8')
        data[img['name']] = str_img_data
        file_ = path('scrapped/json', 'images.json')
    with open(file_, 'w') as ijson:
        ijson.write(json.dumps(data))

def path(path, file):
    if not os.path.exists(path):
            os.makedirs(path)
    return os.path.join(path, file)

if __name__ == "__main__":
    """ You can use this scritp directly or as a lib as __name__ won't be '__main__' when imported as a lib.
    On the other and in the console __name__ is __main__, thus it will run.
    """
    parser = argparse.ArgumentParser(
        description='Scrape a webpage.')
    parser.add_argument(
        '-t',
        '--type',
        choices=['all', 'png', 'jpg'],
        default='all',
        help='The image type we want to scrape.')
    parser.add_argument(
        '-f',
        '--format',
        choices=['img', 'json'],
        default='img',
        help='The format images are saved to.')
    parser.add_argument(
        'url',
        help='The URL we want to scrape for images.')
    args = parser.parse_args()
    scrape(args.url, args.format, args.type)