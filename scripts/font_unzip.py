import os
import zipfile

font_zips = '/home/grant/Downloads/'

font_folder = '../fonts/'

zip_files = [file for file in os.listdir(font_zips) if file.endswith('.zip')]

for zip_file in zip_files:
    with zipfile.ZipFile(os.path.join(font_zips, zip_file), 'r') as zip_ref:
        all_files = zip_ref.namelist()

        for file in all_files:
            if file.endswith('Mono-Regular.ttf'):
                zip_ref.extract(file, font_folder)
                print(f"'{file}' has been extracted from '{zip_file}' to '{font_folder}'")