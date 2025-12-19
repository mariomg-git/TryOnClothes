# Script para ejecutar OOTDiffusion con debug
Write-Host "Activando entorno ootd..." -ForegroundColor Cyan

# Ejecutar con conda y redirigir stderr a stdout
& "C:\Users\AJMM\Miniconda3\Scripts\conda.exe" run -n ootd python run\gradio_ootd.py 2>&1

Write-Host "`nAplicación finalizada. Presiona cualquier tecla..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
