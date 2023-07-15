"""
DOCSTING:

The purpose of this program is the caculate how much edges or vertices a point has in a graph

- user will create a tree via input on the TI-84CE device
- What is a Graph:

Example Graph:

A1 -EDGE1> A2 -EDGE2> A3 -EDGE3> A4 -EDGE4> A1
A2 -EDGE5> A4 -EDGE6> A1
A3 -EDGE7> A1

- What is a Vertex:
- What is an Edge:
"""


class GraphNode:
    """
    graph Node, connects like a web
    """
    node_name: str = 'A1'
    adajacent_edge_count: int = 0
    adjacent_verticies_count: int = 0
    # stores other instances GraphNode
    connectedNodes_child: list = []
    connectedNodes_parent: list = []

    def __init__(self, node_name: str = 'AA1') -> None:
        self.node_name = node_name
        self.adajacent_edge_count: int = 0
        self.adjacent_verticies_count: int = 0
        self.connectedNodes_child: list = []
        self.connectedNodes_parent: list = []

    def add_child_node(self, ParentNode=None):
        # todo add code to check if the ParetNode is an instance of GraphNode
        pass

    def add_parent_node(self, ChildNode=None):
        # todo add code to check if the ChildNode is an instance of GraphNode
        pass


def display_options():
    """
    display the optiosn of the program
    """
    print('A - Add a New Node to your Graph')
    print('L - List all the Nodes connected to a chosen Node in the Graph')
    print('H - Reprint this message')
    print('Q - Quit the Program')


def create_function(current_node: GraphNode) -> GraphNode:
    """
    creates new nodes to link 
    """
    return current_node


if __name__ == '__main__':
    display_options()
    while True:
        user_input: str = input('')
        if user_input == 'H':
            display_options()
        elif user_input == 'L':
            pass
        elif user_input == 'A':
            pass
        elif user_input == 'Q':
            break
        else:
            print('ERROR - NOT A VALID OPTION')
    print('terminating program')
