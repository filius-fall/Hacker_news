from setuptools import setup, find_packages

with open('requirements.txt','r') as f:
    requirements = f.readlines()
    requirements = [i.strip() for i in requirements]
with open('requirements_dev.txt','r') as dev:
    requirements_dev = dev.readlines()
    requirements_dev = [j.strip() for j in requirements_dev]

setup(
    name='Hackerjobs',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'hackerjobs = Hackerjobs.scripts.hackerjobs_script:cli',
        ],
    },
)