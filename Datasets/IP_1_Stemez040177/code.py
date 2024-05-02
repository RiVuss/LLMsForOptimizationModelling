from pyomo.environ import *
from pyomo.opt import SolverFactory

# Create a Concrete Model
model = ConcreteModel()

# Define variables
model.X1 = Var(within=NonNegativeIntegers)
model.X2 = Var(within=NonNegativeIntegers)
model.d1_minus = Var(within=NonNegativeIntegers)
model.d2_minus = Var(within=NonNegativeIntegers)
model.d3_minus = Var(within=NonNegativeIntegers)
model.d21_minus = Var(within=NonNegativeIntegers)
model.d1_plus = Var(within=NonNegativeIntegers)
model.d2_plus = Var(within=NonNegativeIntegers)
model.d3_plus = Var(within=NonNegativeIntegers)
model.d21_plus = Var(within=NonNegativeIntegers)
model.Y11 = Var(within=Binary)
model.Y12 = Var(within=Binary)
model.Y21 = Var(within=Binary)
model.Y22 = Var(within=Binary)
model.Y31 = Var(within=Binary)
model.Y32 = Var(within=Binary)
model.Y41 = Var(within=Binary)
model.Y42 = Var(within=Binary)

# Define parameters
P1 = 4
P2 = 3
P3 = 2
P4 = 1

# Define objective function
model.obj = Objective(expr = P1*model.d1_minus 
                      + P2*model.d21_plus 
                      + 2*P3*model.d2_minus 
                      + P3*model.d3_minus 
                      + P4*model.d2_plus 
                      + 3*P4*model.d3_plus,
                      sense=minimize)

# Define constraints
model.const1 = Constraint(expr = 5*model.X1 
                          + 2*model.X2 
                          + model.d1_minus 
                          - model.d1_plus == 5500)
model.const2 = Constraint(expr = model.X1 
                          + model.d2_minus 
                          - model.d2_plus == 800)
model.const3 = Constraint(expr = model.X2 
                          + model.d3_minus 
                          - model.d3_plus == 320)
model.const4 = Constraint(expr = model.d21_minus 
                          + model.d2_plus 
                          - model.d21_plus == 100)
model.const5 = Constraint(expr = model.d1_minus <= 5500 * model.Y11)
model.const6 = Constraint(expr = model.d1_plus <= 5500 * model.Y12)
model.const7 = Constraint(expr = model.Y11 + model.Y12 == 1)
model.const8 = Constraint(expr = model.d2_minus <= 800 * model.Y21)
model.const9 = Constraint(expr = model.d2_plus <= 100 * model.Y22)
model.const10 = Constraint(expr = model.Y21 + model.Y22 == 1)
model.const11 = Constraint(expr = model.d3_minus <= 320 * model.Y31)
model.const12 = Constraint(expr = model.d3_plus <= 320 * model.Y32)
model.const13 = Constraint(expr = model.Y31 + model.Y32 == 1)
model.const14 = Constraint(expr = model.d21_minus <= 100 * model.Y41)
model.const15 = Constraint(expr = model.d21_plus <= 100 * model.Y42)
model.const16 = Constraint(expr = model.Y41 + model.Y42 == 1)

# Solve the optimization problem
solver = SolverFactory('glpk')
solver.solve(model)

# Display the results
print("Objective Value:", model.obj())
print("X1:", model.X1())
print("X2:", model.X2())
print("d1^-:", model.d1_minus())
print("d1^+:", model.d1_plus())
print("d2^-:", model.d2_minus())
print("d2^+:", model.d2_plus())
print("d3^-:", model.d3_minus())
print("d3^+:", model.d3_plus())
print("d21^-:", model.d21_minus())
print("d21^+:", model.d21_plus())
