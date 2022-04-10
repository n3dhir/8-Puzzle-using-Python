import pygame, random, copy
pygame.init()


class button():
  def __init__(self, color, x,y,width,height, text=''):
    self.color = color
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text

  def draw(self,win):
    pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
    if self.text != '':
      font = pygame.font.SysFont('comicsans', 11)
      text = font.render(str(self.text), 1, (0,0,0))
      win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

  def isOver(self, pos):
    #Pos is the mouse position or a tuple of (x,y) coordinates
    if pos[0] > self.x and pos[0] < self.x + self.width:
      if pos[1] > self.y and pos[1] < self.y + self.height:
        return True
    return False



BFS_button = button((206, 121, 159), 400, 500, 100, 35, "BFS")
bfs_visite = button((206, 121, 159), 400, 550, 100, 35, "0")
bfs_chemin = button((206, 121, 159), 400, 600, 100, 35, "+OO")

DFS_button = button((206, 121, 159), 550, 500, 100, 35, "DFS")
dfs_visite = button((206, 121, 159), 550, 550, 100, 35, "0")
dfs_chemin = button((206, 121, 159), 550, 600, 100, 35, "+OO")


A_STAR_button = button((206, 121, 159), 700, 500, 100, 35, "A*")
a_star_visite = button((206, 121, 159), 700, 550, 100, 35, "0")
a_star_chemin = button((206, 121, 159), 700, 600, 100, 35, "+OO")

MANHATTAN_button = button((206, 121, 159), 850, 500, 100, 35, "MANHATTAN")
manhattan_visite = button((206, 121, 159), 850, 550, 100, 35, "0")
manhattan_chemin = button((206, 121, 159), 850, 600, 100, 35, "+OO")



SHUFFLE_button = button((206, 121, 159), 1100, 600, 80, 35, "SHUFFLE")
RESET_button = button((206, 121, 159), 1200, 600, 80, 35, "RESET")


Noeuds_Visités = button((206, 121, 159), 280, 550, 110, 35, "Noeuds Visités")
longueur_chemin = button((206, 121, 159), 280, 600, 110, 35, "longueur du chemin")





images = []

# initial = [1, 2, 3, 4, 5, 6, 0, 7, 8]
# final = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# initial = [0, 2, 3, 1, 8, 5, 4, 7, 6]
# final = [1, 2, 3, 4, 5, 6, 7, 8, 0]


initial = [1, 2, 7, 8, 5, 0, 3, 6, 4]
final = [1, 2, 3, 8, 0, 4, 7, 6, 5]


# initial = [1, 4, 7, 8, 5, 2, 0, 3, 6]
# final = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# initial = [0, 1, 2, 5, 6, 3, 4, 7, 8]
# final = [1, 2, 3, 4, 5, 6, 7, 8, 0]



# initial = [0, 2, 1, 3, 7, 5, 8, 6, 4]
# final = [1, 2, 3, 4, 5, 6, 7, 8, 0]


# initial = [5, 3, 4, 2, 1, 6, 8, 7, 0]
# final = [1, 2, 3, 4, 5, 6, 7, 8, 0]


# initial = [5, 2, 1, 3, 7, 0, 8, 6, 4]
# final = [1, 2, 3, 4, 5, 6, 7, 8, 0]


# initial = [2, 3, 1, 5, 4, 8, 7, 6, 0]
# final = [1, 2, 3, 4, 5, 6, 7, 8, 0]


# initial = [5, 2, 1, 3, 7, 0, 8, 6, 4]
# final = [0, 2, 1, 3, 7, 5, 8, 6, 4]


initial = [1, 2, 7, 8, 5, 0, 3, 6, 4]
final = [1, 2, 3, 4, 5, 6, 7, 8, 0]


initial = [1, 3, 2, 4, 7, 5, 8, 0, 6]
final = [1, 2, 3, 4, 5, 6, 7, 8, 0]

initial = [4, 3, 1, 7, 2, 6, 8, 5, 0]
final = [1, 2, 3, 4, 5, 6, 7, 8, 0]


# initial = [3, 0, 6, 5, 4, 1, 8, 7, 2]
# final = [1, 2, 3, 4, 5, 6, 7, 8, 0]


initial = [5, 2, 7, 1, 0, 8, 4, 6, 3]
final = [1, 2, 3, 4, 5, 6, 7, 8, 0]

taquin = copy.deepcopy(initial)



def shuffle():
  for i in range(100):
    x = random.randint(0, 8)
    y = random.randint(0, 8)
    taquin[x], taquin[y] = taquin[y], taquin[x]
    images[x], images[y] = images[y], images[x]

def reset(state = initial):
  taquin = copy.deepcopy(state)
  for i in range(9):
    images[i] = pygame.image.load('assets/' + str(taquin[i]) + '-solid.png')
  return taquin


def moves(pos):
  t = []
  if(pos != 2 and pos != 5 and pos != 8):
    t.append(1)
  if(pos != 0 and pos != 3 and pos != 6):
    t.append(-1)
  if(pos != 0 and pos != 1 and pos != 2):
    t.append(-3)
  if(pos != 6 and pos != 7 and pos != 8):
    t.append(3)
  return t

def track(ancestor, node, val, zone):
  pile = []
  pile.append(node)
  while ancestor[str(node)] != node:
    node = ancestor[str(node)]
    pile.append(node)
  zone.text = str(len(pile))
  while pile:
    node = pile[-1]
    pile.pop(-1)
    taquin = reset(node)
    draw(val)
  # print("taquin: ", taquin)

