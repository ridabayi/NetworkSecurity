from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function returns a list of requirements.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read the file and return the list of requirements
            lines = file.readlines()
            # process the lines 
            for line in lines:
                requirement = line.strip()
                ## Ignore comments and empty lines
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")

    return requirement_lst

setup(
    name = "NetworkSecurity",
    version= "0.0.1",
    author = "Rida BAYI",
    author_email="bayi.rida@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    description="A package for network security analysis and monitoring",
)
