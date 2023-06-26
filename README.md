# Basic Flask Project Structure

## A Flask project structure for scalable web application

### Requirements

#### Installed:

- Flask
- python-dotenv

#### Create env:

```python
python3 -m venv env
source env/bin/activate
```

#### How to run

```python
flask run
```

```bash
< PROJECT ROOT >
│
├-- app/
│   ├-- api/
│   │   ├-- __init__.py
│   │   └-- users.py
│   ├-- auth/
│   │   └-- __init__.py
│   ├-- config/
│   │   ├-- environment.py
│   │   ├-- __init__.py
│   │   └-- __pycache__/
│   │       ├-- environment.cpython-310.pyc
│   │       └-- __init__.cpython-310.pyc
│   ├-- databases/
│   │   ├-- __init__.py
│   │   └-- schemas/
│   ├-- forms/
│   ├-- __init__.py
│   ├-- libs/
│   │   └-- __init__.py
│   ├-- models/
│   │   ├-- __init__.py
│   │   └-- user.py
│   ├-- __pycache__/
│   │   └-- __init__.cpython-310.pyc
│   ├-- resources/
│   │   └-- __init__.py
│   ├-- routes/
│   │   ├-- index.py
│   │   ├-- __init__.py
│   │   └-- __pycache__/
│   │       ├-- index.cpython-310.pyc
│   │       └-- __init__.cpython-310.pyc
│   ├-- static/
│   │   ├-- css/
│   │   │   └-- base.css
│   │   ├-- images/
│   │   │   └-- random_free_royalty_and_copyright_image.jpg
│   │   └-- js/
│   │       └-- base.js
│   ├-- templates/
│   │   ├-- accounts/
│   │   ├-- includes/
│   │   ├-- index/
│   │   │   └-- index.html
│   │   └-- layouts/
│   │       └-- base.html
│   ├-- tests/
│   │   └-- __init__.py
│   ├-- util/
│   │   └-- __init__.py
│   └-- views/
├-- README.md
└-- requirements.txt
```
