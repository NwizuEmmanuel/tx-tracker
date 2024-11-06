from setuptools import setup, find_packages

setup(
    name="tx-tracker",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console-scripts':[
            "tx-tracker: main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)