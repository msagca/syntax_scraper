# -*- coding: utf-8 -*-
import setuptools
setuptools.setup(
    name="syntax-scraper",
    version="1.0.4",
    author="Mustafa Said Ağca",
    url="https://github.com/msagca/syntax-scraper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["ieee"],
    install_requires=["antlr4-python3-runtime==4.13.2", "pdfplumber"],
    entry_points={"console_scripts": ["scrape-ieee=ieee.__main__:main"]},
)
