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
    
    # Relationship adders:
    def add_friend(new_friend)
        # The current node 
        # and new_friend become friends
        @friends           << new_friend
        new_friend.friends << self
    end
    def add_parent(new_parent)
        # Gives the current node a new parent 
        # and new_parent a child
        @parents            << new_parent
        new_parent.children << self
    end
    def add_child(new_child)
        # Gives the current node a new child 
        # and new_child a parent
        @children         << new_child
        new_child.parents << self
    end
    
    # Relationship removers:
    def disconnect(node)
        # remove the connection, if it exists with a given node
        # if self in node.children or node.parents
            # remove self and 
            # remove node from self.children or self.parents
    end
    
    
end 
