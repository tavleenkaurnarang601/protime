# Architecture

The workspace contains a Next.js web client (`apps/web`), Express API (`apps/api`), and Prisma database package (`packages/database`). The API is the authorization boundary. Browser tokens are held in session storage and sent as Bearer tokens; production deployments should use an httpOnly cookie/BFF pattern. PostgreSQL is the system of record.
