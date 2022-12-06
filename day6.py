from utils import AOCInputReader

class Day6(object):
    
    def __init__(self, inp) -> None:
        self.inp = inp


    def solve_core(self, len_indicator):
        idx = 0
        marker_searching = True
        while marker_searching and idx <= len(self.inp) - len_indicator:
            test_char = set(self.inp[idx:idx+len_indicator])
            if len(test_char) == len_indicator:
                marker_searching = False
                idx = idx + len_indicator
            else:
                idx += 1
        return idx


    def solve1(self):
       return self.solve_core(4)

    def solve2(self):
        return self.solve_core(14)

if __name__ == "__main__": 
    pass
    #inp = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    reader = AOCInputReader("day6_inp.txt")
    inp = reader.read().strip("\n")
    solver = Day6(inp)
    print(solver.solve1())
    print(solver.solve2())