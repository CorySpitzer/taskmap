    # tm_lib.py
# Class definitions

class Map:
    
    def __init__(self)
        '''
        '''
        self.current_node = Node.new # a default starting node
        pass
    
    def save(name=current_map)
        '''
        '''
        pass
        
    def open_map(path)
        '''
        '''
        pass
        
    def get_path(name=current_map)
        '''
        '''
        pass
        
    def add_node(name)
        '''
        '''
        pass
    
    def go_to_node(node)
        ''' # switch current node to name
        '''
        pass
            

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
        
class Task_db:
    ''' A sqlite3 database of the tasks a given student has done
    '''
    def __init__(self):
        '''
        '''
        pass
        
    

class User:
    ''' A User or student class to allow for multiple people 
        to use the software
    '''
    def __init__(self):
        '''
        '''
        pass



#test = Node('yo', 'do somthing!', [])
