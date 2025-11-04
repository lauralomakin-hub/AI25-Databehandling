# AI25-

##Start-checklista för AI25-Databehandling
1. Öppna projektet korrekt

Öppna alltid hela projektmappen i VS Code, inte bara en enskild fil.
Exempel:
C:\Users\laura\Projekt\code\git\AI25-Databehandling

2. Aktivera den virtuella miljön

Öppna terminalen (Ctrl + ö) och skriv:
source venv/Scripts/activate

Om du ser (venv) i början av raden betyder det att miljön är aktiv.

3. Kontrollera kernel i notebook

När du öppnar en .ipynb-fil:

Klicka uppe till höger på “Select Kernel”.

Välj “AI25-Databehandling (venv)”.

Testa med:
import sys
print(sys.executable)

Sökvägen ska sluta på
…AI25-Databehandling\venv\Scripts\python.exe

4. Installera saknade paket

Om något bibliotek saknas:
python -m pip install -r requirements.txt

eller installera specifika paket:
python -m pip install pandas jupyter ipykernel

5. Uppdatera och spara miljön

Om du lägger till eller uppdaterar paket:
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push

6. Kom ihåg

venv/ ska inte laddas upp till GitHub (det ignoreras i .gitignore).

Din miljö är lokal och påverkar inte globala Python-installationer.

Allt du behöver för att återskapa miljön finns i requirements.txt.