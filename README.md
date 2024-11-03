# Sistema de Árbol Genealógico Interactivo

Objetivo: Desarrollar una aplicación en Python para gestionar un árbol genealógico que permita agregar personas, relaciones familiares (padres, madres, hermanos, pareja) y mascotas. El sistema debe ser interactivo y permitir a los usuarios ver y modificar el árbol genealógico de forma intuitiva.

## Estructuras Básicas
Clase Persona: Representa a cada miembro de la familia con atributos como nombre, fecha de nacimiento, ID único, padre, madre, pareja, hijos y una lista de mascotas.
Clase Mascota: Representa a las mascotas con atributos como nombre, especie y fecha de nacimiento, y se asocia a una persona específica como su dueño.

## Funcionalidades Implementadas

1. Agregar Persona
Permite crear una nueva persona con información básica (nombre, fecha de nacimiento, ID).
Opción de asignar un padre y/o una madre en el momento de agregar la persona.

2. Agregar Hermano/Hermana

Opción Dual:
Agregar un nuevo hermano/hermana: Permite crear una nueva persona y asignarla como hermano/hermana de una persona existente.
Convertir a dos personas existentes en hermanos/hermanas: Permite seleccionar dos personas ya existentes y establecer que tienen los mismos padres.

Asignación de Padres:
Si el hermano existente tiene padres, el nuevo hermano recibe automáticamente esos mismos padres.
Si ninguno tiene padres, se da la opción de crear nuevos padres y asignarlos a ambos.

3. Eliminar Persona

Permite eliminar a una persona del árbol, eliminando también la referencia en los padres y hermanos.

4. Asignar Pareja

Permite establecer una relación de pareja entre dos personas, lo cual se representa en el árbol genealógico.

5. Agregar Mascota

Permite agregar una mascota a una persona específica, asignando los datos de la mascota (nombre, especie, fecha de nacimiento).
Las mascotas se visualizan como nodos en el gráfico, conectados a su dueño, y se distinguen por un color diferente.

6. Asignar Padre o Madre en Cualquier Momento

Permite asignar o cambiar el padre o la madre de una persona en cualquier momento. Si no se encuentra un padre/madre específico, el sistema ofrece la opción de crear uno nuevo.

7. Buscar Relación

Permite verificar la relación entre dos personas en el árbol genealógico.

8. Visualización del Árbol Genealógico

Usa la librería networkx y matplotlib para representar gráficamente el árbol genealógico.
Las personas se representan como nodos conectados por líneas que representan las relaciones familiares (padres, pareja).
Las mascotas se distinguen con un color diferente y se conectan solo a sus dueños.

## Funcionalidad Interactiva del Menú

El sistema tiene un menú interactivo con opciones claras para navegar entre las funcionalidades.
Los usuarios pueden crear relaciones familiares y realizar modificaciones en el árbol de forma intuitiva.
En cada opción que implica seleccionar a una persona, si no se encuentra la persona, el sistema pregunta al usuario si desea intentarlo nuevamente o regresar al menú principal.

## Ejemplo de Flujo de Uso
Agregar a "Juan" como raíz del árbol.
Agregar una mascota ("Fido") a "Juan".
Agregar "Pedro" como hermano de "Juan":
Si "Juan" no tiene padres asignados, el sistema ofrecerá la opción de crear nuevos padres para ambos.
Asignar a "María" como pareja de "Juan".
Agregar a "Ana" como hija de "Juan" y "María".
Convertir a "Ana" y "Pedro" en hermanos (si ya existen ambos, se asignarán los mismos padres).
