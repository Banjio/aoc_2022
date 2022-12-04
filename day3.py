from utils import AOCInputReader

class Day3(object):
    
    _letters = "abcdefghijklmnopqrstuvwxyz"
    _sm_letters_prio = dict(zip(list(_letters), range(1, 27)))
    _cap_letters_prio = dict(zip(list(_letters.upper()), range(27, 53)))
    letters_prio = {**_sm_letters_prio, **_cap_letters_prio}

    def __init__(self, inp) -> None:
        self.inp = inp

    def solve1(self):
        for item in self.inp:
            len_itm = len(item)
            idx_half = len_itm // 2
            comp1 = item[:idx_half]
            comp2 = item[idx_half:]
            yield self.letters_prio[set(comp1).intersection(set(comp2)).pop()]


    def solve2(self):
        iters = len(self.inp) // 3
        for idx in range(iters):
            sub_ls = self.inp[(idx * 3):(idx + 1) * 3]
            yield self.letters_prio[set(sub_ls[0]).intersection(sub_ls[1]).intersection(sub_ls[2]).pop()]


if __name__ == "__main__": 
    reader = AOCInputReader("day3_inp.txt")
    reader2 = AOCInputReader("day3_inp2.txt")
    inp = reader.read().split("\n")
    inp2 = reader2.read().split("\n")
    #inp1 = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", 
    #"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
    #inp2 = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"]
    solver = Day3(inp)
    res = print(sum(solver.solve1()))
    solver2 = Day3(inp2)
    print(sum(solver2.solve2()))
    #res2 = solver.solve2()
    #print(f"Our priorisation score is: {res}")

    #print(sum(({**dict(zip(list("abcdefghijklmnopqrstuvwxyz"), range(1, 27))), **dict(zip(list("abcdefghijklmnopqrstuvwxyz".upper()), range(27, 53)))}[list(set(item[:len(item) // 2]).intersection(item[len(item) // 2:]))[0]] for item in inp)))