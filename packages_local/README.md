# Turorial to create packages using `poetry`

Creation of 2 packages that will be called to the directory myproject. Adding a local directory as a package avoids the adjustement of the `path`. We can just `import _package_` use. 

* Instructions.md: Steps to create packages with two standard layouts (flat and src).

# Create new package using poetry

Poetry replaces `setup.py`, `requirements.txt`, `setup.cfg`, `MANIFEST.in` and `Pipfile` with a simple `pyproject.toml` based project format.

* https://realpython.com/dependency-management-python-poetry/
* https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/ (Structure of package)
* https://setuptools.pypa.io/en/latest/userguide/development_mode.html (Editable installs)

## Dos tipos de layout

```bash
mkdir myproject # Create some dummy folders & files. 
touch myproject/main.py # This will execute something
touch myproject/notebooks/anotebook.ipynb # Remember to creare notebooks dir.

# Options poetry new: --src (default), --flat, --interactive
poetry new package1 --name first_pack --flat
poetry new package2 --name scr_pack --src

# An example of the directory:
.
├── myproject
│   ├── bin
│   ├── config
│   ├── data
│   ├── docs
│   ├── main.py
│   ├── notebooks
│   │   └── anotebook.ipynb
│   └── README.md
└── paquetes
    ├── package1
    │   ├── first_pack
    │   │   ├── __init__.py
    │   │   └── script_pack1.py
    │   ├── pyproject.toml
    │   ├── README.md
    │   └── tests
    │       └── __init__.py
    └── package2
        ├── pyproject.toml
        ├── README.md
        ├── src
        │   └── src_pack
        │       ├── __init__.py
        │       └── script_pack2.py
        └── tests
            └── __init__.py
 
```

### Flat

In this layout, your Python package resides at the root level of the project folder.

## srcon = "^3.12"
requests = "*"

which keeps the code in an additional src/ parent folder. 
* The src layout requires installation of the project to be able to run its code
* the src layout involves an additional step in the development workflow of a project [Editable installation](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).
* The src layout helps prevent accidental usage of the in-development copy of the code. If if an import package exists in the current working directory with the same name as an installed import package, the variant from the current working directory will be used.
* The src layout helps enforce that an editable installation is only able to import files that were meant to be importable. This is especially relevant when the editable installation is implemented using a path configuration file that adds the directory to the import path.
* Running a command-line interface from source with src-layout: A [workaround](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) to run a package in dev mode would be to prepend the package folder to `sys.path`.


## Working with poetry. 

### At location `    ├── package1` 

```bash
poetry install
poetry add requests@ latest
poetry add --group development jupyter
```

It changes the `pyproject.toml` of package1 adding `requests` to the dependencies. Test whether 

Write some function at `script_pack1.py`. Like `def fcn_pack1():`. Test it.

```bash
:Tutorials/paquetes/package1$ poetry run python first_pack/script_pack1.py
```

The `run` command executes the given command inside the project’s virtualenv. 
Also test if some functions are imported

```bash
poetry run python -c "import requests" 
# Or
$ poetry run python -q
>>> import requests
>>> requests.__version__
```

> with `poetry run python ...` the import of pandas succeded
> with `python ...` it threw an error. 
> So `poetry run python` uses the environment because `import pandas` , just work. 

When the environment was activated with `eval $(poetry env activate)` 

```bash
(package-name-py3.*) user@foo: ~/path/bla/package1@ python first_pack/script_pack1.py
> gives a 
> result just as poetry run python ...
```


In `pyoetry.toml` modify to add some stuffs before

```toml
dependencies = [
    "requests (=2.32.3)",
    "beautifulsoup4 (<4.10)",
]
```

And in a CLI session of `package2`:
 
```bash
poetry install
poetry add pandas
poetry add --group desarrollo ipykernel
```

Write some function at `script_pack2.py`. Like `def fcn_pack2():`. 

####Building the packages

Once the scripts and imported packages work, we now build packages from `package1` and `package2`.

```Bash
# At 
user@hostname:~/.../package1$ poetry build
#And at
user@hostname:~/.../package2$ poetry build
```

The command will create the directory `/dist` in both directories. Inside there are two new files: `*.whl` and `*.tar.gz` .  `package2` now looks like this. 

```bash
.
├── dist
│   ├── src_pack-0.1.0-py3-none-any.whl
│   └── src_pack-0.1.0.tar.gz
├── poetry.lock
├── pyproject.toml
├── README.md
├── src
│   └── src_pack
│       ├── __init__.py
│       └── script_pack2.py
└── tests
    └── __init__.py

```

Similar files are also created inside `package1`.

So far we must have build two packages. Now, we have to add them to the project that will use them. 

### At `├── myproject`

First, create a simple script in `main.py` and `nobetook.ipynb`
```python
# At main.py:

import pandas # Just to test. It is not installed in myproject

# Importing package1
from first_pack.script_pack1 import fcn_pack1
print("Test the import from package1")
fcn_pack1()

print("-----------------")

# Importing package2
from src_pack.script_pack2 import fcn_pack2
fcn_pack2()

```


```bash
# Create the pyproject.toml file
poetry init
# Install the dependencies only. 
poetry install --ro-root  # By default installe in editable mode
```

The moment of truth. Add the recent packages to `myproject`

```bash
# At user@hostname:~/.../myproject
poetry add --editable ~/Tutorials/paquetes/package1  # Worked!
poetry add --editable ~/Tutorials/paquetes/package2  # Worked!
# In both cases: Could not find a matching version of package ...
poetry add --editable ~/Tutorials/paquetes/package2/src_pack-0.1.0.tar.gz
poetry add --editable ~/Tutorials/paquetes/package2/src_pack-0.1.0-py3-none-any.whl
```

Test functions in `main.py`

```python
emx@xps17Fedora:~/Tutorials/myproject$ poetry run python main.py

emx@xps17Fedora:~/Tutorials/myproject$ poetry run python
Python 3.11.12 (main, Aug 30 2025, 12:58:45) [GCC 15.2.1 20250808 (Red Hat 15.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
>>> from first_pack.script_pack1 import fcn_pack1
>>> fcn_pack1()  # Should just print something
```

## References

* [Basic commands to work](https://realpython.com/dependency-management-python-poetry/#command-reference)
* [Local installations of projects](https://pip.pypa.io/en/stable/topics/local-project-installs/)
* [Poetry repositories](https://python-poetry.org/docs/repositories/)