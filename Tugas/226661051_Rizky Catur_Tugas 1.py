import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client  = RemoteAPIClient()
sim     = client.require('sim')

left_motor = sim.getObject('/PioneerP3DX/leftMotor')
right_motor = sim.getObject('/PioneerP3DX/rightMotor')

def set_motor_speed(left_speed, right_speed):
    sim.setJointTargetVelocity(left_motor, left_speed)
    sim.setJointTargetVelocity(right_motor, right_speed)
    
sim.setStepping(True)
sim.startSimulation()

for _ in range(190):
    set_motor_speed(2, 2)  
    sim.step()

for _ in range(59):
    set_motor_speed(1.8, 0)  
    sim.step()

for _ in range(180):
    set_motor_speed(2, 2)  
    sim.step()

for _ in range(59):
    set_motor_speed(1.8, 0)  
    sim.step()

for _ in range(184):
    set_motor_speed(2, 2)  
    sim.step()

for _ in range(59):
    set_motor_speed(1.8, 0)  
    sim.step()

for _ in range(172):
    set_motor_speed(2, 2)  
    sim.step()

for _ in range(59):
    set_motor_speed(1.8, 0)  
    sim.step()

for _ in range(44):
    set_motor_speed(1.2, 0)  
    sim.step()

for _ in range(240):
    set_motor_speed(2, 2)  
    sim.step()

for _ in range(44):
    set_motor_speed(1.2, 0)  
    sim.step()

for _ in range(86):
    set_motor_speed(1.1, -0.1)  
    sim.step()


for _ in range(188):
    set_motor_speed(2, 2)  
    sim.step()

for _ in range(59):
    set_motor_speed(2, 0)  
    sim.step()

for _ in range(60):
    set_motor_speed(0.8, 0)  
    sim.step()

for _ in range(248):
    set_motor_speed(2, 2)  
    sim.step()

for _ in range(48):
    set_motor_speed(0, 2)  
    sim.step()

for _ in range(48):
    set_motor_speed(0, 1.8)  
    sim.step()

for _ in range(160):
    set_motor_speed(2, 2)  
    sim.step()

for _ in range(40):
    set_motor_speed(2, -0.5)  
    sim.step()

for _ in range(48):
    set_motor_speed(2, -0.5)  
    sim.step()


sim.stopSimulation()