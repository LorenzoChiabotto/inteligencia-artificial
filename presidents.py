from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

# 0 = Auditorio
# 1 = Hall
# 2 = Prensa

# 0 = Capitalistas
# 1 = Comunistas
# 2 = Centristas
INITIAL_STATE = (
    (2,2,2),
    (0,0,0),
    (0,0,0)
    )
GOAL_STATE = (
    (0,0,0),
    (0,0,0),
    (2,2,2)
    )


def isActionValid(state):
    for sala_index, sala in enumerate(state):
        if sala in ((2,0,0), (0,2,0), (0,0,2)):
            return False
        for partido_index, partido in enumerate(sala):
            if partido == 1:
                if sala_index < 1:
                    if state[sala_index+1][partido_index] == 0:
                        return False
                        
    return True


class Presidents(SearchProblem):
    def is_goal(self, state):
        return GOAL_STATE == state
    
    def actions(self, state):
        available_actions = []
        for sala_index, sala in enumerate(state):
            if sala_index < 2:
                for partido_index, partido in enumerate(sala):
                    if partido > 1:
                        for amount in (1, 2):

                            action = [0,0,0]
                            action[partido_index] = amount
                            action = tuple(row for row in action)
                            action = (sala_index, sala_index+1, action)
                            if isActionValid(self.result(state, action)) and action not in available_actions:
                                available_actions.append(action)

                    if partido > 0:
                        for remaining_index, remaining in enumerate(sala):
                            if remaining_index != partido_index:   
                                if remaining >= 1:                             
                                    action = [0,0,0]
                                    action[partido_index] = 1
                                    action[remaining_index] = 1

                                    action = tuple(row for row in action)
                                    action = (sala_index, sala_index+1, action)
                                    if isActionValid(self.result(state, action)) and action not in available_actions:
                                        available_actions.append(action)
        return available_actions

    def result(self, state, action):
        
        sala_inicial, sala_destino, presidents = action

        #convert tuples to list
        state_modifiable =list(list(row) for row in state)
        for president_id, president in enumerate(presidents):
            state_modifiable[sala_inicial][president_id] -= president
            state_modifiable[sala_destino][president_id] += president

        #convert list to tuples
        state_modifiable = tuple(tuple(row) for row in state_modifiable)
        return state_modifiable


    def cost(self, state1,action, state2):
        return 1

problem = Presidents(INITIAL_STATE)
result = breadth_first(problem, graph_search=True, viewer=WebViewer())

for element in result.path():
    print(element)
print(result)