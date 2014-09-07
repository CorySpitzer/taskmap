# tm_lib.py
# Class definitions


class Node:
    
    def __init__(self, name, content, parents, kids):
        ''' Strings: name and content 
            Lists: parents and kids (children)
        '''
        self.content = content
        self.name = name
        self.parents = parents
        self.kids = kids
        
    def get_kids():
        ''' Return a list of kids
        '''
        return self.kids
        
    def get_parents():
        ''' Return a list of parents
        '''
        return self.parents
        
#test = Node('yo', 'do somthing!', [])
