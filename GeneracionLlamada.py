import random

def main():
    # Pedir los parámetros de generación
    entrada = input("Cantidad de llamadas a generar [30000]: ").strip()
    ll = 30000 if not entrada else int(entrada)

    entrada = input("Cantidad de plantas [75]: ").strip()
    p = 75 if not entrada else int(entrada)

    entrada = input("Tiempo de movimiento (Tm en segundos) [1]: ").strip()
    tm = 1 if not entrada else int(entrada)

    entrada = input("Tiempo de parada (Tp en segundos) [5]: ").strip()
    tp = 5 if not entrada else int(entrada)

    entrada = input("Lapso máximo entre llamadas en segundos [10]: ").strip()
    mt = 10 if not entrada else int(entrada)

    entrada = input("Porcentaje de momentos pico [70]: ").strip()
    sr = 70 if not entrada else int(entrada)

    r = random.Random(42)  # Semilla fija para obtener consistencia
    rr = sr / 100

    # Reporta parámetros de generación
    print(f"\nSe crean {ll} llamadas para {p} plantas, con Tm= {tm} y Tp= {tp}")
    print(f"Tiempo medio entre llamadas {mt // 2} segundos. Porcentaje de momentos pico {100 * rr}%\n")

    with open("llamadas.txt", "w") as f:
        # Graba la primera línea del archivo
        f.write(f"{tm}, {tp}\n")

        t = 1  # La simulación comienza en el tic 1
        for _ in range(ll):
            # En el sr% de las llamadas el tiempo avanza un tic. En el resto avanza un promedio de mt/2 tics
            if r.random() > rr:
                t += r.randint(0, mt - 1)  # equivalente a r.nextInt(mt) en Java
            t += 1

            o = r.randint(0, p - 1)  # Planta de origen aleatoria (equivalente a r.nextLong(p))
            d = r.randint(0, p - 1)  # Planta de destino aleatoria
            while d == o:
                d = r.randint(0, p - 1)  # El destino no puede ser igual al origen

            f.write(f"{t}, {o}, {d}\n")

if __name__ == "__main__":
    main()