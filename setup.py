from setuptools import setup, find_packages

setup(
    name='bis-api-wrapper',
    version='0.1.1',
    author='Vezono',
    author_email='vezonolab@gmail.com',
    description='Wrapper for BIS',
    long_description='Wrapper for BIS',
    url='https://github.com/Vezono/bis-api-wrapper',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)