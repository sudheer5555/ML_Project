#building an appliaction as a pypackages
from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")  for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Sudheer',
    author_email='bsudheer555@gmail.command_options',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)
