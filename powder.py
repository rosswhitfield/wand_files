from mantid.simpleapi import LoadNexus
from wand import loadIntegrateData, reduceToPowder


# Using all autoreduced
norm = LoadNexus(Filename='/HFIR/HB2C/IPTS-7776/shared/autoreduce/HB2C_6585.nxs')
si = LoadNexus(Filename='/HFIR/HB2C/IPTS-7776/shared/autoreduce/HB2C_6578.nxs')

reduceToPowder(si,'si_no_norm')
reduceToPowder(si, norm, 'si_norm')
