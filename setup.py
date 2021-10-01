import pathlib
from setuptools import find_packages,setup


parent_dir = pathlib.Path(__file__).parent
README = (parent_dir/"README.md").read_text()

setup(
	name='krit',
	version='0.1.0',
	description='python geospatial library, with capabilities to generate html/javascript code',
	long_description=README,
	long_description_content_type='text/markdown',
	url='https://github.com/Mohab25/krit.git',
	author='Mohab Khaled',
	author_email='homab3@gmail.com',
	license='MIT',
	packages= find_packages(exclude='tests',)
	

)
