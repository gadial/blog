import pygame
import random
from enum import Enum
import math

# Constants
CELL_SIZE = 40
GRID_WIDTH = 20
GRID_HEIGHT = 15
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Resource colors
RESOURCE_COLORS = {
    'iron': (100, 100, 100),
    'copper': (184, 115, 51),
    'coal': (50, 50, 50),
    'stone': (150, 150, 150)
}

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

class Resource:
    def __init__(self, type):
        self.type = type
        self.color = RESOURCE_COLORS[type]
        self.progress = 0  # Progress along belt (0 to 1)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                       (self.x * CELL_SIZE, self.y * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE))

class Miner:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 2
        self.storage = []
        self.output_direction = Direction.RIGHT
        self.output_pos = (x + 2, y + 1)  # Default output position
        self.extraction_cooldown = 0
        self.extraction_rate = 60  # frames between extractions

    def update(self, resources):
        self.extraction_cooldown -= 1
        if self.extraction_cooldown <= 0 and len(self.storage) < 5:  # Max storage of 5
            # Check for resources in mining area
            for i in range(self.size):
                for j in range(self.size):
                    check_x = self.x + i
                    check_y = self.y + j
                    for idx, (x, y, resource) in enumerate(resources):
                        if x == check_x and y == check_y:
                            self.storage.append(Resource(resource.type))
                            resources.pop(idx)
                            self.extraction_cooldown = self.extraction_rate
                            return

    def draw(self, screen):
        # Draw miner body
        pygame.draw.rect(screen, (100, 100, 100), 
                        (self.x * CELL_SIZE, self.y * CELL_SIZE, 
                         self.size * CELL_SIZE, self.size * CELL_SIZE))
        
        # Draw output direction indicator
        output_x = self.output_pos[0] * CELL_SIZE
        output_y = self.output_pos[1] * CELL_SIZE
        pygame.draw.rect(screen, (150, 150, 150),
                        (output_x, output_y, CELL_SIZE, CELL_SIZE))
        
        # Draw storage indicator
        for i, resource in enumerate(self.storage):
            pygame.draw.circle(screen, resource.color,
                             (self.x * CELL_SIZE + 10 + i * 8,
                              self.y * CELL_SIZE + 10),
                             5)

