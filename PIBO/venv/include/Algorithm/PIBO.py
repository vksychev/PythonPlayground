import numpy
import random
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

#import "~/Work/PythonPlayground/PIBO/initials.py"
N = 6  # number of plants(vehicles)
MaxGen = 1  # MaxGen
alpha = 0.89  # Filter parameter
tau = 0.077  # Troughput accelerator
nu = 0.13  # Tolerance optimiser
gamma = random.random()  # A random vector affecting decision making
E = []  # Edges
# Environmental information
x = []
# Previous environmental information that triggered action
x_ = []
# Perception for xi
F = []
# Compactness of the solution
Z = []
# Signal transduction response level
r = []

M = []  # Tissue integration decision

beta = 0.1  # Temporary pattern generator


def h():
    pass


def check_prediction(xi):
    global alpha
    global nu
    global tau
    global beta
    return


def O():
    x = [(4, 4),  # depot
         (2, 0), (8, 0),  # locations to visit
         (0, 1), (1, 1),
         (5, 2), (7, 2),
         (3, 3), (6, 3),
         (5, 5), (8, 5),
         (1, 6), (2, 6),
         (3, 7), (6, 7),
         (0, 8), (7, 8)]
    data = {}
    # Locations in block units
    # Multiply coordinates in block units by the dimensions of an average city block, 114m x 80m,
    # to get location coordinates.
    data["locations"] = [(l[0] * 114, l[1] * 80) for l in x]
    data["num_locations"] = len(data["locations"])
    data["num_vehicles"] = N
    data["depot"] = 0
    return data


def def_perception():
    for i in range(len(x)):
        F.append(h(min(x[i])) + gamma * (h(max(x[i])) - h(min(x[i]))))


def algorithm():
    O()
    env_inf()
    def_perception()
    result = []
    while N < MaxGen:
        result.append(_iteration())
    return result


def _iteration():
    global beta
    i = random.randrange(0, 4, 1)
    if c((alpha * x[i] > 0) or (beta * x[i] > 0) or (tau * x[i] > 0)) or ((nu * x[i] > 0) and (nu * x[i] <= 0)):
        findMax(G[x[i]])
        beta = 1
    elif alpha == beta == tau <= 0:
        P[G] = 0
        wait_until(alpha > 0 or beta > 0 or tau > 0) or (nu > 0 and nu <= 0)

    Vxitp = None
    Vxit = None
    if M[x[i], t + 1] > M[x[i], t]:
        Vxitp = random.random()
    elif M[x[i], t + 1] < M[x[i], t]:
        Vxit = random.random()
    elif Vxit not in V:
        M[x[i], t] = 0
        return None

    evaluateA(i)
    if A[i] < A_[i]:
        produceC(i)
    elif A[i] < A_[i]:
        C[i] = C[0]
        F[i] = h(min(x[i])) + gamma * (h(max(x[i])) - h(min(x[i])))

    if Z[x[i]] >= Z[x_[i]]:
        Z[x[i]] = Z_[x[i]]
    elif Z[x[i]] <= Z[x_[i]]:
        Z[x_[i]] = Z_[x[i]]
    return solve()

def manhattan_distance(position_1, position_2):
    return (
            abs(position_1[0] - position_2[0]) + abs(position_1[1] - position_2[1]))

def create_distance_callback(data):
    """Creates callback to return distance between points."""
    _distances = {}

    for from_node in range(data["num_locations"]):
        _distances[from_node] = {}
        for to_node in range(data["num_locations"]):
            if from_node == to_node:
                _distances[from_node][to_node] = 0
            else:
                _distances[from_node][to_node] = (
                    manhattan_distance(data["locations"][from_node],
                                       data["locations"][to_node]))

    def distance_callback(from_node, to_node):
        """Returns the manhattan distance between the two nodes"""
        return _distances[from_node][to_node]

    return distance_callback

def add_distance_dimension(routing, distance_callback):
    distance = 'Distance'
    maximum_distance = 3000  # Maximum distance per vehicle.
    routing.AddDimension(
        distance_callback,
        0,  # null slack
        maximum_distance,
        True,  # start cumul to zero
        distance)
    distance_dimension = routing.GetDimensionOrDie(distance)
    # Try to minimize the max distance among vehicles.
    distance_dimension.SetGlobalSpanCostCoefficient(100)

def print_solution(data, routing, assignment):
    """Print routes on console."""
    total_distance = 0
    for vehicle_id in range(data["num_vehicles"]):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        distance = 0
        while not routing.IsEnd(index):
            plan_output += ' {} ->'.format(routing.IndexToNode(index))
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += ' {}\n'.format(routing.IndexToNode(index))
        plan_output += 'Distance of route: {}m\n'.format(distance)
        print(plan_output)
        total_distance += distance
    print('Total distance of all routes: {}m'.format(total_distance))

def solve():
    """Entry point of the program"""
    # Instantiate the data problem.
    data = O()
    # Create Routing Model
    routing = pywrapcp.RoutingModel(
        data["num_locations"],
        data["num_vehicles"],
        data["depot"])
    # Define weight of each edge
    distance_callback = create_distance_callback(data)
    routing.SetArcCostEvaluatorOfAllVehicles(distance_callback)
    add_distance_dimension(routing, distance_callback)
    # Setting first solution heuristic (cheapest addition).
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)  # pylint: disable=no-member
    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
        print_solution(data, routing, assignment)



if __name__ == "__main__":
    solve()
