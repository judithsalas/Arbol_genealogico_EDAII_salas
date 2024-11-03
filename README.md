# Sistema de Árbol Genealógico Interactivo en Python

Este proyecto es un sistema de gestión de árbol genealógico interactivo en Python. La aplicación permite agregar personas, establecer relaciones familiares (padres, hermanos, parejas) y agregar mascotas para cada persona. El sistema también proporciona una visualización gráfica del árbol genealógico, utilizando `networkx` y `matplotlib` para mostrar las conexiones entre personas y mascotas.

## Características

- **Agregar Personas**: Crea nuevas personas en el árbol con atributos como nombre, fecha de nacimiento, y padres/madres asignados.
- **Agregar Hermano/Hermana**: Opción dual para agregar un nuevo hermano a una persona existente o hacer que dos personas ya existentes se conviertan en hermanos.
- **Asignar Pareja**: Establece una relación de pareja entre dos personas, representada con una línea punteada en el gráfico.
- **Agregar Mascota**: Permite agregar una mascota para una persona específica, con atributos como nombre, especie y fecha de nacimiento.
- **Asignar Padre/Madre**: Permite asignar padres a una persona en cualquier momento, incluso después de haber sido creada.
- **Visualización del Árbol Genealógico**: Usa `networkx` y `matplotlib` para mostrar el árbol genealógico de forma gráfica.

## Instalación

Para ejecutar este sistema, necesitas tener Python y las bibliotecas requeridas. Puedes instalarlas utilizando `pip`:

```bash
pip install matplotlib networkx fpdf
```

## Ejecución

Ejecuta el archivo `main.py` para iniciar el programa y acceder al menú interactivo:

```bash
python main.py
```

## Menú de Opciones

1. **Agregar miembro**: Crea un nuevo miembro en el árbol y asigna padres si es necesario.
2. **Agregar hermano/hermana**: Opción dual para agregar un nuevo hermano o hacer que dos personas existentes se conviertan en hermanos.
3. **Eliminar miembro**: Elimina una persona del árbol genealógico.
4. **Asignar pareja**: Define una relación de pareja entre dos personas.
5. **Agregar mascota**: Asocia una mascota a una persona en el árbol.
6. **Asignar padre o madre a un miembro**: Permite asignar padres/madres en cualquier momento.
7. **Buscar relación**: Busca la relación entre dos personas.
8. **Mostrar árbol genealógico**: Muestra el árbol genealógico gráficamente.
9. **Salir**: Cierra el programa.

## Estructura del Código

- `arbol_genealogico.py`: Contiene las clases `Persona`, `Mascota` y `ArbolGenealogico`, las cuales definen la estructura de los miembros, mascotas y las funciones para manejar el árbol genealógico.
- `main.py`: Proporciona la interfaz de usuario en línea de comandos (CLI) para interactuar con el árbol genealógico.

## Ejemplo de Uso

```plaintext
1. Agrega a "Juan" como raíz del árbol.
2. Agrega una mascota llamada "Fido" a "Juan".
3. Agrega a "Pedro" como hermano de "Juan". Si "Juan" no tiene padres asignados, se ofrece la opción de crearlos.
4. Asigna a "María" como pareja de "Juan".
5. Agrega a "Ana" como hija de "Juan" y "María".
6. Convierte a "Ana" y "Pedro" en hermanos (si ya existen ambos, se asignan los mismos padres).
```

## Requerimientos de Software

- Python 3.x
- Matplotlib
- Networkx
- FPDF (para generar informes si es necesario)

## Notas sobre Eficiencia y Escalabilidad

Este sistema es adecuado para familias pequeñas a medianas. Si se planea almacenar relaciones más complejas o un árbol de gran tamaño, es recomendable considerar una base de datos para manejar consultas más avanzadas y mejorar la eficiencia de la visualización.

## Licencia

Este proyecto es de libre uso y distribución para fines educativos y personales.
