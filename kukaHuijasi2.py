import csv
from datetime import datetime, timedelta
 
def viralliset_pisteet():
    opiskelijat = []
    opiskelija_tehtavat = {}
    opiskelija_sanakirja = {}
    with open("tentin_aloitus.csv", "r") as aloitus:
        for tiedot in csv.reader(aloitus, delimiter=";"):
            opiskelijat.append(tiedot)
 
    with open("palautus.csv", "r") as palautus:
 
        for tiedot in csv.reader(palautus, delimiter=";"):
 
            for opiskelija in opiskelijat:
                if tiedot[0] == opiskelija[0]:
                    aloitus_aika = datetime.strptime(opiskelija[1], "%H:%M")
                    lopetus_aika = datetime.strptime(tiedot[3], "%H:%M")
                    aika_ero = lopetus_aika - aloitus_aika
 
                    if aika_ero < timedelta(hours=3):
                        if tiedot[0] in opiskelija_tehtavat:
                            if tiedot[1] in opiskelija_tehtavat[tiedot[0]]:
                                if int(tiedot[2]) > opiskelija_tehtavat[tiedot[0]][tiedot[1]]:
                                    opiskelija_tehtavat[tiedot[0]][tiedot[1]] = int(tiedot[2])
                            else:
                                opiskelija_tehtavat[tiedot[0]][tiedot[1]] = int(tiedot[2])
                        else:
                            opiskelija_tehtavat[tiedot[0]] = {}
                            opiskelija_tehtavat[tiedot[0]][tiedot[1]] = int(tiedot[2])
 
            
            for opiskelija in opiskelija_tehtavat:
                luku = 0
                for tehtava in opiskelija_tehtavat[opiskelija]:
                    luku += opiskelija_tehtavat[opiskelija][tehtava]
 
                opiskelija_sanakirja[opiskelija] = luku
 
    return opiskelija_sanakirja
 
if __name__ == "__main__":
    print(viralliset_pisteet())
