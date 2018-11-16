class GameBoard:

    def __init__(self, N=None, p=None, q=None, board=None):
        self.N = N
        self.p = p  
        self.q = q  
        self.board = board

    # --------- String Representation ---------
    def __str__(self):
        output = "N:" + str(self.N) + "\tp:" + str(self.p) + "\tq:" \
            + str(self.q) + "\n"
        for i in range(self.N):
            for j in range(self.N):
                try:
                    output += self.board[i][j] + " "
                except IndexError:
                    pass

                if (j + 1) % self.q == 0 and j != 0 and j != (self.N - 1):
                    output += "| "

            output += "\n"
            if (i + 1) % self.p == 0 and i != 0 and i != (self.N - 1):
                for k in range(self.N + self.p - 1):
                    output += "- "
                output += "\n"
        return output
