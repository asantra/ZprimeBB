# This file was automatically created by FeynRules 2.3.40
# Mathematica version: 7.0 for Linux x86 (64-bit) (February 18, 2009)
# Date: Tue 8 Dec 2020 11:24:47


from object_library import all_orders, CouplingOrder

QCD = CouplingOrder(name = 'QCD',
                    expansion_order = 99,
                    hierarchy = 1)

QED = CouplingOrder(name = 'QED',
                    expansion_order = 99,
                    hierarchy = 2)

NP = CouplingOrder(name = 'NP',
                   expansion_order = 99,
                   hierarchy = 1)
                   
### original line
#NP = CouplingOrder(name = 'NP',
                   #expansion_order = 99,
                   #hierarchy = 1,
                   #perturbative_expansion = {{NP, 1}, {NP, 0}}[[3,2]])

