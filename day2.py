from utils import AOCInputReader

class Day2(object):
    score_board_wl = {
        "A X": 3,
        "A Y": 0,
        "A Z": 6,
        "B X": 6,
        "B Y": 3,
        "B Z": 0,
        "C X": 0,
        "C Y": 6, 
        "C Z": 3,
        }
    score_board_wl_inv = {key: {3: 3, 6:0, 0:6}[val] for key, val in score_board_wl.items()}
    score_board_item = {"A": 1, "B": 2, "C": 3,"X": 1, "Y": 2, "Z": 3}
    score_board_wl_answer = {
        "A X": "A Z",
        "A Y": "A X",
        "A Z": "A Y",
        "B X": "B X",
        "B Y": "B Y",
        "B Z": "B Z",
        "C X": "C Y",
        "C Y": "C Z", 
        "C Z": "C X",}

    def __init__(self, inp) -> None:
        self.inp = inp

    @staticmethod
    def solve_core(inp, player_right: bool = True):
        score_board = Day2.score_board_wl
        idx_item = 0
        if player_right:
            score_board = Day2.score_board_wl_inv
            idx_item = 2
        return sum((score_board[nr_par] +  Day2.score_board_item[nr_par[idx_item]] for nr_par in inp))

    def solve1(self):
        return self.solve_core(self.inp)

    def solve2(self):
        return self.solve_core([Day2.score_board_wl_answer[item] for item in self.inp])


if __name__ == "__main__": 
    reader = AOCInputReader("day2_inp.txt")
    inp = reader.read().split("\n")
    #inp = ["A Y", "B X", "C Z"]
    solver = Day2(inp)
    res = solver.solve1()
    res2 = solver.solve2()
    print(f"Following the strategy our score is: {res}")
    print(f"Following the new better strategy our score is: {res2}")