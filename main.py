from config import *
import matplotlib.pyplot as plt


def prepare_system(SSIT):
    SSIT.initialize_wells()
    SSIT.set_parents()
    SSIT.set_childs()
    SSIT.set_p0(p0)
    SSIT.set_dt(dt)
    SSIT.print_struct(1)
    SSIT.print_parents()
    return SSIT

def add_eqns(SSIT):
    SSIT.system = []
    SSIT.refresh_some_vals()
    SSIT.add_eqns_for_wells()
    SSIT.set_eqns_for_Q()
    SSIT.add_eqns_for_tubes()
    print(SSIT.system)

    # print(SSIT.system)
    # for eq in SSIT.system:
    #     print(eq)
    # print("\n\n\n\n")
    #
    # print(sym.solve(SSIT.eqns_for_Q))

    return SSIT

# Недоопределенные системы
# Как численно решить недоопределенную систему?

# решить систему с параллельным учаском

"""
Добавить условия на распределение потоков. ? Пропорционально давлению. Посмотреть литературу.
Итерационный процесс реализовать
Давление, D, mu Эквивалентный гидродинамический диаметр
"""

def solve_and_assign(SSIT):
    SSIT.solve_system()
    SSIT.set_pressures()
    SSIT.set_Q()
    SSIT.calculate_k()
    return SSIT



def main(SSIT_conf, Tubes):


    MySSIT = SSIT(SSIT_conf, Tubes)

    MySSIT = prepare_system(MySSIT)

    MySSIT = add_eqns(MySSIT)

    print(MySSIT.system)

    MySSIT = solve_and_assign(MySSIT)

    MySSIT.print_pressures()

    print("k = " + str(MySSIT.get_k()))

    k = MySSIT.get_k()

    k_mass = []

    mist = []


    k_mass.append(k)

    eps = 0.001
    k_inst = 0
    iter = 1
    k_mass = []
    well_pressures = {}

    for well in MySSIT.wells:
        well_pressures[f"p{well.number}"] = []


    while abs(k - k_inst) > eps:
        if iter >= 100:
            break
        MySSIT = add_eqns(MySSIT)
        MySSIT = solve_and_assign(MySSIT)
        k_inst = k
        k = MySSIT.get_k()
        iter += 1
        print("=======================")
        print("iter = " + str(iter))
        print("k = " + str(k))
        print("eps = " + str(abs(k - k_inst)))
        k_mass.append(k)
        for well in MySSIT.wells:
                well_pressures[f"p{well.number}"].append(well.pressure)

        mist.append(abs(k - k_inst))


    fig1 = plt.figure()
    ax = fig1.gca()
    ax.set_ylabel('k')
    ax.set_xlabel("Номер итерации")
    ax.grid(True)
    ax.plot(k_mass)


    fig2 = plt.figure()
    ax = fig2.gca()

    for well in well_pressures:
        ax.plot(well_pressures[well])


    ax.set_ylabel('pressures')
    ax.set_xlabel("Номер итерации")
    ax.legend(well_pressures.keys())
    ax.grid(True)


    fig3 = plt.figure()
    ax = fig3.gca()
    ax.plot(mist)
    ax.grid(True)
    ax.set_xlabel("Номер итерации")
    ax.set_ylabel("eps")

    plt.show()



if __name__ == "__main__":

    main(SSIT_conf, Tubes)


