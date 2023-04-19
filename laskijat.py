from typing import List, Union

# Laskija-luokka, joka sisältää kaksi laskutoimitusta: summaa ja kerro.
# Nämä toiminnot laskevat annettujen lukujen summan tai tulon.
class Laskija:
    def summaa(self, *args: Union[int, float]) -> Union[int, float]:
        # Palauttaa annettujen lukujen summan
        return sum(args)

    def kerro(self, *args: Union[int, float]) -> Union[int, float]:
        # Palauttaa annettujen lukujen tulon
        tulo = 1
        for luku in args:
            tulo *= luku
        return tulo

# MonenLaskija-luokka, joka perii Laskija-luokan.
# Sisältää samat laskutoimitukset kuin Laskija-luokka,
# mutta pystyy käsittelemään mielivaltaisen määrän lukuja.
class MonenLaskija(Laskija):
    pass

# Funktio, joka tulostaa annetut avainsana-argumentit.
def argumenttien_tulostaja(**kwargs):
    for avainsana, arvo in kwargs.items():
        print(f'Argumentin "{avainsana}" arvo on {arvo}.')

# Seuraavat rivit testaavat Laskija- ja MonenLaskija-luokkien toimivuutta,
# sekä argumenttien_tulostaja-funktion toimivuutta.
l = Laskija()
ml = MonenLaskija()

print(l.summaa(11, 31))
print(l.kerro(3, 12))
print()
print(ml.summaa(1, 2, 3, 4, 5))
print(ml.kerro(1, 2, 3, 4, 5))
print()
print(ml.summaa(1, 2, 3, 4, 5, 6, 7))
print(ml.kerro(1, 2, 3, 4, 5, 6 ,7))
print()
argumenttien_tulostaja(eka=42, toka='foo', kolmas=[0, 1, 2])
print()
argumenttien_tulostaja(nimi='Tero', ika=41, kaupunki='Turku', oppilaitos='TAI')
