## Approach

Use `setuptools` to make python package distribiution easier. 

## Source
https://setuptools.pypa.io/en/stable/setuptools.html

## Theory

Three files are required to install python package:

   -   pyproject.toml
   -   setup.cfg
   -   setup.py

To manage project dependency [look](https://setuptools.pypa.io/en/latest/userguide/quickstart.html#dependency-management).

To trigger installation process use command:
```
python setup.py install
```

## Files examples

# pyproject.toml
```
[project]
name = "mypackage"
version = "0.0.1"
dependencies = [
    "requests",
    'importlib-metadata; python_version<"3.8"',
]
```

# setup.cfg
```
[metadata]
name = mypackage
version = 0.0.1

[options]
install_requires =
    requests
    importlib-metadata; python_version > "3.9"
```
Setuptools allows using configuration files (usually setup.cfg) to define a package’s metadata and other options that are normally supplied to the setup() function (declarative config).

# setup.py
```
from setuptools import setup

setup()
```

