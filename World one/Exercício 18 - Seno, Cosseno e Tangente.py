from math import radians, sin, cos, tan
ang = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tange = tan(radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, coss))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(ang, tange))


