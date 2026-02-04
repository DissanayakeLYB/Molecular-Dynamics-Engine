x1, x2 = -1.0, 1.0
v1, v2 = 0.0, 0.0

m = 1.0
k = 10.0
r0 = 1.0
dt = 0.01

for step in range(1000):
    # calculate distance between particles
    r = abs(x2 - x1)

    # calculate force
    F = -k * (r - r0)

    # calculate accelerations
    a1 = -F / m
    a2 = F / m

    # calculate velocities
    v1 = v1 + a1*dt
    v2 = v2 + a2*dt

    # update positions
    x1 = x1 + v1*dt
    x2 = x2 + v2*dt

    if (step % 50 == 0 ):
        print(f"""Step {step}
Particle 1: x = {x1:.3f}, v = {v1:.3f}
Particle 2: x = {x2:.3f}, v = {v2:.3f}
        """)