# python

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

## Git version control

- This will clear the cell ouputs before staging a notebook
- Useful to ensure diffs show only changes in cells.

See [https://timstaley.co.uk/posts/making-git-and-jupyter-notebooks-play-nice/](https://timstaley.co.uk/posts/making-git-and-jupyter-notebooks-play-nice/)

This local git filter depends on *nbconvert* which comes with jupyter core packages (run jupyter --version)

```bash
git config filter.jupyternotebook.clean "jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR"
git config filter.jupyternotebook.required true
echo "*.ipynb filter=jupyternotebook" >> .gitattributes
```

### *jq* much faster

*nbconvert* is too slow so alternatively use *jq*, sed for json data, one caveat is this does not guarantee to conform to jupyter notebook spec but is much faster. *jq* can be installed in a conda env.

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

1. Create a *is-filter.sh* script in root that checks if filter arg exists, here *nbstrip_full*
2. Execute notebook cell to add another *check-nb-filter* filter to git that invokes this script whenever a notebook is staged
3. Set .gitattributes to run *check-nb-filter* for notebook files

```bash
# is-filter.sh
#!/bin/bash

if ! git config --get "filter.$1.clean"; then
  echo "Error: Filter '$1' is not defined" >&2
  exit 1
fi

exec git config --get "filter.$1.clean"
```

```bash
!git config filter.check-nb-filter.clean "./is-filter.sh nbstrip_full"
!git config filter.check-nb-filter.smudge "git config --get filter.nbstrip_full.smudge"
# %echo *.ipynb filter=check-nb-filter>.gitattributes
```
