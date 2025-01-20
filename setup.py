from setuptools import setup, find_packages

setup(
    name="firstdata-v1-encrypt",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pycryptodome>=3.9.0",
    ],
    author="Taiinyy",
    author_email="your.email@example.com",
    description="FirstData V1 card encryption implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Taiinyyy/firstdata-v1-encrypt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)