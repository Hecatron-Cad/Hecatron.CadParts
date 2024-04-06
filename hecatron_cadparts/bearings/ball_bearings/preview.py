# %%
from build123d import *
from ocp_vscode import *
from dataclasses import dataclass

from hecatron_cadparts.bearings.ball_bearings.ballbearing import ball_array

# https://eshop.ntn-snr.com/en/product/629ZZ-SNR/629ZZ

with BuildPart() as preview_part:
    add(ball_array(10, 2, 12))

print(ball_array(10, 2, 10))

show(preview_part)
