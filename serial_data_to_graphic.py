import serial
import matplotlib.pyplot as plt
import time

# Configuration du port série 
ser = serial.Serial("COM6", 9600, timeout=1)

# Listes pour stocker les données
x_data, y_data, z_data = [], [], []
time_data = []

# Configuration du graphique
plt.ion()  # Mode interactif
fig, ax = plt.subplots()
ax.set_title("Données IMU (Accélération)")
ax.set_xlabel("Temps (s)")
ax.set_ylabel("Accélération (m/s²)")

start_time = time.time()

while True:
    try:
        # Lire une ligne de l'Arduino
        line = ser.readline().decode("utf-8").strip()
        if "Accélération" in line:
            values = line.split(": ")[1].split(", ")
            ax_val, ay_val, az_val = map(float, values)

            # Ajouter les nouvelles valeurs
            current_time = time.time() - start_time
            time_data.append(current_time)
            x_data.append(ax_val)
            y_data.append(ay_val)
            z_data.append(az_val)

            # Limiter le nombre de points affichés
            if len(time_data) > 50:
                time_data.pop(0)
                x_data.pop(0)
                y_data.pop(0)
                z_data.pop(0)

            # Mettre à jour le graphique
            ax.clear()
            ax.plot(time_data, x_data, label="X")
            ax.plot(time_data, y_data, label="Y")
            ax.plot(time_data, z_data, label="Z")
            ax.legend()
            plt.pause(0.01)

    except KeyboardInterrupt:
        print("\nArrêt du programme.")
        ser.close()
        break

