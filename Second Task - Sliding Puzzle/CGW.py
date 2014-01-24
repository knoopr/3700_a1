from SearchProblem import *;
import copy

def remove_letter( input_string, letter ):
  return input_string.replace( letter, "" );

def add_letter( input_string, letter ):
  return "".join( sorted( input_string+letter ) );

class CGW( SearchProblem ):

  def __init__( self, state= (1, "CGW", "" ),states_Visited = [0],passed_Previous=[] ):
    self.state = state;
    self.total_States = states_Visited
    self.previous_States = copy.deepcopy(passed_Previous)
    self.total_States[0] += 1
    self.om_nom_nom();
    self.path = "";

  def om_nom_nom( self ):
    if self.state[0] == 1:	# if human is on left side
      right = self.state[2];
      if "G" in right:
        right = remove_letter( right, "C" );
    
      if "W" in right:
        right = remove_letter( right, "G" );

      self.state = (self.state[0], self.state[1], right );

    elif self.state[0] == 2:	# if human is on right side

      left = self.state[1];

      if "G" in left:
        left = remove_letter( left, "C" );

      if "W" in left:
        left = remove_letter( left, "G" );


      self.state = ( self.state[0], left, self.state[2] );
    else:
      raise IndexError( "Side must be 1 or 2" );

  def edges( self ):
    my_edges = [];
    
    if str(self.state[0]) + ":" + self.state[1]+ "," + self.state[2] not in self.previous_States:
        self.previous_States.append(str(self.state[0]) + ":" + self.state[1]+ "," + self.state[2])
    else:
        return my_edges

    if self.state[0]==1:	# human on left-side
      new_human_location = 2;

      for animal in self.state[1]:
        new_left_side = remove_letter( self.state[1], animal );
        new_right_side = add_letter( self.state[2], animal );
        
        my_edges.append( Edge( self, animal, CGW( ( new_human_location,
                                                    new_left_side, 
                                                    new_right_side ),
                                                    self.total_States,
                                                    self.previous_States ) ) );

    elif self.state[0]==2:	# human on right-side
      new_human_location = 1;

      for animal in self.state[2]:
        new_right_side = remove_letter( self.state[2], animal );
        new_left_side = add_letter( self.state[1], animal );
        
        my_edges.append( Edge( self, animal, CGW( ( new_human_location,
                                                    new_left_side, 
                                                    new_right_side ),
                                                    self.total_States,
                                                    self.previous_States ) ) );
        
    else:
      raise IndexError( "Side must be 1 or 2" );
    # finally add one more edge for the human crossing the river alone
    my_edges.append( Edge( self, "-", CGW( ( new_human_location,
                                             self.state[1],
                                             self.state[2] ),
                                             self.total_States,
                                             self.previous_States) ) );


    return my_edges;

  def is_target( self ):
    return self.state[0]==2 and self.state[2] == "CGW";

if __name__ == "__main__":
  print "\nDepth first search results:"
  CGW( state=(1,"CGW",""), states_Visited=[0] ).dfs();
  print "\nBreadth search results:"
  for j in (range(25)):
    CGW( state=(1,"CGW",""), states_Visited=[0] ).bfs(level = j, queue = []);
