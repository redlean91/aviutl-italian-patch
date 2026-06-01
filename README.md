# aviutl-italian-patch
Patch di traduzione in Italiano per AviUtl.

Il codice originale non è mio, tutti i crediti a: Sykhro

## Compilazione:
`windres.exe -v --input-format=rc --output-format=coff --codepage=65001 "it_resource.rc" -o "it_resource.res"
gcc -Os -m32 -s -o "it_mod.aul" -shared -Wl,-s "it_resource.res"`

# italianAupPatchAviutl.py
Serve a trasformare i progetti che usano ancora "Adv.Edit" a "Mod.Avan" per la patch italiana di Exedit o viceversa.
Supporta sia l'inglese sia l'itaiano
