import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)  # Define RED color

# Font
question_font = pygame.font.Font(None, 24)  # Custom font with size 24 for question text
answer_font = pygame.font.Font(None, 24)    # Font size for answer text (can adjust as needed)

# Questions and Answers (each entry is a tuple with question, correct answer, wrong answers, and additional sentences)
questions = [
    ("What is the primary purpose of an Intrusion Detection System (IDS)?",
     'B',
     ['A', 'C', 'D'],
     ["A) Regularly update IDS signatures. ", "B) Monitor network traffic for suspicious activity. ","C) Generate alerts upon detecting potential security breaches.","D) Install antivirus software."]),
    ("Which of the following is a common method used to protect sensitive information in transit?",
     'A',
     ['B', 'C', 'D'],
     ["A) Implement SSL/TLS encryption.", "B) Conduct regular vulnerability assessments.", "C) Use secure VPN connections.", "D) Disable firewalls."]),
    ("What does the term ""phishing"" refer to in cybersecurity?",
     'C',
     ['A', 'B', 'D'],
     ["A) Running security audits.", "B) Developing antivirus software. ", "C) Social engineering technique to trick users into revealing sensitive information.", "D) Conducting penetration tests."]),
    ("Which security measure can help mitigate the risk of data breaches caused by weak passwords?",
     'A',
     ['B', 'C', 'D'],
     ["A) Multi-factor authentication (MFA).", "B) Implementing firewall rules.", "C) Regularly updating software.",  "D) Conducting physical security assessments."]),
    ("What is the purpose of a Virtual Private Network (VPN) in cybersecurity?",
     'B',
     ['A', 'C', 'D'],
     ["A) To secure physical access to buildings.", "B) To establish secure connections between remote users and corporate networks.", "C) To manage database access controls.", "D) To scan and detect malware."]),
    ("What is the first step in responding to a security incident?",
     'B',
     ['A', 'C', 'D'],
     ["A) Notify relevant stakeholders.", "B) Disconnect affected systems from the network.", "C) Conduct forensic analysis.", "D) Update security policies."]),
    ("Which of the following is an example of a physical security control?",
     'A',
     ['B', 'C', 'D'],
     ["A) Implementing biometric access controls.", "B) Deploying intrusion detection systems (IDS).", "C) Enforcing firewall rules.", "D) Conducting security audits."]),
    ("What is the purpose of a Virtual Private Network (VPN) in cybersecurity?",
     'B',
     ['A', 'C', 'D'],
     ["A) To secure physical access to buildings.", "B) To establish secure connections between remote users and corporate networks.", "C) To manage database access controls.", "D) To scan and detect malware."]),
    ("What is the purpose of penetration testing (pen testing)?",
     'A',
     ['B', 'C', 'D'],
     ["A) To simulate real-world attacks to identify vulnerabilities.", "B) To install security patches.", "C) SSL/TLS encryption on web servers.", "D) Virtual Machine monitoring."]),
    ("Which cybersecurity measure can help protect against Distributed Denial of Service (DDoS) attacks?",
     'A',
     ['B', 'C', 'D'],
     ["A) Network firewalls.", "B) Intrusion Prevention Systems (IPS).", "C) To manage database access controls.", "D) To scan and detect malware."]),
    ("How does encryption contribute to data security?",
     'D',
     ['A', 'B', 'C'],
     ["A) By conducting security audits.", "B) By automatically detecting and blocking malware.", "C) By managing user authentication credentials.", "D) By securing data during transmission and storage."]),
    
]

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Security Snake!!!")

# Clock to control game speed
clock = pygame.time.Clock()

# Function to draw the snake
def draw_snake(snake_pos):
    for pos in snake_pos:
        pygame.draw.rect(screen, (0, 255, 0), (pos[0], pos[1], GRID_SIZE, GRID_SIZE))

# Function to move the snake
def move_snake(snake_pos, direction):
    x, y = snake_pos[0]

    if direction == 'UP':
        y -= GRID_SIZE
    elif direction == 'DOWN':
        y += GRID_SIZE
    elif direction == 'LEFT':
        x -= GRID_SIZE
    elif direction == 'RIGHT':
        x += GRID_SIZE

    # Insert new head and remove tail
    snake_pos.insert(0, (x, y))
    if len(snake_pos) > snake_length:
        snake_pos.pop()

