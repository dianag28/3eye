#first thing i need to do is import packages
import pynbody
import matplotlib.pylab as plt
import numpy as np
import BH_functions_new as BHF

#import snapshot we will be looking at
s = pynbody.load ("/media/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.000275/h148.cosmo50PLK.3072g3HbwK1BH.000275")

#convert the units
s.physical_units()

#load any available halo catalogue
h = s.halos()
h15 = h[15]

#function to find bh

def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return BH

#function to find halos that hosts bh

BH = findBH(s)
print('The number of black holes in this snapshot:' , len(BH))

def findBHhalos(s):
     BH = findBH(s)
     BHhalos = BH['amiga.grp']
     return BHhalos
BHhalos = findBHhalos(s)

#we want to look at h5 and h15 specifically

pynbody.analysis.angmom.faceon(h[15])

#now i need to get the x,y,z positions of the black hole
BHposition=BH['pos']

#EDIT
#for h15 i need to do this numpy where function
#this is not necessary for h5
#BHpos = np.where(BHhalos == 15)
#print BHhalos
#print Bhpos
#this is what i did to find out the index for h15 which is 8


#put the x values in a column
#0 is the x position
#change [8] to [0] for h5
BHx= BHposition[[8],0]
print "x position", BHx

#put the y values into a column
#1 is the y position
#change [8] to [0] for h5
BHy= BHposition[[8],1]
print "y position", BHy

#put the z values in a column
#2 is the z position
#change [8] to [0] for h5
BHz= BHposition[[8], 2]
print "z position", BHz

#now i need to do something else hmm
#the first line makes an image of the galaxy
BHF.render(h15, width= '15 kpc', plot= True, ret_im=True)

#the second line adds the ross over the black hole
plt.plot(BHx, BHy,'+')
plt.savefig("new.halo15"+".png")
     
