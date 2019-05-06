import os
from setuptools import setup, find_packages

def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='TestScores',
    version='0.1',
    url='https://trevorxander.com/',
    license='GNU Affero General Public License v3.0',
    author='Trevor Xander',
    author_email='trevorcolexander@gmail.com',
    long_description=read('README.md'),
    install_requires=['scikit-learn', 'matplotlib', 'jupyter', 'pandas'],
    packages=find_packages(),
    entry_points={
    }
)
