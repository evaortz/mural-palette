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


## 22/08/2026
Objetivo: Hacer un test de comprobacion de quantize_image() con caso feliz, manejo de errores de parametros y coso de una imagen con menos de n_color.

Creado tests/test_quantize_image_manual.py con 7 casos:
- Test 1: caso feliz con sketch1.jpeg (n_colors=16)
- Test 2-6: validaciones de tipo/rango (image inválida, n_colors no-int, negativo, >256, =0)
- Test 7: imagen generada en código (Image.new + paste) con exactamente 3 colores reales, pedida con n_colors=16 → caso límite de "colores fantasma"

Apunte: se han usado asserts

### Bug encontrado y corregido gracias al test
En `quantizer.py`, el bucle que reconstruye la paleta de tuplas RGB:
```python
for i in range(0, n_colors * 3, 3):
```
asumía que `raw_palette`siempre tiene `n_colors * 3` elementos.
Con imágenes de pocos colores reales (ej. 3 colores, pedidos con n_colors=16), Pillow
devuelve una paleta más corta porque el test dió este error: `IndexError: list index out of range`.

**Fix:** basar el rango en el tamaño real de la paleta, no en n_colors pedido:
```python
for i in range(0, len(raw_palette), 3):
```


## 24/08/2026
Objetivo: Implementar color_percentages() en pixel_counter.py con su test manual.

Creada y completada la funcion color_percentages():
- Recibe la imagen cuantizada y la paleta (salida de quantize_image)
- Calcula el % de cada color como count / total_pixels * 100
- Devuelve una lista de tuplas (color, percentage)

Creado tests/test_color_percentages_manual.py con 8 casos: caso feliz con sketch1.jpeg,
tipos inválidos (imagen, paleta, color no-tupla), valores inválidos (tupla de tamaño
incorrecto, RGB fuera de rango, RGB no entero), y paleta más corta que los colores reales
de la imagen (índice fuera de rango). 8/8 pasan.

Cambiado el nombre de test_quantize_image_manual.py a test_quantizer_manual.py