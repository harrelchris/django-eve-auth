if (!(Test-Path .venv)) {
    python -m venv .venv
}

.venv\Scripts\activate

python .\app\manage.py runserver
