Introduction
---
Die Suche nach passenden Weiterbildungspraxen in der Allgemeinmedizin ist unnötig schwierig. Hier ist ein einfaches
Skript, anhand dessen man die Suchergebnisse der Webseite der Bayerischen Landesärztekammer auf eine Karte markieren
kann.

Limitations
---
this script will only get the first 100 practices of the search, as this is the maximum to display on one page using
the form. It is possible to modify the request to the server to include an arbitrary number of results in the response
using the browser devtools. The server response will then contain as many results as specified, although it is still
paginated on the page.

Instructions
---
1. visit this website and make a query:
https://secure.blaek.de/Portal/WBBSuchePortal/WBBSuchePortal/Suche
2. Save the result using ```HTML only``` as `input.html` in the directory containing the script
3. run the script, resulting in the file `out.csv`
4. create a new map on
https://www.google.com/maps/
5. import `out.csv`
