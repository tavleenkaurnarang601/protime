# PRO TIME TRACKER

**Track Time. Measure Progress. Work Smarter.**

The entire application server is Python/Django. The UI is rendered by Django templates: no Node.js, React, TypeScript, npm, or browser JavaScript is required for Milestone 1.

## Stack

- Python 3.14+, Django 5.2
- PostgreSQL (production/local Docker); SQLite fallback for quick local development
- Django built-in, CSRF-protected session authentication and password hashing
- Server-rendered HTML and CSS

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
Copy-Item .env.example .env
# Set environment variables from .env in your shell, or use Docker PostgreSQL.
py manage.py migrate
py manage.py seed_demo
py manage.py runserver
```

Open http://127.0.0.1:8000. For PostgreSQL plus the application use `docker compose up --build`.

## Demo accounts (development only)

| Role | Email | Password |
| --- | --- | --- |
| Admin | admin@protime.local | DemoPass123! |
| Manager | manager@protime.local | DemoPass123! |
| Employee | employee@protime.local | DemoPass123! |

## Useful commands

- `py manage.py migrate` — apply schema migrations
- `py manage.py seed_demo` — create idempotent sample data
- `py manage.py test` — run the Python test suite
- `py manage.py createsuperuser` — access the Django admin at `/admin/`

## Security and privacy

Django’s password hashing, CSRF protection, ORM parameterization, secure session cookie settings, X-Frame-Options and content-type protections are enabled. Use a unique `DJANGO_SECRET_KEY`, production HTTPS, and `DJANGO_DEBUG=False` when deploying. This milestone collects no screenshots, keyboard data, application data, website data, or idle activity.