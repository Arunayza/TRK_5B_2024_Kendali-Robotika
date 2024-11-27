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

left_speed = 2  # Kecepatan motor kiri untuk gerakan lurus
right_speed = 2  # Kecepatan motor kanan untuk gerakan lurus
duration_lurus = 10  # Durasi untuk bergerak lurus dalam detik
duration_lurus2 = 5  # Durasi untuk bergerak lurus dalam detik
duration_lurus3 = 14  # Durasi untuk bergerak lurus dalam detik
duration_lurus4 = 20
duration_lurus5 = 25
duration_lurus6 = 32
duration_lurus7 = 27
turn_duration = 3  # Durasi untuk belok dalam detik
turn_duration2 = 2.8  # Durasi untuk belok dalam detik
turn_duration3 = 3.5  # Durasi untuk belok dalam detik
wheel_diameter = 51  # Diameter roda dalam cm

wheel_radius = wheel_diameter / 100 / 2  # Konversi ke meter
wheel_circumference = 2 * math.pi * wheel_radius  # Lingkaran roda dalam meter

steps_lurus = int(duration_lurus * 10)  # Asumsi 10 langkah per detik
steps_belok = int(turn_duration * 10)  # Langkah untuk belokan
steps_belok2 = int(turn_duration2 * 10)  # Langkah untuk belokan
steps_belok3 = int(turn_duration3 * 10)  # Langkah untuk belokan
steps_lurus2 = int(duration_lurus2 * 10)  # Asumsi 10 langkah per detik
steps_lurus3 = int(duration_lurus3 * 10)  # Asumsi 10 langkah per detik
steps_lurus4 = int(duration_lurus4 * 10)  # Asumsi 10 langkah per detik
steps_lurus5 = int(duration_lurus5 * 10)  # Asumsi 10 langkah per detik
steps_lurus6 = int(duration_lurus6 * 10)  # Asumsi 10 langkah per detik
steps_lurus7 = int(duration_lurus7 * 10)  # Asumsi 10 langkah per detik
# Inisialisasi jarak tempuh
distance_traveled = 0

for i in range(2):  # Mengulangi pola lurus → belok kiri sebanyak 2 kali
    # Gerakan lurus
    print(f"\n===> Hasil Gerakan Lurus ke-{i+1} <===")
    for step in range(steps_lurus):
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

        # Hanya menampilkan setiap 5 langkah
        if step % 5 == 0 or step == steps_lurus - 1:
            print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")
    
    # Gerakan belok kiri
    print(f"\n===> Hasil Belokan Kiri ke-{i+1} <===")
    for step in range(steps_belok):
        set_motor_speed(-2, 2)  # Set kecepatan untuk belok kiri
        sim.step()

        # Membaca kecepatan joint motor
        left_velocity = sim.getJointVelocity(left_motor)
        right_velocity = sim.getJointVelocity(right_motor)

        # Menghitung jarak yang ditempuh dalam langkah ini
        left_distance = left_velocity * (1/10) * wheel_circumference
        right_distance = right_velocity * (1/10) * wheel_circumference

        # Akumulasi jarak tempuh
        distance_traveled += (left_distance + right_distance) / 2

        # Hanya menampilkan setiap 5 langkah
        if step % 5 == 0 or step == steps_belok - 1:
            print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")
    
# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")


# Gerakan belok kanan
print(f"\n===> Hasil Belokan Kanan <===")
for step in range(steps_belok):
    set_motor_speed(2, -2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")


print(f"\n===> Hasil Gerakan Lurus ke-{i+1} <===")
for step in range(steps_lurus):
    set_motor_speed(left_speed,right_speed)
    sim.step()
        
        # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

        # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

        # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2  # Rata-rata jarak

        # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Gerakan Lurus ke-{i+1} <===")
for step in range(steps_lurus2):
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

        # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> STOP <===")
for step in range(steps_belok):
    set_motor_speed(0, 0)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")


print(f"\n===> Hasil Belokan Kanan <===")
for step in range(steps_belok):
    set_motor_speed(2, -2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belokan Kanan <===")
for step in range(steps_belok):
    set_motor_speed(2, -2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")
    
# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus3):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belokan KIRI <===")
for step in range(steps_belok):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belokan KIRI <===")
for step in range(steps_belok2):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")


# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus3):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belokan Kanan <===")
for step in range(steps_belok):
    set_motor_speed(2, -2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus4):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belokan Kanan <===")
for step in range(steps_belok):
    set_motor_speed(2, -2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus2):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===>STOP <===")
for step in range(steps_belok):
    set_motor_speed(0, 0)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")


print(f"\n===> Hasil Belokan KIRI <===")
for step in range(steps_belok3):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")


print(f"\n===> Hasil Belokan KIRI <===")
for step in range(steps_belok):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus2):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belokan KIRI <===")
for step in range(steps_belok):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")


print(f"\n===> Hasil Belokan KIRI <===")
for step in range(steps_belok):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus5):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belokan KIRI <===")
for step in range(steps_belok):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus6):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belokan KIRI <===")
for step in range(steps_belok):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus7):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belokan Kiri <===")
for step in range(steps_belok):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
for step in range(steps_lurus):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belokan Kiri <===")
for step in range(steps_belok):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belok} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
step_lurus2 = 100
for step in range(steps_lurus2):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurus2} - Distance Traveled: {distance_traveled:.2f} m")

