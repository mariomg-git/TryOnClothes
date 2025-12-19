# Monitor de progreso para OOTDiffusion
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Monitoreando OOTDiffusion App..." -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

$counter = 0
$maxWait = 300  # 5 minutos máximo

while ($counter -lt $maxWait) {
    $counter += 20
    $minutes = [math]::Floor($counter / 60)
    $seconds = $counter % 60
    
    Write-Host "[$minutes min $seconds seg] Verificando progreso..." -ForegroundColor Yellow
    
    # Buscar proceso Python que ejecuta gradio_ootd.py
    $process = Get-Process python -ErrorAction SilentlyContinue | Where-Object {
        $_.CommandLine -like "*gradio_ootd.py*"
    }
    
    if ($process) {
        Write-Host "  [+] Proceso activo (PID: $($process.Id))" -ForegroundColor Green
        Write-Host "  [+] Uso de CPU: $([math]::Round($process.CPU, 2))s" -ForegroundColor Green
        Write-Host "  [+] Memoria: $([math]::Round($process.WorkingSet64/1MB, 2)) MB" -ForegroundColor Green
    } else {
        Write-Host "  [-] Proceso no encontrado - puede haber terminado o fallado" -ForegroundColor Red
        break
    }
    
    # Buscar si Gradio ya está corriendo
    $gradioRunning = netstat -ano | Select-String ":7860" -Quiet
    if ($gradioRunning) {
        Write-Host ""
        Write-Host "============================================================" -ForegroundColor Green
        Write-Host "EXITO! La aplicacion esta corriendo!" -ForegroundColor Green
        Write-Host "============================================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "Abre tu navegador en: http://127.0.0.1:7860" -ForegroundColor Cyan
        Write-Host ""
        break
    }
    
    Write-Host ""
    Start-Sleep -Seconds 20
}

if ($counter -ge $maxWait) {
    Write-Host "Tiempo de espera agotado. Verifica manualmente el terminal." -ForegroundColor Red
}
