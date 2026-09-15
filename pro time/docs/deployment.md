# Deployment

Build and start PostgreSQL plus Django with `docker compose up --build`. For production, set `DJANGO_DEBUG=False`, a long random `DJANGO_SECRET_KEY`, an exact `ALLOWED_HOSTS` list, HTTPS at a reverse proxy, and a managed PostgreSQL database. Run `py manage.py migrate` before serving the new release.