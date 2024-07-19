#Defining the structure
#Making a cube object
import random as rd
import copy

class Rubic_Cube:

    def __init__(self):
        self.final_cube = {
                "U" : [["W","W","W"],["W","W","W"],["W","W","W"]],  #Upper Face of cube
                "D" : [["R","R","R"],["R","R","R"],["R","R","R"]],  #Down Face of cube
                "L" : [["G","G","G"],["G","G","G"],["G","G","G"]],  #Left Face of cube
                "R" : [["B","B","B"],["B","B","B"],["B","B","B"]],  #Right Face of cube
                "F" : [["Y","Y","Y"],["Y","Y","Y"],["Y","Y","Y"]],  #Front Face of cube
                "B" : [["O","O","O"],["O","O","O"],["O","O","O"]]  #Back Face of cube
                }
        self.count = 0
        
        self.cube = copy.deepcopy(self.final_cube)

        self.moves = [self.move_U,self.move_D,self.move_R,self.move_L,self.move_F,self.move_B,
                      self.move_antiU,self.move_antiD,self.move_antiB,self.move_antiR,
                      self.move_antiL,self.move_antiF]

        self.inverse_moves = {
            "move_U": self.move_antiU,
            "move_D": self.move_antiD,
            "move_R": self.move_antiR,
            "move_L": self.move_antiL,
            "move_F": self.move_antiF,
            "move_B": self.move_antiB,

            "move_antiU": self.move_U,
            "move_antiD": self.move_D,
            "move_antiR": self.move_R,
            "move_antiL": self.move_L,
            "move_antiF": self.move_F,
            "move_antiB": self.move_B
        }
    
    #To Rotate Individual Face
    def rotate_face(self,face,cube):
        cube[face] = [list(row) for row in zip(*cube[face][::-1])]

    def rotate_face_anti(self,face,cube):
        for a,i in enumerate(cube[face]):
            cube[face][a] = i[::-1]
        cube[face] = [list(row) for row in zip(*cube[face][::1])]
    #To make changes in remaining sides
    #Right
    def move_R(self,cube):
        self.rotate_face("R",cube)
        temp = [cube['U'][i][2] for i in range(3)]
        for i in range(3):
            cube['U'][i][2] = cube['F'][i][2]
            cube['F'][i][2] = cube['D'][i][2]
            cube['D'][i][2] = cube['B'][2-i][0]
            cube['B'][2-i][0] = temp[i]
        

    def move_antiR(self,cube):
        self.rotate_face_anti("R",cube)
        temp = [cube['B'][2-i][0] for i in range(3)]
        for i in range(3):
            cube['B'][2-i][0] = cube['D'][i][2]
            cube['D'][i][2] = cube['F'][i][2]
            cube['F'][i][2] = cube['U'][i][2]
            cube['U'][i][2] = temp[i]
        

    
    #Left
    def move_L(self,cube):
        self.rotate_face("L",cube)
        temp = [cube['U'][i][0] for i in range(3)]
        for i in range(3):
            cube['U'][i][0] = cube['F'][i][0]
            cube['F'][i][0] = cube['D'][i][0]
            cube['D'][i][0] = cube['B'][2-i][2]
            cube['B'][2-i][2] = temp[i]
        
    
    def move_antiL(self,cube):
        self.rotate_face_anti("L",cube)
        temp = [cube['B'][2-i][2] for i in range(3)]
        for i in range(3):
            cube['B'][2-i][2] = cube['D'][i][0]
            cube['D'][i][0] = cube['F'][i][0]
            cube['F'][i][0] = cube['U'][i][0]
            cube['U'][i][0] = temp[i]
        
    
    #UP
    def move_U(self,cube):
        self.rotate_face("U",cube)
        temp = [cube['F'][0][i] for i in range(3)]
        for i in range(3):
            cube['F'][0][i] = cube['R'][0][i]
            cube['R'][0][i] = cube['B'][0][i]
            cube['B'][0][i] = cube['L'][0][i]
            cube['L'][0][i] = temp[i]
        

    def move_antiU(self,cube):
        self.rotate_face_anti("U",cube)
        temp = [cube['L'][0][i] for i in range(3)]
        for i in range(3):
            cube['L'][0][i] = cube['B'][0][i]
            cube['B'][0][i] = cube['R'][0][i]
            cube['R'][0][i] = cube['F'][0][i]
            cube['F'][0][i] = temp[i]
        
    
    #Down
    def move_D(self,cube):
        self.rotate_face("D",cube)
        temp = [cube['F'][2][i] for i in range(3)]
        for i in range(3):
            cube['F'][2][i] = cube['L'][2][i]
            cube['L'][2][i] = cube['B'][2][i]
            cube['B'][2][i] = cube['R'][2][i]
            cube['R'][2][i] = temp[i]
        

    def move_antiD(self,cube):
        self.rotate_face_anti("D",cube)
        temp = [cube['R'][2][i] for i in range(3)]
        for i in range(3):
            cube['R'][2][i] = cube['B'][2][i]
            cube['B'][2][i] = cube['L'][2][i]
            cube['L'][2][i] = cube['F'][2][i]
            cube['F'][2][i] = temp[i]
        

    #Front
    def move_F(self,cube):
        self.rotate_face("F",cube)
        temp = [cube['U'][2][i] for i in range(3)]
        for i in range(3):
            cube['U'][2][i] = cube['L'][2-i][2]
            cube['L'][2-i][2] = cube['D'][0][2-i]
            cube['D'][0][2-i] = cube['R'][i][0]
            cube['R'][i][0] = temp[i]
        
    
    def move_antiF(self,cube):
        self.rotate_face_anti("F",cube)
        temp = [cube['R'][i][0] for i in range(3)]
        for i in range(3):
            cube['R'][i][0] = cube['D'][0][2-i]
            cube['D'][0][2-i] = cube['L'][2-i][2]
            cube['L'][2-i][2] = cube['U'][2][i]
            cube['U'][2][i] = temp[i]
    
    
    #Back
    def move_B(self,cube):
        self.rotate_face("B",cube)
        temp = [cube['U'][0][2-i] for i in range(3)]
        for i in range(3):
            cube['U'][0][2-i] = cube['R'][2-i][2]
            cube['R'][2-i][2] = cube['D'][2][i]
            cube['D'][2][i] = cube['L'][i][0]
            cube['L'][i][0] = temp[i]

    def move_antiB(self,cube):
        self.rotate_face_anti("B",cube)
        temp = [cube['L'][i][0] for i in range(3)]
        for i in range(3):
            cube['L'][i][0] = cube['D'][2][i]
            cube['D'][2][i] = cube['R'][2-i][2]
            cube['R'][2-i][2] = cube['U'][0][2-i]
            cube['U'][0][2-i] = temp[i]
    
    def inverse(self,move,cube):
        inverse_move = self.inverse_moves[move.__name__]
        inverse_move(cube)

    #Method to Shuffle cube
    def shuffle(self,no_moves):
        for _ in range(no_moves):
            move = rd.choice(self.moves)
            move(self.cube)
        

    def display(self):
        for row in self.cube["U"]:
            print("       "," ".join(row))
        print()
        for i in range(3):
            print(" ".join(self.cube["L"][i])," "," ".join(self.cube["F"][i])," "," ".join(self.cube["R"][i])," "," ".join(self.cube["B"][i]))
        print()
        for row in self.cube["D"]:
            print("       "," ".join(row))
        
        print("************************")