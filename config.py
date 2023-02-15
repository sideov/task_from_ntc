from classes import *

p0 = 10

dt = 10

Main_Stok = Stok(p0)


Nodes = []

for i in range(12):
    Nodes.append(Node(i))

Nodes[7].alpha = -0.2
Nodes[8].alpha = -0.2
Nodes[9].alpha = -0.2
Nodes[10].alpha = -0.2
Nodes[11].alpha = -0.2

Nodes[7].C = 5
Nodes[8].C = 5
Nodes[9].C = 5
Nodes[10].C = 5
Nodes[11].C = 5

# Nodes[7].Q = sym.Symbol(f"p{Nodes[7].number} * {Nodes[7].alpha}")
# Nodes[8].Q = sym.Symbol(f"p{Nodes[8].number} * {Nodes[8].alpha}")
# Nodes[9].Q = sym.Symbol(f"p{Nodes[9].number} * {Nodes[9].alpha}")
# Nodes[10].Q = sym.Symbol(f"p{Nodes[10].number} * {Nodes[10].alpha}")
# Nodes[11].Q = sym.Symbol(f"p{Nodes[11].number} * {Nodes[11].alpha}")


SSIT_conf = {Main_Stok: Nodes[0],
            Nodes[0]: [Nodes[1]],
            Nodes[1]: [Nodes[2], Nodes[4]],
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

Tubes = [Tube(1, 0, 1, 5, 1), Tube(2, 1, 1, 5, 1),
         Tube(3, 2, 1, 5, 1), Tube(4, 2, 1, 5, 1), Tube(5, 2, 1, 5, 1),
         Tube(6, 4, 1, 5, 1)]