# # variables = set()
#
# #for eqn in MySSIT.system:
# #    list_eqn = eqn.split(" ")
# #    for elem in list_eqn:
# #        if "*" not in elem and "-" not in elem:
# #            try:
# #                int(elem)
# #            except:
# #                variables.add(elem.strip("()"))
#
# #print(variables)
# #print(len(variables))
# #print(len(MySSIT.system))
#
# Qss = sym.solve(MySSIT.eqns_for_Q)
# print(Qss)
# Qs = []
# for i in Qss:
#     Qs.append((str(i), Qss[i]))
# print("Qs: " + str(Qs))
#
#
# eqns_for_p = MySSIT.eqns_for_p
# print("eq_for_p " + str(eqns_for_p))
# eqns_for_p = sym.sympify(eqns_for_p)
# print(eqns_for_p)
#
# new_eqns_for_p = []
#
# for eqn in eqns_for_p:
#     new_eqns_for_p.append(eqn.subs(eqn, Qss))
#
# print(new_eqns_for_p)
#
# solution_for_p = sym.solve(new_eqns_for_p)
#
# print(solution_for_p)
#
# MySSIT.solve_system()
#
# MySSIT.print_solution()
