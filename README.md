# Apache NIFi exersices

## Usage

### Step 1. Create and fill `.env`

create `.env` file in the folder `/app` <br>
```
touch app/.env
```
<br>
Fill it with next environment variables:

```.env
DB_HOST= your postgres host name
DB_PORT= your postgres port
DB_USER= your postgres api user
DB_PASS= password for your user api
DB_NAME= name of your database
```


### Build

Build: <br>
```
sudo docker-compose build --no-cashe
``` 
<br>Run:<br>
```
sudo docker-compose up
```

For running in background mode: <br>
```
sudo docker-compose up -d
```
