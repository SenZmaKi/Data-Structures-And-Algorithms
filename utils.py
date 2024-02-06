import sys
from time import time as current_time
from memory_profiler import memory_usage
from random import randrange
from typing import TypeVar, Callable

T = TypeVar("T")

# Quick sort moment
sys.setrecursionlimit(999999999)


def generate_random_list(size: int = 100, start=1, stop=100) -> list[int]:
    return [randrange(start, stop+1) for _ in range(size)]


def profile(task_title: str, task: Callable[[], T]) -> T:
    start_time = current_time()
    result = task()
    runtime = current_time() - start_time
    print(f"{task_title}: {runtime} s ")
    return result


def swap(array: list[int], idx_1: int, idx_2: int) -> None:
    array[idx_1], array[idx_2] = array[idx_2], array[idx_1]

