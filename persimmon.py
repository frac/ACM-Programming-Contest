#!/usr/bin/python
#coding:utf8

def persimon(field, property_size):
    pass

def create_field(field_desc):
    lines = field_desc.split("\n")
    width, height = map(int,lines[1].split())
    field = [[ 0 for j in xrange(height)] for i in xrange(width)]
    num_trees = int(lines[0])
    for i in xrange(num_trees):
        pos_x, pos_y = map(int, lines[i+2].split() )
        field[pos_x-1][pos_y-1] = 1
    return field
    

def main():
    pass


if __name__ == '__main__':
    main()
