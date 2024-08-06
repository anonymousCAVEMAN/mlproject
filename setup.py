from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path=str)->List[str]:
    '''this funcion will return list of requirnmets'''
    requirements = []
    with open(file_path ) as file_obj:          # yaha requirements.txt bhi pass kar sakte hai
        requirements=file_obj.readlines()       # realines eak eak line ko read karta and harr line ke end mai \n ata hai
        requirements = [req.replace("\n",":") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

'''
- e .   # automatically trigger setup.py file 
        # we want to run install all requirements  at the same time the setup.py py file should run
        # abhi isko file read mai avoid bhi karna padega
'''



setup(
name='mlporject',
version='3.8.0',
author='Divyansh',
author_email='divyanshdonode@gmail.com',
packages=find_packages(),   # at times we might have 100 packages and how to manage 
                            # here we create a text file which will have all the requirments
packages_multiple=get_requirements('requirements.txt')
# install_requires=['pandas','numpy','seaborn',],

)

# how will this setup.py will find that how many package and where is the package file

# now we want to let setup.py to find out how man packages are in the environment
# for that create a new folder SRC source