ids = []
numeros = []
categorias = []
tipos = []
fechas = []
descripciones = []
observaciones = []
while True:
    print("menu principal agrupador numérico")
    print("1) crear número")
    print("2) editar número")
    print("3) eliminar número")
    print("4) buscar número")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #------------------#
    #--|crear_numero|--#
    #------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_numero = 1
        else:
            id_numero = ids[-1] + 1
        numero = float(input("número: "))
        categoria = input("categoría: ")
        tipo = input("tipo de número: ")
        fecha = input("fecha: ")
        descripcion = input("descripción: ")
        observacion = input("observación: ")
        ids.append(id_numero)
        numeros.append(numero)
        categorias.append(categoria)
        tipos.append(tipo)
        fechas.append(fecha)
        descripciones.append(descripcion)
        observaciones.append(observacion)
        print("número registrado correctamente.")
        print("id:", id_numero)
    #-------------------#
    #--|editar_numero|--#
    #-------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar número")
            for i in range(len(ids)):
                print(f"{ids[i]} | {numeros[i]} | {categorias[i]} | {tipos[i]} | {fechas[i]} | {descripciones[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {numeros[posicion]} | {categorias[posicion]} | {tipos[posicion]} | {fechas[posicion]} | {descripciones[posicion]} | {observaciones[posicion]}")
                numeros[posicion] = float(input("nuevo número: "))
                categorias[posicion] = input("nueva categoría: ")
                tipos[posicion] = input("nuevo tipo de número: ")
                fechas[posicion] = input("nueva fecha: ")
                descripciones[posicion] = input("nueva descripción: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|eliminar_numero|--#
    #---------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar número")
            for i in range(len(ids)):
                print(f"{ids[i]} | {numeros[i]} | {categorias[i]} | {tipos[i]} | {fechas[i]} | {descripciones[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {numeros[posicion]} | {categorias[posicion]} | {tipos[posicion]} | {fechas[posicion]} | {descripciones[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    numeros.pop(posicion)
                    categorias.pop(posicion)
                    tipos.pop(posicion)
                    fechas.pop(posicion)
                    descripciones.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|buscar_numero|--#
    #-------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar número")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {numeros[posicion]} | {categorias[posicion]} | {tipos[posicion]} | {fechas[posicion]} | {descripciones[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = numeros[0]
            menor = numeros[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {numeros[i]} | {categorias[i]} | {tipos[i]} | {fechas[i]} | {descripciones[i]} | {observaciones[i]}")
                suma += numeros[i]
                if numeros[i] > mayor:
                    mayor = numeros[i]
                if numeros[i] < menor:
                    menor = numeros[i]
            promedio = suma / len(ids)
            print("estadísticas agrupador numérico")
            print("cantidad de registros:", len(ids))
            print("suma total:", round(suma, 2))
            print("promedio:", round(promedio, 2))
            print("mayor número:", round(mayor, 2))
            print("menor número:", round(menor, 2))
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el agrupador numérico.")
        break
    else:
        print("opción no válida.")