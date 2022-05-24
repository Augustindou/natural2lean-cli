BACK = u"\u001b[1000D" + u"\u001b[1A"

COMPLETED = "▰"
LEFT = "▱"

class ProgressIndicator:
    def __init__(self, length: int):
        self.length = length
        print("\n")
        self.update(0)
    
    def update(self, progress: float):
        n = int(progress*self.length)
        bar = COMPLETED*n + LEFT*(self.length-n) + f" {int(progress*100)}%"
        
        print(BACK + bar)
    
    def finish(self):
        self.update(1)

if __name__ == "__main__":
    import time
    
    prog = ProgressIndicator(30)
    for i in range(20):
        time.sleep(0.1)
        prog.update(i/20)
    prog.finish()