import networkx as nx
import matplotlib.pyplot as plt

class Persona:
    def __init__(self, nombre, fecha_nacimiento, id_unico):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.id_unico = id_unico
        self.padre = None
        self.madre = None
        self.hijos = []  # Lista de hijos para almacenar descendientes
        self.pareja = None  # Nueva referencia para la pareja
        self.mascotas = []  # Lista para almacenar mascotas

    def __str__(self):
        return f"{self.nombre} ({self.fecha_nacimiento})"

class Mascota:
    def __init__(self, nombre, especie, fecha_nacimiento):
        self.nombre = nombre
        self.especie = especie
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"{self.nombre} ({self.especie}, {self.fecha_nacimiento})"


class ArbolGenealogico:
    def __init__(self):
        self.personas = {}  # Diccionario para almacenar personas por id_unico
        self.raices = []  # Lista para almacenar los primeros miembros sin padre ni madre

    def agregar_miembro(self, persona, padre_id=None, madre_id=None):
        """
        Agregar padre si se especifica
        """
        if padre_id:
            padre = self.personas.get(padre_id)
            if padre:
                persona.padre = padre
                padre.hijos.append(persona)
            else:
                print(f"Padre con ID {padre_id} no encontrado.")
                
        """
        Agregar madre si se especifica
        """
        if madre_id:
            madre = self.personas.get(madre_id)
            if madre:
                persona.madre = madre
                madre.hijos.append(persona)
            else:
                print(f"Madre con ID {madre_id} no encontrado.")
        
        """
        Si no se especifica ni padre ni madre, agregar como raíz
        """
        if not padre_id and not madre_id:
            self.raices.append(persona)

        """
        Agregar la persona al diccionario de personas
        """
        self.personas[persona.id_unico] = persona
        print(f"Miembro {persona.nombre} agregado al árbol genealógico.")

    def asignar_pareja(self, id_persona1, id_persona2):
        """
        Asigna una relación de pareja entre dos personas.
        """
        persona1 = self.personas.get(id_persona1)
        persona2 = self.personas.get(id_persona2)

        if persona1 and persona2:
            persona1.pareja = persona2
            persona2.pareja = persona1
            print(f"{persona1.nombre} y {persona2.nombre} ahora son pareja.")
        else:
            print("Una o ambas personas no fueron encontradas en el árbol.")

    def agregar_mascota(self, id_persona, nombre_mascota, especie, fecha_nacimiento):
        """
        Agrega una mascota a una persona específica en el árbol genealógico.
        """
        persona = self.personas.get(id_persona)
        if persona:
            mascota = Mascota(nombre_mascota, especie, fecha_nacimiento)
            persona.mascotas.append(mascota)
            print(f"Mascota {nombre_mascota} agregada a {persona.nombre}.")
        else:
            print("Persona no encontrada. No se pudo agregar la mascota.")

    def eliminar_miembro(self, id_unico):
        persona = self.personas.pop(id_unico, None)
        if persona:
            """
            Remover a la persona de los hijos del padre y madre
            """
            if persona.padre:
                persona.padre.hijos.remove(persona)
            if persona.madre:
                persona.madre.hijos.remove(persona)
            """
            Remover de las raíces si es uno de los primeros
            """
            if persona in self.raices:
                self.raices.remove(persona)
            """
            Remover pareja si la tiene
            """
            if persona.pareja:
                persona.pareja.pareja = None
            return persona
        else:
            print("Miembro no encontrado.")
            return None

    def buscar_relacion(self, id_unico_1, id_unico_2):
        persona1 = self.personas.get(id_unico_1)
        persona2 = self.personas.get(id_unico_2)
        if persona1 and persona2:
            """
            Aquí puedes implementar la lógica para determinar el parentesco
            """
            return f"Relación encontrada entre {persona1.nombre} y {persona2.nombre}."
        else:
            return "Una o ambas personas no fueron encontradas en el árbol."

    def mostrar_arbol(self):
        grafo = nx.DiGraph()
        
        """
        Añadir nodos para personas y sus relaciones (padres, madre, pareja)
        """
        for persona in self.personas.values():
            grafo.add_node(persona.nombre, type='persona')
            if persona.padre:
                grafo.add_edge(persona.padre.nombre, persona.nombre)
            if persona.madre:
                grafo.add_edge(persona.madre.nombre, persona.nombre)
            if persona.pareja:
                grafo.add_edge(persona.nombre, persona.pareja.nombre, style="dotted")
                
            """
            Añadir nodos y aristas para las mascotas
            """
            for mascota in persona.mascotas:
                grafo.add_node(mascota.nombre, type='mascota')
                grafo.add_edge(persona.nombre, mascota.nombre)
        
        """
        Definir los colores de los nodos según el tipo (persona o mascota)
        """
        colores = []
        for nodo, data in grafo.nodes(data=True):
            if data.get('type') == 'persona':
                colores.append('lightblue')  # Color para personas
            elif data.get('type') == 'mascota':
                colores.append('orange')  # Color para mascotas

        """
        Dibujar el grafo
        """
        pos = nx.spring_layout(grafo)
        nx.draw(grafo, pos, with_labels=True, node_size=3000, node_color=colores, font_size=10, font_weight="bold", arrows=False)
        
        """
        Añadir etiquetas a los nodos
        """
        labels = {nodo: nodo for nodo in grafo.nodes}
        nx.draw_networkx_labels(grafo, pos, labels=labels)
        
        plt.show()