class Belt:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.items = []  # List of (resource, progress) tuples

    def update(self):
        # Move items along belt
        for i, (resource, progress) in enumerate(self.items):
            self.items[i] = (resource, progress + 0.01)  # Slower speed for better visibility
        
        # Remove items that have completed their journey
        self.items = [(r, p) for r, p in self.items if p < 1]

    def add_item(self, resource):
        if len(self.items) < 3:  # Max 3 items on belt
            print(f"Adding item to belt at ({self.x}, {self.y})")
            self.items.append((resource, 0))
            return True
        return False

    def draw_base(self, screen):
        # Draw belt base
        pygame.draw.rect(screen, (100, 100, 100), 
                        (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        # Draw direction indicator
        center_x = self.x * CELL_SIZE + CELL_SIZE // 2
        center_y = self.y * CELL_SIZE + CELL_SIZE // 2
        end_x = center_x + self.direction.value[0] * (CELL_SIZE // 3)
        end_y = center_y + self.direction.value[1] * (CELL_SIZE // 3)
        pygame.draw.line(screen, (150, 150, 150), (center_x, center_y), (end_x, end_y), 2)

    def draw_items(self, screen):
        # Draw items on belt
        for resource, progress in self.items:
            # Calculate position based on progress
            if self.direction == Direction.RIGHT:
                x = self.x * CELL_SIZE + progress * CELL_SIZE
                y = self.y * CELL_SIZE + CELL_SIZE // 2
            elif self.direction == Direction.LEFT:
                x = self.x * CELL_SIZE + (1 - progress) * CELL_SIZE
                y = self.y * CELL_SIZE + CELL_SIZE // 2
            elif self.direction == Direction.DOWN:
                x = self.x * CELL_SIZE + CELL_SIZE // 2
                y = self.y * CELL_SIZE + progress * CELL_SIZE
            else:  # UP
                x = self.x * CELL_SIZE + CELL_SIZE // 2
                y = self.y * CELL_SIZE + (1 - progress) * CELL_SIZE
            
            # Draw resource
            pygame.draw.circle(screen, resource.color, (int(x), int(y)), 5)

class Assembler:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 3
        self.inputs = []
        self.output = None
        self.recipe = None
        self.processing_time = 0
        self.processing_cooldown = 0

    def update(self):
        if len(self.inputs) >= 2 and self.processing_cooldown <= 0:
            # Simple recipe: combine any two resources
            self.processing_cooldown = 120  # 2 seconds at 60 FPS
            self.inputs = self.inputs[2:]  # Remove processed items
            self.output = Resource('iron')  # For now, always output iron

    def draw(self, screen):
        # Draw assembler body
        pygame.draw.rect(screen, (150, 150, 150),
                        (self.x * CELL_SIZE, self.y * CELL_SIZE,
                         self.size * CELL_SIZE, self.size * CELL_SIZE))
        
        # Draw input indicators
        pygame.draw.rect(screen, (100, 100, 100),
                        (self.x * CELL_SIZE, self.y * CELL_SIZE,
                         CELL_SIZE, CELL_SIZE))
        
        # Draw output indicator
        pygame.draw.rect(screen, (100, 100, 100),
                        ((self.x + self.size - 1) * CELL_SIZE,
                         (self.y + self.size - 1) * CELL_SIZE,
                         CELL_SIZE, CELL_SIZE))
        
        # Draw processing progress
        if self.processing_cooldown > 0:
            progress = 1 - (self.processing_cooldown / 120)
            pygame.draw.rect(screen, (0, 255, 0),
                           (self.x * CELL_SIZE + CELL_SIZE,
                            self.y * CELL_SIZE + CELL_SIZE,
                            progress * CELL_SIZE, 5))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Factory Game")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game objects
        self.resources = []
        self.miners = []
        self.belts = []
        self.assemblers = []
        
        # Initialize resources
        self.generate_resources()
        
        # Create a working setup
        self.setup_factory()

    def setup_factory(self):
        # Add a miner
        miner = Miner(5, 5)
        self.miners.append(miner)
        
        # Add belts
        for x in range(7, 12):
            self.belts.append(Belt(x, 6, Direction.RIGHT))
        
        # Add an assembler
        self.assemblers.append(Assembler(12, 5))

    def generate_resources(self):
        # Generate resources around the miner position
        for _ in range(20):
            x = random.randint(3, 7)
            y = random.randint(3, 7)
            resource_type = random.choice(list(RESOURCE_COLORS.keys()))
            self.resources.append((x, y, Resource(resource_type)))

    def update(self):
        # Update miners
        for miner in self.miners:
            miner.update(self.resources)
            if miner.storage and not any(belt.items for belt in self.belts if belt.x == miner.output_pos[0] and belt.y == miner.output_pos[1]):
                # Output resource to belt
                belt = next(belt for belt in self.belts if belt.x == miner.output_pos[0] and belt.y == miner.output_pos[1])
                belt.add_item(miner.storage.pop(0))
        
        # Update belts
        for i, belt in enumerate(self.belts):
            belt.update()
            # Check for items reaching the end of the belt
            items_to_remove = []
            for resource, progress in belt.items:
                if progress >= 1:
                    # Find next belt or assembler
                    next_x = belt.x + belt.direction.value[0]
                    next_y = belt.y + belt.direction.value[1]
                    
                    # Debug output
                    print(f"Belt {i} at ({belt.x}, {belt.y}) trying to transfer to ({next_x}, {next_y})")
                    
                    # Find next belt
                    next_belt = None
                    for j, b in enumerate(self.belts):
                        if b.x == next_x and b.y == next_y:
                            next_belt = b
                            print(f"Found next belt {j} at ({b.x}, {b.y})")
                            break
                    
                    if next_belt and len(next_belt.items) < 3:
                        print(f"Transferring to next belt {j}")
                        next_belt.add_item(resource)
                        items_to_remove.append((resource, progress))
                    else:
                        # Check for assembler
                        assembler = next((a for a in self.assemblers if a.x == next_x and a.y == next_y), None)
                        if assembler:
                            print("Transferring to assembler")
                            assembler.inputs.append(resource)
                            items_to_remove.append((resource, progress))
                        else:
                            print("No valid target found")
                            # Keep the item on the belt if no valid target
                            continue
            
            # Remove transferred items
            for item in items_to_remove:
                if item in belt.items:
                    belt.items.remove(item)
        
        # Update assemblers
        for assembler in self.assemblers:
            assembler.processing_cooldown = max(0, assembler.processing_cooldown - 1)
            assembler.update()

    def draw(self, screen):
        # Draw grid
        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, (50, 50, 50), (0, y), (WINDOW_WIDTH, y))
        
        # Draw resources
        for x, y, resource in self.resources:
            pygame.draw.rect(screen, resource.color,
                           (x * CELL_SIZE, y * CELL_SIZE,
                            CELL_SIZE, CELL_SIZE))
        
        # Draw all belts first
        for belt in self.belts:
            belt.draw_base(screen)
        
        # Draw all items on belts
        for belt in self.belts:
            belt.draw_items(screen)
        
        # Draw miners
        for miner in self.miners:
            miner.draw(screen)
        
        # Draw assemblers
        for assembler in self.assemblers:
            assembler.draw(screen)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.update()

            # Draw everything
            self.screen.fill(WHITE)
            self.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run() 