

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/)
(which comes with [pip](https://pip.pypa.io/en/stable/)) installed on your computer. 

Additionally, you can also manage Python dependencies through Poetry, in which case you'll need to install 
[Poetry](https://python-poetry.org/docs/#installation).

---

From your command line (PIP): <br>
NOTE: you need to create a Python environment firs, which is not needed with Poetry

```bash
# Clone this repository
$ git clone https://github.com/jlorenzo681/stylesage-coupons.git

# Go into the repository
$ cd stylesage-coupons

# Install dependencies
$ pip install

# Run the app
$ streamlit run src/coupons.py
```

---

From your command line (Poetry): <br>

```bash
# Clone this repository
$ git clone https://github.com/jlorenzo681/stylesage-coupons.git

# Go into the repository
$ cd stylesage-coupons

# Install dependencies and create venv
$ poetry install

# Enter venv
$ poetry shell

# Run the app
$ streamlit run src/coupons.py
```