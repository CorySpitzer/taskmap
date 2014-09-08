# task_map.py

    # User XP   
    # Begin at dashboard options to 
    # view map and investigate nodes
    # 


# API
    # Add node
    # connect (child or parent)node
    # disconnect

from tm_lib import Node
import sqlite3 as sql3

def main():
    # Create or reopen the task history DB:
    task_db = sql3.connect('data/task.db')
    
    test_node = Node('yo', 'do something!', [],[])
    
    print test_node.kids
    print test_node.parents
    
    current_node = test_node
    help_string = ("(q)uit, (h)elp, (c)urrent node, (l)ist near nodes, " 
                  "enter an integer to select a node, (m)ap the route "
                  " between to points.\n")
                  
    # The input loop:
    go = True
    while go:
        # Get commands: 
        command = raw_input('Enter a command: ')
        if command.lower()[0] == 'q':
            go = False
        elif command.lower()[0] == 'h':
            print help_string
        elif command.lower()[0] == 'c':
            print current_node
        elif command.lower()[0] == 'l':
            print 'A node list...'
            # print a list of nodes going to and coming from current
            # with numbers for each to select
        elif command.lower()[0] == 'm':
            print 'The whole map...'
            # prints, by level the nodes between the two given
        else:
            try:
                # See if the entered command makes sense as an integer
                node_number = int(command[0])
            except ValueError:
                print "Try a different command:"
                print help_string
            
def to_study():
    ''' Return a node/task that has not been studied recently
        Interacts with study time DB
    '''
    # return random node in not_studied_recently
    pass
    



## Content, leads_to
#t1 = ['content', [t2, t3]]
#t2 = ['c2', [t3, t]]
    
    
main()
