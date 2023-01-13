import turtle

# drives the drone
class DroneController:
    def spawnTurtleDrone(orientation):
        drone = turtle.Turtle()
        drone.hideturtle()
        drone.color('red')
        drone.penup()
        drone.speed(1)
        drone.goto(orientation[0] * 24, orientation[1] * 24)
        drone.showturtle()
        return drone

    def driveDrone(drone, instructions):
        for step in instructions:
            # check if its a turn
            if type(step) == int:
                drone.setheading(step)
            # if not, it is a forward step
            else:
                drone.goto(step[0] * 24, step[1] * 24)