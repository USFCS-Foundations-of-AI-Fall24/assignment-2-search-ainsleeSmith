from collections import deque



## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    print("in bfs")
    search_queue = deque()
    closed_list = {}
    state_count = 0 ## I added this
    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        state_count = state_count + 1 ## I added this
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            print("States count: " + str(state_count))
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)

### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True,limit=0) :
    print("in dfs")
    search_queue = deque()
    closed_list = {}
    state_count = 0 ## I added

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        state_count = state_count + 1 ## I added
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            print("States count: " + str(state_count))
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)

## add iterative deepening search here

