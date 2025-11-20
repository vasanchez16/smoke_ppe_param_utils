from setuptools import setup, find_packages

setup(
    name='smoke_ppe_param_utils',
    version='0.1.0',
    package_dir={'': 'src'}, 
    packages=find_packages(where='src'), 
    install_requires=[
        'numpy>=1.18.0',
        'pandas>=1.0.0',
    ],
    author='',
    description='Utilities for scaling and normalizing model parameters.',
    license='MIT',
)