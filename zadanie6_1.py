nazwa_os='Windows'
wersja=8.1
wsparcie_no="nie wspierana"
wsparcie_yes="aktualne wsparcie"

if wersja == 8.0:
    print ("ta wersja {0} jest {1}".format(nazwa_os,wsparcie_no))
if wersja > 8.0:
    print ("Ta wersja {0} ma {1}".format(nazwa_os,wsparcie_yes))
