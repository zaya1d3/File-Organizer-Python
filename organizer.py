import os
import shutil

# directory to organize
directory = os.path.join(os.getcwd(), 'file_organizer', 'files')

# file type rules
file_extensions = {
    'pdf': 'PDFs',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executables',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos'
}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isdir(file_path):
        continue

    extension = filename.split('.')[-1].lower()

    if extension in file_extensions:
        folder_name = file_extensions[extension]
        folder_path = os.path.join(directory, folder_name)

        os.makedirs(folder_path, exist_ok=True)

        shutil.move(file_path, os.path.join(folder_path, filename))
        
#by Zayan Zamir