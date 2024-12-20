import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import math

# Menghubungkan ke CoppeliaSim
client = RemoteAPIClient()
sim = client.require('sim')

left_motor = sim.getObject('/PioneerP3DX/leftMotor')
right_motor = sim.getObject('/PioneerP3DX/rightMotor')

# Fungsi untuk mengatur kecepatan motor
def set_motor_speed(left_speed, right_speed):
    sim.setJointTargetVelocity(left_motor, left_speed)
    sim.setJointTargetVelocity(right_motor, right_speed)

sim.setStepping(True)
sim.startSimulation()

left_speed = 2
right_speed = 2
durasi_lurus = 18.5  
turn_duration = 1.85  
wheel_diameter = 50  

wheel_radius = wheel_diameter / 100 / 2  # Konversi ke meter
wheel_circumference = 2 * math.pi * wheel_radius  # Lingkaran roda dalam meter

steps = int(durasi_lurus * 10)  # Asumsi 10 langkah per detik
turn_steps = int(turn_duration * 10)  # Langkah untuk belokan

distance_traveled = 0

for i in range(4):  # Mengulangi pola lurus → belok sebanyak 4 kali
    # Gerakan lurus
    print(f"--- Hasil Gerakan Lurus ke-{i+1} ---")
    for step in range(steps):
        set_motor_speed(left_speed, right_speed)
        sim.step()
        
        # Membaca kecepatan joint motor
        left_velocity = sim.getJointVelocity(left_motor)
        right_velocity = sim.getJointVelocity(right_motor)

        # Menghitung jarak yang ditempuh dalam langkah ini
        left_distance = left_velocity * (1/10) * wheel_circumference
        right_distance = right_velocity * (1/10) * wheel_circumference

        # Akumulasi jarak tempuh
        distance_traveled += (left_distance + right_distance) / 2  # Rata-rata jarak

        # Hanya menampilkan setiap 10 langkah
        if step % 10 == 0 or step == steps - 1:
            print(f"Langkah {step+1}/{steps} - Distance Traveled: {distance_traveled:.2f} m")
    
    # Gerakan belok
    print(f"--- Hasil Belokan ke-{i+1} ---")
    for step in range(turn_steps):
        set_motor_speed(5, -2) 
        sim.step()

        # Membaca kecepatan joint motor
        left_velocity = sim.getJointVelocity(left_motor)
        right_velocity = sim.getJointVelocity(right_motor)

        # Menghitung jarak yang ditempuh dalam langkah ini
        left_distance = left_velocity * (1/10) * wheel_circumference
        right_distance = right_velocity * (1/10) * wheel_circumference

        # Akumulasi jarak tempuh
        distance_traveled += (left_distance + right_distance) / 2

        # Hanya menampilkan setiap 10 langkah
        if step % 10 == 0 or step == turn_steps - 1:
            print(f"Langkah {step+1}/{turn_steps} - Distance Traveled: {distance_traveled:.2f} m")

print("\n Hasil Akhir ")
print(f"Left Motor Velocity: {left_velocity:.2f} rad/s")
print(f"Right Motor Velocity: {right_velocity:.2f} rad/s")
rotations = distance_traveled / wheel_circumference
print(f"Wheel Rotations: {rotations:.2f}")
print(f"Total Distance Traveled: {distance_traveled:.2f} m")

sim.stopSimulation()
