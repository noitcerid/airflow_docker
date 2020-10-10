# Airflow in Docker

## Project Purpose
This is really an introduction to getting started with Airflow. I feel most comfortable with Python, so leveraging Python with the ability to schedule tasks gives some very powerful options as I research replacements for SSIS and other less-flexible/scalable ETL/ELT tools.

Ultimately, I'd love to see this become a flexible data ingestion engine, with minimal configuration needed but that will take some more time to flesh out.

## Setup Steps
Getting started, I ran into some permissions problems early on with the volumes mounted needing to have those folders (and of course any sub-folders) to have full permissions in order to have permission in the container.

The `docker-compose` will handle the internal container permissions, but these also need to be run on the project volumes.

Commands run:
```
chmod -R 777 ./dags
chmod -R 777 ./data
chmod -R 777 ./logs
chmod -R 777 ./scripts
```
Obviously with some adjustment, they likely wouldn't need unlimited permissions so that's a to-do item prior to putting this in any sort of production setting (if mounted volumes needed to be persisted).

## Notes
Obviously, this is a work in progress (as many of my projects are), but I'm enjoying learning enough to be _dangerous_ while still being able to keep up the existing workload.