import unittest
from lesson12.runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = []

    def setUp(self):
        self.ucein = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in all_results:
            print(i)

    def test1(self):
        tournament = Tournament(90, self.ucein, self.nik)
        all_results.append(tournament.start())
        self.assertTrue(all_results[0][2] == "Ник")

    def test2(self):
        tournament = Tournament(90, self.andrey, self.nik)
        all_results.append(tournament.start())
        self.assertTrue(all_results[1][2] == "Ник")

    def test3(self):
        tournament = Tournament(90, self.ucein, self.andrey, self.nik)
        all_results.append(tournament.start())
        self.assertTrue(all_results[2][3] == "Ник")

#






