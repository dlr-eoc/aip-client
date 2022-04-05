import re
from io import open

from setuptools import find_packages, setup

# Get the long description from the relevant file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

with open("aip_client/__init__.py", encoding="utf-8") as f:
    version = re.search(r'__version__\s*=\s*"(\S+)"', f.read()).group(1)

setup(
    name="aip-client",
    version=version,
    description="Utility to search and download satellite images from Archive Interface delivery Point",
    long_description=long_description,
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Utilities",
    ],
    keywords="aip, esa, satellite, download, GIS",
    author="Markus Kunze",
    author_email="markus.kunze@dlr.de",
    url="https://github.com/markus-kunze/aip-client",
    license="GPLv3+",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=False,
    zip_safe=True,
    install_requires=open("requirements.txt").read().splitlines(),
    extras_require={
        "dev": [
            "pytest >= 3.6.3",
            "pytest-vcr",
            "pytest-socket",
            "requests-mock",
            "pyyaml",
        ],
    }
)
