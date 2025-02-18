import random

# Grid size
SIZE = 5  # 5x5 grid

# Representing the world using a grid (List of Lists)
def create_world():
    world = [['.' for _ in range(SIZE)] for _ in range(SIZE)]  # Create an empty grid

    # Place the Wumpus
    wumpus_x, wumpus_y = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
    world[wumpus_x][wumpus_y] = 'W'  # 'W' represents Wumpus

    # Place the Gold
    gold_x, gold_y = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
    world[gold_x][gold_y] = 'G'  # 'G' represents Gold

    # Place a Pit (just one for simplicity)
    pit_x, pit_y = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
    world[pit_x][pit_y] = 'P'  # 'P' represents Pit

    return world, wumpus_x, wumpus_y, gold_x, gold_y, pit_x, pit_y

class Agent:
    def __init__(self):
        self.x = 0  # starting position (top-left corner)
        self.y = 0  # starting position (top-left corner)
        self.has_gold = False

    def move(self, direction):
        if direction == "up":
            self.x -= 1
        elif direction == "down":
            self.x += 1
        elif direction == "left":
            self.y -= 1
        elif direction == "right":
            self.y += 1
        # Check if the new position is out of bounds
        if self.x < 0 or self.x >= SIZE or self.y < 0 or self.y >= SIZE:
            print("Out of bounds! Try again.")
            return False
        return True

def check_surroundings(world, agent_x, agent_y):
    # Check nearby cells for dangers
    danger = ""
    
    # Check if there is a pit nearby
    if agent_x > 0 and world[agent_x-1][agent_y] == 'P':  # Check above
        danger += "Breeze "
    if agent_x < SIZE-1 and world[agent_x+1][agent_y] == 'P':  # Check below
        danger += "Breeze "
    if agent_y > 0 and world[agent_x][agent_y-1] == 'P':  # Check left
        danger += "Breeze "
    if agent_y < SIZE-1 and world[agent_x][agent_y+1] == 'P':  # Check right
        danger += "Breeze "
    
    # Check if there’s a Wumpus nearby
    if agent_x > 0 and world[agent_x-1][agent_y] == 'W':  # Check above
        danger += "Stench "
    if agent_x < SIZE-1 and world[agent_x+1][agent_y] == 'W':  # Check below
        danger += "Stench "
    if agent_y > 0 and world[agent_x][agent_y-1] == 'W':  # Check left
        danger += "Stench "
    if agent_y < SIZE-1 and world[agent_x][agent_y+1] == 'W':  # Check right
        danger += "Stench "
    
    return danger

def play_game():
    world, wumpus_x, wumpus_y, gold_x, gold_y, pit_x, pit_y = create_world()
    agent = Agent()

    print("Welcome to Wumpus World!")
    
    # Game loop
    while True:
        # Show the world (for debugging)
        print("Current Position:", agent.x, agent.y)
        
        # Check surroundings for danger
        danger = check_surroundings(world, agent.x, agent.y)
        if danger:
            print("Danger nearby:", danger)

        # Ask the agent for a move
        move = input("Enter move (up/down/left/right): ").lower()
        if not agent.move(move):
            continue
        
        # Check for winning or losing conditions
        if (agent.x, agent.y) == (wumpus_x, wumpus_y):
            print("The Wumpus got you! Game Over.")
            break
        elif (agent.x, agent.y) == (pit_x, pit_y):
            print("You fell into a pit! Game Over.")
            break
        elif (agent.x, agent.y) == (gold_x, gold_y):
            print("You found the gold! Now get out!")
            agent.has_gold = True
        
        # If agent has the gold, they need to get out
        if agent.has_gold:
            if (agent.x == 0 and agent.y == 0):  # Escape point is (0, 0)
                print("You escaped with the gold! You win!")
                break

# Start the game
play_game()

