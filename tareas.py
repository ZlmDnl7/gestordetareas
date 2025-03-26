# Mini app de gestión de tareas
tareas = []

def mostrar_tareas():
    if not tareas:
        print("📋 No hay tareas pendientes.")
    else:
        print("\n📌 Lista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def agregar_tarea():
    tarea = input("✍️ Ingresa una nueva tarea: ")
    tareas.append(tarea)
    print("✅ Tarea agregada con éxito.")

def eliminar_tarea():
    mostrar_tareas()
    if tareas:
        try:
            num = int(input("❌ Ingresa el número de la tarea a eliminar: "))
            if 1 <= num <= len(tareas):
                tarea_eliminada = tareas.pop(num - 1)
                print(f"🗑️ Tarea '{tarea_eliminada}' eliminada.")
            else:
                print("⚠️ Número inválido.")
        except ValueError:
            print("⚠️ Ingresa un número válido.")

def main():
    while True:
        print("\n--- 📝 MENÚ ---")
        print("1️⃣ Mostrar tareas")
        print("2️⃣ Agregar tarea")
        print("3️⃣ Eliminar tarea")
        print("4️⃣ Salir")

        opcion = input("👉 Selecciona una opción: ")

        if opcion == "1":
            mostrar_tareas()
        elif opcion == "2":
            agregar_tarea()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            print("👋 Saliendo de la aplicación...")
            break
        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
