# PRO TIME TRACKER

**Track Time. Measure Progress. Work Smarter.**

Milestone 1 provides a production-minded foundation: a TypeScript npm-workspace monorepo, Next.js web app, Express REST API, PostgreSQL/Prisma data model, JWT authentication, role-based access control, dashboards, demo seed data, Docker, and tests.

## Quick start

1. Install Node.js 20+ and Docker Desktop.
2. Copy `.env.example` to `.env` and set a unique `JWT_SECRET`.
3. Run `npm install`.
4. Run `docker compose up -d postgres`.
5. Run `npm run db:generate && npm run db:migrate && npm run db:seed`.
6. Run `npm run dev`, then open http://localhost:3000.

Or start all containers: `docker compose up --build`. The API container applies schema generation and seed data at startup.

## Demo accounts (development only)

| Role | Email | Password |
|---|---|---|
| Admin | admin@protime.local | DemoPass123! |
| Manager | manager@protime.local | DemoPass123! |
| Employee | employee@protime.local | DemoPass123! |

## Commands

- `npm run dev` – web and API development servers
- `npm run build` – build all workspace applications
- `npm test` – API unit/API tests
- `npm run db:migrate` – create/apply the local Prisma migration
- `npm run db:seed` – seed development data

## Security and privacy

Passwords use bcrypt hashes; sessions are signed JWTs; API requests are validated, rate-limited, helmet-protected, CORS-restricted, and role-authorized. Set real secrets and HTTPS at deployment. No monitoring or screenshot collection is implemented in this milestone. Future monitoring must be opt-in, visible to employees, and limited by retention policies.

## Documentation

See `docs/architecture.md`, `docs/database.md`, `docs/api.md`, `docs/privacy.md`, and `docs/deployment.md`.
