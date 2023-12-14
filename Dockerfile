FROM node:latest
WORKDIR /app
COPY . .

RUN yarn install
RUN yarn build

EXPOSE 3000

CMD ["/bin/bash", "-c", "yarn start"]

#run commands
#docker build . -t web
#docker run -p 3000:3000 web
#docker run -it -p 3000:3000 web bash