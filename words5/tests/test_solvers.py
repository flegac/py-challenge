from pathlib import Path
from unittest import TestCase

from solver.common.scores import CustomScore, SquareScore
from solver.common.words import Words
from solver.graph_solver import GraphSolver
from solver.mcts_solver import MCTSSolver
from solver.stack_solver import StackSolver


class TestSolvers(TestCase):
    def setUp(self) -> None:
        self.words = Words.from_path(Path.cwd() / 'resources/words.txt')

    def test_stack_solver(self):
        solver = StackSolver(score=SquareScore)
        solver.run(self.words, max_solutions=10)

    def test_graph_solver(self):
        solver = GraphSolver()
        solver.run(self.words)

    def test_mcts_solver(self):
        solver = MCTSSolver(CustomScore)
        solver.run(self.words, max_solutions=1000)
