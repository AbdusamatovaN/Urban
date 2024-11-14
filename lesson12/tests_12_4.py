import logging
import unittest

from lesson12.runner_and_tournament import Runner

class RunnerTest(unittest.TestCase):

    def test_run(self):
        try:
            runner = Runner([1, 2])
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_walk(self):
        try:
            runner = Runner("Rock", -3)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=True)


    def test_challenge(self):
        runner1 = Runner("Rock")
        runner2 = Runner("Karl")
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


logging.basicConfig(level=logging.INFO, filename="runner_tests.log", filemode="w", encoding='utf-8',
                    format="%(asctime)s %(levelname)s : %(message)s")