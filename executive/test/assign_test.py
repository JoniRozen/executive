import unittest
import sys
import os
from executive.actions.add import AddAction
sys.path.append(os.getcwd())
from executive.actions.assign import AssignAction
from executive.actions.models import Action, AssignedAction
from unittest import mock, TestCase
import datetime

class AssignActionTest(TestCase):
    @mock.patch('executive.actions.add.input', create=True)
    def setUp(self, mocked_input):
        mocked_input.side_effect = ['test_project', '2022-01-1', '1', '']
        a = AddAction()
        a.run()

    @mock.patch('executive.actions.add.input', create=True)
    def test_assignment(self, mocked_input):
        mocked_input.side_effect = ['Jonathan Rozen','1']
        a = AssignAction()
        a.run()
        self.assertEqual(a.options, {'name': 'Jonathan Rozen', 'action_id' : '1', 'time': datetime.date.today()})
    

    def tearDown(self):
        Action.delete_by_id(len(Action))
        AssignedAction.delete_by_id(len(AssignedAction))
        
if __name__ == '__main__': 
    unittest.main() 