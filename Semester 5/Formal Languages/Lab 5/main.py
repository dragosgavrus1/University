from grammar import Grammar


g = Grammar.from_file('g1.txt')
print(g)
print(g.get_nonterminal_productions('S'))
print(g.is_cfg())
print()

g = Grammar.from_file('g2.txt')
print(g)
print(g.get_nonterminal_productions('start'))
print(g.is_cfg())