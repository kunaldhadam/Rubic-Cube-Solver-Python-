from Rubic_Cube import Rubic_Cube
from Prune import Prune
prn = Prune()

class ExtendRubic_Cube(Rubic_Cube):
    def __init__(self):
        super().__init__()

    def is_corner_solved(self,correct_corners):
        indice = [0,2]
        for face in self.final_cube:
            for idx in indice:
                for idc in indice:
                    if self.final_cube[face][idx][idc] == correct_corners[face][idx][idc]:
                        continue
                    else:
                        return False
        return True
    
#---------------------------------------------------------------------------------------------------
    def Brute_force(self,node):
        depth = 0
        while True:
            # if depth == 8:
            #     break
            found, moves_list = self.dfs_with_depth_limit(node,depth)
            if found:
                return moves_list
            depth += 1
    
    def dfs_with_depth_limit(self,node,depth_limit,last_2moves = [],last_move = None):
        if self.is_corner_solved(node): #to solve corners
            return True, []
        if depth_limit <= 0:
            self.count += 1
            return False, [] 
        for move in self.moves:
            #---------------PRUNE USELESS MOVES ----------------
            if prn.prune(move,last_move,last_2moves):
                continue  
            last_2moves.append(move.__name__)
            #---------------------------------------------------
            move(node)
            found,moves_list = self.dfs_with_depth_limit(node,depth_limit-1,last_2moves,move)
            if found:
                return True, [move.__name__] + moves_list
            if len(last_2moves) != 0:
                last_2moves.pop(-1)
            self.inverse(move,node)
        return False, []  # meaning: didnt find the moves
#---------------------------------------------------------------------------------------------------
    

    
            