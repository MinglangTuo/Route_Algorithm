from oop_objects.Graph import graph
from oop_objects.Node import node

class demo():
    def __init__(self):
        self.judge = True



    def comd_line(self):
        a = input("If you want to end the packets transfer? (Y/N) ：")

        if a == "Y":
            self.judge = False
        elif a == "N":
            self.judge = True
        else:
            print("The error input! The packets will transfer !")


    def ls_test(self):
        #create the graph
        route = graph()

        #create the nodes
        x = node("X",1)
        y = node("Y",5)
        z = node("Z",1)
        w = node("W",0)

        '''
        RecursionError: maximum recursion depth exceeded in comparison
        
        w = node("W",7)
        g = node("G",2)
        z = node("Z",0)
        y = node("Y",0)
        x = node("X",0)



        w.add_adj_node(y,0)
        w.add_adj_node(z, 0)
        w.set_aim("G")

        y.add_adj_node(w, 0)
        y.add_adj_node(z, 0)


        z.add_adj_node(y, 0)
        z.add_adj_node(w, 0)
        z.add_adj_node(x, 0)
        z.add_adj_node(g, 0)


        x.add_adj_node(z, 0)
        x.add_adj_node(g, 0)
        x.set_aim("Y")

        g.add_adj_node(x, 0)
        g.add_adj_node(z, 0)
        
        
        route.add_nodes(x, y, z, w, g)
        '''
        #construct the structure
        x.add_adj_node(w,0)
        x.add_adj_node(y,0)
        x.set_aim("W")

        y.add_adj_node(z, 0)
        y.add_adj_node(x, 0)
        y.set_aim("W")

        z.add_adj_node(y, 0)
        z.add_adj_node(w, 0)
        z.set_aim("W")

        w.add_adj_node(z, 0)
        w.add_adj_node(x, 0)

        route.add_nodes(x,y,z,w)


    #initilize the route with ls_algorithm

        route.ls_algorithm()

        route.print_info()   #第一次的nodes的循环


        while self.judge == True:
            route.ls_algorithm_sort(x)
            route.ls_algorithm_sort(y)
            route.ls_algorithm_sort(z)


        #print the address of nodes
        #    route.address_self_nodes()
        #    route.address_sequences_nodes()

            route.declare_edge()     #清空各个点的数值
            route.instead_elements()  #把之前收集到的序列顺序，归还到graph的nodes里面
            #route.print_info()      #

            # print the address of nodes
        #    route.address_self_nodes()
        #    route.address_sequences_nodes()


            #route.print_sequences()   #打印序列顺序

            route.reset_algorithm()  #重新赋值各个点之间的距离
            route.print_info()       #打印信息

            #route.ls_algorithm(x)
            #route.print_sequences()
            route.delete_sequences()

            self.comd_line()


    def dv_test(self):

        # create the graph
        route = graph()

        # create the nodes
        x = node("X", 1)
        y = node("Y", 5)
        z = node("Z", 1)



        #construct the structure
        x.add_adj_node(y,2)
        x.add_adj_node(z,7)


        y.add_adj_node(x, 2)
        y.add_adj_node(z, 1)


        z.add_adj_node(y, 1)
        z.add_adj_node(x, 7)

        route.add_nodes(x,y,z)



        route.print_info()  # 第一次的nodes的循环

        route.dv_algorithm()