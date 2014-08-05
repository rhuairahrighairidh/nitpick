from setuptools import setup, find_packages
setup(
    name='SoN',
    version='0.1.0',
    description='A visualisation library for nupic',
    long_description='',
    url='https://github.com/rhuairahrighairidh/SoN',
    author="Ruaridh O'Donnell",

    packages = ['SoN','SoN.plots'], #the final packages that will end up in site-packages
    #py_modules = ['fileIO','plots'], #modules (python files) that will end up in site-packages
    #package_dir = {'SoN':''},

    #install_requires=['numpy','matplotlib', 'cerebro2'],
    
    package_data = {'SoN': ['documentation/*.ipynb']}

    #data_files=[('docs', ['documentation/demo.ipynb'])] # don't use this, it puts the files in stupid places
)
