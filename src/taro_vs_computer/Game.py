from Board import Board
from Player import Player

class Game:
    def __init__(self):
        self.board = Board()
        human = Player('Taro', 1)         # 変更点はここから3行
        machine = Player('computer', 2)
        self.PLAYER = [human, machine]

    def start(self):
        turn = 0
        while True:                       # 以下をゲームオーバーまで繰り返す
            self.board.draw()                 # ①盤面を表示して
            player = self.PLAYER[ turn ]      # ②プレーヤを選んで
            b2 = player.put_stone( self.board )    # ③そのプレーヤが盤面に石を置いて
            if not b2:
                print('引き分け')
                break
            b1 = self.board.winner(player)
            if b1:
                print( player.name + 'さん　の勝ち')
                break
            turn = (turn+1) % 2               # ④手番を交代する
