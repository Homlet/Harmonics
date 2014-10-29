import pygame

from geometry import *


WHITE  = ( 255, 255, 255 )
BLACK  = (   0,   0,   0 )
RED    = ( 230,  60,   0 )
BLUE   = (  60,   0, 230 )
YELLOW = ( 200, 200,   0 )
GREY   = (  80,  80,  80 )
CARBON = (  34,  34,  34 )
SKY    = ( 135, 206, 235 )


class Camera( Vec3 ):
    def __init__( self, x, y, z, fov, near, far, clamp=None ):
        super().__init__( x, y, z )
        self.fov = fov
        self.near = near
        self.far = far
        self.clamp = clamp

    def move( self, x, y, z ):
        self.x += x
        self.y += y
        self.z += z
        if self.clamp and self not in self.clamp:
            if self.x < self.clamp.x0:
                self.x = self.clamp.x0
            elif self.x > self.clamp.x1:
                self.x = self.clamp.x1
                
            if self.y < self.clamp.y0:
                self.y = self.clamp.y0
            elif self.y > self.clamp.y1:
                self.y = self.clamp.y1

static = Camera( 0, 0, 0, 1, 0, 1 )


class Polygon( list ):
    def __init__( self, color, points ):
        self.color = color
        self.extend( points )


def clip( polygon, camera ):
    for i in range( len( polygon ) ):
        if polygon[i].z - camera.z < camera.far \
        and polygon[i].z - camera.z > camera.near:
            return False
    return True


def render( window, elapsed, polygons, camera=static ):
    for polygon in polygons:
        if clip( polygon, camera ):
            continue

        pygame.draw.lines(
            window,
            polygon.color,
            False,
            [camera_project( v, camera ).list() for v in polygon],
            2
        )
        
