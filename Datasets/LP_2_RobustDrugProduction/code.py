# Robust Drug Production Problem
import pyomo.environ as pyo

# Create a model instance
model = pyo.ConcreteModel()

# Declare decision variables
model.d1 = pyo.Var(domain=pyo.NonNegativeReals)
model.d2 = pyo.Var(domain=pyo.NonNegativeReals)
model.r1 = pyo.Var(domain=pyo.NonNegativeReals)
model.r2 = pyo.Var(domain=pyo.NonNegativeReals)

# Parameters
p1, p2 = 6200, 6900  # Prices of drugs
c1, c2, c3, c4 = 100, 199.90, 700, 800 # Costs
a1, a2, a3, a4 = 0.01, 0.02, 0.500, 0.600  # Active ingredient extraction coefficients
t1M, t2M, t1E, t2E = 90.0, 100.0, 40.0, 50.0  # Time requirements
MPH, EH = 2000, 800  # Manpower and equipment hours limits
S, B = 1000, 100000  # Storage and budget limits

# Objective Function
model.obj = pyo.Objective(expr=(p1*model.d1 + p2*model.d2 - 
                                (c1*model.r1 + c2*model.r2 + c3*model.d1 + c4*model.d2)), sense=pyo.maximize)

# Constraints
model.active_ingredient = pyo.Constraint(expr=(0.995*a1*model.r1 + 0.98*a2*model.r2 - a3*model.d1 - a4*model.d2 >= 0))
model.manpower = pyo.Constraint(expr=(t1M*model.d1 + t2M*model.d2 <= MPH))
model.equipment = pyo.Constraint(expr=(t1E*model.d1 + t2E*model.d2 <= EH))
model.storage = pyo.Constraint(expr=(model.r1 + model.r2 <= S))
model.budget = pyo.Constraint(expr=(c1*model.r1 + c2*model.r2 + c3*model.d1 + c4*model.d2 <= B))

# Solve the model
solver = pyo.SolverFactory('glpk', executable='/usr/bin/glpsol')
result = solver.solve(model)

# Display the results
print(f"Status: {result.solver.status}")
print(f"Objective value: {pyo.value(model.obj)}")
print(f"d1 = {pyo.value(model.d1)}")
print(f"d2 = {pyo.value(model.d2)}")
print(f"r1 = {pyo.value(model.r1)}")
print(f"r2 = {pyo.value(model.r2)}")
