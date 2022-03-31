from random import randrange


class Ship:
    ls = []
    length = None
    direction = None
    start = None

    def __init__(self, start, length, direction):
        count = 0
        self.length = length
        self.direction = direction
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


class GamePole:
    ls_pole = []
    name = ''
    ships_array = None
    cpu_flag = None
    ships_counter = None

    def __init__(self, name, cpu=None):
        if cpu:
            self.name = name
            self.name = name
            self.ls_pole = [['0' for i in (0, 1, 2, 3, 4, 5, 6, 7)] for j in (0, 1, 2, 3, 4, 5, 6, 7)]
            self.ships_array = [[None for i in (0, 1, 2)] for j in (0, 1, 2)]
            self.ships_counter = 6
            self.add_cpu_game_pole()


        else:
            self.name = name
            self.ls_pole = [['0' for i in (0, 1, 2, 3, 4, 5, 6, 7)] for j in (0, 1, 2, 3, 4, 5, 6, 7)]
            self.ships_array = [[None for i in (0, 1, 2)] for j in (0, 1, 2)]
            self.ships_counter = 6

    def __str__(self):
        count = 0
        print(self.name)
        print('  |', *[1, 2, 3, 4, 5, 6])
        print('--' * 8)
        for line in self.ls_pole[1:7]:
            count += 1
            print(count, '|', *line[1:7], end='\n')
        return ''

    # Добавление корабля на игровое поле
    def add_ship_on_pole(self, ship_):
        start = ship_.start
        direct = ship_.direction
        length = ship_.length
        if direct:
            for j in range(start[1], start[1] + length):
                self.ls_pole[start[0]][j] = '■'
        else:
            for i in range(start[0], start[0] + length):
                self.ls_pole[i][start[1]] = '■'

    # функция ввода параметров корабля
    def input_ship_start_coord(self, length):

        print('введите направление корабля: 0 - вертикальное, 1 - горизонтальное')
        while 1:
            try:
                direction = int(input().split()[:1][0])
                if direction not in (0, 1):
                    raise ValueError
                break
            except ValueError:
                print('некорректный ввод, должно быть число 0 или 1')

        print('введите коортинаты начала корабля от 1 до 6')
        while 1:
            try:
                print('введите X-координату начала корабля:')
                x = int(input().split()[:1][0])
                print('введите Y-координату начала корабля:')
                y = int(input().split()[:1][0])
                if x not in (1, 2, 3, 4, 5, 6) or y not in (1, 2, 3, 4, 5, 6):
                    raise Exception('некорректный ввод, должно быть число от 1 до 6')

                if direction:
                    if y + length > 7:
                        raise Exception('корабль выходит за пределы поля')
                else:
                    if x + length > 7:
                        raise Exception('корабль выходит за пределы поля')
                break
            except Exception as e:
                print(e.__str__())

        return (x, y), direction

    # функция для проверки на возможность добавления корабля по заданным параметром на игровое поле исходя из условий
    def check_fields_free(self, ship_):
        x, y, l = ship_.start[0], ship_.start[1], ship_.length
        if ship_.direction:
            if not self.check_fields_is_free(ship_):
                return 0
            elif [self.ls_pole[x - 1][j] for j in range(y - 1, y + l + 1)].count('0') != l + 2:
                return 0
            elif [self.ls_pole[x + 1][j] for j in range(y - 1, y + l + 1)].count('0') != l + 2:
                return 0
            elif [self.ls_pole[i][y - 1] for i in range(x - 1, x + 2)].count('0') != 3:
                return 0
            elif [self.ls_pole[i][y + 1] for i in range(x - 1, x + 2)].count('0') != 3:
                return 0
            elif not self.check_fields_is_free(ship_):
                return 0
            else:
                return 1
        else:
            if not self.check_fields_is_free(ship_):
                return 0
            elif [self.ls_pole[i][y - 1] for i in range(x - 1, x + l + 1)].count('0') != l + 2:
                return 0
            elif [self.ls_pole[i][y + 1] for i in range(x - 1, x + l + 1)].count('0') != l + 2:
                return 0
            elif [self.ls_pole[x - 1][j] for j in range(y - 1, y + 2)].count('0') != 3:
                return 0
            elif [self.ls_pole[x + 1][j] for j in range(y - 1, y + 2)].count('0') != 3:
                return 0
            else:
                return 1

    def check_fields_is_free(self, ship_):
        start = ship_.start
        direction = ship_.direction
        length = ship_.length
        if direction:
            if [self.ls_pole[start[0]][j] for j in range(start[1], start[1] + length)].count('0') == length:
                return 1
        else:
            if [self.ls_pole[i][start[1]] for i in range(start[0], start[0] + length)].count('0') == length:
                return 1
        return 0

    # функция для заполнения массива кораблей игрока
    def add_ships(self):
        print('необходимо разместить корабли на игровом поле \n'
              'корабль из 3-х клеток - 1 шт.\n'
              'корабль из 2-х клеток - 2 шт.\n'
              'корабль из 1-ой клетки - 3 шт. \n'
              'между короблями необходимо выдержать расстояние в одну клетку.\n'
              'корабли задаются посредством задания параметров:(0,1),2,1\n'
              'начальные координаты: например (0,1) - 0 по горизонтали, 1 по вертикали\n'
              'размер коробля: от 1-го до 3-х\n'
              'вертаикальное либо горизонтально расположение: задаётся флагом 0 и 1 соответственно.\n'
              '____________________________________________________________________________________'
              '\n')
        count = 0
        for line in self.ships_array:
            for i in range(len(line) - count):
                while 1:
                    print(f'Осталось {len(line) - count - i} корабль(-я) из {count + 1} клеток(-и)\n'
                          f'введите начальные координаты и направление')
                    start_and_direction = self.input_ship_start_coord(count + 1)
                    s = Ship(start_and_direction[0], count + 1, start_and_direction[1])
                    if self.check_fields_free(s):
                        self.ships_array[count][i] = s
                        self.add_ship_on_pole(s)
                        print(self)
                        break
                    else:
                        print('Клетка занята')
            count += 1

    def add_cpu_game_pole(self):
        count = 0
        for line in self.ships_array:
            for i in range(len(line) - count):
                while 1:
                    try:
                        x = randrange(1, 7)
                        y = randrange(1, 7)
                        direction = randrange(0, 2)

                        if direction:
                            if y + count + 1 > 7:
                                raise Exception
                        else:
                            if x + count + 1 > 7:
                                raise Exception
                    except Exception as e:
                        continue
                    start_and_direction = ((x, y), direction)
                    s = Ship(start_and_direction[0], count + 1, start_and_direction[1])
                    print(start_and_direction[0], count + 1, start_and_direction[1])
                    if self.check_fields_free(s):
                        self.ships_array[count][i] = s
                        self.add_ship_on_pole(s)
                        print(self)
                        break
            count += 1
        # print(self)
