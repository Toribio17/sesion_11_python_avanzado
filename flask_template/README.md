# Flask-API-Template

API template made with Flask for reusable assets

Before running the application, please install the requirements using this command:

`pip install -r requirements.txt`

Add a .env file with the following environment variables[^note]:

```
OUTPUT_RESULTS_PATH=
FILES_INPUT_PATH=
ENVIRONMENT=
GENERAL_PATH=
MONGO_CONNECTION=
```

Run the server with:

`sh gunicorn.sh`

The application will be listening on port 5001

The available routes are:

[/](http://0.0.0.0:5001) -> It returns a welcome message <br />
[/users](http://0.0.0.0:5001/users) -> It returns a list of dummy users <br />
[/ocr](http://0.0.0.0:5001/ocr) -> Will process the PDF document, in the url <br />

For stopping the server, please press **Ctrl** + **C**

[^note]: Fill with the credentials of your Cloudant instance and put the name of the database you want to try in `CLOUDANT_DB` variable
