from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = (('B'),('A','C'), ())

GOAL_STATE = ((),(), ('C','B','A'))



class SussmanAnomaly(SearchProblem):
    def is_goal(self, state):
        return GOAL_STATE == state
    
    def actions(self, state):
        available_actions = []
        
        for stick_id, stick in enumerate(state):            
            if stick:
                if stick_id > 0:
                    available_actions.append((stick_id, -1))

                if stick_id < 2:
                    available_actions.append((stick_id, 1))

        return available_actions

    def result(self, state, action):
        
        stick_remove, stick_move = action

        #convert tuples to list
        state_modifiable = list(list(pile) for pile in state)

        piece = state_modifiable[stick_remove].pop()
        state_modifiable[stick_remove + stick_move].append(piece)

        #convert list to tuples
        state_modifiable = tuple(tuple(row) for row in state_modifiable)
        return state_modifiable


    def cost(self, state1,action, state2):
        return 1

problem = SussmanAnomaly(INITIAL_STATE)
result = breadth_first(problem, graph_search=True, viewer=WebViewer())