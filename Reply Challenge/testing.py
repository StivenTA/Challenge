from random import randint
from time import perf_counter
from typing import List, Tuple

from numpy.random import permutation

def read_input_file(input_file: str) -> dict:
    with open(input_file, 'r') as f:
        # parse the file contents
        # ...
        return parsed_data

def score(order: List[int], distances: List[List[int]]) -> int:
    return sum(distances[order[i - 1]][order[i]] for i in range(len(order)))


def generate_neighbor(order: List[int]) -> Tuple[int, int]:
    x, y = randint(0, len(order) - 1), randint(0, len(order) - 1)
    return x, y


def simulated_annealing(distances: List[List[int]]) -> List[int]:
    order = list(range(len(distances)))
    jest = score(order, distances)
    best = order[:]
    best_res = jest
    t = 1e12
    cooling_rate = 0.999999
    while perf_counter() <= 69 * CLOCKS_PER_SEC:
        x, y = generate_neighbor(order)
        order[x], order[y] = order[y], order[x]
        nowe = score(order, distances)
        delta = nowe - jest
        if delta >= 0 or randint(0, 10 ** 5) == 0:
            jest = nowe
        else:
            order[x], order[y] = order[y], order[x]
        if jest > best_res:
            best_res = jest
            best = order[:]
            print("mam", jest)
        t *= cooling_rate
        if t < 1e-8:
            break
    return best


if __name__ == "__main__":
    input_data = read_input_file("data.txt")
    distances = input_data["distances"]
    output = simulated_annealing(distances)
    write_output_file(output_file, output)
