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
#kotak 
for _ in range(100):
    set_motor_speed(5,5)
    sim.step()

for _ in range(15):
    set_motor_speed(4,-4)
    sim.step()

for _ in range(100):
    set_motor_speed(5,5)
    sim.step()

for _ in range(15):
    set_motor_speed(4,-4)
    sim.step()

for _ in range(100):
    set_motor_speed(5,5)
    sim.step()

for _ in range(15):
    set_motor_speed(4,-4)
    sim.step()

for _ in range(100):
    set_motor_speed(5,5)
    sim.step()

for _ in range(22):
    set_motor_speed(4,-4)
    sim.step()

for _ in range(140):
    set_motor_speed(5,5)
    sim.step()

for _ in range(22):
    set_motor_speed(4,-4)
    sim.step()

for _ in range(100):
    set_motor_speed(5,5)
    sim.step()

for _ in range(22):
    set_motor_speed(4,-4)
    sim.step()

for _ in range(140):
    set_motor_speed(5,5)
    sim.step()

for _ in range(22):
    set_motor_speed(-4,4)
    sim.step()

for _ in range(100):
    set_motor_speed(5,5)
    sim.step()

for _ in range(38):
    set_motor_speed(4,-4)
    sim.step()

set_motor_speed(0,0)
sim.step()
sim.stopSimulation