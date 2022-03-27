class Ship:
    ls = []
    len_ = None

    def __init__(self, start_, len_, duration_):
        count = 0
        self.len_ = len_
        if duration_:
            for i in range(len_):
                self.ls.append((start_[0], start_[1] + count))
                count += 1
        else:
            for i in range(len_):
                self.ls.append((start_[0] + count, start_[1]))
                count += 1

    def __str__(self):
        print(*self.ls)
        return ''


class Game_pole:
    ls_pole = []

    def __init__(self):
        self.ls_pole = [['О' for i in (0, 1, 2, 3, 4, 5)] for j in (0, 1, 2, 3, 4, 5)]

    def __str__(self):
        count = 0
        print(' ', *[1, 2, 3, 4, 5, 6])
        for line in self.ls_pole:
            count += 1
            print(count, *line, end='\n')
        return ''

    def add_ship_on_pole(self, ship_):
        for f in ship_.ls:
            print(f[0], f[1])
            print(self.ls_pole[f[0]][f[1]])
            self.ls_pole[f[0]][f[1]] == '■'
            print(self.ls_pole[f[0]][f[1]])

    def check_field_free(self, field):
        if self.ls_pole[field[0]][field[1]] == 'О':
            return 1
        else:
            return 0


gp = Game_pole()
print(gp)

ship = Ship((0, 1), 3, 0)
print(ship)

gp.add_ship_on_pole(ship)
print(gp)

