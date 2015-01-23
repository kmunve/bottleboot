__author__ = 'kmu'

"""
Show a prarameter in netcdf files from thredds.met.no
"""
#from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import netCDF4


def arome_stats(nca):
    """
    Stastics from a AROME model output.

    nca: numpy array from netcdf variable

    """

    T0 = 273.15
    # Do statistics
    print "Mean: {0}".format(np.nanmean(a))
    print "Standard deviation: {0}".format(np.nanstd(a, dtype=np.float64))
    print "Variance: {0}".format(np.nanvar(a))
    print "Average: {0}".format(np.average(a))
    print "Min: {0}".format(np.nanmin(a))
    print "Max: {0}".format(np.nanmax(a))


def get_date():
    import datetime as dt

    tdt = dt.datetime.now()
    return tdt.strftime('%Y%m%d')
    #return "{0}{1}{2}".format(timestamp.year, timestamp.month, timestamp.day)

# Access netcdf file via OpenDAP
tdt = get_date() # get today's date
filename = 'http://thredds.met.no/thredds/dodsC/arome25/arome_norway_default2_5km_{0}_06.nc'.format(tdt)
vname = 'air_temperature_2m'

nc = netCDF4.Dataset(filename)
h = nc.variables[vname]
x = nc.variables['x']
y = nc.variables['y']

altitude = nc.variables['altitude'][:, :] # retrieve model topography
bkgmap = nc.variables['land_area_fraction'][:, :]
times = nc.variables['time']
jd = netCDF4.num2date(times[:], times.units)
a = h[0, :, :]

# Extract required area
a = np.ones(bkgmap.shape) * np.nan

fracy1 = 320
fracy2 = 390
fracx1 = 180
fracx2 = 250

a[fracy1:fracy2, fracx1:fracx2] = h[0, fracy1:fracy2, fracx1:fracx2]
#print a.shape, type(a)

# Filter by elevation(band)
#za = np.ma.masked_outside(altitude, 1000, 1500)
#a[za.mask == True] = np.nan



'''
Can use 'altitude' to filter out alpine regions or elevation bands
'''

# View map and data
fig = plt.figure(figsize=(10, 12))
ax = fig.add_subplot(111)

xyext = [x[0], x[-1], y[0], y[-1]]
plt.imshow(bkgmap, zorder=0, origin='lower', cmap='pink', extent=xyext)
cax = ax.imshow(a, alpha=0.8, label=vname, zorder=1, origin='lower', cmap='seismic', extent=xyext)
fig.colorbar(cax, orientation='horizontal')
plt.title('{0}\n{1}'.format(vname, tdt))
plt.savefig(r'/home/karsten/mysite/media/arome/{0}_{1}.png'.format(tdt, vname), dpi=90)