class AOCInputReader: 

    def __init__(self, url) -> None:
        self.url = url
    
    def read(self):
        with open(self.url, "r") as f:
            res = f.read()
        return res

