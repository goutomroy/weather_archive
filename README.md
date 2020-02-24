# Take-Home Assignment

Please try to complete as many problems as possible within the allotted time frame. In general, the problems are designed to be completed sequentially. But if you seem to be stuck on a problem. Feel free to skip ahead to the next.

## Problems
[Problem 1 - Parsing an Archive File (2 hours)](problems/PROBLEM_1.md#problem-1---parsing-an-archive-file)

[Problem 2 - Weather Observations API (2.5 hours)](problems/PROBLEM_2.md#problem-2---weather-observations-api)

[Problem 3 - Weather Archive API (1.5 hours)](problems/PROBLEM_3.md#problem-3---weather-archive-api)

[Problem 4 - Asynchronous Archive File Processing (2 hours)](problems/PROBLEM_4.md#problem-4---asynchronous-archive-file-processing)

[Problem 5 - Parsing a Binary Archive File (2 hours)](problems/PROBLEM_5.md#problem-5---parsing-a-binary-archive-file)

## Deliverables
The deliverables for each problem is just the source code. Each problem builds upon another, so there is no need to separate source code by problem. Please submit this same folder back to MDPPS upon completion.

Feel free to initialize this folder as a git repo, make commits to the git repo, and return the .git folder along with source code so that we can review the git history, but this is completely optional.

## Docker
We've also added a [Dockerfile](Dockerfile) for building a simple docker image for this web app, as well as a [docker-compose.yml](docker-compose.yml) file that will spin up a web container, a worker container, a Postgres container, a Rabbitmq container, and a Redis container. You can choose to use all or none of these containers (or Docker in general) for your development and testing.

Feel free to modify any or all of the Docker tooling to suit your needs and tech stack.

## Django
If you choose to implement the API problems with Django, there is already a base django project set up in the **src** folder. You would just need to add one or more apps to this Django project in order to add the required functionality to this Django-based API.

The docker-compose.yml file already defines a web service for running the django runserver.

Using Test is not required, but is preferred.

## Celery
The docker-compose.yml file already defines a worker service for running a celery worker. If you choose to use this worker for testing, note that **celery workers do not auto-reload** upon code changes.
