import turtle

# drives the drone
class DroneController:
    def spawnTurtleDrone(starting_pos):
        drone = turtle.Turtle()
        drone.hideturtle()
        drone.color('red')
        drone.penup()
        drone.speed(1)
        drone.goto(starting_pos[0] * 24, starting_pos[1] * 24)
        drone.showturtle()
        return drone

    def driveDrone(drone, instructions):
        for step in instructions:
            # check if its a turn
            if step == "L":
                drone.left(90)

            elif step == "R":
                drone.right(90)

            elif step == "B":
                drone.right(180)

            # if not, it is a forward step
            else:
                drone.goto(step[0] * 24, step[1] * 24)