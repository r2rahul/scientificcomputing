#%%
'''
<p>
Given is the function $f(a,n)=\lfloor{(\lceil{\sqrt{a}\:\rceil}+\sqrt{a}\:)^n}\rfloor$.<br />
$\lfloor{.}\rfloor$ denotes the floor function and $\lceil{.}\rceil$ denotes the ceiling function.<br />
$f(5,2)=27$ and $f(5,5)=3935$.
</p>
<p>
$G(n) = \displaystyle \sum_{a=1}^n f(a, a^2).$<br />
$G(1000) \text{ mod  } 999\,999\,937=163861845. $<br />
Find $G(5\,000\,000).$ Give your answer modulo $999\,999\,937$.
</p>
'''
#%%
import mpmath as mpm
import numpy as np
#%%
#mpm.mp.dps = 5; mpm.mp.pretty = False
#%%
def f(a,n):
    return mpm.floor(
        mpm.fadd( mpm.ceil(mpm.sqrt(a)), mpm.sqrt(a))**n
    )

def g(n):
    return mpm.fsum(
        [f(a, a**2) for a in mpm.arange(1, (n+ 1))]
               )
#%%
__init__ = main():
    print('f(5, 2) = '.format(f(5, 2)))
    print('f(5, 5) = '.format(f(5, 5)))
    print('***************************')
    print('*******Now G function and result****')
    print('***************************')
    r = 999999937
    gout10 = np.mod(g(10), r)
    print('G(10) = '.format(gout10))
    gout1000 = np.mod(g(1000), r)
    print('G(1000) = '.format(gout1000))
    gout5000000 = np.mod(g(5000000), r)
    print('G(5000000) = '.format(gout5000000))