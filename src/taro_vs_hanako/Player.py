from Board import Board

class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def put_stone(self, board):
        # 引き分けの判定はここから
        vacant = board.vacant()
        if not vacant:
          return False
        # ここまで
        while True:
            s = input(self.name + "さんの手番です。スロット番号は？ : ")
            n = int(s)
            if n in vacant:      # 空きスロットのリストに番号nは含まれているか？
                board.board[ n ] = self.id
                break
        return True
