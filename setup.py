import setuptools
  
with open("README.md", "r") as fh:
    long_description = fh.read()
  
setuptools.setup(
    name="mylovelywallet",
    version="0.1",
    author="MondbevOmator MondbevOmator",
    author_email="contact@otomato.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mondbev1/pytest-tutorial",
    packages=setuptools.find_packages(),
    package_dir={'': 'src'},
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)