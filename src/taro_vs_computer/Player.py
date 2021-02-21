from Board import Board
from random import randint

class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def put_stone(self, board):
        # 引き分けの判定はここから
        vacant = board.vacant()
        if not vacant:
          return False
        # 変更点は以下の部分
        if self.id == 2:      # Computerの場合は乱数で
            n = randint( 0, len(vacant)-1 )
            board.board[ vacant[n] ] = self.id
        else:   # Taroの場合はキーボード入力でスロット番号を指定させる
            while True:
                s = input(self.name + "さんの手番です。スロット番号は？ : ")
                n = int(s)
                if n in vacant:
                    board.board[ n ] = self.id
                    break
        return True
