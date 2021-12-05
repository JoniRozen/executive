import sys
import os
sys.path.append(os.getcwd())
import unittest
from executive.actions.add import AddAction
from executive.actions.models import Action, Project
from unittest import mock, TestCase
import datetime

class AddActionTest(TestCase):
    def setUp(self):
        p = Project(name="testing")
        p.save()

    @mock.patch('executive.actions.add.input', create=True)
    def test_correct_date_instance(self, mocked_input):
        mocked_input.side_effect = ['test_project', '2022-01-1', '1', '']
        a = AddAction()
        a.run()
        self.assertEqual(a.options, {'name': 'test_project', 'deadline': datetime.datetime(2022, 1, 1, 0, 0), 
                        'project': Project['1'], 'context': ''})
    
    @mock.patch('executive.actions.add.input', create=True)
    def test_incorrect_first_instance(self, mocked_input):
        mocked_input.side_effect = ['test_project', '2020-01-1', ' ', '2022-01-1', '1', '']
        a = AddAction()
        a.run()
        self.assertEqual(a.options, {'name': 'test_project', 'deadline': datetime.datetime(2022, 1, 1, 0, 0), 
                        'project': Project['1'], 'context': ''})

    @mock.patch('executive.actions.add.input', create=True)
    def test_None_project(self, mocked_input):
        mocked_input.side_effect = ['test_project','2022-01-1', '', '']
        a = AddAction()
        a.run()
        self.assertEqual(a.options, {'name': 'test_project', 'deadline': datetime.datetime(2022, 1, 1, 0, 0), 
                        'project': None, 'context': ''})

    def tearDown(self):
        Project.delete_by_id(len(Project))
        Action.delete_by_id(len(Action))
        
if __name__ == '__main__': 
    unittest.main() 