def swap(tab, val):
  x = tab.index(0)
  t = copy.deepcopy(tab)
  t[x], t[x + val] = t[x + val], t[x]
  return t

def bfs():
  n = 0
  visited = set()
  ancestor = dict()
  queue = []
  queue.append(taquin)
  visited.add(str(taquin))
  ancestor[str(taquin)] = taquin
  while(queue):
    n += 1
    aux = queue[0]
    queue.pop(0)
    # print(aux)
    if(aux == final):
      # print(n)
      bfs_visite.text = n
      track(ancestor, aux, 250, bfs_chemin)
      break
    x = aux.index(0)
    for i in moves(x):
      state = swap(aux, i)
      if str(state) not in visited:
        queue.append(state)
        visited.add(str(state))
        ancestor[str(state)] = aux





def dfs():
  visited = set()
  ancestor = dict()
  ancestor[str(taquin)] = taquin
  pile = []
  pile.append(taquin)
  n = 0
  while pile:
    n += 1
    state = pile[-1]
    pile.pop(-1)
    # print(state)
    visited.add(str(state))
    if(state == final):
      # print(n)
      dfs_visite.text = n
      track(ancestor, state, 0, dfs_chemin)
      return
    x = state.index(0)
    for i in moves(x):
        aux = swap(state, i)
        if str(aux) not in visited:
          ancestor[str(aux)] = state
          pile.append(aux)



def malplace(state):
  # print("haha",state, final)
  nb = 0
  for i in range(9):
    if state[i] != final[i]:
      nb += 1
  return nb




def distance(state):
  nb = 0
  for i in range(9):
    y = i % 3
    x = (i - y) / 3
    pos = final.index(state[i])
    xx = pos % 3
    yy = (pos - xx) / 3
    nb += abs(x - xx) + abs(y - yy)
  return nb











def heuristique(typedeheuristique):
  n = 0
  openset = set()
  closedset = set()
  G = {}
  H = {}
  parent = {}
  Current = taquin
  strCurrent = str(Current)
  G[strCurrent] = 0
  H[strCurrent] = typedeheuristique(Current)

  openset.add(strCurrent)
  parent[strCurrent] = Current

  while openset:
    n += 1
    aux = min(openset, key=lambda st: G[st] + H[st])
    Current = []
    for i in aux:
      if i == '1':
        Current.append(1)
      if i == '2':
        Current.append(2)
      if i == '3':
        Current.append(3)
      if i == '4':
        Current.append(4)
      if i == '5':
        Current.append(5)
      if i == '6':
        Current.append(6)
      if i == '7':
        Current.append(7)
      if i == '8':
        Current.append(8)
      if i == '0':
        Current.append(0)
    if(Current == final):
      # print(n)
      if typedeheuristique == distance:
        manhattan_visite.text = n
        track(parent, Current, 250, manhattan_chemin)
      else:
        a_star_visite.text = n
        track(parent, Current, 250, a_star_chemin)
      break
    strCurrent = str(Current)
    openset.remove(strCurrent)
    closedset.add(strCurrent)

    for i in moves(Current.index(0)):
      # print("current: ", Current)
      # print(i)
      node = swap(Current, i)
      strNode = str(node)
      if strNode in closedset:
        continue
      if strNode in openset:
        new_g = G[strCurrent] + 1
        if G[strNode] > new_g:
          G[strNode] = new_g
          parent[strNode] = Current
      else:
        G[strNode] = G[strCurrent] + 1
        H[strNode] = typedeheuristique(node)
        parent[strNode] = Current
        openset.add(strNode)







pygame.display.set_caption("8-Puzzle")
window = pygame.display.set_mode((1365, 700))
background = pygame.image.load('assets/background.png')
background = pygame.transform.scale(background, (1365, 700))




for i in range(9):
  images += [pygame.image.load('assets/' + str(taquin[i]) + '-solid.png')]

def draw(val):
  pygame.time.wait(val)
  nl = 0
  for i in range(9):
    if(i % 3 == 0):
      nl += 1
    window.blit(images[i], (95 * (i % 3) + 520, 95 * nl + 50))
  pygame.display.update()





running = True
while running:
  clock = pygame.time.Clock()
  window.blit(background, (0, 0))
  

  BFS_button.draw(window)
  bfs_visite.draw(window)
  bfs_chemin.draw(window)


  DFS_button.draw(window)
  dfs_visite.draw(window)
  dfs_chemin.draw(window)

  A_STAR_button.draw(window)
  a_star_visite.draw(window)
  a_star_chemin.draw(window)

  MANHATTAN_button.draw(window)
  manhattan_visite.draw(window)
  manhattan_chemin.draw(window)

  SHUFFLE_button.draw(window)
  RESET_button.draw(window)


  Noeuds_Visités.draw(window)
  longueur_chemin.draw(window)

  draw(0)
  pygame.display.update()
  clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      if BFS_button.isOver(pos):
        bfs()
      if DFS_button.isOver(pos):
        dfs()
      if A_STAR_button.isOver(pos):
        heuristique(malplace)
      if MANHATTAN_button.isOver(pos):
        heuristique(distance)
      if SHUFFLE_button.isOver(pos):
        bfs_visite.text = "0"
        bfs_chemin.text = "+OO"

        dfs_visite.text = "0"
        dfs_chemin.text = "+OO"


        a_star_visite.text = "0"
        a_star_chemin.text = "+OO"

        manhattan_visite.text = "0"
        manhattan_chemin.text = "+OO"
        shuffle()

      if RESET_button.isOver(pos):
        taquin = reset(taquin)
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False
