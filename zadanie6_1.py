nazwa_os='Windows'
wersja=10
wsparcie_no="nie wspierana"
wsparcie_yes="aktualne wsparcie"

if wersja == 8.0:
    print ("Ta wersja {0} - {1} jest {2}".format(nazwa_os,wersja,wsparcie_no))
if wersja > 8.0:
    print ("Ta wersja {0} - {1} ma {2}".format(nazwa_os,wersja,wsparcie_yes))
