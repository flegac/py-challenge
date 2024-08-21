from sat.sat_problem import SATProblem
from sat.sat_solver import SATSolver

from easy_lib.timing import TimingTestCase


class TestSAT(TimingTestCase):

    def test_sat(self):
        n = 5

        prob = SATProblem.ksat(clause_size=3, var_number=n, clause_number=10 * n)
        print(prob)

        solver = SATSolver(prob)

        solution, wrongs = solver.solve(max_retries=1_000)
        print('solution', solution)
        print(f'wrongs: {len(wrongs)}')
