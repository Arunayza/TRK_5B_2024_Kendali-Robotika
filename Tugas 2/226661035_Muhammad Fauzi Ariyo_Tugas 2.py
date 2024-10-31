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

# Parameter awal
left_speed = -3
right_speed = -3
duration = 2.8
wheel_diameter = 35

# Hitung lingkaran roda
wheel_radius = wheel_diameter / 100 / 2  # Konversi ke meter
wheel_circumference = 2 * math.pi * wheel_radius  # Lingkaran roda dalam meter

# Menghitung jumlah langkah berdasarkan durasi
steps = int(duration * 50)  # Asumsi 10 langkah per detik

# Fungsi untuk maju sejumlah blok tertentu
def move_forward(steps):
    global left_speed, right_speed
    distance_traveled = 0  # Reset jarak tempuh setiap kali maju

    for step in range(steps):
        set_motor_speed(left_speed, right_speed)
        sim.step()

        # Membaca kecepatan joint motor
        left_velocity = sim.getJointVelocity(left_motor)
        right_velocity = sim.getJointVelocity(right_motor)

        # Menghitung jarak yang ditempuh dalam langkah ini
        left_distance = left_velocity * (1 / 10) * wheel_circumference
        right_distance = right_velocity * (1 / 10) * wheel_circumference

        # Akumulasi jarak tempuh
        distance_traveled += (left_distance + right_distance) / 2

        print(f"Left Motor Velocity: {left_velocity:.2f} rad/s")
        print(f"Right Motor Velocity: {right_velocity:.2f} rad/s")
        print(f"Distance Traveled: {distance_traveled:.2f} m")

# Fungsi untuk maju dengan jarak tambahan
def move_forward1(steps1):
    global left_speed, right_speed
    distance_traveled = 0  # Reset jarak tempuh setiap kali maju
    extra_distance = 0.1  # Jarak tambahan yang ingin ditambahkan

    for step in range(steps1):
        set_motor_speed(left_speed, right_speed)
        sim.step()

        # Membaca kecepatan joint motor
        left_velocity = sim.getJointVelocity(left_motor)
        right_velocity = sim.getJointVelocity(right_motor)

        # Koreksi jika ada perbedaan kecil dalam kecepatan
        if abs(left_velocity - right_velocity) > 1:
            if left_velocity > right_velocity:
                left_speed -= 0.00000000000000000000000000001
            else:
                right_speed -= 0.00000000000000000000000000001

        # Menghitung jarak yang ditempuh dalam langkah ini
        left_distance = left_velocity * (1 / 10) * wheel_circumference
        right_distance = right_velocity * (1 / 10) * wheel_circumference

        # Akumulasi jarak tempuh
        distance_traveled += (left_distance + right_distance) / 2

        print(f"Left Motor Velocity: {left_velocity:.2f} rad/s")
        print(f"Right Motor Velocity: {right_velocity:.2f} rad/s")
        print(f"Distance Traveled: {distance_traveled:.2f} m")

    # Menambahkan jarak ekstra setelah selesai
    distance_traveled += extra_distance
    print(f"Distance Traveled after adding extra distance: {distance_traveled:.2f} m")

# Fungsi untuk belok kanan 90 derajat
def turn_right():
    turn_duration = 1.45  # Sesuaikan agar mencapai 90 derajat yang lebih tepat
    turn_steps = int(turn_duration * 20.1)  # Sesuaikan dengan frekuensi langkah
    for _ in range(turn_steps):
        set_motor_speed(2, -2)  # Kecepatan lebih rendah untuk akurasi belokan
        sim.step()

# Jalankan urutan pergerakan
# Maju 4 blok pertama
move_forward(steps)

# Belok kanan pertama
set_motor_speed(0, 0)
sim.step()
turn_right()


# Maju 4 blok kedua dengan jarak tambahan
steps1 = steps + 2  # Misalnya menambahkan 10 langkah lebih banyak
move_forward1(steps1)

# Belok kanan kedua
set_motor_speed(0, 0)
sim.step()
turn_right()

# Maju 4 blok ketiga
move_forward1(steps1)

# Belok kanan ketiga untuk menghadap ke arah awal
set_motor_speed(0, 0)
sim.step()
turn_right()

move_forward1(steps1)

set_motor_speed(0, 0)
sim.step()
turn_right()


# Menghentikan simulasi
sim.stopSimulation()
