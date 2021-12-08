
# Welcome to Weather Station Rasp!

This repository contains the back-end and front-end services.

## App Technologies


* Flask // pip install Flask

Front-end:

- HTML5
- JQuery

Back-end :

- Python 3.8 (Flask framework and others)
- Firebase 

## Project Structure

This app uses Flask to create a mini REST API by making requests to the Firebase temperature and humidity database in order to monitor and simulate a weather station using the Raspberry Pi.

#### Client Application

A Flask view is used to serve the `index.html` as an entry point into the app at the endpoint `/`.


#### Important Files

| Location                  |  Content                                   |
|---------------------------|--------------------------------------------|
| `/app.py`                 | Flask Application                          |
| `/templates/index.html`   | Html Application Entry Point (`/`)         |
| `/static/js/script.js`    | JS Application Entry Point                 |
| `/static/css/style.css`   | CSS Style Entry Point                      |


## API

* `GET/POST/ /`

## How to run

## Installation

Before getting started, you should have the following installed and running:

- [X] Python 3.8 
- [X] Pipenv (pip install pipenv)

##### Project and Dependencies

* Clone this repository:

	```
	git clone https://github.com/theusdmatos/flask_rasp_weather_station_facamp.git
	```
* Enter the project directory
	
	```
	cd flask_rasp_weather_station_facamp
	```
* Setup virtual environment, install dependencies, and activate it:

	```
	pipenv install -r requirements.txt
	```
	```
	pipenv shell
	```


## Development Server

Run Flask Api development server:

```
python app.py
```