# Gerakan belok kiri setelah gerakan lurus terakhir 
print(f"\n===> Hasil Belok kiri Setelah Gerakan Lurus <===")
steps_belokxx = 60
for step in range(steps_belokxx):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belokxx} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
steps_lurusddd = 55
for step in range(steps_lurusddd):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurusddd} - Distance Traveled: {distance_traveled:.2f} m")

# Gerakan belok kiri setelah gerakan lurus terakhir 
print(f"\n===> Hasil Belok kanan Setelah Gerakan Lurus <===")
steps_belokjjj = 30
for step in range(steps_belokjjj):
    set_motor_speed(2, -2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belokjjj} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
steps_lurusppp = 220
for step in range(steps_lurusppp):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurusppp} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belok kanan Setelah Gerakan Lurus <===")
steps_belokjjj = 30
for step in range(steps_belokjjj):
    set_motor_speed(2, -2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_belokjjj} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
steps_lurusppp = 160
for step in range(steps_lurusppp):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurusppp} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belok Kiri <===")
steps_beloklol = 30
for step in range(steps_beloklol):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_beloklol} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
steps_lurusppp = 130
for step in range(steps_lurusppp):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurusppp} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belok Kiri <===")
steps_beloklol = 30
for step in range(steps_beloklol):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_beloklol} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
steps_lurusppp = 139
for step in range(steps_lurusppp):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurusppp} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belok Kiri <===")
steps_beloklols = 60
for step in range(steps_beloklols):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_beloklols} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
steps_lurusppp = 143
for step in range(steps_lurusppp):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurusppp} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belok Kanan <===")
steps_beloklolf = 30
for step in range(steps_beloklolf):
    set_motor_speed(2, -2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_beloklolf} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
steps_lurusppp = 130
for step in range(steps_lurusppp):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurusppp} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belok Kiri <===")
steps_beloklolT = 30
for step in range(steps_beloklolT):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_beloklolT} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus Tambahan <===")
steps_lurusHHH = 100
for step in range(steps_lurusHHH):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurusHHH} - Distance Traveled: {distance_traveled:.2f} m")

print(f"\n===> Hasil Belok Kiri <===")
steps_beloklolTS = 28
for step in range(steps_beloklolTS):
    set_motor_speed(-2, 2)  # Set kecepatan untuk belok kanan
    sim.step()

    # Membaca kecepatan joint motor
    left_velocity = sim.getJointVelocity(left_motor)
    right_velocity = sim.getJointVelocity(right_motor)

    # Menghitung jarak yang ditempuh dalam langkah ini
    left_distance = left_velocity * (1/10) * wheel_circumference
    right_distance = right_velocity * (1/10) * wheel_circumference

    # Akumulasi jarak tempuh
    distance_traveled += (left_distance + right_distance) / 2

    # Menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_belok - 1:
        print(f"Langkah {step+1}/{steps_beloklolTS} - Distance Traveled: {distance_traveled:.2f} m")

# Tambahan gerakan lurus
print(f"\n===> Hasil Gerakan Lurus dan FINISH <===")
steps_lurusTT = 115
for step in range(steps_lurusTT):
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

    # Hanya menampilkan setiap 5 langkah
    if step % 5 == 0 or step == steps_lurus - 1:
        print(f"Langkah {step+1}/{steps_lurusTT} - Distance Traveled: {distance_traveled:.2f} m")


print("\n#==========| Hasil Akhir |==========#")
print("|"f"Left Motor Velocity: {left_velocity:.2f} rad/s    |")
print("|"f"Right Motor Velocity: {right_velocity:.2f} rad/s  |")
rotations = distance_traveled / wheel_circumference
print("|"f"Wheel Rotations: {rotations:.2f}            |")
print("|"f"Total Distance Traveled: {distance_traveled:.2f} m  |")
print("#==========|*|==========#")
sim.stopSimulation()
