# Deployment

Use managed PostgreSQL, set a long unique `JWT_SECRET`, restrict `WEB_ORIGIN`, terminate TLS at a reverse proxy, and run `prisma migrate deploy` before serving traffic. Do not use the development Docker credentials in production.
