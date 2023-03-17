# Final Project - Cloud Computing

This is a Flask application in Python, using a Mongodb database. 

It has a login/register system, and a connected user can access to the list of all users. Every user has a role. If an user is admin, he can delete or edit users (changing username or role for example). You can log out at any moment.

The app is dockerized and can be run with Docker-Compose. It contains two containers, one for the flask app, and one for the mongo database. The database is persistant with volume. The containers are connected by a bridge network.

## Prerequisites
Before starting, you'll need to have the following tools installed on your system:

- Docker
- Docker Compose

## Clone the repository

First, clone the repository containing our Docker image and Docker Compose configuration:

`git clone https://github.com/Carla802/FinalProject.git`

And go inside the new directory.

`cd FinalProject/projet`

## Create a bridge network

Create a bridge network with the name of your choice. We choose network1 here.

`docker network create --driver bridge my-network-projet`

## Run your own containers with Docker-Compose

Instead of running containers manually, you can use Docker-Compose to manage your containers more easily.

### Run the containers

To get your Docker image created and run the containers defined in the Docker-Compose configuration, use the following command:

`docker-compose up --build`

The option --build force docker-compose to re build the images.

Now, your app is running on your port 5007. You can navigate in your browser to the localhost:5007 page.

On the default route, you can login with an existing account. If you don't have one, you can click on the link to register. Once you're connected, you have access to the list of all users and the content of the file TEST.txt

If you are an admin user, you can delete or edit any user.

### Stop the containers

To stop the containers, use the following command:

`docker-compose down`

This will stop and remove all containers defined in the Docker Compose configuration.

Congratulations! You have now successfully built and run containers using Docker-Compose.
