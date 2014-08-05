from setuptools import setup, find_packages
setup(
    name='nitpick',
    version='0.1.0',
    description='A visualisation library for nupic.',
    long_description='',
    url='https://github.com/rhuairahrighairidh/SoN',
    author="Ruaridh O'Donnell",

    packages = ['nitpick','nitpick.plots'], #packages (folders containing __init__.py) that will end up in site-packages
    #py_modules = [#.py files#], #modules (python files) that will end up in site-packages
    #package_dir = #a mapping from names of the packages to folders in the repo

    install_requires=['numpy','matplotlib'],
    
    package_data = {'nitpick': ['documentation/*.ipynb']} #include the ipython notebook documentation

    #data_files=[('docs', ['documentation/demo.ipynb'])] # don't use this, it puts the files in silly places
)
