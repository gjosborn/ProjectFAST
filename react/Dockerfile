FROM node:21.6.1-alpine

ENV NODE_ENV=development

RUN mkdir -p /app

WORKDIR /app

COPY /fast/package*.json ./

RUN npm install

COPY ./fast .

EXPOSE 3000

CMD npm run dev