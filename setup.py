import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zspython",
    version="0.0.1",
    author="Jonathan Arrance",
    author_email="jonathan@zerostack.com",
    description="The Zerostack python API library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JonathanArrance/zsdev/tree/master/pythonSDK",
    packages=setuptools.find_packages(),
    classifiers=(
        'Development Status :: 4 - Beta',
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
