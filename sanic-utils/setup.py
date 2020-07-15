import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sanic-utils",
    version="0.1.1",
    author="Thulani Chivandikwa",
    author_email="chivandikwa.t@gmail.com",
    description="A suite of sanic sanic_utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chivandikwa/sanic-utils",
    packages=setuptools.find_packages(),
    install_requires=["sanic==20.6.3",
                      "dataclasses==0.6",
                      "dataclasses-json==0.5.1"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
