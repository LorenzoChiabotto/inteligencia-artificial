from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = ((0,0),((2,1), (0,4), (4,3)))

GOAL_STATE = ((5,3),())

#FOOD = ((2,1), (0, 4), (4,3))
BLOCKS = ((3,0), (5, 0), (1,1), (3, 1), (2,2), (4, 2), (0,3), (1,4), (3,4), (5,4), (3,5))

EXIT = (5,3)

class Ratabots(SearchProblem):
    def is_goal(self, state):
        return GOAL_STATE == state
    
    def actions(self, state):
        available_actions = []
        ratabot, foods = state
        ratabot_x, ratabot_y = ratabot
             
        if ratabot_x > 0:
            if (ratabot_x -1, ratabot_y) not in BLOCKS:
                available_actions.append((ratabot_x -1, ratabot_y))
        if ratabot_x < 5:
            if (ratabot_x +1, ratabot_y) not in BLOCKS:
                available_actions.append((ratabot_x +1, ratabot_y))

        if ratabot_y > 0:
            if (ratabot_x, ratabot_y-1) not in BLOCKS:
                available_actions.append((ratabot_x, ratabot_y - 1))
        
        if ratabot_y < 5:
            if (ratabot_x, ratabot_y +1) not in BLOCKS:
                available_actions.append((ratabot_x, ratabot_y+1))


        return available_actions

    def result(self, state, action):
        
        ratabot, foods = state

        #convert tuples to list
        state_modifiable = list(list(pile) for pile in state)

        foods_modifiable = list(pile for pile in foods)
        print(action)
        print(foods_modifiable)
        if action in foods_modifiable: 
            foods_modifiable.remove(action)
            state_modifiable[1] = tuple(tuple(row) for row in foods_modifiable)
        state_modifiable[0] = action

        #convert list to tuples
        state_modifiable = tuple(tuple(row) for row in state_modifiable)
        return state_modifiable


    def cost(self, state1,action, state2):
        return 1

problem = Ratabots(INITIAL_STATE)
result = breadth_first(problem, graph_search=True, viewer=WebViewer())