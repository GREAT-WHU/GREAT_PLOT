gmt begin Global_5 png
gmt set MAP_FRAME_TYPE plain
gmt set FONT_LABEL Times-Roman,12p
gmt set FONT_TITLE 12p,Times-Roman
gmt gmtset FONT_ANNOT_PRIMARY=12p,Times-Roman
gmt set FONT_ANNOT_PRIMARY 12p,Times-Roman
::gmt pscoast -JQ20c -Rg -BWSen -Baf -Slightgray -Wthinnest -A10000 -N1 
gmt coast -JQ20c -Rg -Ba30f10g30 -Gwhite -Slightgray  -Wthinnest -A10000 -N1
::gmt pscoast -JQ20c -Rg  -Wthinnest -A10000 -N1 
gmt makecpt -Ccolombia.cpt -T-8000/8000/200 -Icz -H > myTopo.cpt
gmt colorbar -CmyTopo.cpt -DjBC+w10c/0.3c+o0c/-1.2c+m -Baf+l"Elevation(m)"
::gmt makecpt -Cfrance.cpt -T-10000/10000/500 -Icz -H > myTopo.cpt
gmt grdimage @earth_relief_30m   -CmyTopo.cpt 
gmt coast -JQ20c -Rg -Ba30f10g30 -Swhite  -Tdg-30/75+w0.4i+f2+jCM -L-40/-78+c0+w5000+u+f
::-I+d
::gmt pscoast -JQ14c -R73/135/17/55 -BWSen -Baf -Slightgray -Wthinnest -A10000 -N1
::gmt makecpt -Cbam -T0/24/0.01 -Icz -H > Hour.cpt
::gmt colorbar -CHour.cpt -DjMR+w8.5c/0.2c+o-0.7c/0c+m -Bxaf -Byaf+l"UTC/h"

gmt plot data1.txt -Gred -Sc0.05c
gmt plot GNSSsite_info.txt -St0.2c -W0.3p,gray,solid -Gblue
::绘制板块边界
gmt plot plates.dat -W0.3p,black,-


gmt end show
pause
