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
            if pos[0]+i >= len(field) or pos[1]+j >= len(field[i]):
                continue
            if field[pos[0]+i][pos[1]+j]:
                num_trees += 1
    return num_trees

def property_finder(field, property_size):
    max_trees = []
    x = 0
    while x <= len(field) - property_size[0] :
        y = 1
        trees = [get_area(field, property_size, (x,0))]
        while y <= len(field[x]) - property_size[1]:
            print x, y ,field[x][y]
            trees.append( trees[-1] - get_area(field, (1,property_size[1]), (x,y)) + get_area(field, (1,property_size[1]), (x+property_size[0],y)))
            y += 1
        x += 1
        max_trees.extend(trees)
            
    return max(max_trees)

def create_field(field_desc):
    """
    Creates the playing field based on the input
    """
    lines = field_desc.split("\n")

    width, height = map(int,lines[1].split())

    # populates with zero
    field = [[ 0 for j in xrange(height)] for i in xrange(width)]
    
    #places a 1 on each place that there is a tree
    num_trees = int(lines[0])
    for i in xrange(num_trees):
        pos_x, pos_y = map(int, lines[i+2].split() )
        # the problem is 1 indexed so I need to subtract one from the positions
        field[pos_x-1][pos_y-1] = 1
    return field
    

def main():
    pass


if __name__ == '__main__':
    main()
