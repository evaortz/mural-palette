## 18/08/2026
Creando un entorno virtual e instalando las bibliotecas clave del proyecto.

La organización de carpetas de momento va a ser basada en la arquitectura hexagonal, con el objetivo de que la lógica del programa esté aislada de todo lo demás.

En entorno virtual lo he creado con:
```
python -m venv venv
```

Y para entrar en el entorno:
```
venv\Scripts\Activate.ps1
```
Instaladas las librerias de:
- pillow
- numpy
- pip

Añadidas a requirements.txt

Añadido .gitignore



## 20/08/2026
Objetivo: Crear una funcion para cargar una imagen y prepararla para que posteriormente se pueda procesar.

Creado core/__init__.py para que python sepa que lo que hay en core/ es un paquete.
Creados los modulos de image_loader: open_image, check_rgb y resize_image. Probado con un boceto de prueba en assets/samples


## 21/08/2026
Objetivo: Hacer manejo de errores de resize_image y dejar image_loader.py cerrado

image_loader.py está completado, los tres modulos y su validacion

Creado un test manual para validar image_loader.py con 5 casos.

Reorganizada la estructura del proyecto: 
- Problema: El core estaba en la raiz y fallaban los imports. 
- Solución: Creada una carpeta mural_analyzer/ en raiz y un __init__.py dentro para que sea un paquete. también creado setup.py para permitir imports.
- Herramienta: `pip install -e .` para instalar paquete en modo desarrollo
    (Instalado setuptools
    Añadido *.egg-info/ al .gitignore)
- Resultado: imports limpios sin `sys.path` hacks


## 22/08/2026
Objetivo: Implementar quantize_image(image, n_colors=16), una funcion para reducir los colores de una imagen a un numero de colores predominantes (por defecto 16), para ello hay que usar Median Cut de Pillow.Irá en quantizer.py

Creado quantizer.py con quantize_image(image, n_colors=16) terminada pero sin testear.

Validaciones: image debe ser PIL.Image.Image, n_colors debe ser int positivo y <= 256.

Problema que ha aparecido: si la imagen tiene menos colores reales que n_colors, Pillow rellena la paleta con colores "fantasma"
    - Solución: usar getcolors() para saber qué índices de la paleta están realmente en uso, y filtrar la paleta para devolver solo esos colores.

Pendiente: crear test_quantizer_manual.py con casos de validación (tipos inválidos, rangos, imagen con pocos colores) y caso normal.
