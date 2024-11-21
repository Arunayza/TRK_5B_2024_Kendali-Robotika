import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import math

# Menghubungkan ke CoppeliaSim
client = RemoteAPIClient()
sim = client.require('sim')

# Mendapatkan handle untuk motor kiri, motor kanan, dan sensor ultrasonik
left_motor = sim.getObject('/PioneerP3DX/leftMotor')
right_motor = sim.getObject('/PioneerP3DX/rightMotor')

# Sensor ultrasonik (0 = kiri depan, 2 = kiri tengah, 6 = kanan, 4 = depan tengah)
sensors = [sim.getObject(f'/PioneerP3DX/ultrasonicSensor[{i}]') for i in range(8)]

# Fungsi untuk mengatur kecepatan motor
def set_motor_speed(left_speed, right_speed):
    sim.setJointTargetVelocity(left_motor, left_speed)
    sim.setJointTargetVelocity(right_motor, right_speed)

# Fungsi untuk membaca jarak dari sensor ultrasonik
def get_sensor_distance(sensor_handle):
    result, state, detected_point, *_ = sim.readProximitySensor(sensor_handle)
    if state:  # Jika sensor mendeteksi objek
        return math.sqrt(sum(coord**2 for coord in detected_point)) * 100  # Konversi ke cm
    else:
        return float('inf')  # Jika tidak ada deteksi, jarak tak terhingga

# PID Controller
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, target, actual):
        error = target - actual
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative

# Memulai simulasi
sim.setStepping(True)
sim.startSimulation()

# PID Parameters
pid = PIDController(kp=0.8, ki=0.1, kd=0.2)  # Tuning parameter PID
target_distance = 5  # cm, jarak target dari dinding kiri
front_threshold = 10  # cm, ambang deteksi halangan di depan

try:
    while True:
        # Membaca jarak dari sensor kiri (sensor 2) dan depan (sensor 4)
        distance_left = get_sensor_distance(sensors[2])
        distance_front = get_sensor_distance(sensors[4])

        # Jika ada halangan di depan
        if distance_front < front_threshold:
            print("Obstacle detected in front. Turning...")
            # Hentikan sementara dan belok
            set_motor_speed(-2, 2)  # Putar ke kanan
            time.sleep(0.5)  # Durasi putaran
            continue

        # Menghitung koreksi kecepatan dengan PID
        correction = pid.compute(target_distance, distance_left)

        # Menyesuaikan kecepatan motor berdasarkan koreksi
        base_speed = 2  # Kecepatan dasar
        left_speed = base_speed - correction
        right_speed = base_speed + correction

        # Membatasi kecepatan motor untuk stabilitas
        left_speed = max(min(left_speed, base_speed + 1), base_speed - 1.5)
        right_speed = max(min(right_speed, base_speed + 1), base_speed - 1.5)

        set_motor_speed(left_speed, right_speed)
        sim.step()

finally:
    sim.stopSimulation()
