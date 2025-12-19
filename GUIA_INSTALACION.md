# 🎨 OOTDiffusion - Guía de Instalación y Uso

## 📋 Requisitos del Sistema

### Configuración Mínima (CPU)
- **CPU**: Intel i5/i7 o AMD Ryzen 5/7 (4+ cores)
- **RAM**: 16GB (mínimo 12GB)
- **Almacenamiento**: 25GB libres
- **SO**: Windows 10/11
- **Tiempo de procesamiento**: 5-10 minutos por imagen

### Configuración Recomendada (GPU)
- **GPU**: NVIDIA RTX 3060 12GB o superior
- **CPU**: Intel i5 12th gen+ / AMD Ryzen 5 5600+
- **RAM**: 16GB (recomendado 32GB)
- **Almacenamiento**: SSD con 25GB libres
- **SO**: Windows 10/11
- **Tiempo de procesamiento**: 30-60 segundos por imagen

---

## 🚀 Instalación Paso a Paso

### 1. Instalar Miniconda (si no lo tienes)

1. Descargar desde: https://docs.conda.io/en/latest/miniconda.html
2. Ejecutar el instalador
3. Marcar "Add Miniconda to PATH" durante instalación

### 2. Crear Entorno Virtual

Abrir PowerShell o Command Prompt y ejecutar:

```bash
# Navegar a la carpeta del proyecto
cd C:\Users\AJMM\Desktop\Projects2026\OOTDiffusion

# Crear entorno con Python 3.10
conda create -n ootd python=3.10 -y

# Activar entorno
conda activate ootd
```

### 3. Instalar PyTorch

**Para CPU:**
```bash
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cpu
```

**Para GPU (NVIDIA con CUDA 11.8):**
```bash
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
```

### 4. Instalar Dependencias

```bash
# Instalar todas las dependencias
pip install -r requirements.txt

# Instalar paquetes adicionales
pip install facexlib
pip install tb-nightly
```

### 5. Descargar Modelos (Automático)

Los modelos ya están descargados en la carpeta `checkpoints/`. Si necesitas descargarlos nuevamente:

```bash
python download_models_final.py
```

Esto descargará aproximadamente 15GB de modelos.

---

## ▶️ Ejecutar la Aplicación

### Opción 1: Usando el archivo batch (MÁS FÁCIL)

1. Hacer doble clic en: **`INICIAR_APP.bat`**
2. Presionar cualquier tecla cuando se solicite
3. Esperar 2-5 minutos mientras cargan los modelos
4. Cuando veas `Running on local URL: http://0.0.0.0:7865`
5. Abrir navegador en: **http://127.0.0.1:7865**

### Opción 2: Desde terminal

```bash
# Activar entorno
conda activate ootd

# Navegar a la carpeta run
cd C:\Users\AJMM\Desktop\Projects2026\OOTDiffusion\run

# Ejecutar aplicación
python gradio_ootd.py
```

### Opción 3: Desde VS Code

1. Abrir terminal integrada
2. Ejecutar:
```bash
conda activate ootd
cd run
python gradio_ootd.py
```

---

## 🎯 Cómo Usar la Aplicación

### En la interfaz web (http://127.0.0.1:7865):

#### Modo Half-Body (Mitad del cuerpo)
1. **Subir imagen de modelo** (persona de cuerpo completo)
2. **Subir imagen de prenda** (camiseta, blusa, etc. con fondo preferiblemente blanco)
3. Ajustar parámetros:
   - **Images**: 1-4 (número de variaciones)
   - **Steps**: 20-40 (más pasos = mejor calidad pero más lento)
   - **Guidance scale**: 2.0 (recomendado)
   - **Seed**: -1 (aleatorio) o número fijo para resultados reproducibles
4. Click en **"Run"**
5. Esperar (CPU: 5-10 min, GPU: 30-60 seg)

#### Modo Full-Body (Cuerpo completo)
1. Scroll hacia abajo a la sección "Full-body"
2. Subir imagen de modelo
3. Subir imagen de prenda
4. **IMPORTANTE**: Seleccionar categoría correcta:
   - **Upper-body**: Camisas, blusas, chaquetas
   - **Lower-body**: Pantalones, faldas
   - **Dress**: Vestidos completos
5. Click en **"Run"**

### Ejemplos incluidos:
- Modelos: `run/examples/model/`
- Prendas: `run/examples/garment/`

---

## ⚙️ Cambiar de CPU a GPU

### 1. Verificar que tienes GPU NVIDIA

```bash
# En PowerShell/CMD
nvidia-smi
```

Si ves información de tu GPU, continúa. Si no, necesitas instalar drivers NVIDIA.

### 2. Reinstalar PyTorch con CUDA

```bash
# Activar entorno
conda activate ootd

# Desinstalar PyTorch CPU
pip uninstall torch torchvision torchaudio -y

# Instalar PyTorch GPU (CUDA 11.8)
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
```

### 3. Modificar el código para usar GPU

**Archivo a editar**: `run/gradio_ootd.py`

Buscar estas líneas (alrededor de la línea 20):
```python
openpose_model_hd = OpenPose(-1)
parsing_model_hd = Parsing(-1)
ootd_model_hd = OOTDiffusionHD(-1)

openpose_model_dc = OpenPose(-1)
parsing_model_dc = Parsing(-1)
ootd_model_dc = OOTDiffusionDC(-1)
```

