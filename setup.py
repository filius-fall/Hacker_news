from setuptools import setup, find_packages

setup(
    name='Hackerjobs',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'hackerjobs = Hackerjobs.scripts.hackerjobs_script:cli',
        ],
    },
)