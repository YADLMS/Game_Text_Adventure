"""
Juego de aventuras de texto donde el jugador explora lugares, combate enemigos
y encuentra eventos aleatorios. Desarrollado sin técnicas avanzadas.
"""

import random
import time

# Variables globales
jugador = {
    "nombre": "",
    "nivel": 1,
    "experiencia": 0,
    "vida": 100,
    "vida_maxima": 100,
    "oro": 0,
    "inventario": [],
    "habilidades": ["Ataque básico"]
}

def mostrar_estado() -> None:
    """
    Muestra el estado actual del jugador.
    """

    print(f"\n{jugador['nombre']}, estás en el nivel {jugador['nivel']}.")
    print(
        f"vida: {jugador['vida']}/{jugador['vida_maxima']} | "
        f"Oro: {jugador['oro']} | Experiencia: {jugador['experiencia']}"
    )


lugares = [
    {
        "nombre": "Bosque Oscuro",
        "descripcion": "Te encuentras en un bosque denso y oscuro. Los árboles bloquean la luz del sol.",
        "enemigos": [
            {"nombre": "Lobo", "vida": 30, "ataque": 10, "experiencia": 20, "oro": 5},
            {"nombre": "Bandido", "vida": 40, "ataque": 15, "experiencia": 30, "oro": 10}
        ],
        "eventos": ["tesoro", "trampa"]
    },
    {
        "nombre": "Cueva Profunda",
        "descripcion": "Entras en una cueva húmeda y fría. Escuchas goteos en la distancia.",
        "enemigos": [
            {"nombre": "Murciélago Gigante", "vida": 25, "ataque": 8, "experiencia": 15, "oro": 3},
            {"nombre": "Trol", "vida": 60, "ataque": 20, "experiencia": 50, "oro": 20}
        ],
        "eventos": ["tesoro", "fuente mágica"]
    },
    {
        "nombre": "Aldea Abandonada",
        "descripcion": "Llegas a una aldea desierta. Las casas parecen haber sido abandonadas hace tiempo.",
        "enemigos": [
            {"nombre": "Fantasma", "vida": 35, "ataque": 12, "experiencia": 25, "oro": 8}
        ],
        "eventos": ["mercader", "quest"]
    },
    {
        "nombre": "Cima de la Montaña",
        "descripcion": "Alcanzas la cima de una montaña escarpada. El aire es frío y delgado aquí.",
        "enemigos": [
            {"nombre": "Águila Gigante", "vida": 45, "ataque": 18, "experiencia": 35, "oro": 15},
            {"nombre": "Yeti", "vida": 70, "ataque": 25, "experiencia": 60, "oro": 25}
        ],
        "eventos": ["vista panorámica", "santuario"]
    }
]

print("¡Bienvenido al Juego de Aventuras de Texto!")
jugador["nombre"] = input("Ingresa el nombre de tu personaje: ")

