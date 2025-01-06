gmt begin QHlake13 pdf E600
::gmt grdview @earth_relief_30s -R99.1/101.2/36.3/37.6/-500/3000 
::gmt grdview @earth_relief_30s -R99/101/36.3/37.6/0/4500 -JM10c -JZ4c -Qi600 -Ggoogle_sat1.tif  -p215/30 -Wthinnest,black
gmt grdview @earth_relief_30s -R99/101/36.3/37.6/0/5000 -JM10c -JZ4c -Qi600 -Ggoogle_sat1.tif  -p215/30 -N2500+gTAN4 -Wthinnest,black
:: 
::gmt grdview @earth_relief_30s -R99.1/101.2/36.8/38/-5000/4500 -JM10c -JZ4c -Qi600 -Ggoogle_sat.tif  -N-100+gTAN4 -p215/30 -Wthinnest,black
::gmt grdview @earth_relief_30s -R99.1/101.2/35.75/36.79/-1000/4500 -JM10c -JZ4c -Qi600 -Ggoogle_sat4.tif  -N-100+gwhite -p330/30
::gmt grdview @earth_relief_30s -R96.5/103/34.5/40/-1000/4500 -JM10c -JZ4c -Qi600 -Ggoogle_satx.tif  -N-100+gBISQUE2 -p135/30 -Wthinnest,black
::-Ba -BwsENZ
gmt end show
pause