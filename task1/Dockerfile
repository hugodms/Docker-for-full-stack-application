FROM node:10 AS builder

WORKDIR /app

COPY ./package.json ./

RUN npm install

COPY . .

RUN npm run build


FROM node:alpine

WORKDIR /app

COPY --from=builder /app ./

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]
