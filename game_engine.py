import pygame
import sys
import os
import random
import math

# --- Constants ---
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 144
SCALE = 3

# Game Modes: "racer", "brick_breaker", "pong", "maze_runner"
GAME_MODE = "racer"

# Define colors for games
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# --- Helper Functions ---
def display_start_message(screen, message):
    """Displays a message and waits for user input."""
    font = pygame.font.SysFont("Arial", 24)
    text_surface = font.render(message, True, WHITE)
    background_color = BLACK

    screen.fill(background_color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH * SCALE // 2, SCREEN_HEIGHT * SCALE // 2))
    screen.blit(text_surface, text_rect)
    
    controls_font = pygame.font.SysFont("Arial", 16)
    controls_text = controls_font.render("Press any key to continue...", True, GRAY)
    controls_rect = controls_text.get_rect(center=(SCREEN_WIDTH * SCALE // 2, SCREEN_HEIGHT * SCALE // 2 + 30))
    screen.blit(controls_text, controls_rect)
    
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.Clock().tick(60)

def show_controls(screen, current_difficulty):
    """Displays the controls and difficulty selection for the games."""
    controls = {
        "1": "Racer",
        "2": "Brick Breaker",
        "3": "Pong",
        "4": "Maze Runner"
    }
    
    controls_message = "Press a number to select a game:"
    
    pygame.init()
    font = pygame.font.SysFont("Arial", 24)
    
    background_color = BLACK
    screen.fill(background_color)
    
    # Display controls message
    message_surface = font.render(controls_message, True, WHITE)
    message_rect = message_surface.get_rect(center=(SCREEN_WIDTH * SCALE // 2, SCREEN_HEIGHT * SCALE // 2 - 60))
    screen.blit(message_surface, message_rect)
    
    # Display game shortcuts
    for i, (key, name) in enumerate(controls.items()):
        text = f"Press {key}: {name}"
        text_surface = font.render(text, True, GREEN)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH * SCALE // 2, SCREEN_HEIGHT * SCALE // 2 - 20 + i * 30))
        screen.blit(text_surface, text_rect)

    # Display difficulty setting
    difficulty_text = font.render(f"Difficulty: {current_difficulty.upper()}", True, YELLOW)
    difficulty_rect = difficulty_text.get_rect(center=(SCREEN_WIDTH * SCALE // 2, SCREEN_HEIGHT * SCALE // 2 + 100))
    screen.blit(difficulty_text, difficulty_rect)
    
    difficulty_controls = font.render("Press 'E' for Easy, 'M' for Medium, 'H' for Hard", True, GRAY)
    difficulty_controls_rect = difficulty_controls.get_rect(center=(SCREEN_WIDTH * SCALE // 2, SCREEN_HEIGHT * SCALE // 2 + 120))
    screen.blit(difficulty_controls, difficulty_controls_rect)

    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: return "racer", current_difficulty
                elif event.key == pygame.K_2: return "brick_breaker", current_difficulty
                elif event.key == pygame.K_3: return "pong", current_difficulty
                elif event.key == pygame.K_4: return "maze_runner", current_difficulty
                elif event.key == pygame.K_e: return show_controls(screen, "easy")
                elif event.key == pygame.K_m: return show_controls(screen, "medium")
                elif event.key == pygame.K_h: return show_controls(screen, "hard")
        pygame.time.Clock().tick(60)

# --- Game Implementations ---

def run_racer(screen, clock, difficulty):
    """A simple racing game where you dodge oncoming cars."""
    if difficulty == "easy":
        car_speed = 3
        car_spawn_rate = 40
    elif difficulty == "medium":
        car_speed = 5
        car_spawn_rate = 30
    else:  # hard
        car_speed = 7
        car_spawn_rate = 20

    player_width, player_height = 10, 15
    player_x = SCREEN_WIDTH // 2 - player_width // 2
    player_y = SCREEN_HEIGHT - player_height - 5
    player_speed = 3

    car_width, car_height = 10, 15
    cars = []

    score = 0
    font = pygame.font.SysFont("Arial", 20)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
            player_x += player_speed
        
        # Add new cars based on difficulty
        if random.randint(1, car_spawn_rate) == 1:
            car_x = random.choice([10, 20, 30, 50, 90, 70, 110])
            cars.append(pygame.Rect(car_x, -car_height, car_width, car_height))
            
        # Move and check for collisions
        for car in cars[:]:
            car.y += car_speed
            if car.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
                display_start_message(screen, f"Game Over! Score: {score}")
                running = False
            if car.y > SCREEN_HEIGHT:
                cars.remove(car)
                score += 1
        
        # Drawing
        screen.fill(BLACK)
        
        # Draw road lines
        pygame.draw.rect(screen, GRAY, ((SCREEN_WIDTH // 2) * SCALE, 0, 2 * SCALE, SCREEN_HEIGHT * SCALE))
        pygame.draw.rect(screen, GREEN, (0, 0, 20 * SCALE, SCREEN_HEIGHT * SCALE))
        pygame.draw.rect(screen, GREEN, ((SCREEN_WIDTH - 20) * SCALE, 0, 20 * SCALE, SCREEN_HEIGHT * SCALE))
        
        # Draw player and cars
        pygame.draw.rect(screen, WHITE, (player_x * SCALE, player_y * SCALE, player_width * SCALE, player_height * SCALE))
        for car in cars:
            pygame.draw.rect(screen, RED, (car.x * SCALE, car.y * SCALE, car.width * SCALE, car.height * SCALE))
            
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

def run_brick_breaker(screen, clock, difficulty):
    """A classic Brick Breaker game."""
    # Difficulty settings
    if difficulty == "easy":
        paddle_speed = 5
        ball_speed_multiplier = 1.0
    elif difficulty == "medium":
        paddle_speed = 4
        ball_speed_multiplier = 0.8
    else:  # hard
        paddle_speed = 3
        ball_speed_multiplier = 0.4

    # Paddle settings
    paddle_width, paddle_height = 30, 5
    paddle_x = (SCREEN_WIDTH - paddle_width) // 2
    paddle_y = SCREEN_HEIGHT - paddle_height - 5
    
    # Ball settings
    ball_size = 5
    ball_x, ball_y = SCREEN_WIDTH // 2, paddle_y - ball_size
    ball_speed_x = 2 * ball_speed_multiplier
    ball_speed_y = -2 * ball_speed_multiplier
    
    # Brick settings
    brick_width, brick_height = 15, 7
    bricks = []
    brick_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
    for row in range(5):
        for col in range(int(SCREEN_WIDTH / brick_width) - 2):
            x = col * brick_width + brick_width
            y = row * brick_height + brick_height
            bricks.append(pygame.Rect(x, y, brick_width - 1, brick_height - 1))
    
    score = 0
    font = pygame.font.SysFont("Arial", 20)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - paddle_width:
            paddle_x += paddle_speed
        
        # Ball movement
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
        # Ball collision with walls
        if ball_x <= 0 or ball_x >= SCREEN_WIDTH - ball_size:
            ball_speed_x *= -1
        if ball_y <= 0:
            ball_speed_y *= -1
            
        # Ball collision with paddle
        paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
        if paddle_rect.colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
            ball_speed_y *= -1
            
        # Ball collision with bricks
        for brick in bricks[:]:
            if brick.colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
                bricks.remove(brick)
                ball_speed_y *= -1
                score += 1
                
        # Check for game over or win
        if ball_y >= SCREEN_HEIGHT:
            display_start_message(screen, f"Game Over! Score: {score}")
            running = False
        if not bricks:
            display_start_message(screen, f"You Win! Score: {score}")
            running = False

        # Drawing
        screen.fill(BLACK)
        
        # Draw paddle
        pygame.draw.rect(screen, BLUE, (paddle_x * SCALE, paddle_y * SCALE, paddle_width * SCALE, paddle_height * SCALE))
        
        # Draw bricks
        for brick in bricks:
            pygame.draw.rect(screen, random.choice(brick_colors), (brick.x * SCALE, brick.y * SCALE, brick.width * SCALE, brick.height * SCALE))
            
        # Draw ball
        pygame.draw.rect(screen, WHITE, (ball_x * SCALE, ball_y * SCALE, ball_size * SCALE, ball_size * SCALE))
        
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)

def run_pong(screen, clock, difficulty):
    """A single-player Pong game against a computer opponent."""
    if difficulty == "easy":
        ai_speed = 1
        ball_speed = 2
    elif difficulty == "medium":
        ai_speed = 3
        ball_speed = 3
    else:  # hard
        ai_speed = 5
        ball_speed = 4

    paddle_width, paddle_height = 10, 40
    ball_size = 8
    ball_speed_x = ball_speed
    ball_speed_y = ball_speed
    
    player1_y = (SCREEN_HEIGHT - paddle_height) // 2
    computer_y = (SCREEN_HEIGHT - paddle_height) // 2
    
    ball_x = (SCREEN_WIDTH - ball_size) // 2
    ball_y = (SCREEN_HEIGHT - ball_size) // 2
    
    player_score, computer_score = 0, 0
    font = pygame.font.SysFont("Arial", 20)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player1_y > 0:
            player1_y -= 4
        if keys[pygame.K_DOWN] and player1_y < SCREEN_HEIGHT - paddle_height:
            player1_y += 4
        
        if computer_y + paddle_height / 2 < ball_y:
            computer_y += ai_speed
        elif computer_y + paddle_height / 2 > ball_y:
            computer_y -= ai_speed
        
        computer_y = max(0, min(computer_y, SCREEN_HEIGHT - paddle_height))

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - ball_size:
            ball_speed_y *= -1

        player1_rect = pygame.Rect(5, player1_y, paddle_width, paddle_height)
        computer_rect = pygame.Rect(SCREEN_WIDTH - 5 - paddle_width, computer_y, paddle_width, paddle_height)
        ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
        
        if ball_rect.colliderect(player1_rect):
            ball_speed_x = abs(ball_speed_x)
        if ball_rect.colliderect(computer_rect):
            ball_speed_x = -abs(ball_speed_x)

        if ball_x <= 0:
            computer_score += 1
            ball_x = (SCREEN_WIDTH - ball_size) // 2
            ball_y = (SCREEN_HEIGHT - ball_size) // 2
            ball_speed_x *= -1
        elif ball_x >= SCREEN_WIDTH - ball_size:
            player_score += 1
            ball_x = (SCREEN_WIDTH - ball_size) // 2
            ball_y = (SCREEN_HEIGHT - ball_size) // 2
            ball_speed_x *= -1

        if player_score >= 15:
            display_start_message(screen, "You Win!")
            running = False
        elif computer_score >= 15:
            display_start_message(screen, "You Lose!")
            running = False
            
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (player1_rect.x * SCALE, player1_rect.y * SCALE, paddle_width * SCALE, paddle_height * SCALE))
        pygame.draw.rect(screen, WHITE, (computer_rect.x * SCALE, computer_rect.y * SCALE, paddle_width * SCALE, paddle_height * SCALE))
        pygame.draw.rect(screen, WHITE, (ball_rect.x * SCALE, ball_rect.y * SCALE, ball_size * SCALE, ball_size * SCALE))

        score_text = font.render(f"You: {player_score} - Comp: {computer_score}", True, WHITE)
        text_rect = score_text.get_rect(center=(SCREEN_WIDTH * SCALE // 2, 20))
        screen.blit(score_text, text_rect)
        
        pygame.display.flip()
        clock.tick(60)

def run_maze_runner(screen, clock, difficulty):
    """An improved maze game where you navigate a simple maze to find the exit."""
    # Maze layouts based on difficulty
    if difficulty == "hard":
        maze = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        start_pos = (1, 1)
        end_pos = (14, 9)
    elif difficulty == "medium":
        maze = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        start_pos = (1, 1)
        end_pos = (14, 9)
    else: # easy
        maze = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        start_pos = (1, 1)
        end_pos = (14, 9)

    cell_size = 10
    
    player_pos = list(start_pos)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                old_pos = list(player_pos)
                if event.key == pygame.K_UP:
                    player_pos[1] -= 1
                elif event.key == pygame.K_DOWN:
                    player_pos[1] += 1
                elif event.key == pygame.K_LEFT:
                    player_pos[0] -= 1
                elif event.key == pygame.K_RIGHT:
                    player_pos[0] += 1
                
                if not (0 <= player_pos[1] < len(maze) and 0 <= player_pos[0] < len(maze[0]) and maze[player_pos[1]][player_pos[0]] == 0):
                    player_pos = old_pos
        
        if player_pos == list(end_pos):
            display_start_message(screen, "You Win!")
            running = False

        screen.fill(BLACK)
        
        for r, row in enumerate(maze):
            for c, cell in enumerate(row):
                if cell == 1:
                    pygame.draw.rect(screen, GRAY, (c * cell_size * SCALE, r * cell_size * SCALE, cell_size * SCALE, cell_size * SCALE))
                
        pygame.draw.rect(screen, BLUE, (player_pos[0] * cell_size * SCALE, player_pos[1] * cell_size * SCALE, cell_size * SCALE, cell_size * SCALE))
        
        pygame.draw.rect(screen, GREEN, (end_pos[0] * cell_size * SCALE, end_pos[1] * cell_size * SCALE, cell_size * SCALE, cell_size * SCALE))
        
        pygame.display.flip()
        clock.tick(60)

# --- Main Application Logic ---

def main():
    """The main entry point for the application."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE))
    clock = pygame.time.Clock()
    
    current_difficulty = "easy"
    
    while True:
        game_mode, new_difficulty = show_controls(screen, current_difficulty)
        current_difficulty = new_difficulty

        if game_mode == "racer":
            pygame.display.set_caption(f"Racer ({current_difficulty.upper()})")
            run_racer(screen, clock, current_difficulty)
        elif game_mode == "brick_breaker":
            pygame.display.set_caption(f"Brick Breaker ({current_difficulty.upper()})")
            run_brick_breaker(screen, clock, current_difficulty)
        elif game_mode == "pong":
            pygame.display.set_caption(f"Pong ({current_difficulty.upper()})")
            run_pong(screen, clock, current_difficulty)
        elif game_mode == "maze_runner":
            pygame.display.set_caption("Maze Runner")
            run_maze_runner(screen, clock, current_difficulty)

if __name__ == "__main__":
    main()
