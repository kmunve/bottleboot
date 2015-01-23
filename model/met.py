__author__ = 'kmu'


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


class MetArray():
    def __init__(self, mpa, mp_name, mp_unit):
        """
        Base class for all arrays containing meteorological data.

        :param mpa: meteorological parameter array
        """
        self.values = mpa
        self.name = mp_name
        self.unit = mp_unit

        self.mean = np.nanmean(mpa)
        self.variance = np.nanvar(mpa)
        self.stddev = np.nanstd(mpa, dtype=np.float64)
        self.median = np.median(mpa)
        self.avg = np.average(mpa)
        self.min = np.nanmin(mpa)
        self.max = np.nanmax(mpa)

    def __str__(self):
        return "{0} [{1}]\n\n{2}".format(self.name, self.unit, self.values.__str__())

    def print_statistics(self):
        """
        Print statistics to command line.
        """
        print "Mean: {0}".format(self.mean)
        print "Standard deviation: {0}".format(self.stddev)
        print "Variance: {0}".format(self.variance)
        print "Average: {0}".format(self.avg)
        print "Min: {0}".format(self.min)
        print "Max: {0}".format(self.max)



################################################################################
class TemperatureArray(MetArray):
    """
    Subclass with temperature specific settings.
    """
    def kelvin_to_celsius(self):
        """
        Converts values from Kelvin to Celsius.
        """
        t0 = 273.15  # Kelvin
        self.mean -= t0
        self.min -= t0
        self.max -= t0




def from_thredds(thredds_file, met_parameters, plot=False, **kwargs):
    """
    Access netcdf file via OpenDAP service thredds.met.no

    :param thredds_file: URL of file, eg.g 'http://thredds.met.no/thredds/dodsC/arome25/arome_norway_default2_5km_20140428_06.nc'
    :param met_parameters: List of meteorological parameters. Names must match the naming convention in the netCDf file(s).
    """
    import netCDF4

    mpa = {}

    nc = netCDF4.Dataset(thredds_file)

    # Load fixed variables
    x = nc.variables['x']
    y = nc.variables['y']
    altitude = nc.variables['altitude'][:, :]  # retrieve model topography
    bkgmap = nc.variables['land_area_fraction'][:, :]  # retrieve background map
    times = nc.variables['time']
    jd = netCDF4.num2date(times[:], times.units)

    for param in met_parameters:
        h = nc.variables[param]

        if 'extract' in kwargs:
            # Extract required area
            a = np.ones(bkgmap.shape) * np.nan

            fracx1 = kwargs['extract'][0]
            fracx2 = kwargs['extract'][1]
            fracy1 = kwargs['extract'][2]
            fracy2 = kwargs['extract'][3]

            a[fracy1:fracy2, fracx1:fracx2] = h[0, fracy1:fracy2, fracx1:fracx2]
            print a.shape, type(a)
            #x = x[fracx1:fracx2]
            #y = y[fracy1:fracy2]

        elif 'elevation_band' in kwargs:
            # Filter by elevation (band)
            za = np.ma.masked_outside(altitude, kwargs['elevation_band'][0], kwargs['elevation_band'][1])
            a[za.mask == True] = np.nan

        else:
            a = h[0, :, :]

        if plot:
            # View map and data
            fig = plt.figure(figsize=(10, 12))
            ax = fig.add_subplot(111)

            xyext = [x[0], x[-1], y[0], y[-1]]
            plt.imshow(bkgmap, zorder=0, origin='lower', cmap='pink', extent=xyext)
            plt.imshow(a, alpha=0.8, zorder=1, origin='lower', cmap='seismic', extent=xyext)

            label = "Gjsn.:\t{0:.2f}\nMin.:\t{1:.2f}\nMaks\t{2:.2f}".format(np.nanmean(a), np.nanmin(a), np.nanmax(a))
            plt.text(-0.7e6, 0.98e6, label, backgroundcolor='white', fontsize=18)  #,transform = ax.transAxes)
            plt.savefig(r'/home/karsten/mysite/media/arome/{0}.png'.format(param), dpi=90)


        mpa[param] = MetArray(a, param, h.units)

    return mpa


def plot_mpa(mpa):
    import pylab as plt
    # View map and data
    fig = plt.figure(figsize=(10, 12))
    ax = fig.add_subplot(111)

    xyext = [x[0], x[-1], y[0], y[-1]]
    plt.imshow(bkgmap, zorder=0, origin='lower', cmap='pink', extent=xyext)
    plt.imshow(a, alpha=0.8, zorder=1, origin='lower', cmap='seismic', extent=xyext)
    plt.plot(pa)
    #plt.legend()

    plt.show()


if __name__ == "__main__":
    mpa = from_thredds('http://thredds.met.no/thredds/dodsC/arome25/arome_norway_default2_5km_20140505_06.nc',
                       ['air_temperature_2m', 'precipitation_amount_acc', 'precipitation_amount_high_estimate'], plot=True,
                       extract=[180, 250, 320, 390], elevation_band=[1000, 1500])

    print mpa['air_temperature_2m']
    mpa['air_temperature_2m'].print_statistics()
