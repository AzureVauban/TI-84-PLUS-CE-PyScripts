"""
Graph edge & verticies solver
What is an edge?:
what is a vertex?:
What is a graph?:


adajency matrix
[   [0,0,0],
    [0,1,0],
    [1,1,0]
]
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
        self.connected_nodes_child = []
        self.connected_nodes_parent = []

    def link_child_node(self, child_node :GraphNode):
        """
        create a new doubly linked connection between this node as the parent
        and another node was a child
        """
        if not isinstance(child_node, GraphNode):
            raise TypeError('Node must be an instance of', GraphNode)
        if not self.__validate_connection_exists(child_node):
            self.connected_nodes_child.append(child_node)
            child_node.connected_nodes_parent.append(self)
            #! update adajency graph
        else:
            print('UNABLE CONNECT CHILD NODE', child_node.node_label,
                  '\nTO PARENT NODE', self.node_label)

    def link_parent_node(self, parent_node):
        """
        create a new doubly linked connection between this node as the parent
        and another node was a child
        """
        if not isinstance(parent_node, GraphNode):
            raise TypeError('Node must be an instance of', GraphNode)
        if not self.__validate_connection_exists(parent_node):
            self.connected_nodes_child.append(parent_node)
            parent_node.connected_nodes_parent.append(self)
            #! update adajency graph
        else:
            print('UNABLE CONNECT PARENT NODE', parent_node.node_label,
                  '\nTO CHILD NODE', self.node_label)

    def __validate_connection_exists(self, node_check) -> bool:
        """
        checks to see if a connection between this node and another node exists already;
        returns true if connection exists and false if doesn't
        """

        if not isinstance(node_check, GraphNode):
            raise TypeError('Node must be an instance of', GraphNode)
        for node in self.connected_nodes_child:
            if not isinstance(node, GraphNode):
                raise TypeError('child node must an instance of', GraphNode)
        for node in self.connected_nodes_parent:
            if not isinstance(node, GraphNode):
                raise TypeError('parent node must an instance of', GraphNode)
        isnode_presentinchild = node in self.connected_nodes_child
        isnode_presentinparent = node in self.connected_nodes_parent
        #!islist_empty = len(self.connected_nodes_parent) > 0 or len(self.connected_nodes_parent) == 0
        if isnode_presentinparent or isnode_presentinchild:
            return True
        return False


class MyGraph:
    """
    wrapper class for graph nodes
    """
    graph_label = 'A'
    head_node = GraphNode('A0')
    graph_population = 0

    def __init__(self, graph_label: str) -> None:
        self.graph_label = graph_label
        #!initial_node_name = self.graph_label+'_'+str(MyGraph.graph_population)
        self.head_node = GraphNode(
            self.graph_label+'_'+str(MyGraph.graph_population))
        self.graph_population = 1

    def display_graph(self):
        """
        draw the graph on the TI-84 screen using ti_mathplt
        """


def help_prompt():
    """output instructions and user choices
    """
    print('A - Create graphs & add nodes')
    print('D - Remove a node from graph')
    print('L - List nodes within a graph')
    print('H - Display cmd options')
    print('Q - Quit program\n')


def display_list_of_graphs(existing_graphs: list):
    """
    display a list of the names of all existing graphs and their node population count
    """
    graph_names = []
    for graph in existing_graphs:
        if not isinstance(graph, MyGraph):
            raise TypeError('graph must be an instance of', MyGraph)
        graph_names.append(graph.graph_label)
    # print list of all graph names and node count
    print('')
    for count, graphname in enumerate(graph_names, 1):
        print(count, graphname, existing_graphs[count-1].graph_population)
    print('')


def input_pureint(user_prompt: str) -> int:
    """
    prompt the user to into a number, return validated number
    as an integer converted from a string
    """
    while True:
        print(user_prompt)
        user_input = input('').strip()
        if not isinputvalid(user_input):
            print('ERROR - INPUT MUST ONLY CONTAIN NUMBERS')
        else:
            return int(user_input)


def isinputvalid(uinput: str) -> bool:
    """
    validate user input by 
    making sure it only has 
    integers in its input
    """
    for character in uinput:
        if not character in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return False
    return True


def expand_graph(graphs: list):
    """
    prompts user to populate a chosen graph with node
    INPUT TRAIL: A->G(to create first graph)->N->'1'
    """
    # prompt user to select a graph
    if len(graphs) == 0:
        print('ERROR - NO GRAPHS HAVE BEEN CREATED ')
        return graphs
    display_list_of_graphs(graphs)
    while True:  # todo finish
        # user input needs to be a validated string, then converted to an int
        chosen_graph_index = input_pureint(
            'WHICH GRAPH DO YOU WANT TO EXPAND: ')-1
        # validate user choice, as an integer
        if chosen_graph_index < 0 or chosen_graph_index >= len(graphs):
            print('ERROR - YOUR CHOICE MUST BE WITHIN RANGE\n0 - ',
                  end=str(len(graphs))+'\n')
        else:
            break
    while True:
        chosen_graph = graphs[chosen_graph_index]
        if not isinstance(chosen_graph, MyGraph):
            raise TypeError('selected graph should be an instance of', MyGraph)
        if chosen_graph.graph_population > 1:
            # create mini menu for the user to chose a node
            print('NOT IMPLEMENTED YET')
            break
        else:
            # if selected graph has only 1 Node in the population, automatically assume the user will expand that graph
            print('ADDING NEW NODE TO GRAPH: ',
                  end=chosen_graph.graph_label+'\n')
            new_node_name = chosen_graph.head_node.node_label
            new_node_name += str(int(chosen_graph.graph_population))
            #! look at TODO comment below this line,replace sectioned code
            chosen_graph.head_node.link_child_node(GraphNode(new_node_name))
            chosen_graph.graph_population += 1
            # TODO ADD SCRIPT THAT AUTOMATICALLY COUNTS THE POPULATION OF THE GRAPH
            break
    return graphs


def add_expand_graphs(graphs: list) -> list:  # todo finish this method
    """
    create a new graph or add nodes to an existing graph
    N - Create a new node on an existing graph
    G - Create a new graph
    Q - Return to Menu

    """
    while True:
        print('N - Create a new node on an existing graph\nG - Create a new graph\nH - Display options\nQ - Return to Menu\n')
        user_input_expansion = input('SELECT MODE: ').strip().upper()
        print()
        if user_input_expansion == 'N':
            # prompt user for which graph they want to expand
            graphs = expand_graph(graphs)
        elif user_input_expansion == 'G':
            while True:
                name_blacklist = []
                for existing_graph in graphs:
                    if not isinstance(existing_graph, MyGraph):
                        raise TypeError(
                            'existing graph must be an instance of', MyGraph)
                    name_blacklist.append(existing_graph.head_node.node_label)
                new_graph_name = input('NAME OF NEW GRAPH: ')
                print('')
                new_graph_name = new_graph_name.strip()
                if new_graph_name in name_blacklist:
                    print('ERROR - GRAPH MUST HAVE UNIQUE NAME\n')
                else:
                    # add new head graph node to passed graphs list
                    break
            graphs.append(MyGraph(new_graph_name))
        elif user_input_expansion == 'H':
            print('N - Create a new node on an existing graph\nG - Create a new graph\nH - Display options\nQ - Return to Menu\n')
        elif user_input_expansion == 'Q':
            return graphs
        else:
            print('ERROR - NOT VALID OPTION, VALID\nOPTIONS ARE N,G,H,Q\n')


# main script
listofusergraphs = []
print('PRESS 2ND + MODE/QUIT TO STOP\nTWICE RUNNING PROCESS\n')
while True:
    help_prompt()
    # main menu options
    USER_INPUT = input('SELECT MODE: ').strip().upper()
    if USER_INPUT not in ['A', 'D', 'L', 'H', 'Q']:
        print('ERROR, NOT VALID OPTION, VALID\nOPTIONS ARE A,D,L,H,Q\n')
    elif USER_INPUT == 'A':
        #! print('ADD NODE TO GRAPH OR START A\nNEW GRAPH\n')
        listofusergraphs = add_expand_graphs(listofusergraphs)
    elif USER_INPUT == 'D':
        print('REMOVE DESIRED NODES\n* NOT IMPLEMENTED\n')
    elif USER_INPUT == 'L':
        #! print('LIST ALL NODES\n* NOT IMPLEMENTED\n')
        display_list_of_graphs(listofusergraphs)
    elif USER_INPUT == 'H':
        continue
    elif USER_INPUT == 'Q':
        break
    else:
        raise RuntimeError('INVALID MENU CHOICE\n')
# end main script
