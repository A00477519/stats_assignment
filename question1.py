#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:25:49 2023

@author: papantiamoah

question 1
"""

def modify_stack(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.insert(0, new_element)
    elif operation == 'remove':
        our_list.pop(0)
    return our_list
        
    
def modify_queue(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove':
        our_list.pop(0)
    return our_list
        

if __name__ == '__main__':        

    new_list = [1,2,3,4]

    print("Adding new element to the stack")
    new_list = modify_stack(new_list, 'add', 0)
    print(new_list)

    print("Adding remove an element from stack")
    new_list = modify_stack(new_list, 'remove')
    print(new_list)

    print("Adding new element to the queue")
    new_list = modify_queue(new_list, 'add', 5)
    print(new_list)

    print("Adding remove and element from the queue")
    new_list = modify_queue(new_list, 'remove')
    print(new_list)

