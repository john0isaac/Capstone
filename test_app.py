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
        self.manager = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImgwUFNENjhqQVhYa1ZudDZPeW9RdCJ9.eyJpc3MiOiJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2OTE2NzQ1MDU5MzIyOTEwMzY3IiwiYXVkIjpbImpvaG4waXNhYWMiLCJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5NDk1MTY1OCwiZXhwIjoxNTk1MDM4MDU4LCJhenAiOiJhdm1iUlhBY0NjVGJwZDJaS3ljUk5SZ2dUSFJqblJqNCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6aW5kdXN0cmllcyIsImRlbGV0ZTpwZXJzb25zIiwiZ2V0OmluZHVzdHJpZXMgIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDpwZXJzb25zIiwicG9zdDppbmR1c3RyaWVzIiwicG9zdDpwZXJzb25zIl19.hihXPgBibFFYUTpjEryLnRMEY_ADGf9_A98PwaRzpCYwePOcXYHvK1sN0YGfvFHfyWsIfTH_xO6ErbNIk5eEEJ1nYeWcIt74NC06YLOV0HVex4QsMImxBGaUh7wdKi16iFbN8TFjliJOnsGlqaDFTePR_hNIuamBcs-hG3X_ULMIyOVI6AXq2lMxS82f-PRG1-YgDd5FYit-NXdWeJAjKPdNRRICAS7aBYj3zrEOCQXrHv415WtSukjahZLL2_zSNS4oMsG8WRWcZ5O2wXNui3Uw_6ZKuiHb2XYSEKsEtdXZEgjfksk6n5Y01wfMvHTmdU7q5Lh6Xdqh8I3hjtUuuQ'
        self.person = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImgwUFNENjhqQVhYa1ZudDZPeW9RdCJ9.eyJpc3MiOiJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3OTkyMDkxOTg1MzY4MTQ0NTExIiwiYXVkIjpbImpvaG4waXNhYWMiLCJodHRwczovL2VuYWN0dXMtbWEuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5NDk1MjExMiwiZXhwIjoxNTk1MDM4NTEyLCJhenAiOiJhdm1iUlhBY0NjVGJwZDJaS3ljUk5SZ2dUSFJqblJqNCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cGVyc29ucyIsImdldDpwZXJzb25zIiwicGF0Y2g6cGVyc29ucyIsInBvc3Q6cGVyc29ucyJdfQ.bWmwYON5GYNKbObCJSFi-dLfmYocxoaY0ZZz4p_eyxUkPXiHL9-amOaGI4Um-SFYv6vvYlrqFLAY8N0HbbG4SFsin-Wog863xw5YYj-g7uV8s1KrkajOQ3LqkrM41VFT22WIm0Ypm-KDhue4vDeGrCjd1_mQqCQauWqhe6JxuIRtNODjK1XMbQbvrUqDld4It5P90tmtDo9-5BUJKai3lau6Ot9nee2qFM407RU_CS_WgTtCaUIeGuoSh2E5i0oOVlxf9lzyLnfBnjwACJbOBUU8NXj5EclWGtYf1Avjr94jPhabgBJkWIqWfRtSur5HKA6843GOHDlv-yulrR4ADw'
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after each test"""
        pass

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
        res = self.client().post('/persons/search', headers={'Authorization': 'Bearer ' +self.manager}, json={'search': 'like'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['persons'])
        self.assertTrue(data['current_industry'])
        self.assertTrue(data['total_persons'])
    
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

    def test_changing_the_city_of_a_person(self):
        """Test changing the city of a person"""
        res = self.client().patch('/persons/1', headers={'Authorization': 'Bearer ' +self.person}, json={'city': 'Cairo'})
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
        res = self.client().patch('/persons/1', headers={'Authorization': 'Berer '+self.person}, json={'name': 'John Isaac'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401 )
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header must start with "Bearer".')

    def test_delete_a_person(self):
        """Test delete a person"""
        res = self.client().delete('/persons/5', headers={'Authorization': 'Bearer '+self.person})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 5)

    def test_delete_nonexistant_person(self):
        """Test delete nonexistant person"""
        res = self.client().delete('/persons/10000', headers={'Authorization': 'Bearer '+self.person})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resourse not found')
    
    def test_403_unauthorized_deletion_of_person(self):
        """Test 403 unauthorized deletion of person"""
        res = self.client().delete('/persons/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401 )
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_delete_an_industry(self):
        """Test delete an industry"""
        res = self.client().delete('/industries/11', headers={'Authorization': 'Bearer '+self.manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 11)

    def test_delete_nonexistant_industry(self):
        """Test delete nonexistant industry"""
        res = self.client().delete('/industries/50000', headers={'Authorization': 'Bearer '+self.manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resourse not found')

    def test_403_unauthorized_deletion_of_industry(self):
        """Test 403 unauthorized deletion of industry"""
        res = self.client().delete('/industries/1', headers={'Authorization': 'Bearer '+self.person})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403 )
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permissions not found.')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()