import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_desc=f.read()

__version__="0.0.0"
REPO_NAME='Chicken_disease_classification'
AUTHON_NAME='ragibabid127'
AUTHOR_EMAIL='ragibabid127@gmail.com'
REPO_SRC='CNN_Classifier'

setuptools.setup(
    name=REPO_SRC,
    version=__version__,
    author=AUTHON_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small project to classify chicken fecal matter image to detect Coccidiosis',
    long_description=long_desc,
    long_description_content='text/markdown',
    url=f'https://github.com/{AUTHON_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker':f'https://github.com/{AUTHON_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)