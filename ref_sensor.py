import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# Menghubungkan ke CoppeliaSim
client = RemoteAPIClient()
sim    = client.require('sim')

# Mendapatkan handle sensor ultrasonik
ultrasonic_sensor = sim.getObject('/PioneerP3DX/ultrasonicSensor[2]')

# Memulai simulasi
sim.setStepping(True)
sim.startSimulation()

try:
    for _ in range(100):  # Baca data sensor beberapa kali
        # Baca data dari sensor ultrasonik
        detection_state, distance, detected_point, detected_object_handle, detected_surface_normal_vector = sim.readProximitySensor(ultrasonic_sensor)
        
        if detection_state:
            # Jika ada objek terdeteksi, cetak jaraknya
            print(f"Jarak ke objek terdekat: {distance:.2f} meter")
        else:
            # Jika tidak ada objek, tampilkan pesan
            print("Tidak ada objek di depan sensor")
        
        sim.step()
        time.sleep(0.1)  # Sesuaikan frekuensi pembacaan data
finally:
    sim.stopSimulation()
