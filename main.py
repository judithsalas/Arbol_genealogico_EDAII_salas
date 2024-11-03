from arbol_genealogico import Persona, ArbolGenealogico

def crear_persona(arbol):
    '''
    Función auxiliar para crear una nueva persona en el árbol genealógico.
    '''
    nombre = input("Ingrese el nombre del miembro: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del miembro: ")
    id_unico = input("Ingrese un ID único para el miembro: ")
    return Persona(nombre, fecha_nacimiento, id_unico)

def main():
    arbol = ArbolGenealogico()

    while True:
        print("\n--- Menú del Árbol Genealógico ---")
        print("1. Agregar miembro")
        print("2. Agregar hermano/hermana")
        print("3. Eliminar miembro")
        print("4. Asignar pareja")
        print("5. Agregar mascota")
        print("6. Asignar padre o madre a un miembro")
        print("7. Buscar relación")
        print("8. Mostrar árbol genealógico")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
           
            persona = crear_persona(arbol)
            padre_id = input("Ingrese el ID del padre (o presione Enter si no hay padre): ")
            madre_id = input("Ingrese el ID de la madre (o presione Enter si no hay madre): ")
            '''
            Crear un nuevo miembro
            '''

            arbol.agregar_miembro(persona, padre_id=padre_id if padre_id else None, madre_id=madre_id if madre_id else None)
            print(f"Miembro {persona.nombre} agregado con éxito.")
            '''
            Agregar la persona con las referencias de padre y madre
            '''

        elif opcion == "2":
            '''
            Opción dual para agregar o asignar hermano/hermana
            '''
            print("1. Agregar un nuevo hermano/hermana a una persona existente")
            print("2. Convertir a dos personas existentes en hermanos/hermanas")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                '''
                Agregar un nuevo hermano/hermana
                '''
                hermano_id = input("Ingrese el ID del hermano o hermana existente: ")
                hermano = arbol.personas.get(hermano_id)
                
                if hermano:
                    nuevo_hermano = crear_persona(arbol)
                    
                    ''' 
                    Verificar si el hermano existente tiene padres
                    '''
                    if hermano.padre or hermano.madre:
                        padre_id = hermano.padre.id_unico if hermano.padre else None
                        madre_id = hermano.madre.id_unico if hermano.madre else None
                        
                        '''
                        Asignar los mismos padres al nuevo hermano/hermana
                        '''
                        arbol.agregar_miembro(nuevo_hermano, padre_id=padre_id, madre_id=madre_id)
                        print(f"{nuevo_hermano.nombre} agregado como hermano/hermana de {hermano.nombre} con los mismos padres.")
                    
                    else:
                        '''
                        Crear padres si ninguno de los hermanos tiene padres asignados
                        '''
                        print("El hermano existente no tiene padres asignados.")
                        crear_nuevos_padres = input("¿Desea crear nuevos padres para ambos hermanos? (s/n): ").lower()
                        if crear_nuevos_padres == 's':
                            nuevo_padre = crear_persona(arbol)
                            nueva_madre = crear_persona(arbol)
                            
                            '''
                            Agregar los nuevos padres al árbol
                            '''
                            arbol.agregar_miembro(nuevo_padre)
                            arbol.agregar_miembro(nueva_madre)
                            
                            '''
                            Asignar los nuevos padres a ambos hermanos
                            '''
                            arbol.agregar_miembro(hermano, padre_id=nuevo_padre.id_unico, madre_id=nueva_madre.id_unico)
                            arbol.agregar_miembro(nuevo_hermano, padre_id=nuevo_padre.id_unico, madre_id=nueva_madre.id_unico)
                            
                            print(f"{nuevo_hermano.nombre} y {hermano.nombre} ahora son hermanos con nuevos padres: {nuevo_padre.nombre} y {nueva_madre.nombre}.")
                        else:
                            print("No se han asignado padres nuevos.")
                else:
                    print("Hermano o hermana no encontrado.")
            
            elif sub_opcion == "2":
                ''' 
                Convertir a dos personas existentes en hermanos/hermanas
                '''
                id_persona1 = input("Ingrese el ID de la primera persona: ")
                id_persona2 = input("Ingrese el ID de la segunda persona: ")
                persona1 = arbol.personas.get(id_persona1)
                persona2 = arbol.personas.get(id_persona2)

                if persona1 and persona2:
                    if persona1.padre or persona1.madre:
                        '''
                        Si persona1 tiene padres, asignarlos a persona2
                        '''
                        padre_id = persona1.padre.id_unico if persona1.padre else None
                        madre_id = persona1.madre.id_unico if persona1.madre else None
                        arbol.agregar_miembro(persona2, padre_id=padre_id, madre_id=madre_id)
                        print(f"{persona1.nombre} y {persona2.nombre} ahora son hermanos con los mismos padres.")
                    elif persona2.padre or persona2.madre:
                        '''
                        Si persona2 tiene padres, asignarlos a persona1
                        '''
                        padre_id = persona2.padre.id_unico if persona2.padre else None
                        madre_id = persona2.madre.id_unico if persona2.madre else None
                        arbol.agregar_miembro(persona1, padre_id=padre_id, madre_id=madre_id)
                        print(f"{persona1.nombre} y {persona2.nombre} ahora son hermanos con los mismos padres.")
                    else:
                        '''
                        Crear nuevos padres si ninguno tiene
                        '''
                        print("Ninguno de los dos tiene padres asignados. Crearemos nuevos padres.")
                        nuevo_padre = crear_persona(arbol)
                        nueva_madre = crear_persona(arbol)
                        arbol.agregar_miembro(nuevo_padre)
                        arbol.agregar_miembro(nueva_madre)
                        arbol.agregar_miembro(persona1, padre_id=nuevo_padre.id_unico, madre_id=nueva_madre.id_unico)
                        arbol.agregar_miembro(persona2, padre_id=nuevo_padre.id_unico, madre_id=nueva_madre.id_unico)
                        print(f"{persona1.nombre} y {persona2.nombre} ahora son hermanos con nuevos padres: {nuevo_padre.nombre} y {nueva_madre.nombre}.")
                else:
                    print("Una o ambas personas no fueron encontradas.")

        elif opcion == "3":
            '''
            Eliminar miembro
            '''
            id_unico = input("Ingrese el ID único del miembro a eliminar: ")
            eliminado = arbol.eliminar_miembro(id_unico)
            if eliminado:
                print(f"Miembro {eliminado.nombre} eliminado.")
            else:
                print("Miembro no encontrado.")

        elif opcion == "4":
            '''
            Asignar pareja
            '''
            id_persona1 = input("Ingrese el ID de la primera persona: ")
            id_persona2 = input("Ingrese el ID de la segunda persona: ")
            arbol.asignar_pareja(id_persona1, id_persona2)

        elif opcion == "5":
            '''
            Agregar mascota
            '''
            id_persona = input("Ingrese el ID de la persona a la que se le agregará la mascota: ")
            nombre_mascota = input("Ingrese el nombre de la mascota: ")
            especie = input("Ingrese la especie de la mascota: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento de la mascota: ")
            arbol.agregar_mascota(id_persona, nombre_mascota, especie, fecha_nacimiento)

        elif opcion == "6":
            '''
            Asignar padre o madre
            '''
            id_persona = input("Ingrese el ID de la persona a la que desea asignar un padre o madre: ")
            persona = arbol.personas.get(id_persona)

            if persona:
                tipo = input("¿Desea asignar un padre (p) o una madre (m)? ").lower()
                if tipo == 'p':
                    padre_id = input("Ingrese el ID del padre (o presione Enter para crear uno nuevo): ")
                    if padre_id:
                        padre = arbol.personas.get(padre_id)
                        if padre:
                            arbol.agregar_miembro(persona, padre_id=padre_id)
                        else:
                            print("Padre no encontrado.")
                    else:
                        '''
                        Crear un nuevo padre
                        '''
                        nuevo_padre = crear_persona(arbol)
                        arbol.agregar_miembro(nuevo_padre)
                        arbol.agregar_miembro(persona, padre_id=nuevo_padre.id_unico)
                        print(f"Nuevo padre {nuevo_padre.nombre} asignado a {persona.nombre}.")
                elif tipo == 'm':
                    madre_id = input("Ingrese el ID de la madre (o presione Enter para crear una nueva): ")
                    if madre_id:
                        madre = arbol.personas.get(madre_id)
                        if madre:
                            arbol.agregar_miembro(persona, madre_id=madre_id)
                        else:
                            print("Madre no encontrada.")
                    else:
                        '''
                        Crear una nueva madre
                        '''
                        nueva_madre = crear_persona(arbol)
                        arbol.agregar_miembro(nueva_madre)
                        arbol.agregar_miembro(persona, madre_id=nueva_madre.id_unico)
                        print(f"Nueva madre {nueva_madre.nombre} asignada a {persona.nombre}.")
                else:
                    print("Opción no válida.")
            else:
                print("Persona no encontrada.")

        elif opcion == "7":
            '''
            Buscar relación
            '''
            id_1 = input("Ingrese el ID único del primer miembro: ")
            id_2 = input("Ingrese el ID único del segundo miembro: ")
            resultado = arbol.buscar_relacion(id_1, id_2)
            print(resultado)

        elif opcion == "8":
            '''
            Mostrar el árbol genealógico
            '''
            print("Mostrando el árbol genealógico...")
            arbol.mostrar_arbol()

        elif opcion == "9":
            '''
            Salir del programa
            '''
            
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
