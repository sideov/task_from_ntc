p = 5



class Node():
    def __init__(self, number, pressure = 0):
        self.pressure = pressure
        self.number = number
        self.name = f"Node_{number}"

    def get_name(self):
        print(self.name)

    def get_number(self):
        print(self.number)

    def get_pressure(self):
        print(self.pressure)



class Stok():
    def __init__(self, pressure):
        self.pressure = pressure
        pass

class Tube():
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node


Nodes = []
Tubes = []
Main_Stok = Stok(p)

for i in range(12):
    Nodes.append(Node(i))

print("Nodes: ", list(Nodes))

children = {Main_Stok: Nodes[0],
            Nodes[0]: [Nodes[1]],
            Nodes[1]: [Nodes[2]],
            Nodes[2]: [Nodes[3], Nodes[5], Nodes[4]],
            Nodes[3]: [Nodes[7], Nodes[8]],
            Nodes[4]: [Nodes[10], Nodes[6]],
            Nodes[5]: [Nodes[9]],
            Nodes[6]: [Nodes[11]],
            Nodes[7]: [],
            Nodes[8]: [],
            Nodes[9]: [],
            Nodes[10]: [],
            Nodes[11]: []
            }

Tubes = [Tube(Nodes[1], Nodes[0]), Tube(Nodes[2], Nodes[1]), Tube(Nodes[4], Nodes[1]),
         Tube(Nodes[3], Nodes[2]), Tube(Nodes[4], Nodes[2]), Tube(Nodes[5], Nodes[2]),
         Tube(Nodes[6], Nodes[4])]


def print_child(node_to_print, inherit_level = 0):


    if len(children[Nodes[node_to_print]]) == 0:
        return

    for child in children[Nodes[node_to_print]]:
        print("  "*inherit_level + str(child.name))
        print_child(child.number, inherit_level = inherit_level + 1)


print_child(2)

