from config import *

MySSIT = SSIT(SSIT_conf, Tubes)

# MySSIT.print_struct(2)

MySSIT.initialize_wells()

# MySSIT.print_wells()

MySSIT.set_parents()

# MySSIT.print_parents()

MySSIT.add_eqns_for_wells()

MySSIT.set_childs()

# MySSIT.print_childs()

MySSIT.set_eqns_for_Q()

MySSIT.add_eqns_for_tubes()


print(MySSIT.system)

MySSIT.solve_system()

MySSIT.print_solution()

solution = MySSIT.solution

MySSIT.set_pressures()

MySSIT.print_pressures()

MySSIT.calculate_k()

print("k = " + str(MySSIT.get_k()))



