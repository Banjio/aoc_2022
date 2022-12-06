from utils import AOCInputReader
import re
class Day5(object):
    
    def __init__(self, inp) -> None:
        self.inp = inp


    def solve_core(self, custom_sortfunc):
        ls_inp = self.inp.split("\n\n")
        # Alternatively we can use x.isalpha()
        # zip(*string) can transpose a string
        stacks = [list(filter(lambda x: re.match("[a-z]|[A-Z]", x), col)) for col in list(zip(*ls_inp[0].split("\n"))) if col[-1].isdigit()]
        for instruction in ls_inp[1].split("\n"):
                #mv, fromS, toS = list(map(int, list(filter(lambda x: re.match("\d+", x), list(instruction)))))
                mv, fromS, toS = list(map(int, instruction.split()[1::2]))
                instruction.split()
                insert = list(custom_sortfunc(stacks[fromS-1][0:mv]))
                new_stack = stacks[fromS-1][mv:]
                inserted_stack =  insert + stacks[toS-1]
                stacks[fromS-1] = new_stack
                stacks[toS-1] = inserted_stack            
        return("".join([stacks[i][0] for i in range(len(stacks))]))

    def solve1(self):
        return self.solve_core(reversed)

    def solve2(self):
        return self.solve_core(list)
        

if __name__ == "__main__": 
    pass
    inp = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2]"""
    reader = AOCInputReader("day5_inp.txt")
    inp2 = reader.read()
    #inp = reader.read().split("\n")
    solver = Day5(inp2)
    print(solver.solve1())
    print(solver.solve2())
    #print(sum(solver.solve2()))
