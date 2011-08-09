#!/usr/bin/python
#coding:utf8


def get_area(field, p_size, pos):
    """
    get the number of trees in a p_size area starting at pos
    """
    num_trees = 0
    for i in range(p_size[0]):
        for j in range(p_size[1]):
            # avoid going out of the field.
            if (pos[0] + i >= len(field)) or (pos[1] + j >= len(field[i])):
                continue
            if field[pos[0]+i][pos[1]+j]:
                num_trees += 1
    return num_trees


def property_finder(field, state_size):
    """
    finds the most amount of trees in a area of state_size
    """
    max_trees = []
    for y in xrange(len(field[0]) - state_size[1]+1):
        # for each line I calculate the num of trees in the area 
        tree_count = get_area(field, state_size, (0, y))
        trees = [tree_count]
        for  x in xrange(1, len(field) - state_size[0] +1):
            #in order to move the window of interest 
            #for each line I subtract the trees in leftmost slice 
            tree_count -= get_area(field, (1, state_size[1]), (x-1, y))
            #and add the trees in the rightmost slice
            tree_count += get_area(field, (1, state_size[1]), (x+state_size[0]-1, y))
            trees.append(tree_count)
        max_trees.append(max(trees))
    return max(max_trees)


def create_field(num_trees, lines):
    """
    Creates the playing field based on the input
    """
    width, height = map(int, lines[0].split())

    # populates with zero
    field = [[0 for j in xrange(height)] for i in xrange(width)]

    #places a 1 on each place that there is a tree
    for i in xrange(num_trees):
        pos_x, pos_y = map(int, lines[i+1].split())
        # the problem is 1 indexed so I need to subtract one from the positions
        field[pos_x-1][pos_y-1] = 1
    return field


def main():
    while True:
        num_trees = int(raw_input())
        if num_trees == 0:
            break
        lines = []
        for i in xrange(num_trees+1):
            lines.append(raw_input())
        state_size = map(int, raw_input().split())
        print property_finder(create_field(num_trees, lines), state_size)


if __name__ == '__main__':
    main()
