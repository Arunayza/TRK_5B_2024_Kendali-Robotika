import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import math

# Menghubungkan ke CoppeliaSim
client = RemoteAPIClient()
sim = client.require('sim')

# Mendapatkan handle untuk motor kiri dan kanan
left_motor = sim.getObject('/PioneerP3DX/leftMotor')
right_motor = sim.getObject('/PioneerP3DX/rightMotor')

# Fungsi untuk mengatur kecepatan motor
def set_motor_speed(left_speed, right_speed):
    sim.setJointTargetVelocity(left_motor, left_speed)
    sim.setJointTargetVelocity(right_motor, right_speed)

# Memulai simulasi
sim.setStepping(True)
sim.startSimulation()

# Input dari pengguna
# left_speed = float(input("Masukkan kecepatan motor kiri (rad/s): "))
left_speed = 4.15
# right_speed = float(input("Masukkan kecepatan motor kanan (rad/s): "))
right_speed = 4.15
turn_duration = 1.42  # Durasi untuk belok kanan (dalam detik)
straight_duration = 6.98  # Durasi untuk maju (dalam detik)
wheel_diameter = 28  # Diameter roda dalam cm
# float(input("Berapa lama robot harus bergerak (detik)? "))

# float(input("Masukkan diameter roda (cm): "))

# Hitung lingkaran roda
wheel_radius = wheel_diameter / 100 / 2  # Konversi ke meter
wheel_circumference = 2 * math.pi * wheel_radius  # Lingkaran roda dalam meter


# Inisialisasi jarak tempuh
distance_traveled = 0
def move_forward(duration, left_speed, right_speed):
    steps = int(duration * 10)  # Asumsi 10 langkah per detik
    distance_traveled = 0  # Inisialisasi jarak tempuh
    for _ in range(steps):
        set_motor_speed(left_speed, right_speed)
        sim.step()
        
        # Membaca kecepatan joint motor
        left_velocity = sim.getJointVelocity(left_motor)
        right_velocity = sim.getJointVelocity(right_motor)

        # Menghitung jarak yang ditempuh dalam langkah ini
        left_distance = left_velocity * (1/10) * wheel_circumference  # (1/10) untuk konversi dt
        right_distance = right_velocity * (1/10) * wheel_circumference

        # Akumulasi jarak tempuh
        distance_traveled += (left_distance + right_distance) / 2  # Rata-rata jarak

        # Hitung jumlah putaran
        rotations = distance_traveled / wheel_circumference

        # Menampilkan hasil
        print(f"Left Motor Velocity: {left_velocity:.2f} rad/s")
        print(f"Right Motor Velocity: {right_velocity:.2f} rad/s")
        print(f"Distance Traveled: {distance_traveled:.2f} m")
        print(f"Wheel Rotations: {rotations:.2f}")
    return distance_traveled


def turn_right(duration, left_turn_speed, right_turn_speed):
    steps = int(duration * 10.4)  # Asumsi 10 langkah per detik
    for _ in range(steps):
        set_motor_speed(left_turn_speed, right_turn_speed)  # Kecepatan berbeda untuk belok kanan
        sim.step()
        # Menampilkan status belok kanan
        print("Turning right...")

# Loop untuk maju dan belok secara bergantian
total_distance = 0

try:
    # Maju pertama
    print("Moving forward...")
    total_distance += move_forward(straight_duration, left_speed, right_speed)
    
    # Belok kanan pertama
    print("Turning right...")
    turn_right(turn_duration, left_speed, -right_speed)

    # Maju kedua
    print("Moving forward...")
    total_distance += move_forward(straight_duration, left_speed, right_speed)

    # Belok kanan kedua
    print("Turning right...")
    turn_right(turn_duration, left_speed, -right_speed)

    # Maju ketiga
    print("Moving forward...")
    total_distance += move_forward(straight_duration, left_speed, right_speed)
    
    # Belok kanan ketiga
    print("Turning right...")
    turn_right(turn_duration, left_speed, -right_speed)

    # Maju keempat
    print("Moving forward...")
    total_distance += move_forward(straight_duration, left_speed, right_speed)
    
    # Belok kanan terakhir
    print("Turning right...")
    turn_right(turn_duration, left_speed, -right_speed)

    print(f"Total Distance Traveled: {total_distance:.2f} m")

finally:
    # Menghentikan simulasi
    sim.stopSimulation()


sim.stopSimulation()