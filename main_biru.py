import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import math

# Menghubungkan ke CoppeliaSim
client = RemoteAPIClient()
sim = client.require('sim')

# Mendapatkan handle untuk motor kiri dan kanan
left_motor = sim.getObject('/PioneerP3DX/leftMotor')
right_motor = sim.getObject('/PioneerP3DX/rightMotor')

# Mendapatkan handle untuk sensor jarak
left_sensor = sim.getObject('/PioneerP3DX/ultrasonicSensor[0]')
front_sensor = sim.getObject('/PioneerP3DX/ultrasonicSensor[3]')

# Fungsi untuk mengatur kecepatan motor
def set_motor_speed(left_speed, right_speed):
    sim.setJointTargetVelocity(left_motor, left_speed)
    sim.setJointTargetVelocity(right_motor, right_speed)

# Fungsi untuk membaca sensor jarak
def read_sensor(sensor):
    detection_state, detected_distance, _, _, _ = sim.readProximitySensor(sensor)
    if detection_state:
        return detected_distance  # Mengembalikan jarak jika ada deteksi
    else:
        return None  # Tidak ada deteksi

# Memulai simulasi
sim.setStepping(True)
sim.startSimulation()

# Parameter
wall_distance = 0.2  # Jarak yang diinginkan dari dinding (dalam meter)
frontwall_distance = 0.3
base_speed = 5  # Kecepatan dasar motor
turning_speed = 3  # Kecepatan untuk berbelok
distance_tolerance = 0.05  # Toleransi jarak dari dinding (5 cm)

# PID parameters
Kp = 20.0  # Proportional gain
Ki = 0.2   # Integral gain
Kd = 3.0   # Derivative gain

# Initialize error values
prev_error = 0
integral = 0

try:
    while True:
        # Baca jarak dari sensor kiri dan depan
        left_distance = read_sensor(left_sensor)
        front_distance = read_sensor(front_sensor)

        # Front obstacle avoidance
        if front_distance and front_distance < frontwall_distance:  # Jika ada halangan di depan
            print("Obstacle detected in front. Turning...")
            for _ in range(10):
                set_motor_speed(turning_speed, -turning_speed)
        
        elif left_distance is not None:  # Jika sensor kiri mendeteksi dinding
            # PID control for maintaining distance from the wall
            error = wall_distance - left_distance  # Calculate the error
            integral += error  # Integral term
            derivative = error - prev_error  # Derivative term
            prev_error = error  # Update previous error for the next cycle

            # PID control equation for adjusting motor speed
            adjustment = Kp * error + Ki * integral + Kd * derivative

            left_motor_speed = base_speed + adjustment
            right_motor_speed = base_speed - adjustment

            # Limit motor speeds to avoid excessive turning
            left_motor_speed = max(min(left_motor_speed, base_speed + turning_speed), -base_speed - turning_speed)
            right_motor_speed = max(min(right_motor_speed, base_speed + turning_speed), -base_speed - turning_speed)

            print(f"Adjusting motor speeds: Left = {left_motor_speed:.2f}, Right = {right_motor_speed:.2f}")
            set_motor_speed(left_motor_speed, right_motor_speed)  # Set adjusted speeds

        else:
            print("No wall detected on the left. Moving forward...")
            set_motor_speed(base_speed-3, base_speed)  # Maju lurus jika tidak ada dinding

        sim.step()  # Update langkah simulasi
   # Interval waktu setiap langkah

finally:
    # Menghentikan simulasi
    sim.stopSimulation()