Cambiar **-1** por **0** (0 = primera GPU, -1 = CPU):
```python
openpose_model_hd = OpenPose(0)
parsing_model_hd = Parsing(0)
ootd_model_hd = OOTDiffusionHD(0)

openpose_model_dc = OpenPose(0)
parsing_model_dc = Parsing(0)
ootd_model_dc = OOTDiffusionDC(0)
```

### 4. Verificar funcionamiento

```bash
# Ejecutar test rápido
python test_models.py
```

Si no hay errores, la GPU está configurada correctamente.

### 5. Ejecutar aplicación con GPU

```bash
python gradio_ootd.py
```

**Mejora esperada**: De 5-10 minutos → 30-60 segundos por imagen

---

## 🔧 Solución de Problemas Comunes

### Error: "Not enough memory"
**Causa**: Poca RAM disponible

**Soluciones**:
1. Cerrar otros programas (Chrome, navegadores, etc.)
2. Aumentar RAM del sistema a 16GB mínimo
3. Usar solo modo HD (desactivar DC)

### Error: "CUDA not available"
**Causa**: GPU no detectada o PyTorch CPU instalado

**Soluciones**:
1. Verificar drivers NVIDIA actualizados
2. Reinstalar PyTorch GPU (ver sección "Cambiar de CPU a GPU")
3. Ejecutar `nvidia-smi` para verificar GPU

### Error: "Module not found"
**Causa**: Dependencias faltantes

**Solución**:
```bash
conda activate ootd
pip install -r requirements.txt
pip install facexlib
```

### Error: "Port 7865 already in use"
**Causa**: Otra instancia corriendo

**Solución**:
```bash
# Windows PowerShell
taskkill /F /IM python.exe

# O cambiar puerto en gradio_ootd.py:
block.launch(server_name='0.0.0.0', server_port=7866)
```

### Procesamiento muy lento en CPU
**Normal**: CPU tarda 5-10 minutos por imagen

**Soluciones**:
1. Reducir "Steps" a 20 (mínimo)
2. Generar solo 1 imagen a la vez
3. Considerar actualizar a GPU

### Modelos no cargan
**Causa**: Archivos corruptos o faltantes

**Solución**:
```bash
# Re-descargar modelos
python download_models_final.py
```

---

## 📊 Comparación CPU vs GPU

| Aspecto | CPU (i7) | GPU (RTX 3060) | GPU (RTX 4090) |
|---------|----------|----------------|----------------|
| Tiempo/imagen | 5-10 min | 30-60 seg | 15-30 seg |
| RAM necesaria | 16GB | 16GB | 32GB |
| VRAM necesaria | - | 12GB | 24GB |
| Costo energía | Bajo | Medio | Alto |
| Inversión | $0 | ~$400 | ~$1600 |

---

## 🔒 Privacidad y Seguridad

✅ **100% Local**: Todos los modelos y procesamiento en tu PC
✅ **Sin conexión a internet**: Funciona offline después de descargar modelos
✅ **Sin telemetría**: Tus imágenes NO se envían a ningún servidor
✅ **Código abierto**: Puedes revisar todo el código

**Puedes desconectar WiFi mientras usas la app y funcionará perfectamente.**

---

## 📁 Estructura del Proyecto

```
OOTDiffusion/
├── checkpoints/              # Modelos descargados (~15GB)
│   ├── clip-vit-large-patch14/
│   ├── humanparsing/
│   ├── ootd/
│   └── openpose/
├── ootd/                     # Código de inferencia
│   ├── inference_ootd_hd.py
│   ├── inference_ootd_dc.py
│   └── pipelines_ootd/
├── preprocess/               # Preprocesamiento
│   ├── humanparsing/
│   └── openpose/
├── run/                      # Interfaz Gradio
│   ├── gradio_ootd.py       # ← Archivo principal
│   ├── utils_ootd.py
│   └── examples/
├── INICIAR_APP.bat          # Launcher rápido
├── test_models.py           # Verificación de modelos
├── download_models_final.py # Descarga de modelos
└── requirements.txt         # Dependencias
```

---

## 🆘 Soporte y Recursos

### Repositorio Original
- GitHub: https://github.com/levihsu/OOTDiffusion
- Paper: https://arxiv.org/abs/2403.01779

### Comandos Útiles

```bash
# Ver versión de PyTorch y CUDA
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA disponible: {torch.cuda.is_available()}')"

# Ver uso de memoria
python -c "import psutil; print(f'RAM disponible: {psutil.virtual_memory().available/1024**3:.1f}GB')"

# Verificar GPU
nvidia-smi

# Limpiar caché de pip
pip cache purge

# Recrear entorno desde cero
conda deactivate
conda remove -n ootd --all -y
conda create -n ootd python=3.10 -y
```

---

## 📝 Notas Finales

- **Primera ejecución**: Tardará 2-5 minutos cargando modelos en memoria
- **Imágenes recomendadas**: 
  - Modelos: Personas de pie, cuerpo completo, fondo simple
  - Prendas: Fondo blanco, prenda centrada, sin maniquí
- **Calidad**: Mejores resultados con imágenes de alta resolución (1024x768+)
- **Experimentación**: Prueba diferentes valores de "Steps" y "Guidance scale"

---

**¡Listo para usar! 🎉**

Para iniciar: Doble click en `INICIAR_APP.bat` o ejecuta `python run/gradio_ootd.py`
