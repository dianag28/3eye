#my new task is to make a picture of the galaxy in the next snapshot, where the two galaxies are merging!!!
# i need to have two crosses. one for each BH

#import the important stuff
import matplotlib.pylab as plt
import numpy as np
import pynbody
import BH_functions_new as BHF

#snapshot!!
s = pynbody.load("/media/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.000640/h148.cosmo50PLK.3072g3HbwK1BH.000640")

#convert the units
s.physical_units()

#load any available halo catalogue
h= s.halos()
# Jillian said that what I'm looking for is halo 1
h1= h[1]

#Jillian also said there might be many bh in this galaxy so i might need to identify each of the bh separately by their id number instead of plotting every bh

# this code will be repeated for all other snapshots until bh merge so make it flexible

#black hole id function
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return BH

#function to find halos that hosts bh
BH = findBH(s)
print('The number of black holes in this snapshot;', len(BH))

def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH ['amiga.grp']
    return BHhalos

BHhalos = findBHhalos(s)

#print BHhalos[currenthalo]
BH_ID = BH['iord']
BH_ID = BH['iord']

#h1 specifically
pynbody.analysis.angmom.faceon(h[1])

#positions of the bh
BHposition = BH['pos']

#BHpos = np.where(BHhalos ==15)
#print BHhalos
#print BHpos
#h1 index is 13

BHx= BHposition[[13], 0]
print "x position", BHx

BHy= BHposition[[13],0]
print "y position", BHx

BHz= BHposition[[13], 0]
print "z position", BHz


#make my picture
BHF.render(h1, width = '15 kpc', plot= True, ret_im=True)

# add crosses
plt.plot (BHx, BHy, '+')
plt.savefig("practice.cross"+".png")


