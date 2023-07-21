import numpy as np
from netCDF4 import Dataset
import matplotlib
import pylab as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

matplotlib.rcParams['axes.titlesize'] = 12
matplotlib.rcParams['legend.fontsize'] = 10.
matplotlib.rcParams['font.size'] = 12.
matplotlib.rcParams['axes.labelsize'] = 12.
matplotlib.rcParams['xtick.labelsize'] = 12.
matplotlib.rcParams['ytick.labelsize'] = 12.
matplotlib.rcParams['figure.subplot.top'] = 0.9
matplotlib.rcParams['figure.subplot.bottom'] = 0.1
matplotlib.rcParams['figure.subplot.hspace'] = 0.6
matplotlib.rcParams['figure.subplot.wspace'] = 0.2

PATH = '/cnrm/obs/data1/manglar/DPR/new_codes/RTTOV_SIM_PRJ/Paper_RTTOV/Data/Figure_1/'
FILENAME = 'GPM_DPR_trajectory.nc'

# extract  data
ncfile     = Dataset(PATH + FILENAME)
lon                      = (ncfile.variables['lon'])[:]
lat                      = (ncfile.variables['lat'])[:]
ncfile.close()

# Plot DPR trajectory:
fig, ax = plt.subplots()
ax.set_title("")
m= Basemap(projection= 'cyl', resolution= 'l', llcrnrlon= -180., llcrnrlat=-90., urcrnrlon= 180., urcrnrlat= 90.)
m.plot(lon[24, :], lat[24, :], linestyle = 'None', marker = '.', color= 'lightgray',  linewidth=1, zorder = 0)
m.drawcoastlines(linewidth=0.25)
m.drawparallels(np.arange(-90, 90, 45), labels = [1,1,0,1])
m.drawmeridians(np.arange(-180, 180, 45), labels=[1,1,0,1])

# Add a balck color rectangle box to show the case study area:
def draw_screen_poly(lats, lons, m):
    x,y = m(lons, lats)
    xy = zip(x,y)
    poly = Polygon(list(xy), edgecolor='black', alpha=1.0, linewidth=5.0)
    plt.gca().add_patch(poly)
lats = [28, 32, 32, 28]
lons = [-27.0,-27.0,-23,-23]
draw_screen_poly(lats, lons, m)

# Mark starting and ending point of trajectory:
latW_ini   = lat[24, 0]
lonW_ini   = lon[24, 0]
latW_final = lat[24,-1]
lonW_final = lon[24,-1]

m.plot(lonW_ini,   latW_ini,   marker='o', color='k')
m.plot(lonW_final, latW_final, marker='h', color='gray')

PATH_SAVE = '/cnrm/obs/data1/manglar/DPR/new_codes/RTTOV_SIM_PRJ/Paper_RTTOV/Results/'
plt.savefig(PATH_SAVE+'DPR_trajectory.png', dpi=300,bbox_inches = 'tight')
plt.show()



