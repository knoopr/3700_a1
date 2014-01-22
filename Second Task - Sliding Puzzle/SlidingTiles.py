from SearchProblem import *
import random, copy

def Find_space(input_Array):
    for index, numbers in enumerate(input_Array):
        if ' ' in numbers:
            return (index, numbers.index(' '))

def Slide_up(input_Array):
    new_Array = copy.deepcopy(input_Array)
    row, column = Find_space(input_Array)
    if row != 2:
        new_Array[row][column] = new_Array[row+1][column]
        new_Array[row+1][column] = ' '
        return new_Array
    return None



def Slide_right(input_Array):
    new_Array = copy.deepcopy(input_Array)
    row, column = Find_space(input_Array)
    if column != 0:
        new_Array[row][column] = new_Array[row][column-1]
        new_Array[row][column-1] = ' '
        return new_Array
    return None


def Slide_down(input_Array):
    new_Array = copy.deepcopy(input_Array)
    row, column = Find_space(input_Array)
    if row != 0:
        new_Array[row][column] = new_Array[row-1][column]
        new_Array[row-1][column] = ' '
        return new_Array
    return None

def Slide_left(input_Array):
    new_Array = copy.deepcopy(input_Array)
    row, column = Find_space(input_Array)
    if column != 2:
        new_Array[row][column] = new_Array[row][column+1]
        new_Array[row][column+1] = ' '
        return new_Array
    return None

class PUZZLE( SearchProblem ):
    def __init__ (self, state=()):
        self.state = state
        self.path = "";
        
        
    def edges(self):
        my_edges=[]
        if self.state[0] != 50:
            result = Slide_up(self.state[1])
            if result != None:
                my_edges.append( Edge( self, "u" , PUZZLE((self.state[0]+1, result))))

            result = Slide_down(self.state[1])
            if result != None:
                my_edges.append( Edge( self, "d" , PUZZLE((self.state[0]+1, result))))

            result = Slide_left(self.state[1])
            if result != None:
                my_edges.append( Edge( self, "l" , PUZZLE((self.state[0]+1, result))))

            result = Slide_right(self.state[1])
            if result != None:
                my_edges.append( Edge( self, "r" , PUZZLE((self.state[0]+1, result))))
            '''my_edges.append( Edge( self, "d" , PUZZLE((self.state[0]+1, Slide_down(self.state[1])))))
            my_edges.append( Edge( self, "l" , PUZZLE((self.state[0]+1, Slide_left(self.state[1])))))
            my_edges.append( Edge( self, "r" , PUZZLE((self.state[0]+1, Slide_right(self.state[1])))))'''
        
        return my_edges
    

    def is_target(self):
        return self.state[1][0] == [1,2,3] and self.state[1][1] == [4,5,6] and self.state[1][2] == [7,8,' ']

if __name__ == "__main__":
    i = 0
    already_Placed = []
    num_Array = [[]*3 for x in xrange(3)]
        
    random.seed()
    while len(already_Placed) < 9 :    #while we haven't generated 8 numbers and a ' '
        new_Tile = random.randint(1,8)
        if new_Tile not in already_Placed: #Generate one of each number
            num_Array[i % 3].append(new_Tile)
            already_Placed.append(new_Tile)
            i += 1
        elif ' ' not in already_Placed:    #Generate one ' '
            num_Array[i%3].append(' ')
            already_Placed.append(' ')
            i += 1

    print str(num_Array) + ":\n\n"
    PUZZLE(state=(0, num_Array)).dfs()
