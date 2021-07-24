import math
ag = float(input('Digite o angulo em graus: '))
ar = math.radians(ag)
sen = math.sin(ar)
cos = math.cos(ar)
tan = math.tan(ar)
print(' Seno de {}° = {:.2f}\n'.format(ag, sen),
      'Cosseno de {}° = {:.2f}\n'.format(ag, cos),
      'Tangente de {}° = {:.2f}'.format(ag, tan))
