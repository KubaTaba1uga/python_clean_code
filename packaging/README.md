# Approach

Use `setuptools` to make python package distribiution easier. 

# Source
https://setuptools.pypa.io/en/stable/setuptools.html

# Theory

Two files are required to install python package:

   -   pyproject.toml
   -   setup.py

To manage project dependency [look](https://setuptools.pypa.io/en/latest/userguide/quickstart.html#dependency-management).

To trigger installation process use command:
```
pip install .
```

# Files examples
Setuptools allows using configuration files (usually pyproject.toml) to define a package’s metadata and other options that are normally supplied to the setup() function (declarative config).

## pyproject.toml
```
[project]
name = "mypackage"
version = "0.0.1"
dependencies = [
    "requests",
    'importlib-metadata; python_version<"3.8"',
]
```

## setup.py
```
from setuptools import setup

setup()
```

