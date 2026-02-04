x = 0.0
v = 0.0
m = 1.0
F = 1.0
dt = 0.01

for step in range(100):
    a = F / m
    v = v + a*dt
    x = x + v*dt
    print(f"Step {step+1}: Position = {x: .2f}, Velocity = {v: .2f}")