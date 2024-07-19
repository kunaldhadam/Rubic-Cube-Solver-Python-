from Rubic_Cube import Rubic_Cube

class Prune(Rubic_Cube):
    def __init__(self):
        super().__init__()

    #prune inverse moves example L-L'
    def prune_inverse(self,current_move,last_move=None):
        if last_move is not None and last_move.__name__ == self.inverse_moves[current_move.__name__].__name__:
            return True
        return False
    #DONE!!
        
        
    #prune commutative moves example L->R = R->L
    def prune_com(self, current_move ,last_move = None):
        if last_move is not None:
            if last_move.__name__ in ["move_R","move_antiR"] and current_move.__name__ in ["move_L","move_antiL"]:
                return True
            if last_move.__name__ in ["move_D","move_antiD"] and current_move.__name__ in ["move_U","move_antiU"]:
                return True
            if last_move.__name__ in ["move_B","move_antiB"] and current_move.__name__ in ["move_F","move_antiF"]:
                return True
            
            # if last_move.__name__ in ["move_antiU"] and current_move.__name__ in ["move_antiU"]:
            #     return True
            # if last_move.__name__ in ["move_antiD"] and current_move.__name__ in ["move_antiD"]:
            #     return True
            # if last_move.__name__ in ["move_antiF"] and current_move.__name__ in ["move_antiF"]:
            #     return True
            # if last_move.__name__ in ["move_antiB"] and current_move.__name__ in ["move_antiB"]:
            #     return True
            # if last_move.__name__ in ["move_antiL"] and current_move.__name__ in ["move_antiL"]:
            #     return True
            # if last_move.__name__ in ["move_antiR"] and current_move.__name__ in ["move_antiR"]:
            #     return True
            return False
    #DONE!!

    #prune three times similar moves example L->L->L
    def prune_tri(self,current_move,last2moves):
        if len(last2moves) >= 2:
            if last2moves[-1] == last2moves[-2] and current_move.__name__ == last2moves[-2]:
                return True
        return False
    #DONE!!!


    #Has all three prunings
    def prune(self,current_move, last_move= None, last_2moves = None):
        if self.prune_com(current_move,last_move):
             return True
        if self.prune_inverse(current_move,last_move):
            return True
        if self.prune_tri(current_move,last_2moves):
            return True
        return False
