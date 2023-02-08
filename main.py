from config import *
import matplotlib.pyplot as plt




def prepare_system(SSIT):
    SSIT.initialize_wells()
    SSIT.set_parents()
    SSIT.set_childs()
    SSIT.set_p0(5)
    SSIT.set_dt(0.001)
    return SSIT

def add_eqns(SSIT):
    SSIT.system = []
    SSIT.add_eqns_for_wells()
    SSIT.set_eqns_for_Q()
    SSIT.add_eqns_for_tubes()
    print(SSIT.system)
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
    SSIT.calculate_k()
    return SSIT



def main(SSIT_conf, Tubes):

    k_mass = []

    MySSIT = SSIT(SSIT_conf, Tubes)

    MySSIT = prepare_system(MySSIT)

    MySSIT = add_eqns(MySSIT)

    MySSIT = solve_and_assign(MySSIT)

    MySSIT.print_pressures()

    print("k = " + str(MySSIT.get_k()))
    k = MySSIT.get_k()
    k_mass.append(k)

    eps = 0.1
    k_inst = 0
    iter = 0

    while abs(k - k_inst) > eps:
        if iter >= 30:
            break
        MySSIT = add_eqns(MySSIT)
        MySSIT = solve_and_assign(MySSIT)
        k_inst = k
        k = MySSIT.get_k()
        print("eps = " + str(abs(k-k_inst)))
        print("k = " + str(k))
        k_mass.append(k)
        iter += 1

    print(k)

    plt.plot(k_mass)
    plt.ylabel('k')
    plt.xlabel("Номер итерации")
    plt.semilogy()
    plt.show()




if __name__ == "__main__":

    main(SSIT_conf, Tubes)


