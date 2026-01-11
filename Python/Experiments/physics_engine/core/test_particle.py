from vector2 import Vector2
from particle import Particle

dt = 0.1
gravity = Vector2(0, -9.81)

p = Particle(
    mass=1.0,
    position=Vector2(0, 0),
    velocity=Vector2(5, 10)
)

for step in range(10):
    p.apply_force(gravity * p.mass)
    p.update(dt)
    print(p)