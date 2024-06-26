# Alkylation Problem with Couenne
import pyomo.environ as pyo

# Data
x1_l, x1_u = (0, 2000)
x2_l, x2_u = (0, 16000)
x3_l, x3_u = (0, 120)
x4_l, x4_u = (0, 5000)
x5_l, x5_u = (0, 2000)
x6_l, x6_u = (85, 93)
x7_l, x7_u = (90, 95)
x8_l, x8_u = (3, 12)
x9_l, x9_u = (1.2, 4)
x10_l, x10_u = (145, 162)

# Create a model object
model = pyo.ConcreteModel()

# Declare the variables with bounds (assuming bounds x_i^l and x_i^u are defined elsewhere)
model.x1 = pyo.Var(within=pyo.NonNegativeReals, bounds=(x1_l, x1_u))
model.x2 = pyo.Var(within=pyo.NonNegativeReals, bounds=(x2_l, x2_u))
model.x3 = pyo.Var(within=pyo.NonNegativeReals, bounds=(x3_l, x3_u))
model.x4 = pyo.Var(within=pyo.NonNegativeReals, bounds=(x4_l, x4_u))
model.x5 = pyo.Var(within=pyo.NonNegativeReals, bounds=(x5_l, x5_u))
model.x6 = pyo.Var(within=pyo.NonNegativeReals, bounds=(x6_l, x6_u))
model.x7 = pyo.Var(within=pyo.NonNegativeReals, bounds=(x7_l, x7_u))
model.x8 = pyo.Var(within=pyo.NonNegativeReals, bounds=(x8_l, x8_u))
model.x9 = pyo.Var(within=pyo.NonNegativeReals, bounds=(x9_l, x9_u))
model.x10 = pyo.Var(within=pyo.NonNegativeReals, bounds=(x10_l, x10_u))

# Constants in the objective function and bounds
c1, c2, c3, c4, c5 = 0.63, 5.04, 0.035, 10.0, 3.36
d4_l, d4_u, d7_l, d7_u, d9_l, d9_u, d10_l, d10_u = 98/100, 102/100, 99/100, 101/100, 95/100, 105/100, 9/10, 11/10

# Objective function
model.objective = pyo.Objective(expr=c1*model.x4*model.x7 - c2*model.x1 - c3*model.x2 - c4*model.x3 - c5*model.x5, sense=pyo.maximize)

# Constraints
model.constraint1 = pyo.Constraint(expr=(model.x1 * (1.12 + 0.13167 * model.x8 - 0.00667 * model.x8**2)) - d4_l * model.x4 >= 0)
model.constraint2 = pyo.Constraint(expr=-(model.x1 * (1.12 + 0.13167 * model.x8 - 0.00667 * model.x8**2)) + d4_u * model.x4 >= 0)
model.constraint3 = pyo.Constraint(expr=(86.35 + 1.098 * model.x8 - 0.038 * model.x8**2 + 0.325 * (model.x6 - 89)) - d7_l * model.x7 >= 0)
model.constraint4 = pyo.Constraint(expr=-(86.35 + 1.098 * model.x8 - 0.038 * model.x8**2 + 0.325 * (model.x6 - 89)) + d7_u * model.x7 >= 0)
model.constraint5 = pyo.Constraint(expr=(35.82 - 0.222 * model.x10) - d9_l * model.x9 >= 0)
model.constraint6 = pyo.Constraint(expr=-(35.82 - 0.222 * model.x10) + d9_u * model.x9 >= 0)
model.constraint7 = pyo.Constraint(expr=(-133 + 3 * model.x7) - d10_l * model.x10 >= 0)
model.constraint8 = pyo.Constraint(expr=-(-133 + 3 * model.x7) + d10_u * model.x10 >= 0)
model.constraint9 = pyo.Constraint(expr=1.22 * model.x4 - model.x1 - model.x5 == 0)
model.constraint10 = pyo.Constraint(expr=((93000 * model.x3)/(model.x3 * model.x9 + 1000 * model.x3)) - model.x6 == 0)
model.constraint11 = pyo.Constraint(expr=((model.x2 + model.x5)/model.x1) - model.x8 == 0)

# Solve the model
solver=pyo.SolverFactory('couenne')
results = solver.solve(model)

# Display the results
model.pprint()

# Display the results
print("Objective Value:", round(model.objective(), 2))
print("X1:", round(model.x1(), 2))
print("X2:", round(model.x2(), 2))
print("X3:", round(model.x3(), 2))
print("X4:", round(model.x4(), 2))
print("X5:", round(model.x5(), 2))
print("X6:", round(model.x6(), 2))
print("X7:", round(model.x7(), 2))
print("X8:", round(model.x8(), 2))
print("X9:", round(model.x9(), 2))
print("X10:", round(model.x10(), 2))