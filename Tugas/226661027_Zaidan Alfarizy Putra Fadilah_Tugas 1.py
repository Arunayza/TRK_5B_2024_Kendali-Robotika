import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.require('sim')

left_motor = sim.getObject('/PioneerP3DX/leftMotor')
right_motor = sim.getObject('/PioneerP3DX/rightMotor')

def set_motor_speed(left_speed, right_speed):
    sim.setJointTargetVelocity(left_motor, left_speed)
    sim.setJointTargetVelocity(right_motor, right_speed)

sim.setStepping(True)
sim.startSimulation()

for _ in range(200):
    set_motor_speed(2,2)
    sim.step()

for _ in range(53):
    set_motor_speed(1,-1)
    sim.step()

for _ in range(210):
    set_motor_speed(2,2)
    sim.step()

for _ in range(50):
    set_motor_speed(1.1,-1)
    sim.step()

for _ in range(210):
    set_motor_speed(2,2)
    sim.step()

for _ in range(45):
    set_motor_speed(1.5,-1)
    sim.step()

for _ in range(210):
    set_motor_speed(2,2)
    sim.step()

for _ in range(50):
    set_motor_speed(1.1,-1)
    sim.step()

for _ in range(25):
    set_motor_speed(1.1,-1)
    sim.step()

for _ in range(285):
    set_motor_speed(2,2)
    sim.step()

for _ in range(72):
    set_motor_speed(1.2,-1)
    sim.step()

for _ in range(205):
    set_motor_speed(2,2)
    sim.step()

for _ in range(73):
    set_motor_speed(1.2,-1)
    sim.step()

for _ in range(300):
    set_motor_speed(2,2)
    sim.step()

for _ in range(46):
    set_motor_speed(-2,2)
    sim.step()

for _ in range(215):
    set_motor_speed(2,2)
    sim.step()

for _ in range(65):
    set_motor_speed(2,-2)
    sim.step()

sim.stopSimulation