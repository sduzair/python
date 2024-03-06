# Virtual environments

Virtual environments are isolated installation directories that allow you to localize the installation of project dependencies without conflicts.

## Creating a virtual environment with pip

```cmd
python -m venv .venv
```

## Activate the virtual environment

Integrated terminal may automatically activate the environment. Happens when python interpretor is set.

## Install dependencies

```cmd
python -m pip install numpy
```

## Share virtual environment

```cmd
python -m pip freeze > requirements.txt
```

## Recreating virtual environment

```cmd
pip install -r requirements.txt
```

## VSCode

Set python interpretor to the local *.venv* directory

## Other tools to create environments

| Feature | pip freeze > requirements.txt | conda list -e > requirements.txt | conda env export > environment.yml |
| -- | -- | -- | -- |
| Cross-platform | Yes | No | No |
| Same-platform (Windows/Mac) | Yes | Yes | No |
| User machine | Yes | Yes | Yes |
