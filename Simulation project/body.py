from mmap import ACCESS_DEFAULT
from pygame import *
from constants import *

class Body():
    def __init__(self, pos:Vector2 = Vector2(0, 0), vel:Vector2 = Vector2(0, 0), acc:Vector2 = Vector2(0, 0), mass:float = 1, size:int = 1, color = (255, 255, 255)) -> None:
        self.position:Vector2 = pos
        self.velocity:Vector2 = vel
        self.acceleration:Vector2 = acc
        self.mass = mass
        self.size = size
        self.surface: Surface 
        self.color = color

    def update(self, delta:float) -> None:
        self.velocity.x += self.acceleration.x * delta
        self.velocity.y += self.acceleration.y * delta
        
        self.position.x += self.velocity.x * delta
        self.position.y += self.velocity.y * delta

    def apply_force_toward(self, other:super):
        vec:Vector2 = other.position - self.position
        force = GRAVITY * other.mass * self.mass / vec.length()**2
        self.acceleration.x += vec.x * force
        self.acceleration.y += vec.y * force
        


    

    def get_image():
        pass