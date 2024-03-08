from setuptools import setup, find_packages

# Read the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def read_version():
    version = {}
    with open("nonadateconverter/version.py", "r") as f:
        exec(f.read(), version)
        return version["__version__"]


setup(
    name="nonadateconverter",
    version=read_version(),
    author="Navid Nourazar",
    author_email="navid.nourazar@gmail.com",
    description="dateconverter package for Gregorian, Hijri and Jalali",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/naweed1992/nonadateconverter",
    packages=find_packages(
        include=["nonadateconverter", "nonadateconverter.*"]
    ),  # would be the same as name
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=open(
        "requirements.txt"
    ).readlines(),  # external packages acting as dependencies
)
