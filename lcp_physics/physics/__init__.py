import warnings

import lcp_physics.physics.bodies
import lcp_physics.physics.collisions
import lcp_physics.physics.constraints
import lcp_physics.physics.engines
import lcp_physics.physics.forces
import lcp_physics.physics.utils
import lcp_physics.physics.world

from .utils import Params
from .bodies import Body, Circle, Rect, Hull
from .world import World, run_world
from .forces import down_force, ExternalForce
from .constraints import Joint, FixedJoint, XConstraint, YConstraint, RotConstraint, TotalConstraint


__all__ = ['bodies', 'collisions', 'constraints', 'engines', 'forces', 'utils',
           'world', 'Params', 'Body', 'Circle', 'Rect', 'Hull', 'World', 'run_world',
           'down_force', 'ExternalForce', 'Joint', 'FixedJoint', 'XConstraint',
           'YConstraint', 'RotConstraint', 'TotalConstraint']


# Ignore pytorch 0.4 warnings about 0-indexed tensors
warnings.filterwarnings('ignore', category=UserWarning,
                        message='invalid index of a 0-dim tensor')
