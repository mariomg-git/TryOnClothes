@echo off
echo ============================================================
echo Iniciando OOTDiffusion Virtual Try-On
echo ============================================================
echo.
echo INSTRUCCIONES:
echo 1. Esta ventana mostrara el progreso de carga (2-5 minutos)
echo 2. Cuando veas "Running on local URL", abre ese URL en tu navegador
echo 3. NO cierres esta ventana mientras uses la aplicacion
echo.
echo Presiona cualquier tecla para continuar...
pause > nul

call C:\Users\AJMM\Miniconda3\Scripts\activate.bat ootd
cd /d C:\Users\AJMM\Desktop\Projects2026\OOTDiffusion\run
python gradio_ootd.py

echo.
echo ============================================================
echo La aplicacion se ha cerrado
echo ============================================================
pause
