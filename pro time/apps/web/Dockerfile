FROM node:20-alpine
WORKDIR /app
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL
COPY package*.json ./
COPY apps/web/package.json apps/web/package.json
COPY apps/api/package.json apps/api/package.json
COPY packages/database/package.json packages/database/package.json
RUN npm install
COPY . .
RUN npm run build -w @pro-time/web
EXPOSE 3000
CMD ["npm","run","start","-w","@pro-time/web"]