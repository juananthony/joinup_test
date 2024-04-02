Joinup challenge
================

## Pre-requisites
* Anaconda
* Redis
* Celery

## How to run locally

1. Clone the repository
2. Create a virtual environment using environment.yml file
3. Activate the virtual environment
4. Run Django migrations
5. Start Redis database
6. Start Celery worker
7. Run Django server

```bash
git clone
conda env create -f environment.yml
conda activate joinup
cd joinup
python manage.py migrate
celery -A joinup worker -l info
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
  * Curl example:
    ```bash
    curl -X POST http://<HOST>/api-token-auth/ \                                                                                                                                                                                                                               ─╯
         -H 'Content-Type: application/json' \
         -d '{
               "username": "juan@example.com",
               "password": "mySup3rS3cr3tP4ssw0rd"
             }'
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
  * Curl example:
    ```bash
    curl -X POST http://localhost:8000/api/v1/signup/ \                                                                                                                                                                                                                                ─╯
      -H 'Content-Type: application/json' \
      -d '{
           "name": "Juan Antonio",
           "last_name": "Jiménez",
           "email": "juan@example.com",
           "phone": "1234567890",
           "hobbies": "Read, Coding",
           "password": "mySup3rS3cr3tP4ssw0rd"
         }'
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
  * Curl example:
    ```bash
    curl -X GET http://<HOST>/api/v1/profile/ -H 'Authorization: Token 4278100a270ebad6ba5896edea3a21999da561eb'
    ```

## Further improvements
* Remove SQLite database and use PostgreSQL
* Add more tests
* Add more validations
* Add more fields to the user model
* Add user to admin panel

## Questions

### How many database queries does each endpoint make?
  * `POST /api-token-auth`
    * 1 query
  * `POST /api/<str:version_api>/signup`
    * 2 queries
  * `GET /api/<str:version_api>/profile`
    * 2 queries
### How many queries does the asynchronous part make?
  * No one
### Can you provide an example request (like a curl command) for each endpoint?
  * Already provided in the Endpoints section
### What did you think of the test? Did you like it? Did you find it easy, intermediate, or complex?
  * Intermediate. I really enjoyed working with Celery for the first time. 
### Was there any part of the test that you found confusing?
  * No
### Did you learn anything from this test?
  * Yes, I learned how to use Celery
### How long did it take you to complete the test?
* Between 3 and 4 hours in different periods
### What's the most fun thing you've ever developed? What do you enjoy developing the most?
* Design and implement the image uploading part of sesh where every user could upload images from anywhere in the world, and the instant these images were published they should be accessible in a very short time from anywhere in the world. For this, I used a CDN using a push strategy instead of pull so that the images were prewarms before being requested by the first user. This required a complex orchestration of origins from different buckets around the world.
### What do you hate developing the most?
* I don't hate anything, but I don't like to work with old technologies that are not maintained anymore.
### Do you have any quirks when it comes to developing? What are they?
* I like to use the latest technologies and best practices in my projects.
### Would you like to add anything extra? Is there a question you wished we had asked you?
* No
### After taking the test, do you have any additional questions about how we work? Would you change anything about the test to include something you consider important?
* No