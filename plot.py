import math

from geometry import *
from render import *


def wave( start, cycles, wavelength, amplitude, points, func ):
    plot = []
    for i in range( 0, int( points ) ):
        x = i / points * cycles
        plot.append( Vec3(
            start.x + x * wavelength,
            start.y - func( x * 2 * math.pi ) * amplitude,
            1
        ) )
    return Polygon( RED, plot )

def sin( start, cycles, wavelength, amplitude, points ):
    return wave( start, cycles, wavelength, amplitude, points, math.sin )

def cos( start, cycles, wavelength, amplitude, points ):
    return wave( start, cycles, wavelength, amplitude, points, math.cos )

def composite(
    start, cycles, wavelength, amplitude, points, harmonics,
    phase=0, step=1
):
    poly = wave( start, cycles, wavelength, amplitude, points, math.sin )
    for h in range( phase + 2, harmonics + step, step ):
        harmonic = wave(
            start,
            cycles * h,
            wavelength / h,
            amplitude / h,
            points,
            math.sin
        )
        for p in range( points ):
            poly[p].y += harmonic[p].y
    return poly

def saw( start, cycles, wavelength, amplitude, points, harmonics ):
    return composite( start, cycles, wavelength, amplitude, points, harmonics )

def square( start, cycles, wavelength, amplitude, points, harmonics ):
    return composite( start, cycles, wavelength, amplitude, points, harmonics,
                      1, 2 )