while True:
    print(f"\n{jugador['nombre']}, estás en el nivel {jugador['nivel']}.")
    print(
        f"vida: {jugador['vida']}/{jugador['vida_maxima']} | Oro: {jugador['oro']} | Experiencia: {jugador['experiencia']}")

    accion = input("¿Qué quieres hacer? (explorar/descansar/inventario/salir): ").lower()

    if accion == "explorar":
        lugar_actual = random.choice(lugares)
        print(f"\nHas llegado a: {lugar_actual['nombre']}")
        print(lugar_actual['descripcion'])

        if random.random() < 0.7:  # 70% de probabilidad de encuentro
            enemigo = random.choice(lugar_actual['enemigos'])
            print(f"\n¡Te enfrentas a un {enemigo['nombre']}!")

            while enemigo['vida'] > 0 and jugador['vida'] > 0:
                accion_combate = input("¿Qué quieres hacer? (atacar/huir): ").lower()
                if accion_combate == "atacar":
                    daño_jugador = random.randint(5, 15) + jugador['nivel'] * 2
                    enemigo['vida'] -= daño_jugador
                    print(f"Has infligido {daño_jugador} puntos de daño al {enemigo['nombre']}.")

                    if enemigo['vida'] <= 0:
                        print(f"¡Has derrotado al {enemigo['nombre']}!")
                        jugador['experiencia'] += enemigo['experiencia']
                        jugador['oro'] += enemigo['oro']
                        print(f"Ganaste {enemigo['experiencia']} de experiencia y {enemigo['oro']} de oro.")

                        if jugador['experiencia'] >= jugador['nivel'] * 100:
                            jugador['nivel'] += 1
                            jugador['vida_maxima'] += 20
                            jugador['vida'] = jugador['vida_maxima']
                            jugador['experiencia'] = 0
                            print(f"¡Has subido al nivel {jugador['nivel']}! Tu vida máxima ha aumentado.")
                    else:
                        daño_enemigo = random.randint(enemigo['ataque'] - 5, enemigo['ataque'] + 5)
                        jugador['vida'] -= daño_enemigo
                        print(f"El {enemigo['nombre']} te ha infligido {daño_enemigo} puntos de daño.")
                elif accion_combate == "huir":
                    if random.random() < 0.5:
                        print("Has logrado escapar.")
                        break
                    else:
                        print("No has podido escapar.")
                        daño_enemigo = random.randint(enemigo['ataque'] - 5, enemigo['ataque'] + 5)
                        jugador['vida'] -= daño_enemigo
                        print(f"El {enemigo['nombre']} te ha infligido {daño_enemigo} puntos de daño.")
                else:
                    print("Acción no válida. Pierdes tu turno.")
        else:
            evento = random.choice(lugar_actual['eventos'])
            if evento == "tesoro":
                oro_encontrado = random.randint(10, 50)
                jugador['oro'] += oro_encontrado
                print(f"¡Has encontrado un tesoro! Ganas {oro_encontrado} de oro.")
            elif evento == "trampa":
                daño_trampa = random.randint(5, 15)
                jugador['vida'] -= daño_trampa
                print(f"¡Has caído en una trampa! Pierdes {daño_trampa} puntos de vida.")
            elif evento == "fuente mágica":
                curacion = random.randint(20, 40)
                jugador['vida'] = min(jugador['vida'] + curacion, jugador['vida_maxima'])
                print(f"Has encontrado una fuente mágica. Te curas {curacion} puntos de vida.")
            elif evento == "mercader":
                print("Te encuentras con un mercader ambulante.")
                if jugador['oro'] >= 50:
                    comprar = input("¿Quieres comprar una poción de vida por 50 de oro? (si/no): ").lower()
                    if comprar == "si":
                        jugador['oro'] -= 50
                        jugador['inventario'].append("Poción de vida")
                        print("Has comprado una poción de vida.")
                    else:
                        print("Decides no comprar nada.")
                else:
                    print("No tienes suficiente oro para comprar.")
            elif evento == "quest":
                print("Un aldeano te pide ayuda para encontrar un objeto perdido.")
                buscar = input("¿Quieres ayudarlo? (si/no): ").lower()
                if buscar == "si":
                    if random.random() < 0.6:
                        recompensa = random.randint(30, 80)
                        jugador['oro'] += recompensa
                        print(f"¡Has encontrado el objeto! El aldeano te recompensa con {recompensa} de oro.")
                    else:
                        print("No logras encontrar el objeto. El aldeano se decepciona.")
                else:
                    print("Decides no ayudar al aldeano.")
            elif evento == "vista panorámica":
                print("Disfrutas de una vista impresionante. Te sientes renovado.")
                jugador['experiencia'] += 10
                print("Ganas 10 puntos de experiencia.")
            elif evento == "santuario":
                print("Encuentras un antiguo santuario. Sientes una presencia mística.")
                nueva_habilidad = "Bendición divina"
                if nueva_habilidad not in jugador['habilidades']:
                    jugador['habilidades'].append(nueva_habilidad)
                    print(f"Has aprendido una nueva habilidad: {nueva_habilidad}")
                else:
                    jugador['experiencia'] += 20
                    print("Ya conocías la habilidad del santuario. Ganas 20 puntos de experiencia.")

    elif accion == "descansar":
        descanso = random.randint(10, 20)
        jugador['vida'] = min(jugador['vida'] + descanso, jugador['vida_maxima'])
        print(f"Has descansado y recuperado {descanso} puntos de vida.")
        time.sleep(1)

    elif accion == "inventario":
        print("\nTu inventario:")
        for item in jugador['inventario']:
            print(f"- {item}")
        if "Poción de vida" in jugador['inventario']:
            usar_pocion = input("¿Quieres usar una poción de vida? (si/no): ").lower()
            if usar_pocion == "si":
                jugador['inventario'].remove("Poción de vida")
                curacion = 50
                jugador['vida'] = min(jugador['vida'] + curacion, jugador['vida_maxima'])
                print(f"Has usado una poción de vida. Te curas {curacion} puntos de vida.")

    elif accion == "salir":
        print("Gracias por jugar. ¡Hasta la próxima aventura!")
        break

    else:
        print("Acción no válida. Intenta de nuevo.")

    if jugador['vida'] <= 0:
        print("Has perdido toda tu vida. ¡Juego terminado!")
        break

    time.sleep(1)
