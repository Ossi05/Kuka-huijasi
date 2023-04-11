# tee ratkaisu tänne
import csv
from datetime import datetime, timedelta

def huijarit():
    opiskelijat = []
    huijarit = []

    with open("tentin_aloitus.csv", "r") as aloitus:
        for tiedot in csv.reader(aloitus, delimiter=";"):
            opiskelijat.append(tiedot)


    with open("palautus.csv", "r") as palautus:

        for tiedot in csv.reader(palautus, delimiter=";"):
            for opiskelija in opiskelijat:
                if tiedot[0] in opiskelija:
                    aloitus_aika = datetime.strptime(opiskelija[1], "%H:%M")
                    lopetus_aika = datetime.strptime(tiedot[3], "%H:%M")
                    aika_ero = lopetus_aika - aloitus_aika

                    if aika_ero > timedelta(hours=3):
                        if opiskelija[0] not in huijarit:
                            huijarit.append(opiskelija[0])

    return huijarit
    

if __name__ == "__main__":
    print(huijarit())
