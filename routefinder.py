import math
from fileinput import filename
from queue import PriorityQueue
from Graph import Graph, Edge


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = read_mars_graph('MarsMap')
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put((start_state.f, start_state))
    ## you do the rest.
    if use_closed_list :
        closed_list[start_state.location] = True
    while not search_queue.empty() :
        print ("it not empty")
        ## this is a (state, "action") tuple
        next_state = search_queue.get()
        # print("searching location : ")
        # print(next_state.location)
        # state_count = state_count + 1 ## I added this
        if goal_test(next_state):
            print("Goal found")
            print(next_state)
            # print("States count: " + str(state_count))
            ptr = next_state
            while ptr is not None :
                ptr = ptr[1].prev_state
                # print(ptr)
            # print("state count: " + str(state_count))
            return next_state
        else :
            print("this is not the goal")
            edges = next_state[1].mars_graph.get_edges(next_state[1].location)
            # print("edges: " + str(edges))
            successors = []
            for e in edges:
                e = str(e)
                l = e.split(' ')
                successors.append(l[1])
            if use_closed_list : # going to keep track of visited locations in closed_list
                successors = [item for item in successors if item not in closed_list]
                for s in successors:
                    closed_list[s] = True # add new location to closed list
                    new = map_state(location=s)
                    new.mars_graph = next_state[1].mars_graph
                    new.g = next_state[1].g + 1 # since no weight provided for marsmap, assuming 1
                    # print("location: ")
                    # print(s)
                    new.h = heuristic_fn(new)
                    new.f = new.g + new.h
                    search_queue.put((new.f,new))

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    # sqt(a^2 + b2)
    # print("location: " + state.location)
    # print("location: " + state.location)
    info = state.location.split(',')
    x = int(info[0])
    y = int(info[1])
    return math.sqrt(((x - 1)**2) + ((y - 1)**2))

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    g = Graph()
    with open(filename) as f :
        lines = [line for line in f.readlines()]
        for line in lines :
            info = line.split(' ')
            g.add_node(info[0].strip(':'))
            first = True
            for i in info :
                if first :
                    first = False
                else:
                    if not g.has_node(i.strip('\n')) :
                        g.add_node(i.strip('\n'))
                    g.add_edge(Edge(info[0].strip(':'), i.strip('\n')))
        return g

def goal_complete(state) :
    if str(state[1].location) == '1,1' :
        return True
    return False

if __name__=="__main__" :
    s1 = map_state(location='8,8', g=0)
    s1.h = sld(s1)
    result = a_star(s1, sld, goal_complete)
    print(result)
    # read_mars_graph('MarsMap')
    # print("Map: ")
    # print(read_mars_graph('MarsMap'))
