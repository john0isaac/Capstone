import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Person, Industries


class JohnTestCase(unittest.TestCase):
    """This class represents john test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}@{}/{}".format('postgres:davinchi2020','0.0.0.0:5432', database_name)
        setup_db(self.app, self.database_path)

        self.new_person = {
            
        }
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after each test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_retrive_persons(self):
        """Test retrieve persons"""
        res = self.client().get('/persons')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['persons'])
        self.assertTrue(data['total_persons'])

    def test_404_no_data_found_to_retrieve(self):
        """Test 405 no data found to retrieve"""
        res = self.client().get('/persons')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resourse not found')

    def test_retrieve_questions(self):
        """Test retrieve questions"""
        res = self.client().get('/questions')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertEqual(data['total_questions'], 19)
        self.assertTrue(data['categories'])
        self.assertTrue(data['current_category'])
    
    def test_405_using_wrong_method_to_retrieve_questions(self):
        """Test 405 using wrong method to retrieve questions"""
        res = self.client().patch('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_delete_question(self):
        """test delete question"""
        res = self.client().delete('/questions/4')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 4).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(question, None)
    
    def test_422_delete_nonexistent_question(self):
        """test 422 delete nonexistent question"""
        res = self.client().delete('/questions/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_create_new_question(self):
        """test create new question"""
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_405_creation_not_allowed(self):
        """test 405 creation not allowed"""
        res = self.client().post('/questions/45', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_get_specefic_questions_With_results(self):
        """Test get specific questions with results"""
        res = self.client().post('/questions/search', json={'searchTerm': 'pyramid'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(len(data['current_category']))
        self.assertTrue(data['total_questions'])

    def test_get_specefic_questions_Without_results(self):
        """Test get specific questions without results"""
        res = self.client().post('/questions/search', json={'searchTerm': 'jfkf'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions']), 0)
        self.assertEqual(len(data['current_category']), 0)
        self.assertEqual(data['total_questions'], 0)
    
    def test_get_questions_by_category(self):
        """Test get questions by category"""
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertEqual(data['current_category'], 1)
        self.assertTrue(data['total_questions'])

    def test_405_wrong_method_to_get_questions_by_category(self):
        """Test 405 wrong method to get questions by category"""
        res = self.client().post('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_get_question_to_play(self):
        """"Test get question to play"""
        res = self.client().post('/quizzes',  json={"previous_questions": [], "quiz_category": {'id': 1, 'type': 'Science'}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['question']))

    def test_400_for_requesting_nonexistent_category(self):
        """Test 400 for requesting nonexistent category"""
        res = self.client().post('/quizzes', json={"previous_questions": [], "quiz_category": {'id': 10, 'type': 'Economic'}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()