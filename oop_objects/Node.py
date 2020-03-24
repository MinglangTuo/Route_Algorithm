import re

class node():
    '''Represnt the nodes'''
    def __init__(self,name,capacity):
        self.name = name
        self.adj_node = {}
        self.aim  = None
        self.capacity = capacity
        self.flag_find = False
        self.distance_to_start = 9999
        self.Dv = []
        self.update = False


        self.tmp_small_dv1 ={}
        self.tmp_small_dv2 ={}

    '''pre_process the Dv_table'''
    def handle_nodes(self):
        for node in self.Dv:
            for key,value in node.items():
                if key == self.name:
                    for node_name,node_edge in value.items():
                        new_node_name = self.name+"->"+node_name.name
                        self.tmp_small_dv1[new_node_name] = node_edge
                else:
                    for node_name,node_edge in value.items():
                        new_node_name = key+"->"+node_name.name
                        self.tmp_small_dv2[new_node_name] = node_edge



    def print_tmp_nodes(self):
        print("该点的small_dv")
        for key,value in self.tmp_small_dv1.items():
            print(key)
            print(value)

        print("其他点的small_dv")
        for key, value in self.tmp_small_dv2.items():
            print(key)
            print(value)



    def update_nodes(self):
        self.update = False

        destination = "null"
        start = "null"
        tmp = "null"
        distance_start_destination = 0
        distance_tmp_destination = 0
        distance_start_tmp = 0

        for self_dv,self_dv_value in self.tmp_small_dv1.items():
            match1 = re.split('->',self_dv)
            #print(match1)
            start = match1[0]
            destination = match1[1]
            distance_start_destination = self_dv_value

            for other_dv,other_dv_value in self.tmp_small_dv2.items():
                match2 = re.split('->',other_dv)
                if match2[1]==destination:
                    distance_tmp_destination = other_dv_value
                    tmp = match2[0]

                    for find_dv,find_dv_value in self.tmp_small_dv1.items():
                        match3 = re.split('->',find_dv)
                        if match3[1] == tmp:
                            distance_start_tmp = find_dv_value

                            if distance_start_destination> distance_start_tmp+distance_tmp_destination:
                                distance_start_destination = distance_start_tmp+distance_tmp_destination
                                key = start+"->"+destination
                                self.tmp_small_dv1[key] = distance_start_destination
                                self.update = True











    '''change the name of node'''
    def set_name(self,name):
        self.name = name


    '''change the aim of node'''
    def set_aim(self,aim):
        self.aim = aim

    '''Add adjacent_nodes for own node'''
    def add_adj_node(self,nodes,edge):
        self.adj_node[nodes] = edge

    '''reset the node'''
    def reset(self):
        self.adj_node = {}
        self.flag_find = False
        self.distance_to_start = 9999


