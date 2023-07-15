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
    connected_nodes_child: list = []
    connected_nodes_parent: list = []

    def __init__(self, node_name: str = 'AA1') -> None:
        self.node_name = node_name
        self.adajacent_edge_count: int = 0
        self.adjacent_verticies_count: int = 0
        self.connected_nodes_child: list = []
        self.connected_nodes_parent: list = []

    def add_child_node(self, parent_node=None):
        """
        create a Node edge on the current Graph
        """
        self.connected_nodes_child.append(parent_node)

    def add_parent_node(self, child_node=None):
        """
        create a Node edge on the current Graph
        """
        self.connected_nodes_parent.append(child_node)


def create_function(current_node: GraphNode) -> GraphNode:
    """
    creates new nodes to link 
    """
    return current_node


if __name__ == '__main__':
    print('A - Add a New Node to your Graph')
    print('L - List all the Nodes connected to a chosen Node in the Graph')
    print('H - Reprint this message')
    print('Q - Quit the Program')
    while True:
        user_input: str = input('')
        user_input = user_input.upper()
        if user_input == 'H':
            print('A - Add a New Node to your Graph')
            print('L - List all the Nodes connected to a chosen Node in the Graph')
            print('H - Reprint this message')
            print('Q - Quit the Program')

        elif user_input == 'L':
            pass
        elif user_input == 'A':
            pass
        elif user_input == 'Q':
            break
        else:
            print('ERROR - NOT A VALID OPTION')
    print('terminating program')
