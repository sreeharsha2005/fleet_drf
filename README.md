[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)


# FLEET DATA - DJANGO REST FRAMEWORK

### Block diagram
<img width="644" alt="Screenshot 2025-04-19 at 11 54 18 PM" src="https://github.com/user-attachments/assets/9c6a6ae9-6657-43d8-b22c-2d7784f4f823" />


### Introduction
This module does the following operations:
* Create Dynamodb tables and store the received data onto respective tables
* Expose REST APIs to perform CRUD operations on Vehicle Data, Vehicle Operating Data, User Data and Driver data

### REST-API overview
<img width="787" alt="Screenshot 2025-04-19 at 11 50 00 PM" src="https://github.com/user-attachments/assets/1a609294-d303-4185-a9c3-541fbcb1cdcc" />


### Python virtual environment setup
Navigate to the project directory (base directory) where this README file is present
Run the below command to install python virtual environment

```
python3 -m venv env
source env/bin/activate
```

### Install requirement python packages
Run the below command to install the necessary packages listed in requirements file

```
pip3 install -r requirements.txt
```

### Pre-req
Run the below commands for getting dynamodb-local database up and running on local machine
```
docker run -d -p 8000:8000 amazon/dynamodb-local
```
To view the dynamodb-local data on GUI, we can either install dynamodb-admin or NoSQL workbench tool
```
npm install -g dynamodb-admin
```
Run the below command for attaching the dynamodb-admin tool to your database
```
AWS_REGION=localhost AWS_ACCESS_KEY_ID=08qlka AWS_SECRET_ACCESS_KEY=suyfvm dynamodb-admin --dynamo-endpoint=http://localhost:8000
```

### To run the project
Run the below command to start the server on port 8010
```
python3 manage.py runserver 8010
```

### To view the Swagger-UI
To view Swagger GUI for all the endpoints implemented, run the below command in browser
```
http://localhost:8010/swagger-ui/
```

### To view the dynamodb-local data on UI
Once you have installed and run dynamodb-admin, paste the below command in browser
```
http://localhost:8001
```
