
# Task Manager

Lightweight Django-based task management application for creating, updating and tracking tasks locally.

Badges: [build] [coverage] [license]

## Project overview

This repository contains a small Django web application named `task_manager` with a single app `manager` that implements basic task CRUD, templates, and database migrations. It is intended as a starter project or learning/example app you can extend.

Directory highlights

- `manage.py` — Django CLI entrypoint.
- `task_manager/` — Django project package containing `settings.py`, `urls.py`, `wsgi.py` and ASGI configuration.
- `manager/` — Django app with models, views, forms, templates and migrations.
- `db.sqlite3` — default SQLite database used for local development.

This README documents how to get the project running locally, run tests, and where to look for important files.

## Requirements

- Python 3.10+ (3.8+ may work but 3.10+ recommended)
- pip
- (Optional) `poetry` or `pipenv` if you prefer those workflow tools

The project uses SQLite by default (no DB server required). If you want PostgreSQL or another DB, update `task_manager/settings.py` accordingly and set appropriate environment variables.

## Quick start (Windows - PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

If you have a `requirements.txt` (not present by default), run:

```powershell
pip install -r requirements.txt
```

Alternatively, if the project uses `pyproject.toml`/Poetry:

```powershell
poetry install
```

At minimum, install Django:

```powershell
pip install "Django>=4.0"
```

3. Apply migrations and create a superuser

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server

```powershell
python manage.py runserver
```

Open the site at `http://127.0.0.1:8000/` and the admin at `http://127.0.0.1:8000/admin/`.

## Project usage

- The main app is `manager` — look in `manager/views.py`, `manager/models.py`, and `manager/templates/` for the UI.
- Templates: `manager/templates/` contains `base.html`, `home.html`, `tasks.html`, `task_create.html`, and `task_update.html`.
- Migrations are stored under `manager/migrations/` and have been included for schema history.

## Database & migrations

- This project ships with SQLite configured by default via `task_manager/settings.py` and a `db.sqlite3` file at the repository root for quick local development.
- To run migrations:

```powershell
python manage.py migrate
```

- If you switch to PostgreSQL or another engine, update `DATABASES` in `task_manager/settings.py` and set any required environment variables.

## Running tests

Run Django's test suite with:

```powershell
python manage.py test
```

If you add `pytest` to the project, you can run `pytest` instead.

## Common development tasks

- Start server: `python manage.py runserver`
- Create superuser: `python manage.py createsuperuser`
- Shell with project context: `python manage.py shell`
- Make a new migration after changing models: `python manage.py makemigrations` then `python manage.py migrate`

## Configuration

- `task_manager/settings.py` contains the core configuration. For local development the default settings work out of the box.
- Important settings you may want to set via environment variables in production:
	- `DEBUG` — `False` in production
	- `SECRET_KEY` — replace with a strong secret
	- `ALLOWED_HOSTS` — set your hostnames

For production deployments, configure a production-ready database (Postgres), static files handling (WhiteNoise, S3), and HTTPS.

## Static files

For development, Django serves static files automatically. For production, run:

```powershell
python manage.py collectstatic
```

and use a proper static files server or CDN.

## Security notes

- Do not commit `SECRET_KEY` or other secrets to source control.
- Rotate secrets if they are ever exposed.

## Deployment (brief)

Example using Docker (simple):

1. Create a `Dockerfile` and `docker-compose.yml` for the project (not included by default).
2. Build and run with Docker Compose, then point a reverse proxy (nginx) to the app.

For simple deployments, a typical flow is:

```powershell
docker build -t task-manager:latest .
docker run -e SECRET_KEY="<secret>" -p 80:8000 task-manager:latest
```

## Contributing

If you'd like to contribute:

1. Fork the repo.
2. Create a feature branch: `git checkout -b feat/my-feature`.
3. Make changes, add tests when appropriate.
4. Run `python manage.py test` and linters.
5. Open a pull request describing the change.

Please avoid committing secrets or large binary files.

## Troubleshooting

- Database errors: ensure migrations have been applied: `python manage.py migrate`.
- Port in use: the default dev server uses port 8000; change with `python manage.py runserver 0.0.0.0:8001`.
- Template errors: check `manager/templates/` for missing template names or context keys.

## Tests and CI

- This project uses Django's built-in testing framework. Add CI workflows in `.github/workflows/` to run `python manage.py test` on push/PR.

## License

This project does not include a license file by default. If you want to open-source it, consider adding an `LICENSE` file (for example MIT).

## Where to look next

- `manager/models.py` — task model and fields.
- `manager/views.py` — views and endpoints.
- `manager/forms.py` — forms used for create/update flows.
- `manager/templates/` — HTML templates used by views.

If you want, I can also:
- add a `requirements.txt` or `pyproject.toml` dependency spec
- scaffold a `Dockerfile` and `docker-compose.yml`
- add a basic GitHub Actions workflow to run tests

---

Updated on: 2025-12-31

