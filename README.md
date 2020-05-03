# Crud Application

#### Start the application.
1.  Take the clone of the repository.
```
	git clone https://github.com/AI4Finance/CRUD.git
```

2. Configure the database into the .env file. .env file available into the project root directory. below the the dummy db settings.
```
DB_NAME=crud_db
DB_USER=root
DB_PASSWORD=root
DB_HOST=127.0.0.1
DB_PORT=3306
```
3. Build the docker image.
```
 docker-compose -f docker-compose.yml build
```
4. Up docker image(run the application).
```
docker-compose -f docker-compose.yml up --no-build -d
```
