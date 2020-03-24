from CSE205_algorithm.Ls_Route_Algorithm import ls_route_algorithm
from CSE205_algorithm.Dv_Route_Algorithm import dv_route_algorithm
import copy

class graph():
    '''It represent the graph'''
    def __init__(self):
        self.nodes = []
        self.store_sequence = []

        # create the ls-route-algorithm
        self.ls = ls_route_algorithm()
        self.dv = dv_route_algorithm()

    '''Adds the node in the graph'''
    def add_nodes(self,*nodes):
        self.nodes.extend(nodes)


    '''print the text-info for the graph'''
    def print_info(self):
        for element in self.nodes:
            print("the node's name is "+element.name)
            for key,edge in element.adj_node.items():
                print("the adj_node's name is: "+key.name)
                print("the adj_node's edge is: " +str(edge))
        print("\nNext iteration:")




    '''Initilaze the ls_algorithm'''
    def ls_algorithm(self):
        self.ls.search_algorithm(self.nodes)

    '''sort the each node'''
    def ls_algorithm_sort(self,node):
        self.store_sequence.append(self.ls.initial_algorithm(node,self.nodes))
        self.ls.clear_tmp_nodes()

    '''print the sequences of the route'''
    def print_sequences(self):
        for sequence in self.store_sequence:
            for node in sequence:
                print(node.name+"->")
            print("Next sequence:-----------")



    '''Instead the elements in nodes'''
    def instead_elements(self):
        tmp_sequence = copy.deepcopy(self.store_sequence)
        sequence_nodes = []
        sequence = []
        for sequences in tmp_sequence:

            sequence_nodes.append(sequence)
            sequence = []
            for item1 in sequences:
                for item2 in self.nodes:
                    if item1.name == item2.name:
                        sequence.append(item2)
        sequence_nodes.append(sequence)


        self.store_sequence = sequence_nodes[1:]

        #for item in tmp_sequence:
            #print(item[0])






    '''declare all the edges to be 0'''
    def declare_edge(self):
        for item in self.nodes:
            item.flag_find = False
            for key in item.adj_node.keys():
                item.adj_node[key] = 0
                #print(key.name+"----"+str(item.adj_node[key]))




    '''Reset the Graph and re-order the nodes to make the next iteration'''
    def reset_algorithm(self):
       for sequences in self.store_sequence:
           length = len(sequences)
           capacity = sequences[0].capacity
           #print("the capacity is :"+str(capacity))

           for i in range(length):
               if i == length-1:
                   pass
               else:
                sequences[i].adj_node[sequences[i+1]] += capacity
                #print(sequences[i].name+"->"+sequences[i+1].name+": "+str(sequences[i].adj_node[sequences[i+1]]))



    '''Print the address of self.nodes'''
    def address_self_nodes(self):
        for item in self.nodes:
            print(item.name+" ")
            print(id(item))



    '''print the address of nodes in store_sequence '''
    def address_sequences_nodes(self):
        for sequence in self.store_sequence:
            for item in sequence:
                print(item.name+"|||| ")
                print(id(item))

    def dv_algorithm(self):
        copy_nodes = copy.deepcopy(self.nodes)
        self.dv.read_nodes(copy_nodes)


    '''delete the sequences of store_sequences'''
    def delete_sequences(self):
        self.store_sequence = []

