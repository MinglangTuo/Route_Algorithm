import copy
from oop_objects.Node import node


class ls_route_algorithm():
    '''the class about the ls_route_algorithm'''
    def __init__(self):
        self.tmp_node = None
        self.distance = 0
        self.tmp_nodes = []
        self.initial_node = node("xxx",2)

    '''initialize the problem(1)'''
    def search_algorithm(self,nodes):
        for node in nodes:

            #判断该点路径是否存在目标点
            if node.aim != None:
                self.distance = 0
                self.search_process(node)


    '''initialize the problem(2)'''
    def search_process(self,node):

        for key in node.adj_node.keys():
            self.tmp_node = key
            # 如果遇到目标点
            if node.aim == key.name:
                self.distance +=node.capacity
                node.adj_node[key] = self.distance
                node.flag_find = True

            #如果没遇到目标点
        if node.flag_find == False:

            self.distance += node.capacity
            node.adj_node[self.tmp_node] = self.distance
            self.search_process(self.tmp_node)


    '''the ls_route algorithm implementation'''
    def initial_algorithm(self,node,nodes):
        copy_nodes = copy.deepcopy(nodes)

        for item in copy_nodes:
            if item.name == node.name:
                node = item

        self.initial_node = node

        #self.tmp_nodes 没有清零
        self.tmp_nodes.append(self.initial_node)
        len_nodes = len(copy_nodes)
        copy_nodes.remove(self.initial_node)

        #self.print_info(copy_nodes)

        #initial neighbor nodes of the start_node
        for item in copy_nodes:
            #print("the corresponding node is "+item.name)
            for key,value in item.adj_node.items():
                if self.initial_node == key:
                    item.distance_to_start = self.initial_node.adj_node[item]
                    #print(key.name)
                    #print(item.distance_to_start)
                    #print("------")



        #contine to update other nodes
        while len(self.tmp_nodes) != len_nodes:

            #important!! self.initial_node is not specific meaning!
            add_node = self.sort(self.initial_node,copy_nodes)
            self.tmp_nodes.append(add_node)
            copy_nodes.remove(add_node)

            #self.print_info(copy_nodes)

            self.update(add_node,copy_nodes)


            #self.print_info(copy_nodes)


        self.tmp_nodes = self.out_sequences()
        self.tmp_nodes = self.adjacent(self.tmp_nodes)

        #self.print_info(copy_nodes)
        return self.tmp_nodes


    '''the update algorithm to update the graph'''
    def update(self,node,nodes):

        #D(v) = min[D(v),D(w)+C(w,v)]
        for item in nodes:
            for key,value in item.adj_node.items():
                if node == key:
                    tmp_distance = node.distance_to_start+node.adj_node[item]
                    if tmp_distance<item.distance_to_start:
                        item.distance_to_start = tmp_distance


    '''the sort algorithm return the min-node'''
    def sort(self,node,nodes):
        tmp_distance_to_start = 999
        min_node = node

        for item in nodes:
            #print(item.name+"    "+str(item.distance_to_start))
            if tmp_distance_to_start>item.distance_to_start:
                tmp_distance_to_start = item.distance_to_start
                min_node = item

        return min_node


    '''print_node(1)'''
    def print_nodes(self,nodes):
        for item in nodes:
            print(item.name)


    '''print node(2)'''
    def print_info(self,nodes):
        print("the N': ")
        self.print_nodes(self.tmp_nodes)
        print("the N : ")
        self.print_nodes(nodes)
        print("------------")

    '''print the information of nodes' edge'''
    def print_info_nodes(self):
        for element in self.tmp_nodes:
            print("the node's name is "+element.name)
            for key,edge in element.adj_node.items():
                print("the adj_node's name is: "+key.name)
                print("the adj_node's edge is: " +str(edge))


    '''Find the aim and output the sequences of nodes'''
    def out_sequences(self):
        aim = node("xxx",2)

        for item in self.tmp_nodes:
            if item.name == self.initial_node.aim:
                aim = item

        index = self.tmp_nodes.index(aim)
        return self.tmp_nodes[:index+1]


    '''Find whether the sequence is adjacent'''
    def adjacent(self,nodes):
        length = len(nodes)
        tmp_node = nodes[0]
        tmp_nodes = []

        for i in range(length):

            if i == 0:
                tmp_nodes.append(nodes[i])
                pass
            else:
                if i+1>= length:
                    tmp_nodes.append(nodes[i])
                else:
                    for item in nodes[i].adj_node.keys():
                        if item == nodes[i+1]:
                            tmp_nodes.append(nodes[i])
                        else:
                            pass

        return tmp_nodes

    '''clare all the nodes in self.tmp_nodes'''
    def clear_tmp_nodes(self):
        self.tmp_nodes = []