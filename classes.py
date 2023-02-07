import sympy as sym
import random

class Node():
    def __init__(self, number, Q = 0, alpha = 0, C = 0):
        self.pressure = random.random()
        self.number = number
        self.name = f"Node_{number}"
        self.Q = Q
        self.alpha = alpha
        self.C = C
        self.is_well = False
        self.eqn = ""
        self.parent = ""
        self.is_stok = False
        self.childs = []

    def get_name(self):
        print(self.name)

    def get_number(self):
        print(self.number)

    def get_pressure(self):
        print(self.pressure)


class Stok():
    def __init__(self, pressure):
        self.pressure = sym.Symbol("p_stok")
        pass


class Tube():
    def __init__(self, from_node_number, to_node_number, mu, D, lenght):
        self.from_node = from_node_number
        self.to_node = to_node_number
        self.mu = mu
        self.D = D
        self.length = lenght


class SSIT:
    def __init__(self, struct, tubes):
        self.struct = struct
        self.Nodes = list(self.struct.keys())[1:]
        self.tubes = tubes
        self.system = []
        self.wells = []
        self.eqns_for_Q = []
        self.eqns_for_p = []
        self.p0 = 5
        self.dt = 1

    def get_struct(self):
        return self.struct


    def print_struct(self, node_to_print, inherit_level = 0):

        if len(self.struct[self.Nodes[node_to_print]]) == 0:
            return

        for child in self.struct[self.Nodes[node_to_print]]:
            print("  " * inherit_level + str(child.name) +  " Q: " + str(child.Q) + " p: " + str(child.pressure), "C: " + str(child.C))
            self.print_struct(child.number, inherit_level=inherit_level + 1)


    def initialize_wells(self):
        self.Nodes = list(self.struct.keys())[1:]
        for node in self.Nodes:
            if len(self.struct[node]) == 0:
                node.is_well = True
                self.wells.append(node)
            else:
                pass


    def print_wells(self):
        for well in self.wells:
            print("Well: " + well.name + " " + str(well.is_well))


    def add_eqns_for_wells(self):
        for well in self.wells:
            init_p = well.pressure

            eqn1 = f"Q{well.number} - {well.alpha}*{init_p} - {well.C}"
            eqn2 = f"p{well.number} - p{well.parent.number}"

            self.system.append(eqn1)
            self.system.append(eqn2)

            self.eqns_for_Q.append(eqn1)
            self.eqns_for_p.append(eqn2)

    def set_eqns_for_Q(self):
        self.Nodes = list(self.struct.keys())[1:]

        for node in self.Nodes:
            if node.childs:
                eqn = f"Q{node.number}"
                for child in node.childs:
                    eqn = eqn + f" - Q{child.number}"

                self.system.append(eqn)
                self.eqns_for_Q.append(eqn)



    def add_eqns_for_tubes(self):
        self.Nodes = list(self.struct.keys())[1:]
        for tube in self.tubes:
            if tube.to_node == 0:
                eqn = f"(p{tube.from_node} - {self.p0}) * {tube.D}/({tube.length**2}*{tube.mu}) - Q{tube.from_node}"

            else:
                eqn = f"(p{tube.from_node} - p{tube.to_node}) * {tube.D}/({tube.length**2}*{tube.mu}) - Q{tube.from_node}"

            self.system.append(eqn)
            self.eqns_for_p.append(eqn)


    def solve_system(self):
        solution = sym.solve(self.system)
        self.solution = solution


    def print_solution(self):
        print(self.solution)

    def set_pressures(self):
        self.Nodes = list(self.struct.keys())[1:]

        for key in self.solution.keys():
            key = str(key)
            if key.startswith("p"):
                node_number = int(key[1:])
                node = self.Nodes[node_number]
                node.pressure = self.solution[sym.Symbol(key)]



    def print_pressures(self):
        self.Nodes = list(self.struct.keys())[1:]

        for node in self.Nodes:
            print(f"p{node.number} = {node.pressure}")



    def calculate_k(self):
        self.Nodes = list(self.struct.keys())[1:]
        self.k = 0

        for well in self.wells:
            number = well.number
            self.k = self.k + (self.Nodes[number].pressure * self.Nodes[number].alpha + self.Nodes[number].C) * self.dt


        for tube in self.tubes:
            self.k = self.k - tube.length*tube.D/tube.mu



    def get_k(self):
        return self.k


    def set_childs(self):
        self.Nodes = list(self.struct.keys())[1:]

        for node in self.Nodes:
            node.childs = self.struct[node]


    def print_childs(self):
        self.Nodes = list(self.struct.keys())[1:]
        for node in self.Nodes:
            print(f"Node {node.name} has childs {list(child.name for child in node.childs)}")




    def set_parents(self):
        self.Nodes = list(self.struct.keys())[1:]

        for node in self.Nodes:
            if self.struct[node]:
                for child in self.struct[node]:
                    child.parent = node
                    #print(child.name + " has parent " + child.parent.name)



    def print_parents(self):
        self.Nodes = list(self.struct.keys())[1:]
        for node in self.Nodes:
            if node.parent:
                print(f'{node.name} has parent {node.parent.name}')
            else:
                print(f'{node.name} has no parent')
                node.is_stok = True


