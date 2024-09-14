from ortools.sat.python import cp_model

# from mapcoloring import Antenna1

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

## colors: 0: Red, 1: Blue 2: Green
freq = {0 : 'f1',1:'f2',2:'f3'}

Antenna1 = model.NewIntVar(0,2, "A1")
Antenna2 = model.NewIntVar(0,2, "A2")
Antenna3 = model.NewIntVar(0,2, "A3")
Antenna4 = model.NewIntVar(0,2, "A4")
Antenna5 = model.NewIntVar(0,2, "A5")
Antenna6 = model.NewIntVar(0,2, "A6")
Antenna7 = model.NewIntVar(0,2, "A7")
Antenna8 = model.NewIntVar(0,2, "A8")
Antenna9 = model.NewIntVar(0,2, "A9")

## add edges
# Antenna 1 is adjacent to 2,3 and 4.
model.Add(Antenna1 != Antenna2)
model.Add(Antenna1 != Antenna3)
model.Add(Antenna1 != Antenna4)
# Antenna 2 is adjacent to 1, 3, *4*, 5, and 6
model.Add(Antenna2 != Antenna3)
model.Add(Antenna2 != Antenna4)
model.Add(Antenna2 != Antenna5)
model.Add(Antenna2 != Antenna6)
# Antenna 3 is adjacent to 1, 2, 6, and 9
model.Add(Antenna3 != Antenna6)
model.Add(Antenna3 != Antenna9)
# Antenna 4 is adjacent to 1, 2, and 5.
model.Add(Antenna4 != Antenna5)
# Antenna 5 is adjacent to 2 and 4
# Antenna 6 is adjacent to 2, 7 and 8
model.Add(Antenna6 != Antenna7)
model.Add(Antenna6 != Antenna8)
# Antenna 7 is adjacent to 6 and 8
model.Add(Antenna7 != Antenna8)
# Antenna 8 is adjacent to 7 and 9
model.Add(Antenna8 != Antenna9)
# Antenna 9 is adjacent to 3 and 8

status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("A1: %s" % freq[solver.Value(Antenna1)])
    print("A2: %s" % freq[solver.Value(Antenna2)])
    print("A3: %s" % freq[solver.Value(Antenna3)])
    print("A4: %s" % freq[solver.Value(Antenna4)])
    print("A5: %s" % freq[solver.Value(Antenna5)])
    print("A6: %s" % freq[solver.Value(Antenna6)])
    print("A7: %s" % freq[solver.Value(Antenna7)])
    print("A8: %s" % freq[solver.Value(Antenna8)])
    print("A9: %s" % freq[solver.Value(Antenna9)])



