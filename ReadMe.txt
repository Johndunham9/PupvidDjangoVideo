Running locally

docker compose build .

docker-compose up

The local port for the mysql container is being mapped in docker-compose.yml from 3307 to 3306. This is visible if you execute

docker-compose ps

The local filesystem containing the code is being mounted into the web container, so changes in your local filesystem should be reflected in the container's filesystem.

You can run a django migrate with this command:

docker-compose exec web python manage.py migrate

To get "into" the web container, execute

docker-compose exec web bash

To see the logs that each container is putting into stdout, execute

docker-compose logs <container_name(web|db)>
