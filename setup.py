from setuptools import setup, find_packages

setup(
    name='CalculationMethods',
    version='1.0',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        'django',
        'numpy',
    ]
)
