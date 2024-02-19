import csv
import requests 
from PIL import Image 
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open('photo_script_test.csv') as photos_csv:
    photos_csv = list(csv.reader(photos_csv, delimiter = ';'))
    for row in photos_csv[1:]:
        url = row[1]
        if url:
            data = requests.get(url, verify=False).content
            file_name = f'{row[0]}.jpg'
            f = open(file_name, 'wb')
            f.write(data)
            f.close()