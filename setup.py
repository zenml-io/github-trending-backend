""" setup """

import io

from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    LONG_DESC = f.read()

VERSION = "0.0.1"

# This call to setup() does all the work
setup(
    name="wasitrending",
    version=VERSION,
    description="Backend to scrape GitHub Trending data every hour.",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    url="https://github.com/zenml-io/github-trending-backend",
    author="Hedy Li",
    author_email="hedyhyry@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["wasitrending"],
    include_package_data=True,
    install_requires=[
        "Click>=7.0",
        "colorama>=0.4.3",
        "gtrending>=0.3.0,<1.0.0",
        "requests>=2.22.0",
        "rich>=4.0.0,<11.0.0",
        "xdg>=5.1.1,<7.0.0",
    ],
    entry_points={
        "console_scripts": [
            "wasitrending=src.__main__:cli",
        ]
    },
)
