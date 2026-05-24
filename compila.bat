@echo off
TITLE compilazione aviutl-italian-patch

:: Compilazione delle risorse
windres.exe -v --input-format=rc --output-format=coff --codepage=65001 "it_resource.rc" -o "it_resource.res"
gcc -Os -m32 -s -o "it_mod.aul" -shared -Wl,-s "it_resource.res"

:: Messaggio di completamento compilazione
echo Compilazione finita!

:: Pausa per visualizzare il risultato
pause
