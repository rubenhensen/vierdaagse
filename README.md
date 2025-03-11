# Vierdaagse scriptje
Ik heb mijn best gedaan om het programma zo duidelijk mogelijk uit te leggen. Ik twee manieren om het te draaien. De ene is met een .exe, maar ik heb dat niet kunnen testen want ik heb zelf geen windows, dus ik geef dat een 10% kans van slagen. De andere is de manier hoe ik het zelf draai, maar dat is wat ingewikkelder.

## Exe
Het stappenplan:
1. Download het script van Github door op de groen knop met "<> Code" te klikken, en dan op download zip.
2. Pak het zip bestand uit en open de folder met alle bestanden.
3. Open het .exe bestand in de folder `dist/`


## De normale manier
Het is best simpel, maar het kan best ingewikkeld lijken als je nooit zoiets doet. Ik heb geprobeerd zo duidelijk mogelijk alle stappen uit te leggen!

Het stappenplan (ik ga er van uit dat je Windows gebruikt):
1. Download Python https://www.python.org/downloads/windows/
2. Installeer Python. Selecteer de optie "Add python.exe to PATH"
3. Download het script van Github door op de groen knop met "<> Code" te klikken, en dan op download zip.
4. Pak het zip bestand uit en open de folder met alle bestanden.
5. Rechterklik in de folder met SHIFT ingedrukt. Klik op "Open Powershell hier"
6. Er opent als het goed is een blauw scherm met `PS C:\Users\JOUW_ACCOUNT\Downloads\vierdaagse-main>` of iets in die richting.
7. Typ dit commando `pip install selenium playsound` (misschien `pip3 install selenium playsound`). Wacht tot het klaar is.
8. Typ dit commando `python vierdaagse.py` (misschien `python3 vierdaagse.py`)
9. Als het goed werkt, opent nu een browser scherm die automatisch de pagina van de vierdaagse gaat verversen. Als er een ticket vrij komt dan klikt het automatisch op de bestelknop. Dan gaat een geluidje af zodat je naar je computer kan rennen en je gegevens kan invullen.
