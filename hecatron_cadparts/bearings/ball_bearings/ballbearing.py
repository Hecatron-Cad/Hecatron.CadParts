from dataclasses import dataclass
from build123d import *
from hecatron_cadparts.bearings.ball_bearings.opts import *


def ball_array(array_dia: float, ball_dia:float, ball_count: float) -> BuildPart:
    """Generate a circular array of balls for the inside of the ball bearing
    Parameters:
    array_dia: The diameter of the array.
    ball_dia: The diameter of the ball.
    ball_count: The number of balls to use
    """
    with BuildPart() as newpart:
        with PolarLocations(radius=array_dia / 2, count=ball_count):
            Sphere(radius=(ball_dia / 2))
    return newpart

class BBearingPart(BasePartObject):
    def __init__(
        self,
        definition: BBearingOpts = BBearingOpts(),
        appearance: BBearingAppearanceOpts = BBearingAppearanceOpts(),
        rotation: float = 0,
        align: tuple[Align, Align] = (Align.CENTER, Align.CENTER),
        mode: Mode = Mode.ADD,
    ):
        with BuildPart() as newpart:
            # TODO
            with PolarLocations(radius=array_dia / 2, count=4):
                Sphere(radius=(10 / 2))
        super().__init__(obj=newpart.part, rotation=rotation, align=align, mode=mode)


def test():
    bb_part = BBearingPart()

test()
