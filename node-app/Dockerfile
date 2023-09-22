FROM node:14
WORKDIR /app

COPY node-app/package*.json ./

RUN npm install
COPY node-app/ .

EXPOSE 3000

CMD [ "node", "main.js" ]
