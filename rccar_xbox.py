import signal
from xbox360controller import Xbox360Controller
from gpiozero import Robot

robot = Robot(left=(19,26),right=(20,21))


def on_button_pressed(button):
    print('Button {0} was pressed'.format(button.name))
    
    if button.name == "button_a":
        print('[Robot goes Forward]')
        robot.forward()
    elif button.name == "button_b":
        print('[Robot goes Backward]')
        robot.backward()
    elif button.name == "button_trigger_l":
        print('[Robot goes Left]')
        robot.left()
    elif button.name == "button_trigger_r":
        print('[Robot goes Right]')
        robot.right()


def on_button_released(button):
    print('Button {0} was released'.format(button.name))
    print('[Robot was Stoped]')
    robot.stop()

def on_axis_moved(axis):
    print('Axis {0} moved to {1} {2}'.format(axis.name,axis.x,axis.y))
    if axis.name == "axis_l" and axis.x <= -1:
        print("[Robot goes Left]")
    elif axis.name == "axis_l" and axis.x >= 1:
        print("[Robot goes right]")
    elif axis.name == "axis_l" and axis.y <=-1:
        print("[Robot goes Forward]")
    elif axis.name == "axis_l" and axis.y >=1:
        print("[Robot goes Backward]")
    else:
        print("[Robot was Stoped]")
try:
    with Xbox360Controller(0, axis_threshold=0.2) as controller:
        controller.button_b.when_pressed = on_button_pressed
        controller.button_b.when_released = on_button_released

        controller.button_a.when_pressed = on_button_pressed
        controller.button_a.when_released = on_button_released

        controller.button_x.when_pressed = on_button_pressed
        controller.button_x.when_released = on_button_released

        controller.button_y.when_pressed = on_button_pressed
        controller.button_y.when_released = on_button_released

        controller.button_trigger_l.when_pressed = on_button_pressed
        controller.button_trigger_l.when_released = on_button_released

        controller.button_trigger_r.when_pressed = on_button_pressed
        controller.button_trigger_r.when_released = on_button_released

        controller.axis_l.when_moved = on_axis_moved
        controller.axis_r.when_moved = on_axis_moved

        signal.pause()

except KeyboardInterrupt:
    pass
