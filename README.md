## Tool to research efficiency and performance of Python programs

Development of a tool to research efficiency and performance of Python programs.

### Application Requirements
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)


### Installation

Cloning git-repository:
```
git clone git@github.com:OPersian/python_research_tool.git
```

Changing the work directory to cloned project root dir:
```
cd python_research_tool
```

Build the application (might need to use `sudo`):
```
docker-compose -f docker-compose-local.yml build
```

Run the application:
```
docker-compose -f docker-compose-local.yml up
```

Run and rebuild the application:
```
docker-compose -f docker-compose-local.yml up --build
```
