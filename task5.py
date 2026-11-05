def step(altitude, velocity, fuel, thrust):
    new_velocity = velocity + 1.62 - thrust * 0.5
    new_altitude = altitude - new_velocity
    new_fuel = fuel - thrust
    return new_altitude, new_velocity, new_fuel


altitude = 1000
velocity = 0
fuel = 200
time_flight = 0

while altitude > 0:
    print(f"t={time_flight}s | altitude: {altitude:.1f} m | speed: {velocity:.1f} m/s | fuel: {fuel}")
    text = input("Thrust (0-10): ")
    while not text.isdigit() or int(text) > 10 or int(text) > fuel:
        text = input("Thrust (0-10): ")
    thrust = int(text)
    altitude, velocity, fuel = step(altitude, velocity, fuel, thrust)
    time_flight = time_flight + 1

if velocity <= 3:
    print(f"Safe landing at {velocity:.1f} m/s | fuel left: {fuel} | flight time: {time_flight} s")
else:
    print(f"Crashed at {velocity:.1f} m/s | fuel left: {fuel} | flight time: {time_flight} s")
# الحلقة تستمر لين الارتفاع يصير صفر أو أقل (المركبة وصلت السطح)، وفي كل ثانية نسأل المستخدم عن قوة الدفع ونحدّث الحالة.