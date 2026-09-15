FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
COPY apps/api/package.json apps/api/package.json
COPY packages/database/package.json packages/database/package.json
RUN npm install
COPY . .
RUN npm run prisma:generate -w @pro-time/database && npm run build -w @pro-time/api
EXPOSE 4000
CMD ["sh","-c","npm run prisma:push -w @pro-time/database && npm run prisma:seed -w @pro-time/database && npm run start -w @pro-time/api"]