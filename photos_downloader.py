import csv
import requests 
import urllib3
import zipfile
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with zipfile.ZipFile("photos.zip", mode="w") as photos_zip:
    csv_path = input('Podaj ścieżkę do pliku csv: ')
    csv_path = csv_path.strip('\"')

    with open(csv_path,'r') as photos_csv:
        photos_csv_reader = list(csv.reader(photos_csv, delimiter = ';'))
        rows = []

        for line, row in enumerate(photos_csv_reader):
            if line >= 1:
                url = row[1]
                if url:
                    data = requests.get(url, verify=False).content
                    file_name = f'{row[0]}.jpg'
                    photos_zip.writestr(file_name, data)
                    rows.append([row[0], f'/{file_name}'])
            else:
                fields = row

    with open("import_photos.csv", 'w', newline='') as photos_csv:
        photos_csv_writer = csv.writer(photos_csv, delimiter=';')
        photos_csv_writer.writerow(fields)
        photos_csv_writer.writerows(rows)
    
    photos_zip.write('import_photos.csv')
    os.remove('import_photos.csv')