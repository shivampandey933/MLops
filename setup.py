
from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements: List[str] = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
   name="My mlops project",
   version= "0.1.0",
   author= "Shivam Pandey",
   description="end to end mlops project using the deployment of ml models",
   packages= find_packages(),
   install_requires= get_requirements("requirements.txt")
   
)