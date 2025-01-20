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
def f(a, n):
    """
    Calculates a mathematical expression involving square roots and exponents.

    Args:
    a (mpf): The base number for calculations.
    n (int): The exponent to be applied.

    Returns:
    mpf: The floor of the result of (ceil(sqrt(a)) + sqrt(a))^n.

    Note:
    This function uses the mpmath library (mpm) for high-precision arithmetic.
    """
    return mpm.floor(
        mpm.fadd(mpm.ceil(mpm.sqrt(a)), mpm.sqrt(a))**n
    )

def g(n):
    """
    Computes the sum of f(a, a^2) for a range of values.

    Args:
    n (int): The upper limit of the range (inclusive).

    Returns:
    mpf: The sum of f(a, a^2) for a from 1 to n.

    Note:
    This function uses the mpmath library (mpm) for high-precision arithmetic
    and range generation.
    """
    return mpm.fsum(
        [f(a, a**2) for a in mpm.arange(1, (n + 1))]
    )

#%%
if __name__ == '__main__':
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