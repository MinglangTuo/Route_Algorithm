from oop_objects.Node import node

class dv_route_algorithm():
    '''the class about the dv_route_algorithm'''

    def __init__(self):
        self.stop = False



    #read the adj_nodes and establish the Dv_table
    def read_nodes(self,nodes):
        length = len(nodes)
        for i in range(length):
            small_dv = {}
            for node in nodes:
                small_dv[node.name] = node.adj_node
                nodes[i].Dv.append(small_dv)

        for node in nodes:
            node.handle_nodes()
            print("------------first raw-data")
            node.print_tmp_nodes()
            node.update_nodes()
            print("The iteration by the algorithm")
            node.print_tmp_nodes()
            print("----------------next node:")

        self.circle_iteration(nodes)




    '''judge whether the algorithm stop'''
    def signature(self,nodes):
        self.stop = True

        for node in nodes:
            if node.update == True:
                self.stop = False




    '''deliver the changed dv to the adj_nodes'''
    def deliver(self,nodes):
        self.signature(nodes)

        if self.stop == False:
            for update_node in nodes:
                if update_node.update == True:
                    for other_node in nodes:
                        if other_node.name == update_node.name:
                            pass
                        else:
                            self.exchange(update_node,other_node)





    '''exchange the nodes_info'''
    def exchange(self,update_node,other_node):
        for node1_key,node1_value in other_node.tmp_small_dv2.items():
            for node2_key,node2_value in update_node.tmp_small_dv1.items():
                if node1_key == node2_key:
                    other_node.tmp_small_dv2[node1_key] = node2_value



    def circle_iteration(self,nodes):
        while self.stop == False:

            self.deliver(nodes)

            print("The new iteration by the algorithm")
            for node in nodes:
                node.print_tmp_nodes()

            #update the nodes
            for node in nodes:
                node.update_nodes()



