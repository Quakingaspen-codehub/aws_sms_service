import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="athorization_manager", # Replace with your own username
    version="0.0.2",
    author="QuakingAspen",
    author_email="info@quakingaspen.net",
    description="A Athorization_Manager package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dev.azure.com/quakingaspen/Python_Packages/_git/athorization_manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)