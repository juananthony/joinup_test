Joinup challenge
================

## How to run locally

1. Clone the repository
2. Create a virtual environment using environment.yml file
3. Activate the virtual environment
4. Run Django migrations
5. Run Django server

```bash
git clone
conda env create -f environment.yml
conda activate joinup
cd joinup
python manage.py migrate
python manage.py runserver
```

## Endpoints

* `POST /api-token-auth` - Get token
  * Headers:
    * Content-Type: application/json
  * Request body:
    ```json
    {
      "username": "juan@example.com",
      "password": "mySup3rS3cr3tP4ssw0rd"
    }
    ```
  * Response body:
    ```json
    {
      "token": "eyJ0eXAiOi"
    }
    ```
* `POST /api/<str:version_api>/signup` - Create a new user
  * Headers:
    * Content-Type: application/json
  * Request body:
    ```json
    {
      "name": "Juan Antonio",
       "last_name": "Jiménez",
       "email": "juan@example.com",
       "phone": "1234567890",
       "hobbies": "Read, Coding",
       "password": "mySup3rS3cr3tP4ssw0rd"
    }
    ```
* `GET /api/<str:version_api>/profile` - Get user profile
  * Headers:
    * Authorization: Token <token>
  * Response body:
    ```json
    {
      "name": "Juan Antonio",
      "last_name": "Jiménez",
      "email": "juan@example.com",
      "phone": "1234567890",
      "hobbies": "Read, Coding",
      "email_validated": false,
      "phone_validated":false
    }
    ```

## Endpoint calls

## Questions

