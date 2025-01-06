gmt begin Rainfall png
gmt set MAP_FRAME_TYPE plain
gmt set FONT_TITLE 12p
gmt set MAP_TITLE_OFFSET 0p
gmt coast -R5/16/47/55.2 -JM10c -Df  -Wthinnest  -A50000 -N1  -Bxa2 -Bya2 -B+t"Rainfall" 
gmt psclip -R5/16/47/55.2 -JM10c gadm36_DEU_0.gmt
gmt psxy rainfall.txt -CRAINC.cpt -Ss0.25c -JM10c
gmt coast -R5/16/47/55.2 -JM10c -Df  -Wthinnest  -A50000 -N1  
gmt end show
pause