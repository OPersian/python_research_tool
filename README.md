## Tool to research Python programs

So far, the next programs are available for research:

- arrays addition;
- matrices multiplication.

Available tasks' parameters are as follows:

- data size;
- data type.

Tasks can be configured and run from <URL-TBD>.

The research itself is the results of programs execution: time taken and space taken.

CSV reports with results are available for download from <URL-TBD>.

### Application Requirements

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)


### Installation

Cloning git-repository:
```
git clone git@github.com:OPersian/python_research_tool.git
```

Changing the work directory to the cloned project root dir:
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

### Testing

TBD

```
docker exec -it python_research_tool python manage.py test --settings=python_research_tool.settings
```

### Future Improvements

Description TBD
