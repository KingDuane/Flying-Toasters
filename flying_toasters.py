'''
                    @         @                 @@@@@       @         @@@@@@@@@@
                  @@@       @@@             @@@@@@@@@@@@@   @@@       @@@@@@@@@@
               @@@@@@    @@@@@@           @@@@@@@@@@@@@@@@@ @@@@@@    @@@@@@@@@@
             @@@@@@@@  @@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@@@   @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@X@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@X@@@@@@@@@    @@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@           @@@@@       @@@@@@@@@@@@@@@@@@@@

                  @@@@@@      @@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@    @@@   @@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@     
 @@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@ @@@@@@@@@     @@@@@@@@@@     
   @@@@@@@@@@@@@@@            @@@@@@@@@@@@@@@@@@@@    @@@        @@@@@@@@@@     
      @@@@@@@@                @@@@@@@@@@@@@@@@@@@@               @@@@@@@@@@     
'''
"""
Flying Toasters! Prototype
------------------------
A tribute to the classic After Dark 2.0 screensaver 1-bit prototype from the 1-bit Macintosh era.
This version is platform-independent and can be adapted to different display systems.

Originally created for MicroPython on a RP2040 with LCD display, this version has been
modified to work with any Python graphics system by implementing a simple display interface.
"""

import random
import time

# Sprite definitions for the toaster animation frames
TOASTER_FRAME1 = [
    "                        █   ",
    "           ███        ██   █",
    "         ██  █       █   ██ ",
    "        █   ██████      █   ",
    "       █  ██      ██        ",
    "      █ ██          ██      ",
    "      ██      ██       █    ",
    "    ██      ██          █   ",
    "  ██      ██     ██     █   ",
    " █      ██     ██       █   ",
    "█            ██       ███   ",
    "█          ██       ██   ██ ",
    "█ ██              ██   ██  █",
    "█   ██          ██   ██   █ ",
    "█     ██      ██    █    █  ",
    "█   █   █  ███     █    █   ",
    "█   █    █        █    █    ",
    "█ ███    █       █    █ █   ",
    "█ ████   █       █      █   ",
    "█   ██   █              █   ",
    "█   █    █             █    ",
    "█   █    █            █     ",
    " █       █          ██      ",
    "  ██     █        ██        ",
    "    ██   █      ██          ",
    "      ██      ██            ",
    "        ██████              "
]

TOASTER_FRAME2 = [
    "                       ██   ",
    "                      █    █",
    "                     █    █ ",
    "            ██████      ██  ",
    "          ██      ██        ",
    "        ██          ██      ",
    "      ██      ██       █    ",
    "    ██      ██          █   ",
    "  ██      ██     ██     █   ",
    " █      ██     ██       █   ",
    "█            ██       █ █   ",
    "█          ██       ██  █   ",
    "█ ██              ██    █   ",
    "█   ██          ██        █ ",
    "█     ██      ██       ███ █",
    "█   █   █  ███             █",
    "█   █    █               ██ ",
    "█  ██    █       █   ████   ",
    "█ ████   █        ███   █   ",
    "█   ██   █              █   ",
    "█   █    █             █    ",
    "█   █    █            █     ",
    " █       █          ██      ",
    "  ██     █        ██        ",
    "    ██   █      ██          ",
    "      ██      ██            ",
    "        ██████              "
]

TOAST = [
    "        ██        ",
    "      ██  ██      ",
    "     █      ██    ",
    "  ███         ██  ",
    "██              ██",
    "█ █           ██ █",
    "██ ██      ███  ██",
    "  █   ███  █   ██ ",
    "   ███   ██ ███   ",
    "     ███  █       ",
    "        ██        "
]

