import os
from pathlib import Path
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s \n')

project_name='CNN_Classifier'

file_list= [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/logger.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/config.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'notebooks/trials.ipynb',
    'templates/index.html'
]

for file in file_list:
    file_path=Path(file)
    file_dir, file_name=os.path.split(file_path)

    if file_dir!='':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Folder {file_dir} created')

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            logging.info(f'{file_path} created')

    else:
        logging.info(f'{file_name} exists at {file_dir}')
