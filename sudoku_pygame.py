# Coding:utf-8
import pygame, random
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.draw.rect(screen, (147, 147, 147), (0, 0, 800, 500))
BACKGROUND = (147, 147, 147)
WINXSIZE = 800
WINYSIZE = 500


class Button:
    def __init__(self, screen, coords=(0, 0, 10, 10), text=''):
        self.screen = screen
        self.coords = coords
        self.rect = pygame.draw.rect(self.screen, (0, 0, 168), (self.coords[0], self.coords[1],
                                     self.coords[2] - self.coords[0],
                                     self.coords[3] - self.coords[1]))
        self.writing = text
        self.text = [SimbolRunes(screen, sim, (255, 230, 230),
                                 (1 + coords[0] + ind * ((coords[2] - coords[0]) // len(text)),
                                  coords[1],
                                  coords[0] + (ind + 1) * ((coords[2] - coords[0]) // len(text)) - 1,
                                  coords[3])) for ind, sim in enumerate(text)]
        self.color = (0, 0, 168)
    
    def clicked(self):
        if self.color == (0, 0, 168):
            self.color = (168, 0, 0)
            self.rect = pygame.draw.rect(self.screen, (168, 0, 0), (self.coords[0], self.coords[1],
                                         self.coords[2] - self.coords[0],
                                         self.coords[3] - self.coords[1]))
        else:
            self.color = (0, 0, 168)
            self.rect = pygame.draw.rect(self.screen, (0, 0, 168), (self.coords[0], self.coords[1],
                                         self.coords[2] - self.coords[0],
                                         self.coords[3] - self.coords[1]))
        self.text = [SimbolRunes(screen, sim, (255, 230, 230),
                                 (1 + self.coords[0] + ind * ((self.coords[2] - self.coords[0])\
                                                              // len(self.writing)), self.coords[1],
                                  self.coords[0] + (ind + 1) * ((self.coords[2] - self.coords[0])\
                                                           // len(self.writing)) - 1,
                                  self.coords[3])) for ind, sim in enumerate(self.writing)]


class ChangeButton:  # 2 arrows, text and changing number
    def __init__(self, screen, coords=(0, 0, 10, 10), text='', changingNum=3):
        self.screen = screen
        self.text = text
        self.coords = coords
        self.rect = pygame.draw.rect(self.screen, (0, 168, 168), (self.coords[0], self.coords[1],
                                     self.coords[2] - self.coords[0],
                                     self.coords[3] - self.coords[1]))
        self.chagingNum = changingNum
        xsize = self.coords[2] - self.coords[0]
        ysize = self.coords[3] - self.coords[1]
        self.title = [SimbolRunes(self.screen, sim, (195, 170, 230),
                                 (1 + self.coords[0] + ind * ((self.coords[2]\
                                                               - self.coords[0]) // len(self.text)),
                                  self.coords[1],
                                  self.coords[0] + (ind + 1) *\
                                  ((self.coords[2] - self.coords[0]) // len(self.text)) - 1,
                                  self.coords[1] + (self.coords[3] - self.coords[1]) // 2)
                                 ) for ind, sim in enumerate(text)]
        self.showNum = SimbolRunes(self.screen, str(changingNum), (240, 160, 0),
                                   (self.coords[0] + 4 * ((self.coords[2] - self.coords[0]) // 9),
                                    self.coords[3] - (2 * (self.coords[3] - self.coords[1]) // 10),
                                    self.coords[0] + 5 * (self.coords[2] - self.coords[0]) // 9,
                                    self.coords[3]))
        self.larrow = pygame.draw.polygon(self.screen, (0, 147, 0), ((self.coords[0] + xsize // 10,
                                          self.coords[3] - ysize // 10),
                                          (self.coords[0] + 3 * (xsize // 10),
                                          self.coords[3] - ysize // 10),
                                          (self.coords[0] + xsize // 5,
                                          self.coords[3] - 3 * (ysize // 10))))
        
        self.rarrow = pygame.draw.polygon(self.screen, (0, 147, 0), ((self.coords[2] - xsize // 5,
                                          self.coords[3] - ysize // 10),
                                          (self.coords[2] - 3 * (xsize // 10),
                                          self.coords[3] - 3 * (ysize // 10)),
                                          (self.coords[2] - xsize // 10,
                                          self.coords[3] - 3 * (ysize // 10))))
        
    def cangeNum(self, updowm='u'):
        if updown == 'u' and self.changeNum < 15:
            self.changeNum += 1
        elif self.changeNum > 1:
            self.changeNum += 1
        draw.rect(self.screen, (0, 168, 168),
                  (self.coords[0] + 4 * ((self.coords[2] - self.coords[0]) // 9),
                                    self.coords[3] - (2 * (self.coords[3] - self.coords[1]) // 10),
                                    (self.coords[2] - self.coords[0]) // 9,
                                    2 * (self.coords[3] - self.coords[1]) // 10))
            
        
class SimbolRunes:
    def __init__(self, screen, simbol=' ', color=(0, 0, 0), coords=(0, 0, 10, 10)):
        self.lines = []
        self.color = color
        xsize = coords[2] - coords[0]
        ysize = coords[3] - coords[1]
        sim = simbol.lower()
        if sim == '0':
            self.lines = pygame.draw.lines(screen, color, True, ((coords[0], coords[3]),
                             (coords[2], coords[3]), (coords[0] + xsize // 2, coords[1])), 1)
        elif sim == '1' or sim == 'i':
            self.lines = pygame.draw.line(screen, color, (coords[0] + xsize // 2, coords[1]),
                             (coords[0] + xsize // 2, coords[3]))
        elif sim == '2':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[1]),
                             (coords[2], coords[1]), (coords[2], coords[1] + ysize // 2),
                             (coords[0], coords[3]), (coords[2], coords[3])), 1)
        elif sim == '3':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[1]),
                             (coords[2], coords[1]), (coords[0], coords[1] + ysize // 2),
                             (coords[2], coords[3]), (coords[0], coords[3])), 1)
        elif sim == '4':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[2], coords[3]),
                             (coords[2], coords[1]), (coords[0], coords[1] + ysize // 2),
                             (coords[2], coords[1] + ysize // 2)), 1)
        elif sim == '5':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[2], coords[1]),
                             (coords[0], coords[1]), (coords[2], coords[1] + ysize // 2),
                             (coords[2], coords[3]), (coords[0], coords[3])), 1)
        elif sim == '6':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[2], coords[1]),
                             (coords[0], coords[1] + ysize // 2), (coords[0], coords[3]),
                             (coords[2], coords[3]), (coords[0], coords[1] + ysize // 2)), 1)
        elif sim == '7':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[1]),
                             (coords[2], coords[1]), (coords[0], coords[1] + ysize // 2),
                             (coords[0], coords[3])), 1)
        elif sim == '8':
            self.lines = pygame.draw.lines(screen, color, True, ((coords[0], coords[1]),
                             (coords[2], coords[1]), (coords[0], coords[3]),
                             (coords[2], coords[3])), 1)
        elif sim == '9':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[3]),
                             (coords[2], coords[1] + ysize // 2), (coords[2], coords[1]),
                             (coords[0], coords[1]), (coords[2], coords[1] + ysize // 2)), 1)
        elif sim == 'a':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[3]),
                             (coords[2], coords[1]), (coords[2], coords[3]),
                             (coords[2], coords[1] + ysize // 2), (coords[0] + xsize // 2,
                                                                   coords[1] + ysize // 2)), 1)
        elif sim == 'b':
            self.lines = pygame.draw.lines(screen, color, True, ((coords[0], coords[1]),
                             (coords[2], coords[1]), (coords[0], coords[1] + ysize // 2),
                             (coords[2], coords[1] + ysize // 2), (coords[0], coords[3])), 1)
        elif sim == 'c':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[2], coords[1]),
                             (coords[0], coords[1] + ysize // 2), (coords[2], coords[3])), 1)
        elif sim == 'e':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[2], coords[1]),
                             (coords[0], coords[1] + ysize // 2), (coords[2],
                                                                   coords[1] + ysize // 2),
                             (coords[0], coords[1] + ysize // 2), (coords[2], coords[3])), 1)
        elif sim == 'f':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[3]),
                             (coords[0], coords[1] + ysize // 2), (coords[2], coords[3]),
                             (coords[0], coords[1] + ysize // 3), (coords[0], coords[1]),
                             (coords[2], coords[1] + ysize // 2)), 1)
        elif sim == 'k':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[1]),
                             (coords[0], coords[1] + ysize // 2), (coords[2], coords[1]),
                             (coords[0], coords[1] + ysize // 2), (coords[2], coords[3]),
                             (coords[0], coords[1] + ysize // 2), (coords[0], coords[3])), 1)
        elif sim == 'l':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[1]),
                             (coords[0], coords[3]), (coords[2], coords[3])), 1)
        elif sim == 'o':
            self.lines = pygame.draw.lines(screen, color, True, ((coords[0] + xsize // 2,
                                                                  coords[1]),
                             (coords[2], coords[1] + ysize // 2), (coords[0] + xsize // 2, coords[3]),
                             (coords[0], coords[1] + ysize // 2)), 1)
        elif sim == 'r':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[3]),
                             (coords[0], coords[1]), (coords[2], coords[1] + ysize // 2),
                             (coords[0], coords[1] + ysize // 2), (coords[2], coords[3])), 1)
        elif sim == 's':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[2], coords[1]),
                             (coords[0], coords[1] + ysize // 2), (coords[2],
                                                                   coords[1] + ysize // 2),
                             (coords[0], coords[3])), 1)
        elif sim == 't':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0],
                                                                   coords[1] + ysize // 2),
                             (coords[0] + xsize // 2, coords[1]), (coords[0] + xsize // 2,
                                                                   coords[3]),
                             (coords[0] + xsize // 2, coords[1]), (coords[2],
                                                                   coords[1] + ysize // 2)), 1)
        elif sim == 'v':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[1]),
                             (coords[0] + xsize // 2, coords[3]), (coords[2], coords[1])), 1)
        elif sim == 'x':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[1]),
                             (coords[0] + xsize // 2, coords[1] + ysize // 2),
                             (coords[0], coords[3]), (coords[2], coords[1]),
                             (coords[0] + xsize // 2, coords[1] + ysize // 2),
                             (coords[2], coords[3])), 1)
        elif sim == 'y':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[1]),
                             (coords[0] + xsize // 2, coords[1] + ysize // 2),
                             (coords[2], coords[1]),
                             (coords[0] + xsize // 2, coords[1] + ysize // 2),
                             (coords[0] + xsize // 2, coords[3])), 1)
        elif sim == 'z':
            self.lines = pygame.draw.lines(screen, color, False, ((coords[0], coords[1]),
                             (coords[2], coords[1]), (coords[0], coords[3]),
                             (coords[2], coords[3])), 1)



def stolb(y0, x0):#проверка столба
    for y in range(n):
        if main_array[y][x0] == main_array[y0][x0] and y != y0:
            return False
    return True

def stroka(y0, x0):#проверка строки
    for x in range(n):
        if main_array[y0][x] == main_array[y0][x0] and x != x0:
            return False
    return True

def blok(y0, x0):#проверка блока
    for x in range((x0 // l) * l, (x0 // l + 1) * l):
        for y in range((y0 // k) * k, (y0 // k + 1) * k):
            if y != y0 and x != x0 and main_array[y][x] == main_array[y0][x0]:
                return False
    return True

def shuffledrange(*args):
    a = list(range(*args))
    random.shuffle(a)
    return a

def check(i, j):#общая проверка
    if stolb(i, j) and stroka(i, j) and blok(i, j):
        return True
    else:
        return False

def generator(r):#генерируем поле
    global generator_run
    if r == n ** 2:
        return True
    x = para[r][0]
    y = para[r][1]
    #print(r, x, y)
    generator_run += 1
    if generator_run > 10 ** 6:
        return False
    for i in range(1, 1 + n):
        main_array[x][y] = i
        #print_array()
        if check(x, y):
            if generator(r + 1):
                return True
    if generator_run <= 10 * 10 ** 6:
        main_array[x][y] = 0
    return False

def clearer():#стираем клетки
    global deleted_pairs
    deleted_pairs = []
    pairs = [(i, j) for i in range(n) for j in range(n)]
    random.shuffle(pairs)
    for i in pairs:
        timer = main_array[i[0]][i[1]]
        numbers = 1
        for j in range(1, 1 + n):
            if j == timer:
                continue
            main_array[i[0]][i[1]] = j
            if check(i[0], i[1]):
                numbers += 1
        main_array[i[0]][i[1]] = timer
        if numbers == 1:
            deleted_pairs.append((i[0], i[1], main_array[i[0]][i[1]]))
            main_array[i[0]][i[1]] = 0
    main_array[deleted_pairs[-1][0]][deleted_pairs[-1][1]] = deleted_pairs[-1][2]

def easy_generator():
    numbers = [i for i in range(1, 1 + n)]
    random.shuffle(numbers)
    for i in range(n):
        main_array[i] = numbers[:]
        timer = numbers[-l:]
        del numbers[-l:]
        timer.extend(numbers)
        numbers = timer
        if (i + 1) % k == 0:
            timer = numbers[-1]
            del numbers[-1]
            numbers.insert(0, timer)

def start_sudoku():
    n, k, l = fieldSizebtn.chagingNum, blockXSizebtn.chagingNum, blockYSizebtn.chagingNum
    if n != k * l:
        return
    if n < 8:
        generator(0)
    else:
        easy_generator()
def easy_filler(r):
    global filler_run
    if r == len(read_pairs):
        return True
    x = read_pairs[r][0]
    y = read_pairs[r][1]
    #print(r, x, y)
    filler_run += 1
    if filler_run > 10 ** 6:
        return False
    for i in range(1, 1 + n):
        main_array[x][y] = i
        #print_array()
        if check(x, y):
            if easy_filler(r + 1):
                return True
    if filler_run <= 10 * 10 ** 6:
        main_array[x][y] = 0
    return False
def solve_sudoku():
    easy_filler(0)
filter_run = 0
generator_run = 0
n = 1
l = 1
k = 1
main_array = [[0 for i in range(n)] for i in range(n)]
para = [(i, j) for i in range(n) for j in range(n)]
random.shuffle(para)
generator_run = 0

restartbtn = Button(screen, (WINXSIZE // 10, WINYSIZE // 20, 3 * (WINXSIZE // 10),
                             3 * (WINYSIZE // 20)), 'restart')
solvebtn = Button(screen, (WINXSIZE // 10, 5 * (WINYSIZE // 20), 3 * (WINXSIZE // 10),
                             7 * (WINYSIZE // 20)), 'solve')
fieldSizebtn = ChangeButton(screen, (WINXSIZE // 10, 9 * (WINYSIZE // 20), 3 * (WINXSIZE // 10),
                                     11 * (WINYSIZE // 20)), 'field size', 9)
blockXSizebtn = ChangeButton(screen, (WINXSIZE // 10, 13 * (WINYSIZE // 20), 3 * (WINXSIZE // 10),
                                     15 * (WINYSIZE // 20)), 'block x size')
blockYSizebtn = ChangeButton(screen, (WINXSIZE // 10, 17 * (WINYSIZE // 20), 3 * (WINXSIZE // 10),
                                     19 * (WINYSIZE // 20)), 'block y size')

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mcoords = event.pos
            if WINXSIZE // 10 <= mcoords[0] <= 3 * (WINXSIZE // 10):
                if WINYSIZE // 20 <= mcoords[1] <= 3 * (WINYSIZE // 20):  # restart
                    restartbtn.clicked()
                    start_sudoku()
                elif 5 * (WINYSIZE // 20) <= mcoords[1] <= 7 * (WINYSIZE // 20):  # solve
                    solvebtn.clicked()
                    solve_sudoku()
            elif WINXSIZE // 10 <= mcoords[0] <= 1.5 * (WINXSIZE // 10):  # left arrows
                if 9 * (WINYSIZE // 20) <= mcoords[1] <= 11 * (WINYSIZE // 20):  # field
                    fieldSizebtn.cangeNum()
                    print(0)
                if 13 * (WINYSIZE // 20) <= mcoords[1] <= 15 * (WINYSIZE // 20):  # block x
                    blockXSizebtn.cangeNum()
                if 17 * (WINYSIZE // 20) <= mcoords[1] <= 19 * (WINYSIZE // 20):  # block y
                    blockYSizebtn.cangeNum()
            elif 1.5 * (WINXSIZE // 10) <= mcoords[0] <= 3 * (WINXSIZE // 10):  # right arrows
                if 9 * (WINYSIZE // 20) <= mcoords[1] <= 11 * (WINYSIZE // 20):  # field
                    fieldSizebtn.cangeNum('')
                if 13 * (WINYSIZE // 20) <= mcoords[1] <= 15 * (WINYSIZE // 20):  # block x
                    blockXSizebtn.cangeNum('')
                if 17 * (WINYSIZE // 20) <= mcoords[1] <= 19 * (WINYSIZE // 20):  # block y
                    blockYSizebtn.cangeNum('')
    pygame.display.flip()
