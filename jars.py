from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = (3,1,0,0)

GOAL_STATE = (1,1,1,1)

class Jars(SearchProblem):
    def is_goal(self, state):
        return GOAL_STATE == state
    
    def actions(self, state):
        available_actions = []
             
        for jar_index, jar in enumerate(state):
            if jar > 0:
                for jar2_index, jar2 in enumerate(state):
                    if jar2 != jar:
                        if jar2 < jar2_index + 1:
                            available_actions.append((jar_index, jar2_index))


        return available_actions

    def result(self, state, action):
        
        jar_from, jar_to = action

        #convert tuples to list
        state_modifiable = list(pile for pile in state)
        
        needed = (jar_to + 1) - state_modifiable[jar_to]
        
        if state_modifiable[jar_from] >= needed:
            state_modifiable[jar_from] -= needed
            state_modifiable[jar_to] += needed
        else:
            state_modifiable[jar_to] += state_modifiable[jar_from]
            state_modifiable[jar_from] = 0

        #convert list to tuples
        state_modifiable = tuple(row for row in state_modifiable)
        return state_modifiable


    def cost(self, state1,action, state2):
        return 1

problem = Jars(INITIAL_STATE)
result = breadth_first(problem, graph_search=True, viewer=WebViewer()) 