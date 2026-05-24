# A.U.T.P (AviUtl Translation Project)
# Redlean, iMoeAria, Katto

# English: This script can be used to patch the .aup (AviUtl1 Project Files) to use "Mod.Avanz." instead of "Adv.Edit"
# Italian: Questo script può essere usato per applicare una patch a un .aup (AviUtl1 Project Files) per usare "Mod.Avanz." invece che "Adv.Edit"

from tkinter import Tk, filedialog
import os
import time
import sys

# Defining base functions
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


def open_file():
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    root.attributes("-topmost", True)  # Bring dialog to front

    file_path = filedialog.askopenfilename()

    root.destroy()
    return file_path  # Absolute path as string


def save_file(default_name="output.aup"):
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    file_path = filedialog.asksaveasfilename(
        initialfile=default_name,
        defaultextension=".aup",
        filetypes=[("AviUtl1 Project File", "*.aup"), ("All Files", "*.*")]
    )

    root.destroy()
    return file_path


def convert_file(oldAup="", newAup="", toReplace=1):
    fs_o = open(oldAup, "rb")
    fs_n = open(newAup, "wb")
    
    old_data = fs_o.read()
    
    if toReplace == 1:
        new_data = old_data.replace(b"Adv.Edit", b"Mod.Avan")
    elif toReplace == 2:
        new_data = old_data.replace(b"Mod.Avan", b"Adv.Edit")
    
    fs_n.write(new_data)
    
    fs_o.close()
    fs_n.close()
    
# Defining string tables to have multiple languages

it_string_table = {
	"0001": 'Convertitore file progetto per AviUtl per usare "Mod.Avan" invece che "Adv.Edit"',
	"0002": "Parte di A.U.T.P. (AviUtl Translation Project)",
	"0003": "Cosa desideri fare? -> ",
	"0004": "Aprendo il progetto...",
	"0005": "Salvando il progetto...",
	"0006": "Finito! Uscendo in 3 secondi...",
	"0007": "[1] Convertire da Adv.Edit a Mod.Avan",
	"0008": "[2] Convertire da Mod.Avan a Adv.Edit",
	"0009": "[3] Esci",
	"0010": "Opzione invalida!"
}

en_string_table = {
	"0001": 'Converter for AviUtl project files to use "Mod.Avan" instead of "Adv.Edit"',
	"0002": "Part of A.U.T.P. (AviUtl Translation Project)",
	"0003": "What do you want to do? -> ",
	"0004": "Opening the project...",
	"0005": "Saving the project...",
	"0006": "Done! Exiting in 3 seconds...",
	"0007": "[1] Convert Adv.Edit to Mod.Avan",
	"0008": "[2] Convert da Mod.Avan to Adv.Edit",
	"0009": "[3] Exit",
	"0010": "Invalid option!"
}

# Initialization of the program itself

clear()

print("Select a language / Scegli una lingua")
print("-------------------------------------")
print("[1] Italian/Italiano")
print("[2] English/Inglese")
print("-------------------------------------")

lang_choose = input("-> ")
avail_lang = ["1", "2"]

while lang_choose not in avail_lang:
	print("Language invalid! / Lingua invalida!")
	time.sleep(3)
	clear()
	print("Select a language / Scegli una lingua")
	print("-------------------------------------")
	print("[1] Italian/Italiano")
	print("[2] English/Inglese")
	print("-------------------------------------")

	lang_choose = input("-> ")
	
if lang_choose == "1":
	string_table = it_string_table
elif lang_choose == "2":
	string_table = en_string_table
	
# Showing the menu
clear()

def showMainMenu():
	print(string_table["0001"])
	print(string_table["0002"])
	print("-------------------------------------------------------------")
	print(string_table["0007"])
	print(string_table["0008"])
	print(string_table["0009"])
	print("-------------------------------------------------------------")

showMainMenu()

avail_options = ["1", "2", "3"]
option = input(string_table["0003"])
while option not in avail_options:
	print(string_table["0010"])
	time.sleep(3)
	clear()
	showMainMenu()
	option = input(string_table["0003"])

if option == "1":
    project_file = open_file()
    
    filename = os.path.basename(project_file)
    
    new_project_file = save_file(default_name=filename)
    
    convert_file(oldAup=project_file, newAup=new_project_file, toReplace=1)
    
    print(string_table["0006"])
    time.sleep(3)
    sys.exit(-1)
    
elif option == "2":
    project_file = open_file()
    
    filename = os.path.basename(project_file)
    
    new_project_file = save_file(default_name=filename)
    
    convert_file(oldAup=project_file, newAup=new_project_file, toReplace=2)
    
    print(string_table["0006"])
    time.sleep(3)
    sys.exit(-1)
    
elif option == "3":
	print(string_table["0006"])
	time.sleep(3)
	sys.exit(-1)
		

