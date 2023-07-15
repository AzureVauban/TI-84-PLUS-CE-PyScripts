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


def create_node_connection(current_node: GraphNode) -> GraphNode:
    """
    creates new nodes to link 
    """
    while True:
        user_choice: str = input(
            'P - Create a new parent Node\nC - Create a new child Node').strip().upper()
        if user_choice == 'P':
            pass  # todo add a function that allows to user to input a list of Nodes
        elif user_choice == 'C':
            pass  # todo add a function that allows to user to input a list of Nodes
        elif user_choice == 'Q':
            return current_node
        elif user_choice == 'H':
            print('P - Create a new parent Node')
            print('C - Create a new child Node')
            print('Q - Return to main menu')
            print('H - display options')
        else:
            print('NOT A VALID CHOICE')


if __name__ == '__main__':
    print('A - Add a New Node to your Graph')
    print('L - List all the Nodes connected to a chosen Node in the Graph')
    print('H - Reprint this message')
    print('Q - Quit the Program')
    first_node_created: bool = False
    stored_graphs: list = []  # lists of all the graphs the user creates during runtime
    while True:
        user_input: str = input('').strip().upper()
        if user_input == 'H':
            print('A - Add a New Node to your Graph')
            print('L - List all the Nodes connected to a chosen Node in the Graph')
            print('H - Reprint this message')
            print('Q - Quit the Program')

        elif user_input == 'L' and len(stored_graphs) != 0:
            for node in stored_graphs:
                print(node.node_name, '-', len(node.connected_nodes_parent),
                      '-', len(node.connected_nodes_child))
        elif user_input == 'L' and len(stored_graphs) == 0:
            print('ERROR - NO GRAPHS CREATED')
        elif user_input == 'A' and not first_node_created:
            # ? have the user create a graph with one Node in it
            stored_graphs.append(
                GraphNode(input('What is the name of the graph you are creating: ')
                          .strip().upper()))
            print('CREATED NEW GRAPH: ', end=stored_graphs[len(
                stored_graphs)-1].node_name+'\n')
        elif user_input == 'A' and first_node_created:
            # ? prompt user if new graph is needed
            user_input = input(
                'Do you want to create another Graph (Y/N): ').strip().upper()
            if user_input == 'Y':
                stored_graphs.append(GraphNode(
                    input('What is the name of the graph you are creating: ').strip().upper()))
            elif user_input == 'N':
                # ? prompt user to add a new node,expand graph
                pass
                # todo finsh creating function to expand selected graph
            else:
                print('ERROR - INPUT NOT VALID - MUST BE Y/N')
            # todo finish adding input flows
        elif user_input == 'Q':
            break
        else:
            print('ERROR - NOT A VALID OPTION - A,L,H,Q')
    print('terminating program')
