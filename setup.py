import setuptools
import os


with open('requirements.txt') as f:
    required = f.read().splitlines()



with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smsman",
    version="0.0.1",
    author="https://github.com/banyoupls",
    author_email="anton223@protonmail.com",
    description="sms-man.com module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SMS-MAN/smsman",
    project_urls={
        "Bug Tracker": "https://github.com/SMS-MAN/smsman/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "smsman"},
    packages=setuptools.find_packages(where="smsman"),
    python_requires=">=3.7",
    install_requires=required
)