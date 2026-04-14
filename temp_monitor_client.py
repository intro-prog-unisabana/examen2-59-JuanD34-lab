# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor


def main():
    # TODO: Pedir el nombre del archivo al usuario usando input()
    filename = input("Enter the filename:\n").strip()
    # TODO: Abrir el archivo y leer el numero de lecturas n
    with open(filename, "r") as f:
        n = int(f.readline().strip())
    # TODO: Crear el monitor usando temp_monitor.init(n)
    monitor = temp_monitor.init(n)
    # TODO: Leer las n temperaturas y agregarlas con temp_monitor.add_reading()
    for _ in range(n):
        temp = float(f.readline().strip())
        temp_monitor.add_reading(monitor, temp)
    # TODO: Imprimir la racha creciente mas larga
    #       usando temp_monitor.longest_rising_streak()
    streak = temp_monitor.longest_rising_streak(monitor)
    print(f"longest rising streak: {streak}")

    pass


if __name__ == "__main__":
    main()
