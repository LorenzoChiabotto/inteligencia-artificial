from simpleai.search import (
    backtrack, 
    CspProblem
)

from itertools import combinations

#---------------------------VARIABLES----------------------------------------#
variables = ('p1','p2','p3','p4','p5','p6','p7','p8')

INTERCONECTADAS = (
   ('p1','p3'),
   ('p2','p3'),
   ('p5','p6'),
   ('p7','p8')
    )

domains = {}
for var in variables:
    domains[var] = [
        'escudo mejorado',
        'sistema de comunicaciones'
    ]

domains['p7'].extend(['bahía médica', 'sistema de evasión', 'motor de salto a velocidad de la luz'])
domains['p8'].extend(['bahía médica', 'sistema de evasión', 'motor de salto a velocidad de la luz'])

domains['p1'].extend(['sistema de ocultamiento', 'sistema de apuntamiento de armas', 'lanzador de torpedos de protones'])
domains['p2'].extend(['sistema de ocultamiento', 'sistema de apuntamiento de armas', 'lanzador de torpedos de protones'])
domains['p3'].extend(['sistema de ocultamiento', 'sistema de apuntamiento de armas'])
domains['p4'].extend(['sistema de apuntamiento de armas'])
domains['p5'].extend(['sistema de ocultamiento', 'bahía médica', 'bahía de carga mejorada'])
domains['p6'].extend(['bahía médica', 'bahía de carga mejorada'])


constraints = []

def allDiff(variables, values):    
    return len(set(values)) == len(set(variables))
constraints.append((variables, allDiff))


def hide_system_and_motor(variables, values):    
    return not ('motor de salto a velocidad de la luz' in values and 'sistema de ocultamiento' in values) 
    
constraints.append((variables, hide_system_and_motor))


def lanzador_conexion(variables, values):
    p1, p2, p3 = values

    return ('lanzador de torpedos de protones' == p1 or 'lanzador de torpedos de protones' == p2) and 'sistema de apuntamiento de armas' == p3
    
constraints.append((('p1','p2','p3'), lanzador_conexion))


def shield_and_communication(variables, values):
    return not (set(values) == set(('escudo mejorado', 'sistema de comunicaciones')))

for interconect in INTERCONECTADAS:    
    constraints.append((interconect, shield_and_communication))





result = backtrack(CspProblem(variables, domains, constraints))

print('Result: ')
print(result)