# Django-PostgreSQL-Todo-Application
Django - PostgreSQL Todo Application

## Installation

```bash
mkdir todo
cd todo
pipenv install django
pipenv shell
django-admin startproject todo .
python3 manage.py runserver 7000
python3 manage.py startapp todoplayground
```
- In VSCODE, view > command pallette > Then type Python: Select Interpreter. Then select pipenv related path.
- Update INSTALLED_APPS with "todoplayground" in settings.py

```
pipenv install faker
pipenv install django-bootstrap5
pipenv install psycopg2-binary
pipenv install python-dotenv
```

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 create_dummy_tasks.py
python3 manage.py runserver
```
