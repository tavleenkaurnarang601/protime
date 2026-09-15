# Architecture

PRO TIME TRACKER uses one Python/Django application. Django templates render the web interface, Django views enforce authentication and role-aware access, and Django ORM is the only database access layer. PostgreSQL is used in Docker/production; SQLite is a local fallback. No Node.js runtime is required.