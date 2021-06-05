# URL Shortener app 
Save shortened URLS in a mongoDB database

## Project Structure 
```
├── Procfile
├── README.md
├── __init__.py
├── app.py
├── boot
│   ├── DBConnection.py
│   └── __init__.py
├── controllers
│   ├── UrlController.py
│   └── __init__.py
├── helpers
│   ├── __init__.py
│   └── helpers.py
├── middlewares
│   ├── ContentMiddleware.py
│   └── __init__.py
├── models
│   ├── UrlModel.py
│   └── __init__.py
├── requirements.txt
└── services
    ├── UrlService.py
    └── __init__.py
```


## APIs Base URLs
* `Deployed`: https://shortened-url-api.herokuapp.com/
* `Local`: http://127.0.0.1:5000/


## End points
`Deployed`:
* [GET] https://shortened-url-api.herokuapp.com/shortlinks
* [POST] https://shortened-url-api.herokuapp.com/shortlinks
* [PUT] https://shortened-url-api.herokuapp.com/shortlinks/{slug}

`Local`:
* [GET] http://127.0.0.1:5000/shortlinks
* [POST] http://127.0.0.1:5000/shortlinks
* [PUT] http://127.0.0.1:5000/shortlinks/{slug}


### Setup Locally
* ``Make sure you have python and pip installed``
* Open your terminal in the project directory
* Then type: ```pip install -r requirements.txt```


### Run
* Open your terminal in the project directory
* To start the server type: `python app.py`
* `Note`: Server will start on localhost on port 5000 [http://localhost:5000](http://localhost:5000)
