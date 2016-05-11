import qstns
from random import Random


def get_questions():
    list = []
    r = Random()
    for l in qstns.qlist_all_categories:
        # print('len of list = ' + str(len(l)))
        i = r.randint(0, len(l) - 1)
        print(i)
        list.append(l[i])
    return list
