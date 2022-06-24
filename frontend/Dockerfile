FROM node:16

LABEL version="1.0"
LABEL description="React Fronten fot the wayuu_HR API"

WORKDIR /app

COPY ./package*.json ./

RUN npm install
RUN mkdir node_modules/.cache && chmod -R 777 node_modules/.cache

COPY . .

CMD ["npm", "run", "start"]