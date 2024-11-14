import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# Connect to CoppeliaSim
client = RemoteAPIClient()
sim = client.require('sim')

# Get sensor handle
sensorKiri_handle = sim.getObject('/PioneerP3DX/ultrasonicSensor[1]')

# Start the simulation
sim.setStepping(True)
sim.startSimulation()

try:
    while True:
        # Read sensor values
        detectedKiri, distanceKiri = sim.readProximitySensor(sensorKiri_handle)[:2]

        # Print detected distances if an object is detected
        if detectedKiri:
            print(f"sensorKiri: Detected distance = {distanceKiri} meters")
        else:
            print("sensorKiri: No object detected")

        # Step simulation and wait before next reading
        sim.step()
    

finally:
    # Stop simulation
    sim.stopSimulation()
