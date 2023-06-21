from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    this fn will return list of required files 
    '''
    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [res.replace("\n", " ") for res in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


    
setup(
    name= 'mlproject',
    version='0.0.1',
    author="Umang Babu",
    author_email="eekobi.2@gmail.com",
    
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')

)