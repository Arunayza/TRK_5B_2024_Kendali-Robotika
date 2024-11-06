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
left_speed = 2
# right_speed = float(input("Masukkan kecepatan motor kanan (rad/s): "))
right_speed = 2
duration = 9.6
turn_duration = 1.85
# float(input("Berapa lama robot harus bergerak (detik)? "))
# diameter ban berdasarkan absen
wheel_diameter = 30
# float(input("Masukkan diameter roda (cm): "))
# Hitung lingkaran roda
wheel_radius = wheel_diameter / 100 / 2  # Konversi ke meter
wheel_circumference = 2 * math.pi * wheel_radius  # Lingkaran roda dalam meter
# Menghitung jumlah langkah berdasarkan durasi
steps = int(duration * 10)  # Asumsi 10 langkah per detik
# Inisialisasi jarak tempuh
distance_traveled = 0

for _ in range(4):
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

    turn_steps = int(turn_duration * 10)
    for _ in range(turn_steps):
        set_motor_speed(5, -2)  # Motor kiri berhenti, motor kanan berjalan
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
        
sim.stopSimulation()