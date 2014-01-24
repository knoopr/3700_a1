class SearchProblem:
  """
  This class represents the superclass for a search problem.

  Programmers should subclass this superclass filling in specific
  versions of the methods that are stubbed below.
  """

  def __init__( self, state=None ):
    """
    Stub
    Constructor function for a search problem.

    Each subclass should supply a constructor method that can operate with
    no arguments other than the implicit "self" argument to create the
    start state of a problem.

    It should also supply a constructor method that accepts a "state"
    argument containing a string that represents an arbitrary state in
    the given search problem.

    It should also initialize the "path" member variable to a string.
    """
    raise NotImplementedError("__init__");

  # class variable holding a set of strings representing states of the
  # problem that have been visited by the search algorithm
  visited = set();

  def edges( self ):
    """
    Stub
    This method must supply a list or iterator for the Edges leading out 
    of the current state.
    """
    raise NotImplementedError("edges");

  def is_target( self ):
    """
    Stub
    This method must return True if the current state is a goal state and
    False otherwise.
    """

    raise NotImplementedError("is_target");

  def __repr__( self ):
    """
    This method must return a string representation of the current state
    which can be "eval"ed to generate an instance of the current state.
    """

    return self.__class__.__name__ + "( " + repr(self.state) + ")";

  def target_found( self ):
    """
    This method is called when the target is found.

    By default it prints out the path that was followed to get to the 
    current state.
    """
    print "Depth = " + str(len(self.path)),
    print "Total States = " + str(self.total_States[0]),
    print "- Solution: " + self.path

  def continue_search( self ):
    """
    This method should return True if the search algorithm is to continue
    to search for more solutions after it has found one, or False if it
    should not.
    """
    return True;

  def dfs( self ):
    """
    Perform a depth first search originating from the node, "self".
    Recursive method.
    """
  
    self.visited.add( repr(self ) );	# add current node to class variable
					# visited
    for action in self.edges(): # consider each edge leading out of this node
      action.destination.path = self.path + str(action.label);	
					# get the label associated with the
					# action and append it to the path
					# string
      if action.destination.is_target(): 
				# check if destination of edge is target node
        action.destination.target_found();	# perform target found action
        if not self.continue_search():	# stop searching if not required
          break;
      if repr(action.destination) in self.visited:
        continue;		# skip if we've visited this one before

      action.destination.dfs();			# resume recursive search 



  def bfs(self, level=0, queue = []):
    if not queue:
      queue.append(Edge( "", "", self))
    
    while queue and not len(queue[0].destination.path) == level:
        #while not cur_Queue:#not cur_Queue.index(0).destination.state[0] == 25:
      queue_Node = queue.pop(0)
      for action in queue_Node.destination.edges():
        action.destination.path = queue_Node.destination.path + str(action.label);
        #print action.destination.path,
        #print action.destination.state[0]
        queue.append(action)


    for action in queue:
        if action.destination.is_target():
          action.destination.target_found()
          if not self.continue_search():
            break

class Edge:
  """
  This class represents an edge between two nodes in a SearchProblem.
  Each edge has a "source" (which is a subclass of SearchProblem), a
  "destination" (also a subclass of SearchProblem) and a text "label".
  """

  def __init__( self, source, label, destination ):
    """
    Constructor function assigns member variables "source", "label" and
    "destination" as specified.
    """
    self.source = source;
    self.label = label;
    self.destination = destination;

  def __repr__( self ):
    return "Edge(" + repr( self.source ) + "," + \
                     repr( self.label ) + "," + \
                     repr( self.destination ) + ")";
