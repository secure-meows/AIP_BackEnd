from django.db import models
from Crypto.Util import number
import random

# Create your models here.
class PublicKey(models.Model):

    a = models.CharField(max_length=500)
    b = models.CharField(max_length=500)
    c = models.CharField(max_length=500)
    n = models.CharField(max_length=500)
    g = models.CharField(max_length=500)
    h = models.CharField(max_length=500)
    p = models.CharField(max_length=500)

    le = 2050
    ls = 8196
    ln = 4096

    classno = models.CharField(max_length=10, unique=True)

    def get_int(self, name):
        if isinstance(name, (list, tuple)):
            ret = []
            for i in name:
                if i in ('a', 'b', 'c', 'n', 'g', 'h', 'p'):
                    ret.append(int(self.__getattribute__(i)))
            return ret
        if name in ('a', 'b', 'c', 'n', 'g', 'h', 'p'):
            return int(self.__getattribute__(name))
        else:
            return None

    @classmethod
    def create(cls, classno):
        p = number.getStrongPrime(2048)
        q = number.getStrongPrime(2048)
        n = p*q
        randlis = [random.randrange(0, 1<<1024) for _ in range(4)]
        rand2lis = list(map(lambda x: pow(x, 2, n) ,randlis))
        h = rand2lis[3]
        r = random.randrange(100)
        g = pow(h, r, n)
        obj = cls(
            classno = classno,
            n = str(n),
            a = str(rand2lis[0]),
            b = str(rand2lis[1]),
            c = str(rand2lis[2]),
            h = str(rand2lis[3]),
            p = str(p),
            g = str(g)
        )
        return obj