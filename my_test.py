from final import *
from finalProject import *
import pytest
import pytest_benchmark
# # def my_benchmark(option):
# #     argument1 = {i: [1]*i for i in [10, 100, 1000, 10000, 100000]}
# #     performance_test(argument1=argument1)

def test_pytesttest(benchmark):
    benchmark(perfomance_test)

def test_pytesttest2(benchmark):
    benchmark(aperformance_test)

