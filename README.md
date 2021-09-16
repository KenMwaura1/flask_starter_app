# flask_starter_app
simple flask starter app utilizing docker to showcase seasonal anime using jikanpy (myanimelist unofficial api).

## Docker Quickstart
**Using Docker is recommended, as it guarantees the application is run using compatible versions of Python and Node**.

Inside the app there a Dockerfile to help you get started. 

To build the development version of the app

```bash
docker build -t flask-starter-app .   
```

To run the app
```bash
 docker run --name=flask-app -p 5001:5000 -t -i flask-starter-app  
```
If everything went well, the app should be running on [localhost:5001](http://localhost:5001)
