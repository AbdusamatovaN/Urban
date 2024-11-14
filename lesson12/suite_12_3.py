import unittest
import test_runner
import tests_12_2

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

textTestRunner = unittest.TextTestRunner(verbosity=2)
textTestRunner.run(runnerST)