class Board:
    def __init__(self):
        self.board = [0,0,0,\
                      0,0,0,\
                      0,0,0]

    def draw(self):
        bd = ['', '', '',\
              '', '', '',\
              '', '', '']
        n = 0
        for val in self.board:
            if val==0:
                bd[n] = str(n)
            elif val==1:
                bd[n] = 'X'
            elif val==2:
                bd[n] = 'O'
            n += 1
        print( '/---|---|---\\')
        print( '| {} | {} | {} |'.format(bd[0], bd[1], bd[2]) )
        print( '|---|---|---|')
        print(f'| {bd[3]} | {bd[4]} | {bd[5]} |')
        print( '|---|---|---|')
        print(f'| {bd[6]} | {bd[7]} | {bd[8]} |')
        print( '\\---|---|---/')

    def winner(self, player):
        def scan(n1, n2, n3):
            return self.board[n1]!=0 and\
                   self.board[n1]==self.board[n2] and\
                   self.board[n1]==self.board[n3]
        return scan(0,1,2) or scan(3,4,5) or scan(6,7,8) or\
               scan(0,3,6) or scan(1,4,7) or scan(2,5,8) or\
               scan(0,4,8) or scan(2,4,6)

    def vacant(self):
        empty = []
        for n, slot in enumerate(self.board):
            if slot == 0:
                empty.append(n)
        return empty

