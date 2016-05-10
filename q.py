class Q:
    def __init__(self, q, vargs):
        self.q = q
        self.vargs = vargs
        for v in vargs:
            if vargs[v]:
                self.right = v

    def is_right(self, e):
        # keys = self.vargs.keys()
        # for k in keys:
        #     if k == e:
        #         return self.vargs[e]
        #
        # print('choose one of the listed variants')
        return e == self.right


q1 = [
    Q('Сколько лет мне?', {'23': 1, '21': 0, '18': 0, '25': 0}),
    Q('Мое любимое число?', {'13': 1, '11': 0, '1': 0, '3': 0})
]

q2 = [
    Q('Сколько раз нужно молиться?', {'3': 0, '7': 0, '4': 0, '5': 1}),
    Q('Сколько раз ты молишься?', {'3': 0, '7': 0, '4': 0, '5': 1}),
    Q('Какие оценки получал в школе?', {'3': 0, '7': 0, '4': 0, '5': 1}),
    Q('Какой день сегодня?', {'День победы !': 1, '8 мая': 0, 'обычный': 0, 'понедельник': 0})
]

qlist_all_categories = [q1, q2]
