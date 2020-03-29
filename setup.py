import setuptools

with open("README.md", 'r') as file:
    long_description = file.read()

setuptools.setup(
    name="CardCollection",
    version="0.0.0",
    author="Etienne Thompson",
    author_email="et@etiennethompson.com",
    description="Programs allowing for tracking card collections and prices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EtienneThompson/CardCollection",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)