# Function to generate fruits (answers)
def generate_fruits(correct_answer, wrong_answers):
    fruits = [(correct_answer, (random.randint(0, (SCREEN_WIDTH // GRID_SIZE - 2)) * GRID_SIZE,
                                 random.randint(0, (SCREEN_HEIGHT // GRID_SIZE - 2)) * GRID_SIZE))]
    for answer in wrong_answers:
        fruits.append((answer, (random.randint(0, (SCREEN_WIDTH // GRID_SIZE - 2)) * GRID_SIZE,
                                random.randint(0, (SCREEN_HEIGHT // GRID_SIZE - 2)) * GRID_SIZE)))
    random.shuffle(fruits)  # Shuffle the fruits to randomize their positions
    return fruits

# Function to restart the game with a new question
def restart_game():
    global snake_pos, snake_length, direction, current_question, fruits

    # Reset snake position and length
    snake_pos = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    snake_length += 1
    direction = 'RIGHT'

    # Get the next question from the list
    current_question = (current_question + 1) % len(questions)

    # Generate fruits for the new question
    correct_answer, wrong_answers, additional_sentences = questions[current_question][1:]
    fruits = generate_fruits(correct_answer, wrong_answers)
                             
# Function to restart the game when hitting a wall or snake itself
def restart_game1():
    global snake_pos, snake_length, direction, current_question, fruits

    # Reset snake position and length
    snake_pos = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    snake_length = 1
    direction = 'RIGHT'

    # Get the next question from the list
    current_question = (current_question + 1) % len(questions)

    # Generate fruits for the new question
    correct_answer, wrong_answers, additional_sentences = questions[current_question][1:]
    fruits = generate_fruits(correct_answer, wrong_answers)

# Initialize game variables
snake_pos = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
snake_length = 1
direction = 'RIGHT'
current_question = 0
correct_answer, wrong_answers, additional_sentences = questions[current_question][1:]
fruits = generate_fruits(correct_answer, wrong_answers)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Move the snake
    move_snake(snake_pos, direction)

    # Check if snake eats any fruit (answer)
    for fruit_type, fruit_pos in fruits:
        if snake_pos[0] == fruit_pos:
            if fruit_type == correct_answer: 
                snake_length += 1
                restart_game()  # Move to the next question if the correct answer is eaten
            else:
                # If wrong answer is eaten, stay on the same question (do not restart)
                #snake_length += 1  # Still grow the snake
                pass
            break  # Exit loop after snake eats a fruit

    # Check if snake hits the wall
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= SCREEN_WIDTH or
            snake_pos[0][1] < 0 or snake_pos[0][1] >= SCREEN_HEIGHT):
        restart_game1()

    # Check if snake collides with itself
    if snake_pos[0] in snake_pos[1:]:
        restart_game1()

    # Draw everything
    screen.fill(BLACK)
    
    # Draw main question text
    question_text = question_font.render(questions[current_question][0], True, WHITE)
    screen.blit(question_text, (20, 20))  # Position the main question text
    
    # Draw additional sentences below the main question text
    text_y = 20 + question_text.get_height() + 10  # Start below the main question
    for sentence in additional_sentences:
        sentence_text = question_font.render(sentence, True, WHITE)
        screen.blit(sentence_text, (20, text_y))
        text_y += sentence_text.get_height() + 5  # Adjust spacing between sentences
    
    # Draw fruits (answers)
    for fruit_type, fruit_pos in fruits:
        if fruit_type == correct_answer:
            fruit_text = answer_font.render(fruit_type, True, RED)  # Correct answer in white
        else:
            fruit_text = answer_font.render(fruit_type, True, RED)  # Incorrect answers in red
        screen.blit(fruit_text, fruit_pos)  # Draw fruit text
    
    # Draw snake
    draw_snake(snake_pos)

    # Update the display
    pygame.display.flip()

    # Control game speed
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
