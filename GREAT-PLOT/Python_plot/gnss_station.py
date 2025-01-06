import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import pandas as pd
import numpy as np

mpl.rcParams["font.family"] = 'Arial'  # 默认字体类型
mpl.rcParams["mathtext.fontset"] = 'cm'  # 数学文字字体
mpl.rcParams["font.size"] = 13
#latlon.xlsx存储了地点名、经纬度信息
station = pd.read_excel('latlon.xlsx')
proj = ccrs.PlateCarree()
fig = plt.figure(figsize=(6, 4), dpi=100)  # 创建画布
ax = fig.subplots(1, 1, subplot_kw={'projection': proj})  # 创建子图
extent = [115, 118, 39.3, 41.3]  ##经纬度范围
ax.set_extent(extent)
with open('C:/Users/qiuyu/.local/share/cartopy/shapefiles/natural_earth/physical/CN-border-La.dat') as src:
    context = src.read()
    blocks = [cnt for cnt in context.split('>') if len(cnt) > 0]
    borders = [np.fromstring(block, dtype=float, sep=' ') for block in blocks]
for line in borders:
    ax.plot(line[0::2], line[1::2], '-', color='k', lw=0.3, transform=ccrs.Geodetic())
# add lon and lat
gl = ax.gridlines(draw_labels=True, linestyle=":", linewidth=0.3, x_inline=False, y_inline=False, color='k')
gl.top_labels = False  # 关闭上部经纬标签
gl.right_labels = False
gl.xformatter = LONGITUDE_FORMATTER  # 使横坐标转化为经纬度格式
gl.yformatter = LATITUDE_FORMATTER
gl.xlocator = mticker.FixedLocator(np.arange(114, 120, 1))
gl.ylocator = mticker.FixedLocator(np.arange(38, 43, 1))
gl.xlabel_style = {'size': 12}  # 修改经纬度字体大小
gl.ylabel_style = {'size': 12}
ax.set_extent([114.99, 118.01, 39.3, 41.3], crs=ccrs.PlateCarree())

ax.plot(station_urban.iloc[0, :], station_urban.iloc[1, :], 'o', markersize=4, color='red', label='Station 1',
        transform=ccrs.Geodetic())
ax.plot(station_suburban.iloc[0, :], station_suburban.iloc[1, :], 'x', markersize=6, color='magenta', label='Station 2',
        transform=ccrs.Geodetic())
ax.plot(station_rural.iloc[0, :], station_rural.iloc[1, :], '^', markersize=6, color='seagreen', label='Station 3',
        transform=ccrs.Geodetic())

# add title
ax.set_title('Location', fontsize=13)
# add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.35, 0.75), borderaxespad=0, frameon=False, markerscale=2)

plt.savefig('station.png'，bbox_inches = 'tight')
plt.show()
