
rooms = {
    "Living Room": 20,
    "Bedroom": 22,
    "Kitchen": 24
}

COMFORT_TEMP = 22

# Memory: previous heater states
heater_state = {
    "Living Room": "OFF",
    "Bedroom": "OFF",
    "Kitchen": "OFF"
}

def model_based_agent(room, temperature):
    previous_state = heater_state[room]

    if temperature < COMFORT_TEMP:
        if previous_state == "OFF":
            heater_state[room] = "ON"
            action = "Heater turned ON"
        else:
            action = "Heater remains ON (no change)"
    else:
        if previous_state == "ON":
            heater_state[room] = "OFF"
            action = "Heater turned OFF"
        else:
            action = "Heater remains OFF (no change)"

    print(f"{room}: Temp = {temperature}°C → {action}")

print("Model-Based Reflex Agent Output:\n")

for room, temp in rooms.items():
    model_based_agent(room, temp)
