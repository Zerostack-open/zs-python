# ZeroStack Python SDK v0.1 Beta - Beta

Python SDK library for interacting with ZeroStack Cloud Operating System API

Description
-----------

The ZeroStack ZSPython SDK is a library that will help developers and datacenter engineers
integrate with, and automate the ZeroStack cloud platform. The ZSPython SDK seamlessly integrate 
with the ZeroStack Cloud Platform using the Python language. The ZSPython library is imported
like any other Python library and reduces the time to value of the ZeroStack cloud platform.

Compatibility
-------------

|  Component    | Version       |
|:--------------|:--------------|
| ZCOS Star     | 3.0 - 3.0.x   |
|:--------------|:--------------|
| ZCOS Sky.     | 26.x - 27.x   |    

Getting Help
------------

If you have any questions or comments about this product, open an issue
on our [GitHub repo](https://github.com/solidfire/solidfire-sdk-python)
or reach out to the online developer community at
[ThePub](http://netapp.io). Your feedback helps us focus our efforts on
new features and capabilities.

Documentation
-------------


Installation
------------

**From PyPI**

    pip install zspython-sdk

**From Source**

*Note*: It is recommended using
[virtualenv](https://github.com/pypa/virtualenv) for isolating the
python environment to only the required libraries.

Alternatively, for development purposes or to inspect the source, the
following will work:

    git clone git@github.com:zerostack-open/zs-python.git
    cd zspython
    git checkout develop
    pip install -e ".[dev, test, docs, release]"
    python setup.py install

Then append the location of this directory to the `PYTHONPATH`
environment variable to use the SDK in other python scripts:

    export PYTHONPATH=$PYTHONPATH:/path/to/zs-python-sdk/

That's it -- you are ready to start interacting with your ZeroStack
cluster using Python!

Videos
------

**Getting Started**

[This video](https://www.youtube.com/watch?v=3g028LYmiN4) is a walkthrough of getting started with the ZeroStack Python
SDK. You will see how install the SDK, connect to a ZeroStack cluster,
and use it to perform simple operations like retrieving and modifying
accounts and volumes.

Examples
--------

### Step 1 - Build an object using the factory


### Step 2 - Call the API method and retrieve the result


### More examples using the Python SDK

	

More Examples
-------------



Logging
-------

To configure logging responses, execute the following:

	import logging



Timeouts
--------

Connection timeout (useful for failing fast when a host becomes
unreachable):
