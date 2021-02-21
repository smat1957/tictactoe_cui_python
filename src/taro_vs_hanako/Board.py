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
        row0 = self.board[0]!=0 and\
               self.board[0]==self.board[1] and self.board[0]==self.board[2]
        row1 = self.board[3]!=0 and\
               self.board[3]==self.board[4] and self.board[3]==self.board[5]
        row2 = self.board[6]!=0 and\
               self.board[6]==self.board[7] and self.board[6]==self.board[8]
        col0 = self.board[0]!=0 and\
               self.board[0]==self.board[3] and self.board[0]==self.board[6]
        col1 = self.board[1]!=0 and\
               self.board[1]==self.board[4] and self.board[1]==self.board[7]
        col2 = self.board[2]!=0 and\
               self.board[2]==self.board[5] and self.board[2]==self.board[8]
        crs0 = self.board[0]!=0 and\
               self.board[0]==self.board[4] and self.board[0]==self.board[8]
        crs1 = self.board[2]!=0 and\
               self.board[2]==self.board[4] and self.board[2]==self.board[6]
        if col0 or col1 or col2 or row0 or row1 or row2 or crs0 or crs1:
            return True

    def vacant(self):
        empty = []
        for n, slot in enumerate(self.board):
            if slot == 0:
                empty.append(n)
        return empty

