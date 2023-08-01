#!/usr/bin/env python3

# unit test to test the functionalities of the process_emails script

import unittest
from process_emails import find_email

class EmailsTest(unittest.TestCase):
    def test_basic(self):
        # since the module to be tested was imported the first argument of the commandline will be None instead of the script name
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@abc.edu"
        self.assertEqual(find_email(testcase), expected)
    def test_one_name(self):
        # Test missing parameter
        testcase = [None, "John"]
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)
    def test_two_name(self):
        # testing edge cases: employees that dont exist
        testcase = [None, "Roy","Cooper"]
        expected = "No email address found"
        self.assertEqual(find_email(testcase), expected)
        
if __name__ == '__main__':
  unittest.main()