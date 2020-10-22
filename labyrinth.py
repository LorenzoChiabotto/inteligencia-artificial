from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = (1)
GOAL_STATE = (21)

ROOMS = {
    1:(9,12),
    2:(5,6,7,3),
    3:(2,4,8),
    4:(21,3,8),
    5:(6,2),
    6:(9,5,2),
    7:(9,2),
    8:(4,10,3),
    9:(1,12,6,7),
    10:(8,11,15),
    11:(10),
    12:(1,9,17,14),
    13:(14,17,19),
    14:(12,13),
    15:(10,16,18),
    16:(15,20),
    17:(12,13,19),
    18:(15),
    19:(13,17,20),
    20:(16,19),
    21:(4),
}

class Labyrinth(SearchProblem):
    def is_goal(self, state):
        return GOAL_STATE == state
    
    def actions(self, state):
        available_actions = []
        print(ROOMS.get(state))
        for room in ROOMS.get(state):
            available_actions.append((room))

        return available_actions

    def result(self, state, action):
        
        room = action

        #convert tuples to list
        state_modifiable = state
        state_modifiable = (room)
        #convert list to tuples
        return state_modifiable


    def cost(self, state1,action, state2):
        return 1

problem = Labyrinth(INITIAL_STATE)
result = breadth_first(problem, graph_search=True, viewer=WebViewer())

for element in result.path():
    print(element)
print(result)