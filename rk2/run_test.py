import unittest
import sys

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.', pattern='test_*.py')

    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)

    sys.exit(0 if result.wasSuccessful() else 1)
