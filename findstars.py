import pynbody
import numpy as np
import pandas as pd
import matplotlib.ticker as plt
from matplotlib.ticker import NullFormatter

#upload snapshot you are inquiring about
s = pynbody.load ("/media/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.004096/h148.cosmo50PLK.3072g3HbwK1BH.004096" )

#convert the units
s.physical_units()
h=s.halos()
print (h)

BHindex = pynbody.filt.LowPass('tform',0.0)
BHs = s.star[BHindex]
halos = BHs['amiga.grp']
print halos

halos = np.unique(halos)
print( halos)

h1=h[1]

#find how many stars are inside this whole snapshot
stars = s.stars[0:]
print('The number of stars in this snapshot:', len(stars))


#find how many black holes are inside this whole snapshot
def findBH(s):
    #filt.Lowpass returns particles whose prop exceeds min (unit string)
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return BH

BH = findBH(s)
print('The number of black holes in this snapshot: ', len(BH))
def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos
BHhalos = findBHhalos(s)
currenthalo= np.argsort(BHhalos)


#find how many stars are in galaxy 1 (halo 1)
stars=s.stars[0:]
print('The number of stars in h1 ',len(h1.star))
#find how many black holes are in galaxy 1 (halo 1)
for i in currenthalo:
    currenthalo= BHhalos[i]
    #try also: halos= BHhalos[h5]
    bh = BH[i]
    print ('currenthalo: ',currenthalo)
    print ('bh ,',len(bh))
#nbh= len(h1.BH)
#print ('The number of black hole', )
