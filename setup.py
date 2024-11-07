from setuptools import setup, find_packages

setup(
    name="tx-tracker",
    version="1.0",
    packages=find_packages(),
    author="Onyeka Nwizu",
    py_modules=["main"],
    description="A task tracker CLI app.",
    requires=["prettytable"]
    entry_points={
        'console_scripts': [
            'tx-tracker = main:app',
        ],
    },
)