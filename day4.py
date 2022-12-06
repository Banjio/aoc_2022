from utils import AOCInputReader

class Day3(object):
    
    def __init__(self, inp) -> None:
        self.inp = inp


    def solve_core(self, cond):
         for elem in self.inp:
            ls_spl = elem.split(",")
            e1 = list(map(int, ls_spl[0].split("-")))
            e2 = list(map(int, ls_spl[1].split("-")))
            yield cond(e1, e2)

    def solve1(self):
        cond = lambda e1, e2: (e1[0] >= e2[0] and e1[1] <= e2[1]) or (e1[0] <= e2[0] and e1[1] >= e2[1])
        return self.solve_core(cond)

    def solve2(self):
        cond = lambda e1, e2: (e1[1] >= e2[0]) and (e2[1] >= e1[0])
        return self.solve_core(cond)

if __name__ == "__main__": 
    #inp = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]
    reader = AOCInputReader("day4_inp.txt")
    inp = reader.read().split("\n")
    solver = Day3(inp)
    print(sum(solver.solve1()))
    print(sum(solver.solve2()))