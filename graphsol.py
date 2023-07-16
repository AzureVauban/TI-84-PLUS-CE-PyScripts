"""
Graph edge & verticies solver
What is an edge?:
what is a vertex?:
What is a graph?:
"""


def sq_rt(val: float):
    """
    function obtained from https://stackoverflow.com/questions/46183020/square-root-without-pre-defined-function-in-python#:~:text=Also%20there%20are%20other%20methods,square%20roots%20like%20shown%20here.&text=here%20is%20the%20way%20you,any%20inbuilt%20function%20of%20python.&text=Basically%20the%20program%20run%20for,true%20%2D%20return%20i%20and%20break
    """
    x_val = val
    y_val = 1.000000  # iteration initialisation.
    e_val = 0.000001  # accuracy after decimal place.
    while x_val-y_val > e_val:
        x_val = (x_val+y_val)/2
        y_val = val/x_val
    return x_val


def abs_val(val: float):
    """
    return the absolute value of 
    a number
    """
    if val < 0:
        return val * -1
    return val


def power(val: float, expo: float) -> float:
    """
    function obtained from https://stackoverflow.com/questions/5246856/how-did-python-implement-the-built-in-function-pow
    """
    p_value = 1
    if expo < 0:
        val = 1/val
        # ? might need to make an absolute value function
        expo = abs_val(expo)

    # Exponentiation by Squaring

    while expo:
        if expo % 2:
            p_value *= val
        val *= val
        expo //= 2
    return p_value


class GraphNode:
    """
    graph Node, connects like a web
    """
    node_label = 'A'
    adjacency_matrix = []
    # stores other instances GraphNode
    connected_nodes_child = []
    connected_nodes_parent = []

    def __init__(self, node_label: str) -> None:
        self.node_label = node_label

    def link_child_node(self, child_node):
        """
        create a new doubly linked connection between this node as the parent
        and another node was a child
        """
        if not isinstance(child_node, GraphNode):
            raise TypeError('Node must be an instance of', GraphNode)
        self.connected_nodes_child.append(child_node)
        child_node.connected_nodes_parent.append(self)

    def validate_connection_exists(self, node_check) -> bool:
        """
        checks to see if a connection between this node and another node exists already;
        returns true if connection exists and false if doesn't
        """

        if not isinstance(node_check, GraphNode):
            raise TypeError('Node must be an instance of', GraphNode)
        return False

    def link_parent_node(self, parent_node):
        """
        create a new doubly linked connection between this node as the child
        and another node was a parent
        """


class MyGraph:
    """
    wrapper class for graph nodes
    """
    head_node = GraphNode('A0')

    def __init__(self, graph_label: str) -> None:
        self.head_node = GraphNode(graph_label)

    def display_graph(self):
        """
        draw the graph on the TI-84 screen using ti_mathplt
        """


# main script
print('PRESS 2ND + MODE/QUIT TO STOP\nTWICE RUNNING PROCESS')
# end main script
