# vision-static-file-server

vision static file server based on Nginx web server.

# docker-compose.yml
This server contains only docker-compose file and configuration of Nginx.
* The server can be upload files manually.
* The server enable the Cross-Origin Resource Sharing (CORS) policy for foreign web servers or web browsers.
* The volumes are redirect to host volume. Please reference the docker compose file.

# Uploading Tool
Once the uploading tool is done, we can use the tool upload our resources to this server (in the host not in the docker container).
