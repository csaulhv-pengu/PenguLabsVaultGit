import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class ProjectileMotionSimulation:
    def __init__(self, v_0, theta_deg, g=9.81, dt=0.05):
        # Parámetros físicos
        self.v_0 = v_0
        self.theta = np.deg2rad(theta_deg)
        self.g = g
        self.dt = dt

        # Tiempo
        self.t = 0.0
        self.t_final = self.calculate_t_final()

        # Historial
        self.x_history = []
        self.y_history = []

    # -----------------------------
    # Física
    # -----------------------------
    def calculate_t_final(self):
        return 2 * self.v_0 * np.sin(self.theta) / self.g

    def calculate_position(self, t):
        x = self.v_0 * np.cos(self.theta) * t
        y = self.v_0 * np.sin(self.theta) * t - 0.5 * self.g * t**2
        return x, y

    def calculate_velocity(self, t):
        vx = self.v_0 * np.cos(self.theta)
        vy = self.v_0 * np.sin(self.theta) - self.g * t
        v = np.sqrt(vx**2 + vy**2)
        return vx, vy, v

    def calculate_acceleration(self):
        ax = 0.0
        ay = -self.g
        a = self.g
        return ax, ay, a

    # -----------------------------
    # Animación
    # -----------------------------
    def animate(self):
        fig, ax = plt.subplots()
        ax.set_title("Projectile Motion Simulation")

        ax.set_xlabel("x (m)")
        ax.set_ylabel("y (m)")
        ax.grid(True)

        ax.set_xlim(0, self.v_0**2 / self.g)
        ax.set_ylim(0, self.v_0**2 / (2 * self.g))

        # Elementos gráficos
        trajectory, = ax.plot([], [], lw=2)
        projectile, = ax.plot([], [], "o")

        vel_arrow = ax.quiver(0, 0, 0, 0, color="red", scale=50)
        acc_arrow = ax.quiver(0, 0, 0, 0, color="blue", scale=50)

        velocity_text = ax.text(0, 0, "", fontsize=14, color="red")
        acceleration_text = ax.text(0, 0, "", fontsize=14, color="blue")

        def update(frame):
            # Forzar último paso a t_final
            if self.t + self.dt > self.t_final:
                self.t = self.t_final
            else:
                self.t += self.dt

            x, y = self.calculate_position(self.t)
            vx, vy, v = self.calculate_velocity(self.t)
            ax_val, ay_val, a = self.calculate_acceleration()

            self.x_history.append(x)
            self.y_history.append(y)

            trajectory.set_data(self.x_history, self.y_history)
            projectile.set_data([x], [y])

            vel_arrow.set_offsets([x, y])
            vel_arrow.set_UVC(vx, vy)

            acc_arrow.set_offsets([x, y])
            acc_arrow.set_UVC(ax_val, ay_val)

            velocity_text.set_position((x + 0.2, y + 0.2))
            velocity_text.set_text(
                f"v = ({vx:.2f}, {vy:.2f}) m/s\n|v| = {v:.2f} m/s"
            )

            acceleration_text.set_position((x + 0.2, y - 0.5))
            acceleration_text.set_text(
                f"a = ({ax_val:.1f}, {ay_val:.1f}) m/s²"
            )

            if self.t >= self.t_final:
                anim.event_source.stop()

            return (
                trajectory,
                projectile,
                vel_arrow,
                acc_arrow,
                velocity_text,
                acceleration_text
            )

        anim = FuncAnimation(
            fig,
            update,
            interval=30,
            blit=True
        )

        plt.show()


# -----------------------------
# Ejecución
# -----------------------------
simulation = ProjectileMotionSimulation(
    v_0=20,
    theta_deg=60,
    g=9.81,
    dt=0.01
)

simulation.animate()