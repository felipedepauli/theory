from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="power_electronics",
    version="0.0.1",
    author="Felipe Camargo de Pauli",
    author_email="fcdpauli@gmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_typ="text/markdown",
    url="https://github.com/felipedepauli/theory/tree/main/python/09_packages",
    packages=find_packages(),
    install_requirements=requirements,
    python_requires='>=3.8'
)