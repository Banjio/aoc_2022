from typing import Any
from utils import AOCInputReader


class Day1(object):
    
    def __init__(self, model_input: Any) -> None:
        self.inp = model_input
        self.res = []

    
    def calc_calories(self):
        last_pos = 0
        self.res = []
        for idx in range(len(self.inp) -1):
            if self.inp[idx] == '\n' and self.inp[idx + 1] == '\n':
                self.res.append(sum(map(lambda x: int(x), self.inp[last_pos:idx].split("\n"))))
                last_pos = idx + 2
        
        return self

    def solve_part_1(self):
        return max(self.res)

    def solve_part_2(self):
        return sum(sorted(self.res, reverse=True)[:3])
        
        



if __name__ == "__main__":
    #inp = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
    reader = AOCInputReader("day1_inp.txt")
    input = reader.read()
    solver = Day1(input)
    p1 = solver.calc_calories().solve_part_1()
    p2 = solver.calc_calories().solve_part_2()
    print(f"Calories For one elve {p1} and for three elves {p2}")

    