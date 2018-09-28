# Fast Food Fast APIs

Contains all APIs for the Fast food fast web application which is an online food application.

[![Build Status](https://travis-ci.org/cleopasrotich/fast_foods_v1.svg?branch=master)](https://travis-ci.org/cleopasrotich/fast_foods_v1)[![Coverage Status](https://coveralls.io/repos/github/cleopasrotich/fast_foods_v1/badge.svg)](https://coveralls.io/github/cleopasrotich/fast_foods_v1)


## Endpoints used

| Method  | Endpoint | Description |
| ------- | -------  | ----------- |
| POST    | '/fast_foods/api/v1/orders' | post all the orders |
| GET     | '/fast_foods/api/v1/orders' | recieve all orders |
| GET_one | '/fast_foods/api/v1/orders/<int:order_id>' | get only one order id |
| PUT     | '/fast_foods/api/v1/orders/<int:order_id>' | edit a specific order |
| DELETE  | '/fast_foods/api/v1/orders/<int:order_id>' | delete a specific order |


*you should have all the above endpoints working smoothly*

## Follow the instructions below to get started

1. make a new directory and install your venv with this line:

   $*python3 -m venv venv*

1. activate your venv :

    $. *venv/bin/activate*

1. clone the repo :

    $*git clone https://github.com/cleopasrotich/fast_foods_v1*

1. install some requirements of the project:

    $*pip install -r requirements.txt*

1. run tests with this command:

    $*nosetests --with-coverage --cover-package=app*

1. run the app with this command on activated venv:

    $*export FLASK_APP=run.py* then
    $*flask run*

1. when venv is not activated just run:

    $*python run.py*

## Screenshots of the API test on Postman.

![GEt_all](pics/Get_all.png)

![GEt_one](pics/get_one.png)
