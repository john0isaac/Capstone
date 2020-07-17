# Capstone

This is my final nanodegree project and I'm so excited to finish it i thought of many ideas but none matched what they needed so i said to myself why don't i use all my knowldege to implement this final application.
The application can:

1) Display persons in our data base. persons should show all the needed information about them for employers.
2) Display industries for managers to edit them.
3) Delete persons or industries.
4) Add new person and require that they include all the information needed.
5) Add new industry by managers.
6) Search for persons based on a text query string.

Completing this app gave me the ability to structure plan, implement, and test an API - skills essential for enabling my future applications to communicate with others.

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Testing

To run the tests, run

```bash
dropdb capstone_test
createdb capstone_test
psql capstone_test < capstone_test.psql
python test_app.py
```

## API Documentation

### Getting Started

- Base URL For App: [Hosted APP on Heroku](https://john0isaac.herokuapp.com/)
- Authentication: [Auth0 to Generate Tokens](https://enactus-ma.auth0.com/login?state=g6Fo2SBscGdJbzBPb0lKYlNxaUk0TWtvMzVlckoyb1NvOEU1ZaN0aWTZIHl5ZzBlU3NuTllkcWZZb0t3YW1rd0RXM1NQOWZRLVUwo2NpZNkgYXZtYlJYQWNDY1RicGQyWkt5Y1JOUmdnVEhSam5SajQ&client=avmbRXAcCcTbpd2ZKycRNRggTHRjnRj4&protocol=oauth2&audience=john0isaac&response_type=token&redirect_uri=http://locahost:8080)

Before testing the live app export the manager and person tokens in your terminal session:

```bash
export Manager='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImgwUFNENjhqQVhYa1ZudDZPeW9RdCJ9.eyJpc3MiOiJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2OTE2NzQ1MDU5MzIyOTEwMzY3IiwiYXVkIjpbImpvaG4waXNhYWMiLCJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5NDk1MTY1OCwiZXhwIjoxNTk1MDM4MDU4LCJhenAiOiJhdm1iUlhBY0NjVGJwZDJaS3ljUk5SZ2dUSFJqblJqNCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6aW5kdXN0cmllcyIsImRlbGV0ZTpwZXJzb25zIiwiZ2V0OmluZHVzdHJpZXMgIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDpwZXJzb25zIiwicG9zdDppbmR1c3RyaWVzIiwicG9zdDpwZXJzb25zIl19.hihXPgBibFFYUTpjEryLnRMEY_ADGf9_A98PwaRzpCYwePOcXYHvK1sN0YGfvFHfyWsIfTH_xO6ErbNIk5eEEJ1nYeWcIt74NC06YLOV0HVex4QsMImxBGaUh7wdKi16iFbN8TFjliJOnsGlqaDFTePR_hNIuamBcs-hG3X_ULMIyOVI6AXq2lMxS82f-PRG1-YgDd5FYit-NXdWeJAjKPdNRRICAS7aBYj3zrEOCQXrHv415WtSukjahZLL2_zSNS4oMsG8WRWcZ5O2wXNui3Uw_6ZKuiHb2XYSEKsEtdXZEgjfksk6n5Y01wfMvHTmdU7q5Lh6Xdqh8I3hjtUuuQ'
```

```bash
export Person='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImgwUFNENjhqQVhYa1ZudDZPeW9RdCJ9.eyJpc3MiOiJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3OTkyMDkxOTg1MzY4MTQ0NTExIiwiYXVkIjpbImpvaG4waXNhYWMiLCJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5NDk1MjExMiwiZXhwIjoxNTk1MDM4NTEyLCJhenAiOiJhdm1iUlhBY0NjVGJwZDJaS3ljUk5SZ2dUSFJqblJqNCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cGVyc29ucyIsImdldDpwZXJzb25zIiwicGF0Y2g6cGVyc29ucyIsInBvc3Q6cGVyc29ucyJdfQ.bWmwYON5GYNKbObCJSFi-dLfmYocxoaY0ZZz4p_eyxUkPXiHL9-amOaGI4Um-SFYv6vvYlrqFLAY8N0HbbG4SFsin-Wog863xw5YYj-g7uV8s1KrkajOQ3LqkrM41VFT22WIm0Ypm-KDhue4vDeGrCjd1_mQqCQauWqhe6JxuIRtNODjK1XMbQbvrUqDld4It5P90tmtDo9-5BUJKai3lau6Ot9nee2qFM407RU_CS_WgTtCaUIeGuoSh2E5i0oOVlxf9lzyLnfBnjwACJbOBUU8NXj5EclWGtYf1Avjr94jPhabgBJkWIqWfRtSur5HKA6843GOHDlv-yulrR4ADw'
```

### Error handling

Invoking any of the following errors will return a JSON object in this format:

```JSON
{
  "success": False,
  "error": 400,
  "message": "bad request"
}
```

The API will return three error types when request fail:

- 400: Bad Request
- 405: Method Not Allowed
- 422: Not Processable
- 404: Resourse Not Found

And Authentication Errors 401, 403

### Endpoints

**GET /industries**

* General:

  - Fetches a dictionary of industries consists of id and industry
  - Request Arguments: None
  - Returns:  industries dictionary consists of id and industry, total industries number, success value.
* Sample:`curl -H "Authorization: Bearer ${Manager}" https://john0isaac.herokuapp.com/industries`

```JSON
{
  "industries":[
    {"id":1,"industry":"Accountants"},
    {"id":2,"industry":"Agriculture"},
    {"id":3,"industry":"Airlines"},
    {"id":4,"industry":"Banking"},
    {"id":5,"industry":"Construction"},
    {"id":6,"industry":"Dairy"},
    {"id":7,"industry":"Education"},
    {"id":8,"industry":"Farming"},
    {"id":9,"industry":"Health"},
    {"id":10,"industry":"Labor"}
    ],
  "success":true,
  "total_industries":10
}
```

**GET /persons**

* General:

  - Fetches list of persons and total number of persons
  - Request Arguments: None
  - Returns: A list of persons, number of total persons, and success value.
* Sample:`curl https://john0isaac.herokuapp.com/persons -H "Authorization: Bearer ${Person}"`

```JSON
{
  "persons":[
    {"city":"Cairo","facebook_line":"www.facebook.com/john0isaac","id":1,"industry_id":3,"info":"I like reading books a lot and i like going to the institue of arts to watch cute things","name":"John Isaac","phone":"451-879-454","seeking_job":true,"website":"john0isaac.herokuapp.com"},
    {"city":"Russia","facebook_line":"www.facebook.com/marie0curie","id":2,"industry_id":2,"info":"I like playing in my labrotory with chemical stuff to discover new things","name":"Marie Curie","phone":"232-435-235","seeking_job":false,"website":"marie0curie.herokuapp.com"},
    {"city":"America","facebook_line":"www.facebook.com/albert0einstein","id":3,"industry_id":1,"info":"I like the concept of time and that it is relative to other things can be different","name":"Albert Einstein","phone":"294-234-233","seeking_job":false,"website":"albert0einstein.herokuapp.com"},
    {"city":"Ohio","facebook_line":"www.facebook.com/james0charles","id":4,"industry_id":4,"info":"My mother used to say to me that one day i will be an amazing man","name":"James Charles","phone":"342-644-646","seeking_job":true,"website":"james0charles.herokuapp.com"}
    ],
  "success":true,
  "total_persons":4
}
```

**GET /categories/{category.id}/questions**

* General:

  - Fetches The current category id, a list of questions inside the category every question consists of a dictionry including answer, category, difficulty, id, question and total number of questions
  - Request Arguments: Category ID
  - Returns: A list of questions, number of total questions, current category and categories, success value.
* Sample:`curl http://127.0.0.1:5000/category/1/questions`

```JSON
{
"current_category": 1,
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 3
}
```

**DELETE /questions/{question.id}**

* General:

  - Deletes a certain question by a given ID if exists
  - Request Arguments: Question id
  - Returns: success value.
* Sample:`curl http://127.0.0.1:5000/questions/23 -X DELETE`

```JSON
{
  "success": true
}
```


**POST /questions**

* General:

  - Creates a new question using the submitted question and answer text, difficulty and category score.
  - Request Arguments: question, answer, category, difficulty
  - Returns: success value.
* Sample:`curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "What is the biggest pyramid?","answer": "The great pyramid", "category": 4, "difficulty": 2 }'`

```JSON
{
  "success": true
}
```

**POST /questions/search**

* General:

  - Search for any question using the submitted search term which is a substring of the question.
  - Request Arguments: Search Term
  - Returns: current category, question, answer, category, difficulty, id, success value, total questions.
* Sample:`curl -H "Authorization: Bearer ${Manager}" https://john0isaac.herokuapp.com/questions/search -X POST -H "Content-Type: application/json" -d '{"search": "pyramid"}'`

```JSON
{
"current_category": [
    4
  ],
  "questions": [
    {
      "answer": "The great pyramid",
      "category": 4,
      "difficulty": 2,
      "id": 25,
      "question": "What is the biggest pyramid?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```



**POST /quizzes**

* General:

  - Gets questions to play the quiz.
  - Request Arguments: Previous questions, Quiz category 
  - Returns: success value, queestion, answer, category, difficulty, question id.
* Sample:`curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"id": 1, "type": "Science"}}'`

```JSON
{
 "question": {
    "answer": "Alexander Fleming",
    "category": 1,
    "difficulty": 3,
    "id": 21,
    "question": "Who discovered penicillin?"
  },
  "success": true
}
```
curl http://127.0.0.1:5000/persons/14 -X PATCH -H "Content-Type: application/json" -d '{"seeking_job":true}'

curl http://127.0.0.1:5000/persons/14 -X PATCH -H "Content-Type: application/json" -d '{"seeking_job":false, "industry_id":23}'


 curl http://127.0.0.1:5000/persons/14 -X PATCH -H "Content-Type: application/json" -d '{"seeking_job":true, "industry_id":23}'

curl http://127.0.0.1:5000/persons/14 -X PATCH -H "Content-Type: application/json" -d '{"name":"tata mama", "city":"New Jersy", "phone":"864-029-546", "website":"tata0mama.herokuapp.com", "facebook_link":"www.facebook.com/tata0mama", "seeking_job":true, "industry_id":23, "info": "hey there iam using whatsapp"}'

curl http://127.0.0.1:5000/persons/14 -X PATCH -H "Content-Type: application/json" -d '{"seeking_job":true}'

curl http://127.0.0.1:5000/persons/search -X POST -H "Content-Type: application/json" -d '{"search":"whatsapp"}'

curl http://127.0.0.1:5000/persons/14 -X PATCH -H "Content-Type: application/json" -d '{"name":"tata mama", "city":"New Jersy", "phone":"864-029-546", "website":"tata0mama.herokuapp.com", "facebook_link":"www.facebook.com/tata0mama", "seeking_job":false, "industry_id":23, "info": "hey there iam using whatsapp"}'

curl http://127.0.0.1:5000/persons -X POST -H "Content-Type: application/json" -d '{"name":"tata mama", "city":"New Jersy", "phone":"864-029-546", "website":"tata0mama.herokuapp.com", "facebook_link":"www.facebook.com/tata0mama", "seeking_job":true, "industry_id":23}'

curl http://127.0.0.1:5000/persons/search -X POST -H "Content-Type: application/json" -d '{"search":"like"}'

curl http://127.0.0.1:5000/industries -X POST -H "Content-Type: application/json" -d '{"industry":"toto"}'

curl http://127.0.0.1:5000/industries?page=2

curl http://127.0.0.1:5000/industries