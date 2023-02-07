from config import *


def prepare_system(SSIT):
    SSIT.initialize_wells()
    SSIT.set_parents()
    SSIT.set_childs()
    SSIT.set_p0(5)
    SSIT.set_dt(1)
    return SSIT

def add_eqns(SSIT):
    SSIT.add_eqns_for_wells()
    SSIT.set_eqns_for_Q()
    SSIT.add_eqns_for_tubes()
    return SSIT

def solve_and_assign(SSIT):
    SSIT.solve_system()
    SSIT.set_pressures()
    SSIT.calculate_k()
    return SSIT



def main(SSIT_conf, Tubes):

    MySSIT = SSIT(SSIT_conf, Tubes)

    MySSIT = prepare_system(MySSIT)

    MySSIT = add_eqns(MySSIT)

    MySSIT = solve_and_assign(MySSIT)

    MySSIT.print_pressures()

    print("k = " + str(MySSIT.get_k()))


if __name__ == "__main__":
    main(SSIT_conf, Tubes)


