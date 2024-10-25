import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.require('sim')

left_motor = sim.getObject('/PioneerP3DX/leftMotor')
right_motor = sim.getObject('/PioneerP3DX/rightMotor')

def set_motor_speed (left_speed, right_speed):
    sim.setJointTargetVelocity(left_motor,left_speed)
    sim.setJointTargetVelocity(right_motor,right_speed)

sim.setStepping(True)
sim.startSimulation()

for _ in range(190):
    set_motor_speed(2,2)
    sim.step()

for _ in range(55):
    set_motor_speed(2,0)
    sim.step()

for _ in range(180):
    set_motor_speed(2,2)
    sim.step()

for _ in range(50):
    set_motor_speed(2,0)
    sim.step()

for _ in range(190):
    set_motor_speed(2,2)
    sim.step()

for _ in range(55):
    set_motor_speed(2,0)
    sim.step()

for _ in range(180):
    set_motor_speed(2,2)
    sim.step()

for _ in range(55):
    set_motor_speed(3,0)
    sim.step()

for _ in range(220):
    set_motor_speed(2,2)
    sim.step()

for _ in range(50):
    set_motor_speed(3,0)
    sim.step()

for _ in range(140):
    set_motor_speed(2,2)
    sim.step()

for _ in range(58):
    set_motor_speed(3,0)
    sim.step()

for _ in range(250):
    set_motor_speed(2,2)
    sim.step()

for _ in range(63):
    set_motor_speed(0,3)
    sim.step()

for _ in range(180):
    set_motor_speed(2,2)
    sim.step()

for _ in range(50):
    set_motor_speed(0,0)
    sim.step()

for _ in range(48):
    set_motor_speed(3,-3)
    sim.step()

sim.stopsimulation()