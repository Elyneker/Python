# -*- coding: utf-8 -*-
"""
Bloco:
    height = 1
    length = integer

Grid:
    height = w
    width  = h

Rules:
    1 - Blocos podem ser empilhados sobre outros contanto que não saia por um espaço aberto nem passe o limite do grid 
    2 - Todos os blocos são alinhados no grid
    3 - Qualquer dois blocos em uma linha necessita de 1 espaço entre eles
    4 - A linha mais abaixo é ocupada por um bloco de largura w
    5 - A altura máxima do castelo é igual a h
    6 - O castelo é feito de um número n de blocos
"""

def createGrid(columns, lines):
    grid = []
    for line in range(0, lines):
        grid.append([])

        for column in range(0, columns):
            grid[line].append(0)

    return grid

def factorial_with_sum(integer):
    count = 0
    
    for x in range(1, integer + 1):
        count += x
    
    return count

def possibilitiesAmountPerUnit(grid):
    gridWidth = len(grid[0])
    count = 0

    for x in range(1, gridWidth + 1):
        count += x

    return count

def possibilitiesAmountPerGroups(grid, block_size):
    grid_size = len(grid[0])

    qtd_groups = grid_size / (block_size + 1)
    module_groups = grid_size % (block_size + 1)

    if module_groups == block_size:
        qtd_groups += 1

    def possibilitiesPerTypeOfGroup(grid_size, block_size, qtd_groups):
        _possibilities = 1
        _new_grid = grid_size - (qtd_groups - 1)
        _total_of_block_unit = qtd_groups * block_size
        
        if _new_grid > _total_of_block_unit:
            _possibilities = _new_grid - _total_of_block_unit

            return factorial_with_sum(_possibilities + 1)
        else:
            return factorial_with_sum(_possibilities)

    # for group in range(1, qtd_groups + 1):
    print 'qtd_max: %i' %possibilitiesPerTypeOfGroup(grid_size, block_size, 3)

    return qtd_groups

print createGrid(3, 1)
print possibilitiesAmountPerGroups(createGrid(11, 1), 2)