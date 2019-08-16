import MDAnalysis as mda
import MDAnalysis.analysis.hbonds
import pandas as pd
import numpy as np
from numpy.linalg import norm
from MDAnalysis.lib import distances
import MDAnalysis.analysis.distances
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


Windows = []
for i in range(1,22):
    universe = mda.Universe('umbrella%d.gro' %i)
    Windows.append(universe)




h = MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(Windows[0],'protein','protein')
h.run()
h.generate_table()
df = pd.DataFrame.from_records(h.table)
#print(df)

z = np.linspace(0.2316,4.001,num = 21)



donor_acceptor = [ [] for i in range(len(df.index)) ]
k = 0
for i in donor_acceptor: #hydrogen bonds from MDAnalysis
    i.append(df.loc[[k],['donor_index']].values[0][0])
    i.append(df.loc[[k],['acceptor_index']].values[0][0])
    k += 1
donor_acceptor = [ [88,70], [122, 39], [122, 39], [32, 129], [62, 99] ]#Inwards hydrogen bonds- obtained from vmd


k = 0
bond_distance = [ [] for i in range(len(Windows)) ]
for i in Windows:
    for j in donor_acceptor:
        donor = i.select_atoms('bynum %d' %(j[0]+1))
        acceptor = i.select_atoms('bynum %d' %(j[1]+1))
        x = MDAnalysis.analysis.distances.dist(acceptor,donor)
        bond_distance[k].append(x[2][0])
    k +=1

bond_distance = np.array(bond_distance)

fig = plt.figure()
ax1 = fig.add_subplot(111)
for i in range(len(donor_acceptor)):
    ax1.plot(bond_distance[:,i],marker = 'o', markersize = 3,linewidth = 1)
ax1.plot([],[],label = 'Hydrogen Bond Distance \nin Hairpin',linewidth = 0)
horiz_line = np.array([3 for i in range(len(Windows)+1)])
ax1.plot(horiz_line,color = 'k',linestyle = 'dashed')
ax1.set_xlabel(r'Histogram Number')
ax1.set_ylabel(r'Hydrogen Bond Distance ($\AA$)')
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.ylim([1,6])
plt.xlim([0,21])
leg = ax1.legend()
plt.savefig('HB_hairpin.pdf')
plt.show()
