from setuptools import find_packages, setup
from typing import List
HYPE_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    ''' This function returns a list of requirements'''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]

    if HYPE_E_DOT in requirements:
        requirements.remove(HYPE_E_DOT)
        
    return requirements

setup(
    name='ML_project',
    version='0.0.1',
    author ="KARAM",
    author_email="raj.kachhadiya15@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'), 
    
)