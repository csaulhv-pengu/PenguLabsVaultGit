from vector2 import Vector2

class Particle:
    """
    A simple physical particle.
    Represents a point mass in 2D space.
    """

    def __init__(self, mass, position=None, velocity=None):
        """
        Create a new particle.
        
        :param mass: particle mass (must be > 0)
        :param position: initial position
        :param velocity: initial velocity
        """
        if mass <= 0:
            raise ValueError("Mass must be positive")
        
        self.mass = float(mass)

        self.position = position if position is not None else Vector2(0,0)
        self.velocity = velocity if velocity is not None else Vector2(0, 0)

        # Accumalted force (reset every step)
        self.force = Vector2(0, 0)

        # ------ Force handling ------

    def apply_force(self, force):
        """
        Apply a fforce to the particle.

        Forces are accumulated and applied during the update step.
        """
        self.force += force
    
    def clear_forces(self):
        """
        Clear all accumulated forces
        """
        self.force = Vector2

        # ------ Physics update ------

    def update(self, dt):
        """
        Update the particle state using Euler integration.

        Parameters:
        dt (float): time step
        """
        # Newton's second law: F = m * a
        acceleration = self.force * (1.0 / self.mass)

        # Integrate velocity
        self.velocity += acceleration * dt

        # Integrate position
        self.position += self.velocity * dt

        # Clear forces after update
        self.clear_forces()

    # ---------- Debug ----------

    def __repr__(self):
        return (
            f"Particle(mass={self.mass}, "
            f"position={self.position}, "
            f"velocity={self.velocity})"
        )
