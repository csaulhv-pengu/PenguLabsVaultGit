import math

class Vector2:
    """
    A simple 2D vector class.
    This is the foundation of the physics engine
    """

    def __init__(self, x=0.0, y=0.0):
        """
        Create a new 2D vecotr
        
        :param x: X component
        :param y: Y component
        """

        self.x = float(x)
        self.y = float(y)

    def copy(self):
        """
        Return a copy of the vector
        """
        return Vector2(self.x, self.y)

    def __add__(self, other):
        """
        v3 = v1 + v2
        """
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Vector subtraction.
        v3 = v1 + v2
        """
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """
        Scalar multiplication
        v2 = v1 * k
        """
        return Vector2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """
        Scalar multiplication (reversed).
        k * v
        """
        return self.__mul__(scalar)

    # ------ Vector math ------

    def lenght(self):
        """
        Return the magnite (length) of the vector.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalize(self):
        """
        Return a unit vector in the sama direction.
        """
        lenght = self.lenght()
        if lenght == 0:
            return Vector2(0.0, 0.0)
        return Vector2(self.x / lenght, self.y / lenght)
    
    def dot(self, other):
        """
        Dot product between two vector.
        """
        return self.x * other.x + self.y * other.y
    
    # ------ Rotation ------

    def rotate(self, angle_rad):
        """
        Rotate the vector by an angle (in radians).

        Uses the 2D rotation matrix:
        [ cosθ  -sinθ ]
        [ sinθ   cosθ ]
        """
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)

        x_new = cos_a * self.x - sin_a * self.y
        y_new = sin_a * self.x + cos_a * self.y

    # ------ For Debugging ------
    def __repr__(self):
        """
        String representation for debugging
        """
        return f"Vector2(X={self.x}.4f, y={self.y:.4f})"