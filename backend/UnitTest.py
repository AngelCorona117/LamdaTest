import time
import schedule
import unittest
from WebAutomation import testing

class TestTestingLamda(unittest.TestCase):

    def test_plattform(self):
        #test plattform 1 time
        self.assertTrue(testing())

def run_tests():
    unittest.main(exit=False)

# run the script every x time (just to add some realism to the database)
schedule.every(1).minutes.do(run_tests)
while True:
    schedule.run_pending()
    time.sleep(1)