class DisplayInterface:
    """
    Abstract base class for display interfaces.
    Implement this class to adapt the animation to your display system.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def fill(self, color):
        """Fill the entire display with a color"""
        raise NotImplementedError
        
    def draw_pixel(self, x, y, color):
        """Draw a single pixel at the specified coordinates"""
        raise NotImplementedError
        
    def show(self):
        """Update the display with any buffered changes"""
        raise NotImplementedError

class FlyingObject:
    def __init__(self, display_width, display_height, is_toaster=True, initial_spread=False):
        self.is_toaster = is_toaster
        self.sprite = TOAST if not is_toaster else TOASTER_FRAME1
        self.width = 27 if is_toaster else 18
        self.height = 27 if is_toaster else 11
        
        if initial_spread:
            # Distribute objects across the screen initially
            section = display_width // 4
            quadrant = random.randint(0, 3)
            self.x = random.randint(quadrant * section - self.width, 
                                  (quadrant + 1) * section)
            self.y = random.randint(-self.height * 2, display_height//2)
        else:
            self.x = display_width + random.randint(0, 150)
            self.y = random.randint(-self.height * 2, display_height//3)
        
        self.speed_x = -3.0
        self.speed_y = 1.5
        
        self.frame = random.randint(0, 1) if is_toaster else 0
        self.frame_counter = 0
        self.frame_delay = 2
        
    def update(self, display_width, display_height):
        """Update object position and animation frame"""
        self.x += self.speed_x
        self.y += self.speed_y
        
        if self.is_toaster:
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay:
                self.frame_counter = 0
                self.frame = (self.frame + 1) % 2
        
        # Reset position when object moves off screen
        if self.x < -self.width or self.y > display_height:
            if random.random() < 0.5:
                self.y = random.randint(-self.height * 3, -self.height)
            else:
                self.y = random.randint(0, display_height//3)
            
            self.x = display_width + random.randint(0, 200)
            
            if self.is_toaster:
                self.frame = random.randint(0, 1)
            
        return True

def draw_sprite(display, sprite, x, y, outline_color=0xFFFF, fill_color=0x0000):
    """Draw a sprite with specified fill and outline colors"""
    height = len(sprite)
    width = len(sprite[0])
    
    # Fill the sprite
    for row in range(height):
        left_edge = width
        right_edge = 0
        
        # Find the edges of each row
        for col in range(width):
            if sprite[row][col] == '█':
                left_edge = min(left_edge, col)
                right_edge = max(right_edge, col)
        
        # Fill between the edges
        if right_edge >= left_edge:
            for col in range(left_edge, right_edge + 1):
                pixel_x = int(x) + col
                pixel_y = int(y) + row
                
                if (0 <= pixel_x < display.width and 
                    0 <= pixel_y < display.height):
                    display.draw_pixel(pixel_x, pixel_y, fill_color)
    
    # Draw the outline
    for row in range(height):
        for col in range(width):
            if sprite[row][col] == '█':
                pixel_x = int(x) + col
                pixel_y = int(y) + row
                
                if (0 <= pixel_x < display.width and 
                    0 <= pixel_y < display.height):
                    display.draw_pixel(pixel_x, pixel_y, outline_color)

def run_animation(display, duration_ms=180000, num_toasters=5, num_toast=2):
    """
    Run the flying toasters animation
    
    Args:
        display: Display interface object
        duration_ms: Duration to run in milliseconds
        num_toasters: Number of toaster objects
        num_toast: Number of toast objects
    """
    start_time = time.time() * 1000  # Convert to milliseconds
    
    objects = []
    
    # Create toasters
    for i in range(num_toasters):
        objects.append(FlyingObject(display.width, display.height, True, True))
    
    # Create toast
    for i in range(num_toast):
        objects.append(FlyingObject(display.width, display.height, False, True))
    
    frame_interval = 30  # milliseconds between frames
    last_update = time.time() * 1000
    
    while (time.time() * 1000 - start_time) < duration_ms:
        current_time = time.time() * 1000
        
        if current_time - last_update >= frame_interval:
            display.fill(0x0000)  # Black background
            
            for obj in objects:
                obj.update(display.width, display.height)
                if obj.is_toaster:
                    sprite = TOASTER_FRAME2 if obj.frame == 1 else TOASTER_FRAME1
                else:
                    sprite = TOAST
                draw_sprite(display, sprite, obj.x, obj.y)
            
            display.show()
            last_update = current_time
        
        time.sleep(0.001)  # Small delay to prevent busy-waiting
    
    return True

# Example implementation of DisplayInterface using Pygame
def create_pygame_display(width=320, height=240):
    """
    Create a Pygame-based display implementation
    Requires: pip install pygame
    """
    import pygame
    
    class PygameDisplay(DisplayInterface):
        def __init__(self, width, height):
            super().__init__(width, height)
            pygame.init()
            self.screen = pygame.display.set_mode((width, height))
            self.buffer = pygame.Surface((width, height))
            
        def fill(self, color):
            # Convert 16-bit color to RGB
            r = (color >> 11) & 0x1F
            g = (color >> 5) & 0x3F
            b = color & 0x1F
            rgb = (r << 3, g << 2, b << 3)
            self.buffer.fill(rgb)
            
        def draw_pixel(self, x, y, color):
            # Convert 16-bit color to RGB
            r = (color >> 11) & 0x1F
            g = (color >> 5) & 0x3F
            b = color & 0x1F
            rgb = (r << 3, g << 2, b << 3)
            self.buffer.set_at((int(x), int(y)), rgb)
            
        def show(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
            self.screen.blit(self.buffer, (0, 0))
            pygame.display.flip()
            return True
    
    return PygameDisplay(width, height)

if __name__ == '__main__':
    # Example usage with Pygame display
    display = create_pygame_display(1280, 720)
    run_animation(display, duration_ms=30000)  # Run for 30 seconds