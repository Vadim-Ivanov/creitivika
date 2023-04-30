import pygame
from math import sin, cos, tan, pi, sqrt, atan2, asin
import math
import random

num_pul = 1
screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Уворот от пуль")


WHITE = (255, 255, 255)
YELLOW = (225, 225, 0)

x1 = 100
y1 = 100
bullet_x = 100
bullet_y = 100
Vp = 0.5
x = 1000
y = 750
x_s, y_s = x, y
V = 0.1
a = 70

target_size = 40
bullet_size = 15




def calculate_target_position(target_pos, target_velocity, time):
    return [target_pos[0] + target_velocity[0] * time, target_pos[1] + target_velocity[1] * time]

def calculate_lead_point(shooter_pos, target_pos, target_velocity, bullet_speed):
    target_distance = math.sqrt((target_pos[0] - shooter_pos[0]) ** 2 + (target_pos[1] - shooter_pos[1]) ** 2)
    time_to_impact = target_distance / bullet_speed

    for _ in range(5):  # Итерации для уточнения времени столкновения
        target_future_pos = calculate_target_position(target_pos, target_velocity, time_to_impact)
        target_distance = math.sqrt((target_future_pos[0] - shooter_pos[0]) ** 2 + (target_future_pos[1] - shooter_pos[1]) ** 2)
        time_to_impact = target_distance / bullet_speed

    return target_future_pos, time_to_impact

shooter_position = [bullet_x, bullet_y]
target_position = [x, y]
target_velocity = [math.cos(a * math.pi / 180) * V, -math.sin(a * math.pi / 180) * V]
print(target_velocity)
bullet_speed = Vp

lead_point, time_of_impact = calculate_lead_point(shooter_position, target_position, target_velocity, bullet_speed)
print("Точка прицеливания:", lead_point)
print("Время столкновения:", time_of_impact)

time = []
t = time_of_impact
x_k = lead_point[0]
y_k = lead_point[1]
b = 0
Vx = (x_k-bullet_x)*(abs(Vp)/(sqrt((bullet_x - x_k)**2 + ((bullet_y - y_k)**2))))
Vy = (y_k-bullet_y)*(abs(Vp)/(sqrt((bullet_x - x_k)**2 + ((bullet_y - y_k)**2))))


while True:
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen, YELLOW, (x1, y1), t * Vp)
    pygame.draw.circle(screen, WHITE, (x_s, y_s), t * V)
    
    if a > 0:
        y -= V * math.sin(a * math.pi / 180)
    else:
        y += V * math.sin(-a * math.pi / 180)
    x += V * math.cos(a * math.pi / 180)
    
    pygame.draw.rect(screen, (255,0,0), (x, y, target_size, target_size))
    if bullet_x > x - 0.1 and bullet_x < x + 0.1: 
        print(bullet_x, bullet_y, x, y)
    if b > 0:
        bullet_y += Vy
    else:
        bullet_y += Vy
    bullet_x += Vx
    pygame.draw.rect(screen, (255,0,0), (bullet_x, bullet_y, bullet_size, bullet_size))
    pygame.draw.rect(screen, (255,0,0), (x_k, y_k, 10, 10))
    pygame.display.update()

pygame.quit()