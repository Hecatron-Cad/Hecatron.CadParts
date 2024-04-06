from dataclasses import dataclass

@dataclass
class BBearingOpts:
    """Ball Bearing Options
    Parameters:
    outer_dia: Diameter of the outside of the bearing
    outer_ring: How deep the outer ring is
    inner_dia: Diameter of the inside of the bearing
    inner_ring: How deep the inner ring is
    ball_dia: The diameter of the balls
    ball_count: The number of balls to use
    width: The width of the bearing
    fillet_radius: The radius of the fillet to be applied to the outer edges
    """
    outer_dia: float = 26
    outer_ring: float = 3.5
    inner_dia: float = 9
    inner_ring: float = 4.9
    ball_dia: float = 10
    ball_count:int = 5
    width: float = 8
    fillet_radius: float = 0.3

class BBearingAppearanceOpts:
    """Ball Bearing Appearance Options
    Parameters:
    shield_text: Text to embed on the shield
    show_shield_left: If to show the shield
    show_shield_right: If to show the shield
    show_cage: If to include the cage
    show_balls: If to include the balls
    """
    shield_text: str = ""
    show_shield_left: bool = False
    show_shield_right: bool = False
    show_cage: bool = False
    show_balls: bool = True
