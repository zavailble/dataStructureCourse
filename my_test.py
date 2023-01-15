from final import *
from tree import *
import pytest
import pytest_benchmark

def test_pytesttest(benchmark):
    benchmark(perfomance_test)

def test_pytesttest2(benchmark):
    benchmark(aperformance_test)

