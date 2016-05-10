from q import Q
from utils import get_questions


class GameSingle:
    def __init__(self, uname, chatid):
        self.uname = uname
        self.chatid = chatid
        self.score = 0
        self.qlist = []
        self.cq = None
        self.status = 0  # 0-game not exists, 1-game is active, 2-user won 3-user lose

    def start_game(self):
        self.qlist = get_questions()
        # self.cq = self.qlist.pop(0)
        self.status = 1

    def next(self):
        if len(self.qlist) > 0:
            self.cq = self.qlist.pop(0)
        else:
            self.cq = None
            self.status = 2

# g = GameSingle('m13')
# g.start_game()
#
# while True:
#     g.next()
#     if g.cq is not None:
#         print(g.cq.q)
#         keys = g.cq.vargs.keys()
#         for i in keys:
#             print(i)
#         v = str(input())
#
#         if g.cq.is_right(v):
#             print('That\'s right !')
#         else:
#             print('Sorry, your answer is wrong :(')
#             print('You lose..')
#             break
#     else:
#         print("You won " + g.uname)
#         break
# print('Game over')
