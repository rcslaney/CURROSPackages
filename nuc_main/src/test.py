import drive
import time

drive.init()
drive.full_reset_and_calibrate_all()

print("Starting test loop")
while True:
    drive.axis_states()
    drive.drive_velocity(0.5, 0)
    drive.flipper_velocity(0, 0.5)
    time.sleep(1)
    drive.drive_velocity(0, 0)
    drive.flipper_velocity(0, 0)
    time.sleep(1)
    drive.drive_velocity(-0.5, 0)
    drive.flipper_velocity(0, -0.5)
    time.sleep(1)
    drive.drive_velocity(0, 0)
    drive.flipper_velocity(0, 0)
    time.sleep(1)
