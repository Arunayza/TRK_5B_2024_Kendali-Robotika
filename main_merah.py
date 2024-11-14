import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import math

# Menghubungkan ke CoppeliaSim
client = RemoteAPIClient()
sim = client.require('sim')

# Mendapatkan handle untuk motor kiri, motor kanan, dan sensor ultrasonik
left_motor = sim.getObject('/PioneerP3DX/leftMotor')
right_motor = sim.getObject('/PioneerP3DX/rightMotor')

sensors = [sim.getObject(f'/PioneerP3DX/ultrasonicSensor[{i}]') for i in range(8)]

# Fungsi untuk mengatur kecepatan motor
def set_motor_speed(left_speed, right_speed):
    sim.setJointTargetVelocity(left_motor, left_speed)
    sim.setJointTargetVelocity(right_motor, right_speed)

# Fungsi untuk membaca jarak dari sensor ultrasonik
def get_sensor_distance(sensor_handle):
    return sim.readProximitySensor(sensor_handle)[1] * 100  # Mengonversi dari meter ke cm

# Memulai simulasi
sim.setStepping(True)
sim.startSimulation()

# Parameter kecepatan dan durasi
left_speed = 2
right_speed = 2
wheel_diameter = 47  # diameter roda dalam cm
wheel_radius = wheel_diameter / 100 / 2  # konversi ke meter
wheel_circumference = 2 * math.pi * wheel_radius  # lingkaran roda dalam meter
distance_traveled = 0  # Inisialisasi jarak tempuh

# Tahap 1: Maju selama beberapa detik
move_duration = 8  # waktu bergerak maju dalam detik
steps = int(move_duration * 10)  # Asumsi 10 langkah per detik

try:
    # Tahap 1: Robot bergerak maju selama beberapa detik
    print("Tahap 1: Robot bergerak maju...")
    for _ in range(steps):
        set_motor_speed(left_speed, right_speed)
        sim.step()
    
    # Tahap 2: Putar balik ke kiri
    print("Tahap 2: Robot berputar balik ke kiri...")
    turn_duration = 3  # durasi putar balik
    turn_steps = int(turn_duration * 10)

    for _ in range(turn_steps):
        set_motor_speed(-2, 2)  # Motor kiri mundur, motor kanan maju untuk belok kiri
        sim.step()

    # Tahap 3: Robot bergerak maju selama beberapa detik
    print("Tahap 3: Robot bergerak maju...")
    for _ in range(steps):
        set_motor_speed(left_speed, right_speed)
        sim.step()
    
    # Tahap 4: Putar balik ke kiri
    print("Tahap 4: Robot berputar balik ke kiri...")
    turn_duration = 3  # durasi putar balik
    turn_steps = int(turn_duration * 10)

    for _ in range(turn_steps):
        set_motor_speed(-2, 2)  # Motor kiri mundur, motor kanan maju untuk belok kiri
        sim.step()
    
    # Tahap 5: Robot bergerak maju hingga sensor 3 dan 4 mendeteksi objek kurang dari 10 cm
    print("Tahap 5: Robot bergerak maju sampai sensor 3 dan 4 mendeteksi objek kurang dari 10 cm...")
    while True:
        # Membaca jarak dari sensor 3 dan 4
        distance_3 = get_sensor_distance(sensors[3])
        distance_4 = get_sensor_distance(sensors[4])

        # Mengecek jika keduanya mendeteksi objek kurang dari 20 cm
        if distance_3 < 20 and distance_4 < 20:
            print("Objek terdeteksi di depan, robot akan belok kiri...")
            turn_duration = 3  # durasi putar balik
            turn_steps = int(turn_duration * 10)

            for _ in range(turn_steps):
                set_motor_speed(2, -1)  # Motor kiri maju, motor kanan mundur untuk belok kiri
                sim.step()
    

finally:
    sim.stopSimulation()

