FROM node:16-alpine

# Create app directory
WORKDIR /app

RUN rm -rf node_modules
RUN npm install -g npm@8.5.3
RUN npm cache clean --force

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY . .
# COPY package*.json ./

RUN npm install --legacy-peer-deps
# If you are building your code for production
# RUN npm ci --only=production
RUN npm run build
# Bundle app source

# COPY build ./build
RUN npm install express
RUN mv ./dist/tradingfrontend/* ./dist
 
EXPOSE 8080
CMD [ "node", "/app/server.js"]
    