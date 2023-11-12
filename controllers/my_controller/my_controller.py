from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 320
RPC=robot.getDevice("RPC")
flag=0

while robot.step(timestep) != -1:
    if(flag%10==0):
      RPC.setPosition(-0.3)
    else:
      RPC.setPosition(0.2)
    flag=flag+1