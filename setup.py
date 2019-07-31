import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-coinlib-api-wrapper",
    version="1.0",
    author="Jeffrey Zhang",
    author_email="jeffrey346@gmail.com",
    description="Python Coinlib API Wrapper",
    long_description="A Python package that simplifies access to Coinlib's REST API by directly routing all endpoints and parameters through Python objects.",
    long_description_content_type="text/markdown",
    url="https://github.com/jeffreyzhang2001/python-coinlib-api-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests>=2.22.0',
        'urllib3>=1.25.3',
    ],
)