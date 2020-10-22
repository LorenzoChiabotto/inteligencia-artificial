from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = (
    (1,1,1,1,1,1,1,1),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
)



class EightQueens(SearchProblem):
    def is_goal(self, state):
        return state == GOAL_STATE

    def actions(self, state):
        row_zero, col_zero = find(0, state)
        
        available_actions = []. 

        if row_zero > 0:
            available_actions.append(state[row_zero-1][col_zero])
        if row_zero < 2:
            available_actions.append(state[row_zero+1][col_zero])

        if col_zero > 0:
            available_actions.append(state[row_zero][col_zero - 1])
        if col_zero < 2:
            available_actions.append(state[row_zero][col_zero + 1])

        return available_actions

    def result(self, state, action):
        row_zero, col_zero = find(0, state)
        row_piece, col_piece = find(action, state)
        
        #convert tuples to list
        state_modifiable = list(list(row) for row in state)
        state_modifiable[row_zero][col_zero] = action
        state_modifiable[row_piece][col_piece] = 0

        #convert list to tuples
        state_modifiable = tuple(tuple(row) for row in state_modifiable)
        return state_modifiable        


    def cost(self, state1,action, state2):
        return 1
