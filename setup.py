from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        return file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Aryan',
    author_email='aryanahmadchaudhary@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)