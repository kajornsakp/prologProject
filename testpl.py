from  pyswip import Prolog
# p = Prolog()
# p.consult('/Users/kajornsak/PycharmProjects/prologProject/prolog/prolog-ai.pl')
# x = p.query("start")
# y = p.query("pacman(X,Y,_)")
# print list(y)

p = Prolog()

p.consult('prolog/init.pl')
p.consult('prolog/prolog-ai.pl')
#p.consult('prolog/test.pl')
p.query('start')
x = p.query("pacman(X,Y,_)")
print list(x)
p.query('move_pacman(4,4)')
y = p.query('pacman(X,Y,_)')
print list(y)