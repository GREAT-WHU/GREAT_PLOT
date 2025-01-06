gmt begin station png
gmt grdimage @earth_relief_01m -JM15c -R-130/-118/35/50 -Baf -BWSen -I+d
gmt colorbar -Dx-10c/-1.5c+w20c/0.5c -Bxaf+l"Elevation (m)"
gmt plot gnss_station.csv -Sc0.3c -Gred -Wthinnest,black -i1,2
gmt text gnss_station.csv -F+f10p,Helvetica-Bold,black+jTL -Dj0.2c/0.2c -i1,2,0
echo "H 10p,Helvetica-Bold gnss_stations" > legend.txt
echo "S 0.3c c red thinnest,black 0.4c GNSS Station" >> legend.txt
gmt legend legend.txt -Dx0.5c/0.5c+w3c/1.5c+o0.2c/0.2c -F+gwhite+p1p -DjBR
gmt end show



