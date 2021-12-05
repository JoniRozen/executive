import unittest
import sys
import os
sys.path.append(os.getcwd())
from executive.actions.schedule import ScheduleAction
from executive.actions.models import ScheduledAction
from unittest import mock, TestCase
import datetime

class AssignActionTest(TestCase):

    @mock.patch('executive.actions.add.input', create=True)
    def test_schedule_acion(self, mocked_input):
        mocked_input.side_effect = ['test_action', '0 0 12 ? JAN,FEB,MAR,APR *']
        s = ScheduleAction()
        s.run()
        self.assertEqual(s.options, {'name': 'test_action', 'cron' : '0 0 12 ? JAN,FEB,MAR,APR *'})
    

    def tearDown(self):
        ScheduledAction.delete_by_id(len(ScheduledAction))
        
if __name__ == '__main__': 
    unittest.main() 