'''
The code reproduces the results of the paper:

*Sorensen, E. H., Qian, E., Schoen, R., & Hua, R. (2004, December 31). Multiple Alpha Sources and Active Management. Journal of Portfolio Management. Institutional Investor Journals Umbrella. https://doi.org/10.3905/jpm.2004.319928*

Except some waviness in some plots the paper reproduces all the results of the paper

'''
#%%
import numpy as np
import scipy as sc
import sympy as sm
from sympy.plotting import plot
import math
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
%matplotlib inline
#%%
#Test sympy
x = sm.symbols('x')
p1 = plot(x*x, show = True)

# %%
#Exhibit 1 panel 1
rho = np.linspace(-0.50, 1, 1000)
wq = 0.5
wf = 0.5 
icqt = 0.40
icft = 0.40
icstd = 0.086
sf = 0.086
sq = 0.086
sfq = 0
tau = 1 / np.sqrt(1 - 2*wq*wf*(1 - rho))
comb = icqt*wq + icft * wf
comp_ic = tau * comb
c_std = np.sqrt(sq**2 * wq**2 + 2 * sfq * wq * wf + sf**2 * wf**2)
com_std = tau*c_std
ir = comp_ic / com_std
# %%
plt.plot(rho, comp_ic)

# %%
plt.plot(rho, com_std)

# %%
plt.plot(rho, ir)

# %%
#Exhibit 2
#Pause

#%%
#Exhibit 4 to 6
e3icq = .07
e3sigmaq = 0.10
e3irq = 0.70
e3wq  = .50
e3icf = .04
e3sigmaf = .05
e3irf = 0.80
e3wf = 0.5
e3rho = 0
e3tau = 1.41
#%%
#Exhbit 4
e4rhoic = np.linspace(-1, 1, 100)
comb = e3icq*e3wq + e3icf * e3wf
comp_ic = e3tau * comb
cterm = 2*e3wq*e3wf*e4rhoic*e3sigmaf*e3sigmaq
c_std = np.sqrt(e3sigmaq**2 * e3wq**2 +  e3sigmaf**2 * e3wf**2 + cterm)
#%%
comb = e3icq*e3wq + e3icf * e3wf
comp_ic = e3tau * comb
com_std = e3tau*c_std
ir = comp_ic / com_std
#%%
plt.plot(e4rhoic, comp_ic*np.ones(100)/e3tau)
#%%
plt.plot(e4rhoic, com_std)
#%%
plt.plot(e4rhoic, ir)
#%%
#Exhibit 5
e5wq = np.linspace(0, 1, 10)
comb = e3icq*e5wq + e3icf * e3wf
comp_ic = e3tau * comb
#%%
c_std = np.sqrt(e3sigmaq**2 * e5wq**2 +  e3sigmaf**2 * e3wf**2)
com_std = e3tau*c_std
ir = comp_ic / com_std
#%%

plt.plot(e5wq, ir)

# %%
#Exhibit 6
e6icf = np.outer(np.linspace(0, .01, 30), np.ones(30))
e6wq = np.linspace(0, 1, 30).T # transpose
#%%
comb = e3icq*e6wq + e6icf * e3wf
comp_ic = e3tau * comb
#%%
c_std = np.sqrt(e3sigmaq**2 * e6wq**2 +  e3sigmaf**2 * e3wf**2)
com_std = e3tau*c_std
#%%
e6ir = comp_ic / com_std

#%%
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(e6icf, e6wq, e6ir, cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
plt.show()

'''
import plotly.graph_objects as go
fig = go.Figure(data=[go.Surface(x = e6icf, y = e6wq, z = e6ir)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
fig.update_layout(title='Exhibit 6')
fig.show()
'''