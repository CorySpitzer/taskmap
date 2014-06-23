# tm_lib.rb
# Class definitions

class Node
    attr_accessor :children, :parents, :friends
    
    def initialize(children, parents, friends) 
        # Takes three arrays which can be thought of as
        # leads_to, depends_on, and related
        @children = children
        @parents = parents
        @friends = friends
    end
    
    def add_friend(new_friend)
        # The current node and new_friend become friends:
        # Adds new_friend to @friends array
        # And adds self to new_friend.friends
        # Removes other relationships with the current node
    end
    
    def add_parent(new_parent)
        # Gives the current node a new parent and new_parent a child:
        # Adds new_parent to @parents array
        # And adds self to new_parent.children
        # Removes other relationships with the current node
    end
    
    def add_child(new_child)
        # Gives the current node a new child and new_child a parent:
        # Adds new_child to @children array
        # And adds self to new_child.parents
        # Removes other relationships with the current node
    end
end 
