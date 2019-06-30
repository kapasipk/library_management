# library_management
An implementation of REST APIs in Python Django, Postgres and Docker.

## Setup
The application has been containerized using Docker. To run this locally, [docker](https://docs.docker.com/install/) needs to be installed locally.

Once docker has been installed, use the following command to bring up the containers. This could take some time as it will fetch the intermediate images as well.
```
docker-compose up --build
```

This will bring up 2 containers - python django app server and postgres database. The server will be available at http://localhost:8000/

## Commands

To run commands inside the containers, use the following command - 
```
docker exec -it <container_name> /bin/bash

For eg: 
docker exec -it library_management_app_1 /bin/bash
docker exec -it library_management_db_1 /bin/bash
```

To migrate the database, run - 
```
docker exec -it library_management_app_1 python my_apps/manage.py test lib_app --noinput
```

To run tests, run - 
```
docker exec -it library_management_app_1 python my_apps/manage.py test lib_app --noinput
```

To connect to the postgres database, run -
```
docker exec -it library_management_db_1 psql --username=postgres
```

To generate the latest coverage report, run the following 2 commands. The first command generates the coverage report and the second and third command allows us to view the reports.
```
docker exec -it library_management_app_1 coverage run --source='.' my_apps/manage.py test lib_app

docker exec -it library_management_app_1 coverage html 		# View report as html
docker exec -it library_management_app_1 coverage report	# View report as command line output
```

## Code coverage - 99%
```
Name                                                    Stmts   Miss  Cover
---------------------------------------------------------------------------
my_apps/lib_app/__init__.py                                 0      0   100%
my_apps/lib_app/admin.py                                    1      0   100%
my_apps/lib_app/migrations/0001_initial.py                  6      0   100%
my_apps/lib_app/migrations/0002_auto_20190629_0640.py       4      0   100%
my_apps/lib_app/migrations/0003_book_deleted.py             4      0   100%
my_apps/lib_app/migrations/0004_auto_20190629_0954.py       5      0   100%
my_apps/lib_app/migrations/__init__.py                      0      0   100%
my_apps/lib_app/models.py                                  23      0   100%
my_apps/lib_app/serializers.py                              6      0   100%
my_apps/lib_app/tests.py                                   73      0   100%
my_apps/lib_app/views.py                                   47      0   100%
my_apps/manage.py                                          12      2    83%
my_apps/my_apps/__init__.py                                 0      0   100%
my_apps/my_apps/settings.py                                20      0   100%
my_apps/my_apps/urls.py                                    10      0   100%
---------------------------------------------------------------------------
TOTAL                                                     211      2    99%
```
