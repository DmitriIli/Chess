class Ship:
    ls = []
    length = None
    direction = None
    start = None

    def __init__(self, start, length, direction):
        count = 0
        self.length = length
        self.duration = direction
        self.start = start
        if direction:
            for i in range(length):
                self.ls.append((start[0], start[1] + count))
                count += 1
        else:
            for i in range(length):
                self.ls.append((start[0] + count, start[1]))
                count += 1

    def __str__(self):
        print(*self.ls)
        return ''


class Game_pole:
    ls_pole = []
    name = ''
    ships_array = None

    def __init__(self, name):
        self.name = name
        self.ls_pole = [['0' for i in (0, 1, 2, 3, 4, 5, 6, 7)] for j in (0, 1, 2, 3, 4, 5, 6, 7)]
        self.ships_array = [[None for i in (0, 1, 2)] for j in (0, 1, 2)]

    def __str__(self):
        count = 0
        print(self.name)
        print('  |', *[1, 2, 3, 4, 5, 6])
        print('--' * 8)
        for line in self.ls_pole[1:7]:
            count += 1
            print(count, '|', *line[1:7], end='\n')
        return ''

    def add_ship_on_pole(self, ship_):
        for f in ship_.ls:
            self.ls_pole[f[0]][f[1]] = '■'

    def input_ship_start_coord(self):
        while 1:
            print('введите коортинаты начала корабля от 1 до 6')
            while 1:
                print('введите X-координату начала корабля:')
                x = int(input().split()[:1])
                print('введите Y-координату начала корабля:')
                y = int(input().split()[:1])
                if x in range(1, 7) and y in range(1, 7):
                    start = (x, y)
                    break
                else:
                    print('Некорректный ввод')
            print('введите направление корабля: 0 - вертикальное, 1 - горизонтальное')
            while 1:
                direction = int(input().split()[:1])
                if direction in (0, 1):
                    break
                else:
                    print('Некорректный ввод')
            return start, direction

    def check_fields_free(self, ship_):

        if ship_.duration:
            x, y, l = ship_.start[0], ship_.start[1], ship_.length
        else:
            y, x, l = ship_.start[0], ship_.start[1], ship_.length
        if ([self.ls_pole[x - 1][j] for j in range(y - 1, y + l + 1)].count('0')) != l + 2:
            return 0
        elif [self.ls_pole[x + 1][j] for j in range(y - 1, y + l + 1)].count('0') != l + 2:
            return 0
        elif [self.ls_pole[i][y - 1] for i in range(x - 1, x + 2)].count('0') != 3:
            return 0
        elif [self.ls_pole[i][y + 1] for i in range(x - 1, x + 2)].count('0') != 3:
            return 0
        else:
            return 1

    def add_ships(self):
        print('необходимо разместить корабли на игровом поле \n'
              'корабль из 3-х клеток - 1 шт.\n'
              'корабль из 2-х клеток - 2 шт.\n'
              'корабль из 1-ой клетки - 3 шт. \n'
              'между короблями необходимо выдержать расстояние в одну клетку.\n'
              'корабли задаются посредством задания параметров:(0,1),2,1\n'
              'начальные координаты: например (0,1) - 0 по горизонтали, 1 по вертикали\n'
              'размер коробля: от 1-го до 3-х\n'
              'вертаикальное либо горизонтально расположение: задаётся флагом 0 и 1 соответственно.')
        count = 0
        for line in self.ships_array:
            for i in range(len(line) - count):
                while 1:
                    print(f'Осталось {3 - count} кораблей из {count + 1} клеток\n'
                          f'введите начальные координаты и направление')
                    start_and_direction = self.input_ship_start_coord()
                    s = Ship(start_and_direction[0], count + 1, start_and_direction[1])
                    if self.check_fields_free(s):
                        self.ships_array[count].append(s)

                        break
                    else:
                        print('некорректный ввод, повторите')
                count += 1


print('-' * 10)
gp = Game_pole('Игрок 1')
print(gp)
gp.add_ships()
print(gp)
