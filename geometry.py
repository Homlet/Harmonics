WIDTH = 800
HEIGHT = 600
H_WIDTH = WIDTH / 2
H_HEIGHT = HEIGHT / 2


class Vec2( object ):
    def __init__( self, x, y ):
        self.x = x
        self.y = y

    def list( self ):
        return [self.x, self.y]

    def __add__( self, other ):
        return Vec2( self.x + other.x, self.y + other.y )

    def __sub__( self, other ):
        return self + -other

    def __mul__( self, scalar ):
        return Vec2( self.x * scalar, self.y * scalar )

    def __rmul__( self, scalar ):
        return self * scalar

    def __neg__( self ):
        return Vec2( -self.x, -self.y )

    def __len__( self ):
        return 2

    def __getitem__( self, index ):
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise Exception( "Vector index out of bounds." )

    def __setitem__( self, index, value ):
        if index == 0:
            self.x = value
        if index == 1:
            self.y = value
        raise Exception( "Vector index out of bounds." )

class Vec3( object ):
    def __init__( self, x, y, z ):
        self.x = x
        self.y = y
        self.z = z

    def list( self ):
        return [self.x, self.y, self.z]

    def __add__( self, other ):
        return Vec3( self.x + other.x, self.y + other.y, self.z + other.z )

    def __sub__( self, other ):
        return self + -other

    def __mul__( self, other ):
        return Vec3( self.x * scalar, self.y * scalar, self.z * scalar )

    def __rmul__( self, other ):
        return self * other

    def __neg__( self ):
        return Vec3( -self.x, -self.y, -self.z )

    def __len__( self ):
        return 3

    def __getitem__( self, index ):
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        if index == 2:
            return
        raise Exception( "Vector index out of bounds." )

    def __setitem__( self, index, value ):
        if index == 0:
            self.x = value
        if index == 1:
            self.y = value
        if index == 2:
            self.z = value
        raise Exception( "Vector index out of bounds." )

class Rect( object ):
    def __init__( self, x, y, w, h ):
        self.x0 = x
        self.y0 = y
        self.x1 = x + w
        self.y1 = y + h
        self.w = w
        self.h = h

    def __contains__( self, vector ):
        return self.x0 <= vector.x <= self.x1 \
           and self.y0 <= vector.y <= self.y1


def camera_project( p, camera ):
    p -= camera
    return project( p, camera.fov )

def project( p, fov ):
    scale = ( 1 + ( p.z - 1 ) * fov )
    if scale == 0:
        scale = 0.001
    return Vec2(
        H_WIDTH + p.x / scale,
        H_HEIGHT + p.y / scale
    )
