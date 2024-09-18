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
    search_queue.put(start_state)
    ## you do the rest.
    if use_closed_list :
        closed_list[start_state] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.get()
        # state_count = state_count + 1 ## I added this
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            # print("States count: " + str(state_count))
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            # print("state count: " + str(state_count))
            return next_state
        else :
            successors = next_state.mars_graph.get_edges(next_state.location)
            if use_closed_list : # going to keep track of visited locations in closed_list
                successors = [item for item in successors if item[0] not in closed_list]
                for s in successors:
                    closed_list[s[0]] = True # add new location to closed list
                    new = map_state(s)
                    new.g = next_state.g + 1 # since no weight provided for marsmap, assuming 1
                    new.f = new.g + new.h
                    search_queue.put(new)

            # successors = next_state[0].successors(next_state.)
            # state_count = state_count + len(successors)  ## I added
            # print("state count: " + str(state_count))
            # if use_closed_list :
            #     successors = [item for item in successors
            #                         if item[0] not in closed_list]
            #     for s in successors :
            #         closed_list[s[0]] = True
            # search_queue.extend(successors)

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    # sqt(a^2 + b2)
    # print("location: " + state.location)
    print("location: " + state.location)
    info = state.location.split(',')
    x = info[0]
    y = info[1]
    math.sqrt(((x - 1)**2) + ((y - 1)**2))

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
                    g.add_node(i)
                    g.add_edge(Edge(info[0].strip(':'), i))
    return g


