from setuptools import setup, find_packages


def read_version():
    version = {}
    with open("nonadateconverter/version.py", "r") as f:
        exec(f.read(), version)
        return version["__version__"]


setup(
    name="nonadateconverter",
    version=read_version(),
    description="dateconverter package for Gregorian, Hijri and Jalali",
    author="Navid Nourazar",
    author_email="navid.nourazar@gmail.com",
    packages=find_packages(
        include=["nonadateconverter", "nonadateconverter.*"]
    ),  # would be the same as name
    install_requires=open(
        "requirements.txt"
    ).readlines(),  # external packages acting as dependencies
)
