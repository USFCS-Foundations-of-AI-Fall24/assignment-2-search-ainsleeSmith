from unittest import TestCase
from mars_planner import *
from routefinder import *
from search_algorithms import *

class Test(TestCase):
    # Tests for Question 2 part 5
    def test_breadth_first_search(self):
        s = RoverState()
        result = breadth_first_search(s, action_list, mission_complete)
        print(result)

    def test_depth_first_search(self):
        s = RoverState()
        result = depth_first_search(s, action_list, mission_complete)
        print(result)

    def test_depth_limited_search(self):
        s = RoverState()
        result = depth_limited_search(s, action_list, mission_complete, 17)
        print(result)

    # Tests for Question 2 part 6
    def test_problem_decomposition(self):
        s = RoverState()
        print("move to sample:")
        moveToSample = breadth_first_search(s, action_list, sample_loc_goal)
        print(moveToSample)
        print("remove sample: ")
        removeSample = breadth_first_search(moveToSample[0], action_list, remove_sample_goal)
        print(removeSample)
        print("return to charger: ")
        returnToCharger = breadth_first_search(removeSample[0], action_list, charge_loc_goal)
        print(returnToCharger)

    # Tests for Question 3
    def test_a_star(self):
        s = map_state(location='8,8', g=0)
        s.h = sld(s)
        result = a_star(s, h1, goal_complete)
        print(result)

    def test_ucs(self):
        s = map_state(location='8,8', g=0)
        s.h = h1(s)
        result = a_star(s, h1, goal_complete)
        print(result)

    # Test for Question 4
    def test_constraints(self):
        import frequencies
