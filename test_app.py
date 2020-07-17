import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db


class JohnTestCase(unittest.TestCase):
    """This class represents john test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        database_name = "capstone_test"
        self.database_path = "postgresql://{}@{}/{}".format('postgres:davinchi2020','0.0.0.0:5432', database_name)
        setup_db(self.app, self.database_path)

        self.new_person = {
            'name': 'Hossam Okasha',
            'info': 'young engineer who is willing to learn new things',
            'city': 'Giza',
            'phone': '343-686-594',
            'website': 'hossam0okasha.herokuapp.com',
            'facebook_link': 'www.facebook.com/hossam0okasha',
            'seeking_job': True,
            'industry_id': 1
        }

        self.new_industry = {
            'industry': 'Engineering',
        }
        self.manager = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImgwUFNENjhqQVhYa1ZudDZPeW9RdCJ9.eyJpc3MiOiJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2OTE2NzQ1MDU5MzIyOTEwMzY3IiwiYXVkIjpbImpvaG4waXNhYWMiLCJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5NDg2MzE3OSwiZXhwIjoxNTk0OTQ5NTc5LCJhenAiOiJhdm1iUlhBY0NjVGJwZDJaS3ljUk5SZ2dUSFJqblJqNCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6aW5kdXN0cmllcyIsImRlbGV0ZTpwZXJzb25zIiwiZ2V0OmluZHVzdHJpZXMgIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDpwZXJzb25zIiwicG9zdDppbmR1c3RyaWVzIiwicG9zdDpwZXJzb25zIl19.cg0fS7-I2yMT0_xn2Pu_S5H_sPCE2AligO7nXMuXIIu-JNciB_W64er1XGXl7OdGWisQ_A1yW6bk1qwZ0w7WnUg1fF86C7FrEf7sCdp3Gf4kMeM3wCAkZ9vD2irg0h1ISkDzlh3NEcFnZDggHDY_lJ6rNfX-f6ZLsUBqE9nJpM5R0sgpUnTSZI_fBZy2iT4veedwkwyXEtzPTs44x2GWPW8DXp6xPN1FAuZelW75swCwS8gF1FgCmcz4eb-tfYBUJ758FVIwU6SFmw4NfKSA02phaUkRgR_Ztx7IFgfixAL1vvQWjRX9f4wnQoeHurLTRVP5qWzwUy8EvnZ_09tQlQ'
        self.person = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImgwUFNENjhqQVhYa1ZudDZPeW9RdCJ9.eyJpc3MiOiJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3OTkyMDkxOTg1MzY4MTQ0NTExIiwiYXVkIjpbImpvaG4waXNhYWMiLCJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5NDg2MzI0OCwiZXhwIjoxNTk0OTQ5NjQ4LCJhenAiOiJhdm1iUlhBY0NjVGJwZDJaS3ljUk5SZ2dUSFJqblJqNCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cGVyc29ucyIsImdldDpwZXJzb25zIiwicGF0Y2g6cGVyc29ucyIsInBvc3Q6cGVyc29ucyJdfQ.PMmNWzFOxcLe7G5bbTDGxixKrzu4T9sxIHOpBuvC2SMAxUqODzGd0KENo5eMnsQUC2ujLfraoXXphZVek2kZCurkmU2VAO-OOzCynv5diANOjQ7Gb1YTlGcDuqhztg2g_rdqs-zsMsoJ4X4zKxcX8hrVY6mQiQCLgR1HkDIBa0uoo4jjjuGTwSdjqfx1AxTKcozrHSQiw6SM87Wi_AsHDmhbRosIsgWg6gz4LraJ8UVGwkGCRk7VNQUvrc1h8MoY4Lv59Aj1goPhMYbkstbqqDOkxsbAp6Jpm6whySh0wKXH-k4W5157QM53uvRuZXIrBM45GuVTK91_5NfQ1bkIXg'
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after each test"""
        pass

    
    def test_404_no_persons_found_to_retrieve(self):
        """Test 404 no persons found to retrieve"""
        res = self.client().get('/persons', headers={'Authorization': 'Bearer ' +self.manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resourse not found')
    
    def test_404_no_industries_found_to_retrieve(self):
        """Test 404 no data found to retrieve"""
        res = self.client().get('/industries', headers={'Authorization': 'Bearer ' +self.manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resourse not found')

    def test_create_new_industry(self):
        """test create new question"""
        res = self.client().post('/industries', headers={'Authorization': 'Bearer ' +self.manager}, json=self.new_industry)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['industry'])

    def test_422_sending_unprocessable_data_to_industries(self):
        """test 422 sending unprocessable data to industries"""
        res = self.client().post('/industries', headers={'Authorization': 'Bearer ' +self.manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')   

    def test_403_unauthorized_creation_of_new_industry(self):
        """test 403 unauthorized creation of new question"""
        res = self.client().post('/industries', headers={'Authorization': 'Bearer ' +self.person}, json=self.new_industry)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403 )
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permissions not found.')

    def test_create_new_person(self):
        """test create new person"""
        res = self.client().post('/persons', headers={'Authorization': 'Bearer ' +self.person}, json=self.new_person)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['person'])

    def test_422_sending_unprocessable_data_to_persons(self):
        """test 422 sending unprocessable data to persons"""
        res = self.client().post('/persons', headers={'Authorization': 'Bearer ' +self.person})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable') 

    def test_401_no_auth_to_create_new_person(self):
        """test 401 no auth to create new person"""
        res = self.client().post('/persons', json=self.new_person)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401 )
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_retrive_industry(self):
        """Test retrieve industry"""
        res = self.client().get('/industries', headers={'Authorization': 'Bearer ' +self.manager})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['industries'])
        self.assertTrue(data['total_industries'])

    def test_retrive_persons(self):
        """Test retrieve persons"""
        res = self.client().get('/persons', headers={'Authorization': 'Bearer ' +self.manager})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['persons'])
        self.assertTrue(data['total_persons'])

    def test_search_for_a_person(self):
        """Test search for a person"""
        res = self.client().post('/persons/search', headers={'Authorization': 'Bearer ' +self.manager}, json={'search': 'engineer'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['persons'])
        self.assertEqual(data['current_industry'], [1])
        self.assertEqual(data['total_persons'], 1)
    
    def test_search_for_non_existant_person(self):
        """Test search for a non existant person"""
        res = self.client().post('/persons/search', headers={'Authorization': 'Bearer ' +self.person}, json={'search': 'maker'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['persons'], [])
        self.assertEqual(data['current_industry'], [])
        self.assertEqual(data['total_persons'], 0)

    def test_401_no_token_to_search_for_a_person(self):
        """Test 401 no token to search for a person"""
        res = self.client().post('/persons/search', headers={'Authorization': 'Bearer '}, json={'search': 'engineer'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401 )
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Token not found.')

    def test_changing_the_name_of_a_person(self):
        """Test changing the name of a person"""
        res = self.client().patch('/persons/1', headers={'Authorization': 'Bearer ' +self.person}, json={'name': 'John Isaac'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['persons'], 1)

    def test_404_changing_the_name_of_a_nonexistant_person(self):
        """Test 404 changing the name of a nonexistant person"""
        res = self.client().patch('/persons/4100', headers={'Authorization': 'Bearer ' +self.person}, json={'name': 'John Isaac'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resourse not found')

    def test_401_wrong_header_to_change_the_name(self):
        """Test 401 wrong name to change the name"""
        res = self.client().patch('/persons/4100', headers={'Authorization': 'Berer '+self.person}, json={'name': 'John Isaac'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401 )
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Token not found.')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()