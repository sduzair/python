# python

- [python](#python)
  - [Creating a Virtual Environment with Python](#creating-a-virtual-environment-with-python)
  - [IDE](#ide)
    - [JupyterLab](#jupyterlab)
    - [VSCode](#vscode)
  - [Git version control](#git-version-control)
    - [**nbconvert** jupyter core package](#nbconvert-jupyter-core-package)
    - [_jq_ much faster](#jq-much-faster)
      - [For powershell](#for-powershell)
    - [To display error when filter not configured](#to-display-error-when-filter-not-configured)
      - [1. Create a _check-nb-filter.sh_ script in root that checks if a notebook filter exists, here _nbstrip\_full_](#1-create-a-check-nb-filtersh-script-in-root-that-checks-if-a-notebook-filter-exists-here-nbstrip_full)
      - [2. Execute this in a notebook cell to add an additional _check-nb-filter_ filter to git config which invokes above script whenever a notebook is staged](#2-execute-this-in-a-notebook-cell-to-add-an-additional-check-nb-filter-filter-to-git-config-which-invokes-above-script-whenever-a-notebook-is-staged)
      - [3. Set .gitattributes to run _check-nb-filter_ for notebook files](#3-set-gitattributes-to-run-check-nb-filter-for-notebook-files)

## Creating a Virtual Environment with Python

```bash
# create virtual env
python -m venv .venv  # name can be the folder name

# install dep
pip install <dep>

# store requirements
pip freeze > requirements.txt

# store python version
python --version > python_version.txt

# git ignore the virtual env folder and notebook artifacts
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore

# install deps to reproduce env
pip install -r requirements.txt
```

## IDE

### JupyterLab

A better newer notebook IDE than the older jupyter notebook. Provides extensions like vscode allowing features like:

- Vim
- Git version control

```bash
pip install jupyterlab
jupyter lab
```

Con:

- Required to be pip installed each time in a virtual env
  - Alternatively, can be installed on a user level or in a conda env but pip install is still needed for python kernel

### VSCode

Equally good as JupyterLab. Advantage:

- No IDE specific pip install
- No metadata or cell output displayed using following settings

```json
"notebook.diff.ignoreMetadata": true,
"notebook.diff.ignoreOutputs": true
```

## Git version control

- This will clear the cell ouputs before staging a notebook
- Useful to ensure diffs show only changes in cells.

See [https://timstaley.co.uk/posts/making-git-and-jupyter-notebooks-play-nice/](https://timstaley.co.uk/posts/making-git-and-jupyter-notebooks-play-nice/)

### **nbconvert** jupyter core package

This local git filter depends on _nbconvert_ which comes with jupyter core packages (run jupyter --version)

```bash
git config filter.jupyternotebook.clean "jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR"
git config filter.jupyternotebook.required true
echo "*.ipynb filter=jupyternotebook" >> .gitattributes
```

### _jq_ much faster

_nbconvert_ is too slow so alternatively use _jq_, sed for json data, one caveat is this does not guarantee to conform to jupyter notebook spec but is much faster. _jq_ can be installed in a conda env.

```bash
git config filter.nbstrip_full.clean "jq --indent 1 \
        '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
        | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
        | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
        | .cells[].metadata = {} \
        '"
git config filter.nbstrip_full.smudge cat
git config filter.nbstrip_full.required true
echo "*.ipynb filter=nbstrip_full" >> .gitattributes
```

#### For powershell

```powershell
git config filter.nbstrip_full.clean 'jq --indent 1 \
        "(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
        | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
        | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
        | .cells[].metadata = {} \
        "'
```

### To display error when filter not configured

#### 1. Create a _check-nb-filter.sh_ script in root that checks if a notebook filter exists, here _nbstrip_full_

```bash
# check-nb-filter.sh
#!/bin/bash

if ! git config --get "filter.$1.clean"; then
  echo "Error: Filter '$1' is not defined" >&2
  exit 1
fi

exec git config --get "filter.$1.clean"
```

#### 2. Execute this in a notebook cell to add an additional _check-nb-filter_ filter to git config which invokes above script whenever a notebook is staged

```bash
!git config filter.check-nb-filter.clean "./check-nb-filter.sh nbstrip_full"
!git config filter.check-nb-filter.smudge "git config --get filter.nbstrip_full.smudge"
```

Note: If the notebook filter does not exist _check-nb-filter_ filter can only log this and cannot prevent staging of changes.

#### 3. Set .gitattributes to run _check-nb-filter_ for notebook files

```bash
# %echo *.ipynb filter=check-nb-filter>.gitattributes
```
