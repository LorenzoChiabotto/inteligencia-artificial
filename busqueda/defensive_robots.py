from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

MAX_ROW = 4
MAX_COL = 5

OBSTACLES = (
    (0,2),
    (1,3),
    (2,1),
)
EXITS = (
    (3,2),
    (0,4),
)

INITIAL_STATE = ((0,1),(0,1))


class EightQueens(SearchProblem):
    def is_goal(self, state):
        return set(EXITS) == set(state)

    def actions(self, state):
        available_actions = []        

        for robot_index, robot in enumerate(state):
            moves = (
                (-1,0),
                (1,0),
                (0,-1),
                (0,1)
            )
            for move in moves:
                move_x, move_y = move
                robot_position_x, robot_position_y = robot

                new_position = (
                    (robot_position_x + move_x),
                    (robot_position_y + move_y)
                )

                if(new_position[0] in range(MAX_ROW) and new_position[1] in range(MAX_COL)):
                    if(new_position not in OBSTACLES):
                        available_actions.append((robot_index, new_position))

        return available_actions

    def result(self, state, action):

        robot_index, new_position = action
        position_x, position_y = new_position

        #convert tuples to list
        state_modifiable = list(state)
        state_modifiable[robot_index] = new_position

        #convert list to tuples
        state_modifiable = tuple(tuple(row) for row in state_modifiable)
        return state_modifiable        


    def cost(self, state1,action, state2):
        return 1
