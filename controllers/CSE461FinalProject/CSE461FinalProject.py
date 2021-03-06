from controller import Robot
from controller import Camera

TIME_STEP = 32
max_speed=5.0

last_error=I=D=P=error=0
kp=1.5
ki=0
kd=0.3

robot = Robot()

cm = Camera("camera")
cm.enable(TIME_STEP)  
cm.recognitionEnable(TIME_STEP)

left_motor_front = robot.getDevice('wheel_lf')
left_motor_front.setPosition(float('inf'))
left_motor_front.setVelocity(0.0)


right_motor_front = robot.getDevice('wheel_rf')
right_motor_front.setPosition(float('inf'))
right_motor_front.setVelocity(0.0)

left_motor_back = robot.getDevice('wheel_lb')
left_motor_back.setPosition(float('inf'))
left_motor_back.setVelocity(0.0)

right_motor_back= robot.getDevice('wheel_rb')
right_motor_back.setPosition(float('inf'))
right_motor_back.setVelocity(0.0)

right_ir = robot.getDevice('RIGHT')
right_ir.enable(TIME_STEP)
mid_ir = robot.getDevice('MID')
mid_ir.enable(TIME_STEP)
left_ir = robot.getDevice('LEFT')
left_ir.enable(TIME_STEP)

while robot.step(TIME_STEP) != -1:
    right_ir_val = right_ir.getValue()
    mid_ir_val = mid_ir.getValue()
    left_ir_val = left_ir.getValue()
    
    print("Left {0}, Middle {1}, right {2}".format(left_ir_val,mid_ir_val,right_ir_val))
    
    if left_ir_val < 350 and right_ir_val < 350 and mid_ir_val >= 350:
        error=0

    elif left_ir_val < 350 and right_ir_val >= 350 and mid_ir_val >= 350:
        error=-1

    elif left_ir_val >= 350 and right_ir_val < 300 and mid_ir_val >= 350:
        error=1


    elif left_ir_val >= 350 and right_ir_val < 350 and mid_ir_val < 350:
        error=2

    elif left_ir_val < 350 and right_ir_val >= 350 and mid_ir_val < 350:
        error=-2
    elif left_ir_val < 350 and right_ir_val <350 and mid_ir_val < 350:
        error=1
    P=error
    I=error+I
    D=error-last_error
    balance=int((kp*P)+(ki*I)+(kd*D))
    last_error=error   
    
    left_Speed=max_speed-balance
    
    right_Speed=max_speed+balance
    
    if left_Speed> max_speed :
        left_motor_front.setVelocity(left_Speed)
        right_motor_front.setVelocity(0)
        left_motor_back.setVelocity(left_Speed)
        right_motor_back.setVelocity(0) 
    if right_Speed> max_speed :
        left_motor_front.setVelocity(0)
        right_motor_front.setVelocity(right_Speed)
        left_motor_back.setVelocity(0)
        right_motor_back.setVelocity(right_Speed)  
    if left_Speed < 0:
        left_motor_front.setVelocity(0)
        right_motor_front.setVelocity(right_Speed)
        left_motor_back.setVelocity(0)
        right_motor_back.setVelocity(right_Speed)

    if right_Speed < 0:
        left_motor_front.setVelocity(left_Speed)
        right_motor_front.setVelocity(0)
        left_motor_back.setVelocity(left_Speed)
        right_motor_back.setVelocity(0)
    if right_Speed ==  max_speed:
        left_motor_front.setVelocity(left_Speed)
        right_motor_front.setVelocity(right_Speed)
        left_motor_back.setVelocity(left_Speed)
        right_motor_back.setVelocity(right_Speed)
        
    pass