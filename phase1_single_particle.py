x = 0.0         # position
v = 1.0         # velocity
dt = 0.01        # timestep

for step in range(100):
    x = x + v*dt
    print(f"Step {step + 1}: x = {x :.2f}")