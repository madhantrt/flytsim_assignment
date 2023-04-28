import time
from flyt_python import api
drone = api.navigation(timeout=120000)

time.sleep(3)

print 'taking off'
drone.take_off(10.0)

print 'starting mission'
#Used Pythagorean theorem to find the height
drone.position_set(10, 0, 0, relative=True)
drone.position_set(-5, 8.6603, 0, relative=True)
drone.position_set(-5, -8.6603, 0, relative=True)


print 'Landing'
drone.land(async=False)

drone.disconnect()
