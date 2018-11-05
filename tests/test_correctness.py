import unittest

from pymop import *


def load(name):

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources")

    X = np.loadtxt(os.path.join(path, "%s.x" % name))
    F = np.loadtxt(os.path.join(path, "%s.f" % name))

    G = None
    if os.path.exists(os.path.join(path, "%s.g" % name)):
        G = np.loadtxt(os.path.join(path, "%s.g" % name))

    return X, F, G


problems = [
    ('DTLZ1', [10, 3]), ('DTLZ2', [10, 3]), ('DTLZ3', [10, 3]), ('DTLZ4', [10, 3]), ('DTLZ5', [10, 3]),
    ('DTLZ6', [10, 3]) ,('DTLZ7', [10, 3]),
    ('ZDT1', [10]), ('ZDT2', [10]), ('ZDT3', [10]), ('ZDT4', [10]), ('ZDT6', [10]),
    ('TNK', []), ('Rosenbrock', [10]), ('Rastrigin', [10]), ('Griewank', [10]), ('OSY', []), ('Kursawe', []),
    ('WeldedBeam', []), ('Carside', []), ('BNH', [])
]


class CorrectnessTest(unittest.TestCase):

    def test_problems(self):
        for entry in problems:
            name, params = entry
            print("Testing: " + name)

            X, F, CV = load(name)
            problem = globals()[name](*params)
            F_, G_ = problem.evaluate(X)

            if problem.n_obj == 1:
                F = F[:, None]

            self.assertTrue(np.all(np.abs(F_ - F) < 0.00001))

            if problem.n_constr > 0:
                G_[G_<0] = 0
                CV_ = np.sum(G_, axis=1)
                self.assertTrue(np.all(np.abs(CV_ - CV) < 0.00001))


if __name__ == '__main__':
    unittest.main()
