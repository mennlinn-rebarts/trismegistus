##game_of_life_02.py 0.2 191201 ##started git hub project made from game_of_life_01.py

import random

class Life_World:
    def __init__(world, life_grid, grid_size, population):
        world.life_grid = life_grid
        world.grid_size = grid_size
        world.population = population
	
    def print_world(world):
        print(f'World populaton is {world.population}.')

    def print_world_test(world, number):
        print(f'World populaton is {world.population}.  Test #:{number}')	
	
world_1 = Life_World([], 0, 0)

grid_size = 5
index = 0

# def fill_list(n):
    # return range(1, n+1)

#fills list, l, with 1 to len(l)    
def fillmylist(l, n):
    l.extend(range(1, n + 1))

def fillmylist_0or1(l, n):
    l.extend(range(1, random.getrandbits(1)))

def print_grid(grid):
    for li in grid:
        print (li)

#populates life_grid with random 1's and 0's
def seed_life_grid(grid_size):
    grid = []
    for i in range(grid_size):
        grid.append([])
    # for li in grid:
        # fillmylist_0or1(li, grid_size)   
    for li in grid:
        fillmylist(li, grid_size)
    for li in grid:
        for item in range(0, len(li)):
            li[item] = random.getrandbits(1)
        #print (li)
    return grid

def count_live_neighbors(grid, row, col, grid_size):
    live_neighbors = 0
    if ((row == 0)and(col == 0)):
        live_neighbors = grid[0][1]+grid[1][0]+grid[1][1]
    elif ((row == 0)and(col < grid_size-1)):
        live_neighbors = grid[0][col-1]+grid[0][col+1]+grid[1][col-1]+grid[1][col]+grid[1][col+1]
    elif ((row == 0)and(col == grid_size-1)):
        live_neighbors = grid[row][col-1]+grid[row+1][col-1]+grid[row+1][col]
    elif ((row > 0 and row < grid_size-1)and(col == 0)):
        live_neighbors = grid[row-1][col]+grid[row-1][col+1]+grid[row][col+1]+grid[row+1][col]+grid[row+1][col+1]
    elif ((row > 0 and row < grid_size-1)and(col > 0 and col < grid_size-1)):
        live_neighbors = grid[row-1][col-1]+grid[row-1][col]+grid[row-1][col+1]+grid[row][col-1]+grid[row][col+1]+grid[row+1][col-1]+grid[row+1][col]+grid[row+1][col+1]
    elif ((row > 0 and row < grid_size-1)and(col == grid_size-1)):
        live_neighbors = grid[row-1][col-1]+grid[row-1][col]+grid[row][col-1]+grid[row+1][col-1]+grid[row+1][col]
    elif ((row == grid_size-1)and(col == 0)):
        live_neighbors = grid[row-1][col]+grid[row-1][col+1]+grid[row][col+1]
    elif ((row == grid_size-1)and(col < grid_size-1)):
        live_neighbors = grid[row-1][col-1]+grid[row-1][col]+grid[row-1][col+1]+grid[row][col-1]+grid[row][col+1]
    elif ((row == grid_size-1)and(col == grid_size-1)):
        live_neighbors = grid[row-1][col-1]+grid[row-1][col]+grid[row][col-1]
    else:
        live_neighbors = -1
    return live_neighbors

def live_or_die(cell, live_neighbors):
    if (cell == 0):
        if (live_neighbors == 3):
            cell = 1
        else:
            cell = 0            
    elif (cell == 1):
        if ((live_neighbors == 2) or (live_neighbors == 3)):
            cell = 1
        else:
            cell = 0
    else:
        cell = -1
    return cell

def iterate_life_grid(grid, grid_size):
    #row = 0
    #col = 0
    next_grid = seed_life_grid(grid_size)
    #live_grid = grid
    for row in range(grid_size):
        for col in range(grid_size):
            #print(grid[row][col], end = '')
            live_neighbors = count_live_neighbors(grid, row, col, grid_size)
            #print(live_neighbors)
            #print(live_neighbors, end='')
            next_grid[row][col] = live_or_die(grid[row][col], live_neighbors)
            #live_grid[row][col] = live_neighbors
        #print("")
    return next_grid
    #return live_grid
  
  
print ("genesis:")
life_grid = seed_life_grid(grid_size)
print_grid(life_grid)
# n = 2
# print(life_grid[n][n])
# print(life_grid[n-1][n+1])
# life_grid_temp = life_grid
# print_grid(life_grid_temp)
step_count = 10
for step in range(step_count):
    life_grid = iterate_life_grid(life_grid, grid_size)
    print("")
    print ("next grid:")
    print_grid(life_grid)

world_1.life_grid = life_grid

print("world 1:")
print_grid(world_1.life_grid)

world_1.print_world()
#world_1 is implicit 1st argument
world_1.print_world_test(5)

# life_grid = iterate_life_grid(life_grid, grid_size)
# print("")
# print ("next grid:")
# print_grid(life_grid)


##count_live_neighbors test
# live_neighbors = count_live_neighbors(life_grid, 0, 0, grid_size)
# print(live_neighbors, end='')
# live_neighbors = count_live_neighbors(life_grid, 0, 4, grid_size)
# print(live_neighbors, end='')
# live_neighbors = count_live_neighbors(life_grid, 2, 2, grid_size)
# print(live_neighbors, end='')
# live_neighbors = count_live_neighbors(life_grid, 4, 0, grid_size)
# print(live_neighbors, end='')
# live_neighbors = count_live_neighbors(life_grid, 4, 4, grid_size)
# print(live_neighbors, end='')
# live_neighbors = count_live_neighbors(life_grid, -1, -1, grid_size)
# print(live_neighbors, end='')


# for item in life_grid:
    # print(item)
# for item in life_grid:
    # print(id(item))


   
# grid = []
# for i in range(grid_size):
    # grid.append([])
# for li in grid:
    # print(id(li)) #prints address of list
    # print (li) #prints contents of list
# for li in grid:
    # fillmylist(li, grid_size)
    # print (li)
# for li in grid:
    # for item in range(0, len(li)):
        # li[item] = 0
    # print (li)
# for li in grid:
    # for item in range(0, len(li)):
        # li[item] = random.getrandbits(1)
    # print (li)  




###notes/scratchpad below
# build an array prototype
# grid = []
# for i in range(5):
    # grid.append([])
# for li in grid:
    # print(id(li))
    
    
# bool(random.getrandbits(1))

# class Person:
  # def __init__(self, name, age):
    # self.name = name
    # self.age = age
  # def myfunc(self):
    # print("Hello my name is " + self.name)
# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

#print(f'Total score for {name} is {score}')
