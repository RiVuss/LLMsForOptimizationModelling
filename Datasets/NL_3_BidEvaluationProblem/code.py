# Bid Evaluation Non-Linear
from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeReals, Binary, sum_product

# Create a model
model = ConcreteModel()

# Define indices for vendor B and vendor E subproblems
indices_2 = ['21', '22', '23', '24', '25']
indices_5 = ['51', '52']

# Variables
model.x = Var(['11', *indices_2, '31', '41', *indices_5], within=NonNegativeReals)
model.y = Var(['11', *indices_2, '31', '41', *indices_5], within=Binary)

# Objective function
model.cost = Objective(expr=3855.84 * model.y['11'] +
                          125804.84 * model.y['21'] +
                          269304.84 * model.y['22'] +
                          464304.84 * model.y['23'] +
                          761304.84 * model.y['24'] +
                          1623982.84 * model.y['25'] +
                          13456.00 * model.y['31'] +
                          6583.98 * model.y['41'] +
                          84000 * model.y['52'] +
                          61.150 * model.x['11'] +
                          68.099 * model.x['21'] +
                          66.049 * model.x['22'] +
                          64.099 * model.x['23'] +
                          62.119 * model.x['24'] +
                          62.019 * model.x['31'] +
                          72.488 * model.x['41'] +
                          70.150 * model.x['51'] +
                          68.150 * (0.9995**(model.x['52']/1000)) * model.x['52'],
                      sense=1)

# Demand constraint
model.const1 = Constraint(expr = sum(model.x[var] for var in ['11', '21', '22', '23', '24', '25', '31', '41', '51', '52']) == 239600.48)

# Vendor-specific constraints
model.const2 = Constraint(expr = model.x['11'] <= 33000 * model.y['11'])
model.const3 = Constraint(expr = model.x['21'] >= 22000.001 * model.y['21'])
model.const4 = Constraint(expr = model.x['21'] <= 70000 * model.y['21'])
model.const5 = Constraint(expr = model.x['22'] >= 70000.001 * model.y['22'])
model.const6 = Constraint(expr = model.x['22'] <= 100000 * model.y['22'])
model.const7 = Constraint(expr = model.x['23'] >= 100000.001 * model.y['23'])
model.const8 = Constraint(expr = model.x['23'] <= 150000 * model.y['23'])
model.const9 = Constraint(expr = model.x['24'] >= 150000.001 * model.y['24'])
model.const10 = Constraint(expr = model.x['24'] <= 160000 * model.y['24'])
model.const11 = Constraint(expr = model.x['25'] <= 22000 * model.y['25'])
model.const12 = Constraint(expr = sum(model.y[b] for b in indices_2) <= 1)
model.const13 = Constraint(expr = model.x['31'] <= 165600 * model.y['31'])
model.const14 = Constraint(expr = model.x['41'] <= 12000 * model.y['41'])
model.const15 = Constraint(expr = model.x['51'] <= 42000 * model.y['51'])
model.const16 = Constraint(expr = model.x['52'] >= 42000.001 * model.y['52'])
model.const17 = Constraint(expr = model.x['52'] <= 77000 * model.y['52'])
model.const18 = Constraint(expr = sum(model.y[e] for e in indices_5) <= 1)

# Solve the model using the CBC solver
from pyomo.opt import SolverFactory
solver = SolverFactory('couenne')
solver.solve(model)

# Display the results
model.pprint()


print("Objective Value:", model.cost())

for v in model.x:
    print(f"X{v}: {round(model.x[v].value, 2)}")

for v in model.y:
    print(f"Y{v}: {round(model.y[v].value, 2)}")