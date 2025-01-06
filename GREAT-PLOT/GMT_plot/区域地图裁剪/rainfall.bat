gmt begin rainfall png
gmt set MAP_FRAME_TYPE plain
gmt set FONT_TITLE 12p
gmt set MAP_TITLE_OFFSET 0p
gmt colorbar -CRAINC.cpt -DjMR+w3.5c/0.15c+o4.5c/0c+m  -L -Byaf+l"mm" -R4.4/16.1/49/55
gmt surface rainfall.txt  -R4.4/16.1/49/55 -I1m -Grainfall.grd
gmt psclip  -R4.4/16.1/49/55   -JM10c DEU_NE.gmt
gmt grdimage rainfall.grd -R4.4/16.1/49/55 -JM10c -CRAINC.cpt
gmt psxy gadm36_DEU_1.gmt -W0.3p,black
gmt end show
pause