import json
import datetime
from typing import Dict, List, Any

class AsesorBodaIA:
    def __init__(self):
        self.progreso_usuario = {
            "informacion_personal": {},
            "detalles_boda": {},
            "presupuesto": {},
            "invitados": [],
            "proveedores": {},
            "cronograma": {},
            "lista_tareas": [],
            "notas_especiales": []
        }
        self.archivo_progreso = "progreso_boda.json"
        self.cargar_progreso()
    
    def cargar_progreso(self):
        """Carga el progreso guardado del usuario"""
        try:
            with open(self.archivo_progreso, 'r', encoding='utf-8') as file:
                self.progreso_usuario = json.load(file)
            print("✨ ¡Bienvenido de vuelta! He cargado tu progreso anterior.")
        except FileNotFoundError:
            print("✨ ¡Hola! Soy tu asesor de bodas con inteligencia artificial.")
            print("Estoy aquí para ayudarte a planear la boda de tus sueños paso a paso. 💕")
    
    def guardar_progreso(self):
        """Guarda el progreso actual del usuario"""
        with open(self.archivo_progreso, 'w', encoding='utf-8') as file:
            json.dump(self.progreso_usuario, file, indent=2, ensure_ascii=False)
        print("💾 Progreso guardado exitosamente.")
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal con opciones empáticas"""
        print("\n" + "="*50)
        print("💒 ASESOR DE BODAS IA - MENÚ PRINCIPAL 💒")
        print("="*50)
        print("1. 👫 Información personal y de la pareja")
        print("2. 💍 Detalles de la boda (fecha, lugar, estilo)")
        print("3. 💰 Planificación de presupuesto")
        print("4. 📝 Gestión de invitados")
        print("5. 🏪 Proveedores y servicios")
        print("6. 📅 Cronograma y fechas importantes")
        print("7. ✅ Lista de tareas pendientes")
        print("8. 📋 Ver resumen completo de tu boda")
        print("9. 💾 Guardar progreso")
        print("0. 👋 Salir")
        print("="*50)
    
    def recopilar_informacion_personal(self):
        """Recopila información personal de manera empática"""
        print("\n💕 Empecemos conociendo un poco sobre ustedes como pareja.")
        print("Esta información me ayudará a personalizar mis recomendaciones.")
        
        if not self.progreso_usuario["informacion_personal"]:
            print("\n¿Podrías contarme sobre ustedes?")
            nombre1 = input("Nombre del primer integrante: ")
            nombre2 = input("Nombre del segundo integrante: ")
            tiempo_relacion = input("¿Cuánto tiempo llevan juntos? ")
            historia_amor = input("Cuéntame brevemente su historia de amor (opcional): ")
            
            self.progreso_usuario["informacion_personal"] = {
                "nombre1": nombre1,
                "nombre2": nombre2,
                "tiempo_relacion": tiempo_relacion,
                "historia_amor": historia_amor,
                "fecha_registro": str(datetime.datetime.now())
            }
            
            print(f"\n¡Qué hermoso, {nombre1} y {nombre2}! 💕")
            print("Me emociona mucho poder ayudarlos en este momento tan especial.")
        else:
            info = self.progreso_usuario["informacion_personal"]
            print(f"\n¡Hola de nuevo {info['nombre1']} y {info['nombre2']}! 😊")
            print("¿Te gustaría actualizar alguna información personal? (s/n)")
            if input().lower() == 's':
                self.progreso_usuario["informacion_personal"] = {}
                self.recopilar_informacion_personal()
    
    def planificar_detalles_boda(self):
        """Ayuda a planificar los detalles principales de la boda"""
        print("\n💍 Ahora hablemos sobre los detalles de su boda soñada.")
        
        print("\n¿Ya tienen una fecha en mente?")
        fecha = input("Fecha deseada (DD/MM/AAAA) o 'por definir': ")
        
        print("\n¿Han pensado en el lugar de la ceremonia?")
        lugar_ceremonia = input("Lugar de ceremonia (iglesia, jardín, playa, etc.): ")
        
        print("\n¿Y para la recepción?")
        lugar_recepcion = input("Lugar de recepción: ")
        
        print("\n¿Qué estilo de boda imaginan?")
        print("(Ejemplos: elegante, rústica, moderna, vintage, bohemia, minimalista)")
        estilo = input("Estilo de boda: ")
        
        print("\n¿Aproximadamente cuántos invitados esperan?")
        num_invitados = input("Número estimado de invitados: ")
        
        self.progreso_usuario["detalles_boda"] = {
            "fecha": fecha,
            "lugar_ceremonia": lugar_ceremonia,
            "lugar_recepcion": lugar_recepcion,
            "estilo": estilo,
            "numero_invitados": num_invitados,
            "ultima_actualizacion": str(datetime.datetime.now())
        }
        
        print("\n✨ ¡Perfecto! Ya tengo una idea clara de lo que buscan.")
        self.generar_recomendaciones_personalizadas()
    
    def generar_recomendaciones_personalizadas(self):
        """Genera recomendaciones basadas en los detalles proporcionados"""
        detalles = self.progreso_usuario["detalles_boda"]
        estilo = detalles.get("estilo", "").lower()
        
        print(f"\n💡 Basándome en su estilo '{estilo}', aquí tienes algunas recomendaciones:")
        
        if "rústico" in estilo:
            print("🌾 Para una boda rústica considera: decoración con madera, flores silvestres, iluminación cálida")
        elif "elegante" in estilo:
            print("✨ Para una boda elegante: colores neutros, flores clásicas, vajilla fina")
        elif "playa" in estilo or "bohem" in estilo:
            print("🌊 Para una boda bohemia/playa: telas fluidas, colores tierra, decoración natural")
        
        print("\n📝 Agregando tareas recomendadas a tu lista...")
        self.agregar_tareas_automaticas()
    
    def gestionar_presupuesto(self):
        """Ayuda a planificar y controlar el presupuesto"""
        print("\n💰 Hablemos sobre el presupuesto. Esto nos ayudará a tomar decisiones inteligentes.")
        
        presupuesto_total = input("\n¿Cuál es su presupuesto total aproximado? $")
        
        print("\n📊 Te ayudo a distribuir el presupuesto de manera inteligente:")
        print("Distribución recomendada:")
        print("• Lugar y catering: 40-50%")
        print("• Vestido y traje: 8-10%")
        print("• Fotografía: 10-15%")
        print("• Flores y decoración: 8-10%")
        print("• Música/DJ: 8-10%")
        print("• Otros gastos: 10-15%")
        
        try:
            total = float(presupuesto_total.replace('$', '').replace(',', ''))
            self.progreso_usuario["presupuesto"] = {
                "total": total,
                "lugar_catering": total * 0.45,
                "vestimenta": total * 0.09,
                "fotografia": total * 0.12,
                "decoracion": total * 0.09,
                "musica": total * 0.09,
                "otros": total * 0.16,
                "gastos_registrados": [],
                "fecha_creacion": str(datetime.datetime.now())
            }
            print(f"\n✅ Presupuesto configurado: ${total:,.2f}")
        except ValueError:
            print("❌ Por favor ingresa un número válido para el presupuesto.")
    
    def gestionar_invitados(self):
        """Ayuda a gestionar la lista de invitados"""
        print("\n📝 Gestión de invitados - ¡Una de las partes más emocionantes!")
        
        print("\n¿Qué te gustaría hacer?")
        print("1. Agregar nuevos invitados")
        print("2. Ver lista actual")
        print("3. Categorizar invitados")
        print("4. Volver al menú principal")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            self.agregar_invitados()
        elif opcion == "2":
            self.mostrar_lista_invitados()
        elif opcion == "3":
            self.categorizar_invitados()
    
    def agregar_invitados(self):
        """Permite agregar invitados a la lista"""
        print("\n👥 Vamos a agregar invitados a tu lista.")
        print("Puedes agregarlos uno por uno. Escribe 'terminar' cuando hayas acabado.")
        
        while True:
            nombre = input("\nNombre del invitado (o 'terminar'): ")
            if nombre.lower() == 'terminar':
                break
            
            relacion = input("Relación contigo (familia, amigo, compañero de trabajo, etc.): ")
            confirmacion = input("¿Confirmó asistencia? (s/n/pendiente): ")
            
            invitado = {
                "nombre": nombre,
                "relacion": relacion,
                "confirmacion": confirmacion,
                "fecha_agregado": str(datetime.datetime.now())
            }
            
            self.progreso_usuario["invitados"].append(invitado)
            print(f"✅ {nombre} agregado a la lista.")
        
        print(f"\n🎉 Total de invitados: {len(self.progreso_usuario['invitados'])}")
    
    def mostrar_lista_invitados(self):
        """Muestra la lista actual de invitados"""
        invitados = self.progreso_usuario["invitados"]
        if not invitados:
            print("\n📝 Aún no has agregado invitados.")
            return
        
        print(f"\n👥 Lista de invitados ({len(invitados)} personas):")
        print("-" * 50)
        for i, invitado in enumerate(invitados, 1):
            print(f"{i}. {invitado['nombre']} - {invitado['relacion']} - {invitado['confirmacion']}")
    
    def agregar_tareas_automaticas(self):
        """Agrega tareas recomendadas automáticamente"""
        tareas_basicas = [
            "Reservar lugar de ceremonia",
            "Reservar lugar de recepción", 
            "Contratar catering",
            "Buscar fotógrafo",
            "Comprar/rentar vestido de novia",
            "Comprar/rentar traje del novio",
            "Enviar invitaciones",
            "Organizar prueba de menú",
            "Contratar música/DJ",
            "Planear decoración floral"
        ]
        
        for tarea in tareas_basicas:
            if not any(t["descripcion"] == tarea for t in self.progreso_usuario["lista_tareas"]):
                nueva_tarea = {
                    "descripcion": tarea,
                    "completada": False,
                    "prioridad": "media",
                    "fecha_creacion": str(datetime.datetime.now())
                }
                self.progreso_usuario["lista_tareas"].append(nueva_tarea)
    
    def gestionar_tareas(self):
        """Gestiona las tareas pendientes"""
        print("\n✅ Gestión de tareas - ¡Mantengamos todo organizado!")
        
        tareas = self.progreso_usuario["lista_tareas"]
        if not tareas:
            print("\n📝 No tienes tareas registradas aún.")
            self.agregar_tareas_automaticas()
            tareas = self.progreso_usuario["lista_tareas"]
        
        print(f"\n📋 Tienes {len(tareas)} tareas registradas:")
        
        pendientes = [t for t in tareas if not t["completada"]]
        completadas = [t for t in tareas if t["completada"]]
        
        print(f"\n⏳ Pendientes ({len(pendientes)}):")
        for i, tarea in enumerate(pendientes, 1):
            print(f"  {i}. {tarea['descripcion']} - Prioridad: {tarea['prioridad']}")
        
        print(f"\n✅ Completadas ({len(completadas)}):")
        for i, tarea in enumerate(completadas, 1):
            print(f"  {i}. {tarea['descripcion']}")
        
        print("\n¿Qué te gustaría hacer?")
        print("1. Marcar tarea como completada")
        print("2. Agregar nueva tarea")
        print("3. Volver al menú principal")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            self.completar_tarea()
        elif opcion == "2":
            self.agregar_tarea_personalizada()
    
    def completar_tarea(self):
        """Marca una tarea como completada"""
        pendientes = [t for t in self.progreso_usuario["lista_tareas"] if not t["completada"]]
        
        if not pendientes:
            print("\n🎉 ¡Felicidades! No tienes tareas pendientes.")
            return
        
        print("\n¿Cuál tarea completaste?")
        for i, tarea in enumerate(pendientes, 1):
            print(f"{i}. {tarea['descripcion']}")
        
        try:
            indice = int(input("\nNúmero de tarea: ")) - 1
            if 0 <= indice < len(pendientes):
                pendientes[indice]["completada"] = True
                pendientes[indice]["fecha_completada"] = str(datetime.datetime.now())
                print(f"\n🎉 ¡Excelente! Tarea '{pendientes[indice]['descripcion']}' marcada como completada.")
            else:
                print("❌ Número de tarea inválido.")
        except ValueError:
            print("❌ Por favor ingresa un número válido.")
    
    def agregar_tarea_personalizada(self):
        """Permite agregar una tarea personalizada"""
        descripcion = input("\nDescripción de la nueva tarea: ")
        print("Prioridad (alta/media/baja): ")
        prioridad = input().lower()
        
        if prioridad not in ["alta", "media", "baja"]:
            prioridad = "media"
        
        nueva_tarea = {
            "descripcion": descripcion,
            "completada": False,
            "prioridad": prioridad,
            "fecha_creacion": str(datetime.datetime.now())
        }
        
        self.progreso_usuario["lista_tareas"].append(nueva_tarea)
        print(f"✅ Tarea '{descripcion}' agregada con prioridad {prioridad}.")
    
    def mostrar_resumen_completo(self):
        """Muestra un resumen completo y empático de toda la planificación"""
        print("\n" + "="*60)
        print("💒 RESUMEN COMPLETO DE TU BODA SOÑADA 💒")
        print("="*60)
        
        # Información personal
        info = self.progreso_usuario["informacion_personal"]
        if info:
            print(f"\n👫 PAREJA FELIZ:")
            print(f"   {info.get('nombre1', 'No especificado')} & {info.get('nombre2', 'No especificado')}")
            print(f"   Tiempo juntos: {info.get('tiempo_relacion', 'No especificado')}")
            if info.get('historia_amor'):
                print(f"   Su historia: {info['historia_amor']}")
        
        # Detalles de la boda
        detalles = self.progreso_usuario["detalles_boda"]
        if detalles:
            print(f"\n💍 DETALLES DE LA BODA:")
            print(f"   📅 Fecha: {detalles.get('fecha', 'Por definir')}")
            print(f"   ⛪ Ceremonia: {detalles.get('lugar_ceremonia', 'Por definir')}")
            print(f"   🎉 Recepción: {detalles.get('lugar_recepcion', 'Por definir')}")
            print(f"   ✨ Estilo: {detalles.get('estilo', 'Por definir')}")
            print(f"   👥 Invitados estimados: {detalles.get('numero_invitados', 'Por definir')}")
        
        # Presupuesto
        presupuesto = self.progreso_usuario["presupuesto"]
        if presupuesto:
            print(f"\n💰 PRESUPUESTO:")
            print(f"   Total: ${presupuesto.get('total', 0):,.2f}")
            print(f"   Lugar y catering: ${presupuesto.get('lugar_catering', 0):,.2f}")
            print(f"   Vestimenta: ${presupuesto.get('vestimenta', 0):,.2f}")
            print(f"   Fotografía: ${presupuesto.get('fotografia', 0):,.2f}")
        
        # Progreso de tareas
        tareas = self.progreso_usuario["lista_tareas"]
        if tareas:
            completadas = len([t for t in tareas if t["completada"]])
            total = len(tareas)
            porcentaje = (completadas / total * 100) if total > 0 else 0
            
            print(f"\n✅ PROGRESO DE PLANIFICACIÓN:")
            print(f"   Tareas completadas: {completadas}/{total} ({porcentaje:.1f}%)")
            
            if porcentaje < 30:
                print("   🌱 ¡Apenas comenzando! Cada paso cuenta.")
            elif porcentaje < 70:
                print("   🌿 ¡Buen progreso! Vas por buen camino.")
            else:
                print("   🌟 ¡Increíble! Ya casi tienes todo listo.")
        
        # Invitados
        invitados = self.progreso_usuario["invitados"]
        if invitados:
            confirmados = len([i for i in invitados if i["confirmacion"].lower() == "s"])
            print(f"\n👥 INVITADOS:")
            print(f"   Total en lista: {len(invitados)}")
            print(f"   Confirmados: {confirmados}")
        
        print("\n" + "="*60)
        print("💕 MENSAJE PERSONAL DE TU ASESOR IA:")
        print(f"Queridos {info.get('nombre1', '')} y {info.get('nombre2', '')},")
        print("Ha sido un honor acompañarlos en la planificación de su boda.")
        print("Cada detalle que hemos trabajado juntos refleja el amor que se tienen.")
        print("¡Su día especial será absolutamente mágico! 💫")
        print("\n🎊 ¡Que vivan los novios! 🎊")
        print("="*60)
        
        # Guardar automáticamente el resumen
        self.guardar_resumen_final()
    
    def guardar_resumen_final(self):
        """Guarda un resumen final en un archivo separado"""
        try:
            with open("resumen_boda_final.txt", "w", encoding="utf-8") as file:
                file.write("RESUMEN FINAL DE PLANIFICACIÓN DE BODA\n")
                file.write("="*50 + "\n\n")
                
                info = self.progreso_usuario["informacion_personal"]
                if info:
                    file.write(f"PAREJA: {info.get('nombre1', '')} & {info.get('nombre2', '')}\n")
                    file.write(f"TIEMPO JUNTOS: {info.get('tiempo_relacion', '')}\n\n")
                
                detalles = self.progreso_usuario["detalles_boda"]
                if detalles:
                    file.write("DETALLES DE LA BODA:\n")
                    file.write(f"Fecha: {detalles.get('fecha', 'Por definir')}\n")
                    file.write(f"Ceremonia: {detalles.get('lugar_ceremonia', 'Por definir')}\n")
                    file.write(f"Recepción: {detalles.get('lugar_recepcion', 'Por definir')}\n")
                    file.write(f"Estilo: {detalles.get('estilo', 'Por definir')}\n\n")
                
                file.write(f"Generado el: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
            
            print("\n💾 Resumen final guardado en 'resumen_boda_final.txt'")
        except Exception as e:
            print(f"❌ Error al guardar resumen: {e}")
    
    def ejecutar(self):
        """Función principal que ejecuta el asesor de bodas"""
        print("💒✨ ¡Bienvenidos a su Asesor de Bodas con Inteligencia Artificial! ✨💒")
        print("Estoy aquí para hacer que la planificación de su boda sea una experiencia mágica y sin estrés.")
        
        while True:
            self.mostrar_menu_principal()
            
            try:
                opcion = input("\n💕 ¿Qué te gustaría hacer hoy? (0-9): ")
                
                if opcion == "1":
                    self.recopilar_informacion_personal()
                elif opcion == "2":
                    self.planificar_detalles_boda()
                elif opcion == "3":
                    self.gestionar_presupuesto()
                elif opcion == "4":
                    self.gestionar_invitados()
                elif opcion == "5":
                    print("\n🏪 Gestión de proveedores (próximamente)")
                    print("Mientras tanto, te recomiendo investigar: fotógrafos, floristas, catering, música")
                elif opcion == "6":
                    print("\n📅 Cronograma (próximamente)")
                    print("Recuerda: reservar servicios 6-12 meses antes, invitaciones 2-3 meses antes")
                elif opcion == "7":
                    self.gestionar_tareas()
                elif opcion == "8":
                    self.mostrar_resumen_completo()
                elif opcion == "9":
                    self.guardar_progreso()
                elif opcion == "0":
                    print("\n💕 ¡Gracias por permitirme ser parte de su historia de amor!")
                    print("Recuerden que el día más importante es el que celebra su amor. 💒")
                    print("¡Nos vemos pronto para continuar planeando su boda perfecta! ✨")
                    self.guardar_progreso()
                    break
                else:
                    print("❌ Opción no válida. Por favor elige un número del 0 al 9.")
                
                input("\nPresiona Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n\n💾 Guardando progreso antes de salir...")
                self.guardar_progreso()
                print("¡Hasta la próxima! 👋")
                break
            except Exception as e:
                print(f"❌ Ocurrió un error: {e}")
                print("No te preocupes, tu progreso está a salvo. Intentemos de nuevo.")

# Crear y ejecutar el asesor de bodas
if __name__ == "__main__":
    asesor = AsesorBodaIA()
    asesor.ejecutar()