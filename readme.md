# Event-Manager Projekt

Ein Testprojekt im Rahmen des GFU Django Kurses.


## Aufgabe Nachmittag

- ein neues Environment anlegen und mit pip-tools und requirements.in-Dateien Django installieren
- ein neues Django-Projekt erstellen, zb. company_projekt
- zwei Models anlegen (1 : N Verbindung), zb. Blog und Artikel, Company und Employees, Warenkorb und Produkt
- Makemigrations und migrate
- auf der Shell ein paar Objekte anlegen

## virtuelles Environment  anlegen und Starten

    python -m venv .envs/companyenv
    .envs/companyenv/Scripts/activate
    (companyenv) pip install pip-tools

## Datei Struktur anlegen

    (companyenv) mkdir company_project
    cd company_project

    (companyenv) mkdir company_manager
    cd company_manager

    # requirements.in und requirements-dev.in erstellen
    (companyenv) pip-compile requirements.in
    (companyenv) pip-compile requirements-dev.in
    (companyenv) pip-sync requirements.txt requirements-dev.txt


## Neues Django Projekt erstellen

    (companyenv) django-admin startproject company_manager .
    (companyenv) python manage.py startapp company

## in den Settings registrieren

    INSTALLED_APPS = [
        ...
        "company",
        ...
    ]

## Legacy Datenbank einbinden

https://docs.djangoproject.com/en/4.2/howto/legacy-databases/