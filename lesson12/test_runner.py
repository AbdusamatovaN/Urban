import unittest

from lesson12.runner import Runner


class RunnerTest(unittest.TestCase):
    def test_run(self):
        runner = Runner("Rock")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_walk(self):
        runner = Runner("Rock")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_challenge(self):
        runner1 = Runner("Rock")
        runner2 = Runner("Karl")
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

