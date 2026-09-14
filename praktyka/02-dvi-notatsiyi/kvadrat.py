i = None

pen_in5.down()
for i in range(1, 5):
    tank_drive.off(brake=True)
    tank_drive.on_for_rotations(20, 20, 2)
    tank_drive.off(brake=True)
    if i == 4:
        break
    training_wheels.turn_right()
pen_in5.up()
tank_drive.on_for_seconds(20, 20, 3)
time.sleep(0.5)
motorA.on_for_seconds(100, 3, block=False)
motorB.on_for_seconds((-100), 3)
time.sleep(0.5)
tank_drive.on_for_seconds(100, 100, 10)
exit()
