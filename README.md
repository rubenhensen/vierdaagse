# Vierdaagse scriptje
Ik heb mijn best gedaan om het programma zo duidelijk mogelijk uit te leggen. Het is best simpel, maar het kan best ingewikkeld lijken als je nooit zoiets doet. Ik heb geprobeerd zo duidelijk mogelijk alle stappen uit te leggen!

Het stappenplan (ik ga er van uit dat je Windows gebruikt):
1. Installeer https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Bij Optional: klik MSVC aan
2. Download Python https://www.python.org/downloads/windows/
3. Installeer Python. Selecteer de optie "Add python.exe to PATH"
4. Download het script van Github door op de groen knop met "<> Code" te klikken, en dan op download zip.
5. Pak het zip bestand uit en open de folder met alle bestanden.
6. Rechterklik in de folder met SHIFT ingedrukt. Klik op "Open Powershell hier" (Zou kunnen dat er terminal staat ipv powershell)
7. Er opent als het goed is een blauw scherm met `PS C:\Users\JOUW_ACCOUNT\Downloads\vierdaagse-main>` of iets in die richting.
8. Type dit commando `python.exe -m pip install --upgrade pip`. Wacht tot het klaar is.
9. Typ dit commando `pip install --upgrade setuptools wheel`. Wacht tot het klaar is.
10. Typ dit commando `pip install selenium playsound`. Wacht tot het klaar is.
11. Typ dit commando `python vierdaagse.py`
12. Als het goed werkt, opent nu een browser scherm die automatisch de pagina van de vierdaagse gaat verversen. Als er een ticket vrij komt dan klikt het automatisch op de bestelknop. Dan gaat een geluidje af zodat je naar je computer kan rennen en je gegevens kan invullen.
