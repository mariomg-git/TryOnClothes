# TryOnClothes - OOTDiffusion Windows Implementation

Una implementación de OOTDiffusion optimizada para Windows que permite generar imágenes de personas probándose diferentes prendas de ropa usando IA.

> **Basado en**: OOTDiffusion: Outfitting Fusion based Latent Diffusion for Controllable Virtual Try-on [[arXiv paper](https://arxiv.org/abs/2403.01779)]<br>
> **Implementación Windows por**: mariomg-git<br>
> **Proyecto original**: [levihsu/OOTDiffusion](https://github.com/levihsu/OOTDiffusion)

![demo](images/demo.png)

## 🌟 Características

- ✅ **Compatibilidad total con Windows**
- ✅ **Interfaz web fácil de usar** (Gradio)
- ✅ **Carga de modelos local** (sin descargas online)
- ✅ **Scripts automatizados** para instalación y ejecución
- ✅ **Dos modos**: HD (alta definición) y DC (controlado por datos)

## 🚀 Instalación Rápida

### 1. Clonar el repositorio
```bash
git clone https://github.com/mariomg-git/TryOnClothes.git
cd TryOnClothes
```

### 2. Instalar dependencias
```bash
# Crear entorno conda
conda create -n ootd python=3.10
conda activate ootd

# Instalar paquetes
pip install -r requirements.txt
```

### 3. Descargar modelos
```bash
python download_models_final.py
```

### 4. Ejecutar la aplicación
```bash
INICIAR_APP.bat
```

La aplicación se abrirá en: **http://127.0.0.1:7865**

## 📋 Guía Detallada

Para instrucciones paso a paso, consulta: [GUIA_INSTALACION.md](GUIA_INSTALACION.md)

## 🎯 Uso

1. **Subir imagen de modelo**: Sube una foto de una persona
2. **Subir prenda**: Sube la imagen de la ropa que quieres probar
3. **Seleccionar categoría**: 
   - Upper-body (parte superior)
   - Lower-body (parte inferior) 
   - Dress (vestido)
4. **Ajustar parámetros** y hacer clic en **Run**

## 🛠 Scripts Incluidos

- `INICIAR_APP.bat` - Inicia la aplicación rápidamente
- `run_app.bat` - Script principal de ejecución
- `run_debug.ps1` - Para debuguear problemas
- `download_models_final.py` - Descarga todos los modelos necesarios
- `test_models.py` - Verifica que los modelos funcionen
- `monitor_app.ps1` - Monitorea el estado de la aplicación

## ⚠ Requisitos del Sistema

- **OS**: Windows 10/11
- **RAM**: 8GB mínimo, 16GB recomendado
- **Espacio**: ~15GB para modelos y código
- **Python**: 3.9-3.11
- **GPU**: NVIDIA recomendada (funciona en CPU pero más lento)

## 🔧 Solución de Problemas

### Error: "No se puede conectar a HuggingFace"
✅ **Solucionado** - Los modelos se cargan localmente

### Error: "No funciona la URL 0.0.0.0:7865"
✅ **Solucionado** - Configurado para usar 127.0.0.1:7865

### Problemas con paths/rutas
✅ **Solucionado** - Rutas absolutas configuradas automáticamente

## 📁 Estructura del Proyecto

```
TryOnClothes/
├── checkpoints/          # Configuraciones de modelos
├── ootd/                # Código principal de inferencia  
├── preprocess/          # Preprocesamiento de imágenes
├── run/                 # Scripts de ejecución y UI
├── images/              # Imágenes de ejemplo
├── *.py                 # Scripts de utilidad
└── *.bat               # Scripts de Windows
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## Citation
```
@article{xu2024ootdiffusion,
  title={OOTDiffusion: Outfitting Fusion based Latent Diffusion for Controllable Virtual Try-on},
  author={Xu, Yuhao and Gu, Tao and Chen, Weifeng and Chen, Chengcai},
  journal={arXiv preprint arXiv:2403.01779},
  year={2024}
}
```

## 📄 Licencia

Este proyecto está basado en el trabajo original de [OOTDiffusion](https://github.com/levihsu/OOTDiffusion) con modificaciones para mejorar la compatibilidad con Windows y facilitar su uso.

## 🙏 Créditos

- **Proyecto original**: [OOTDiffusion](https://github.com/levihsu/OOTDiffusion)
- **Implementación Windows**: mariomg-git
- **Comunidad**: Gracias a todos los contribuidores

---

### 💡 ¿Necesitas ayuda?

Si encuentras algún problema, por favor:

1. Revisa la [Guía de Instalación](GUIA_INSTALACION.md)
2. Ejecuta `run_debug.ps1` para ver errores detallados  
3. Abre un [Issue](https://github.com/mariomg-git/TryOnClothes/issues) con el error completo

**¡Disfruta probándote ropa virtualmente! 👕👗**

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=levihsu/OOTDiffusion&type=Date)](https://star-history.com/#levihsu/OOTDiffusion&Date)

## TODO List
- [x] Paper
- [x] Gradio demo
- [x] Inference code
- [x] Model weights
- [ ] Training code
