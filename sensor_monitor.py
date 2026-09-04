from datetime import datetime

print("========================================")
print("     SMART SENSOR MONITORING SYSTEM")
print("========================================")

readings = {
    "temperature": [],
    "humidity": [],
    "voltage": [],
    "current": []
}


def check_status(value, warning, critical):
    if value >= critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    else:
        return "NORMAL"


def display_statistics():
    print("\n----------- SENSOR STATISTICS -----------")

    names = {
        "temperature": "Temperature",
        "humidity": "Humidity",
        "voltage": "Voltage",
        "current": "Current"
    }

    for sensor, values in readings.items():
        if values:
            print(f"\n{names[sensor]}")
            print(f"Average : {sum(values) / len(values):.2f}")
            print(f"Minimum : {min(values):.2f}")
            print(f"Maximum : {max(values):.2f}")


while True:
    print("\n1. Enter Sensor Readings")
    print("2. View Statistics")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\n--- ENTER SENSOR READINGS ---")

        temperature = float(input("Temperature (°C): "))
        humidity = float(input("Humidity (%): "))
        voltage = float(input("Voltage (V): "))
        current = float(input("Current (A): "))

        readings["temperature"].append(temperature)
        readings["humidity"].append(humidity)
        readings["voltage"].append(voltage)
        readings["current"].append(current)

        temp_status = check_status(temperature, 35, 40)
        humidity_status = check_status(humidity, 70, 80)
        voltage_status = check_status(voltage, 5.0, 5.5)
        current_status = check_status(current, 1.0, 1.5)

        print("\n----------- CURRENT STATUS ------------")
        print(f"Temperature : {temperature:.2f} °C [{temp_status}]")
        print(f"Humidity    : {humidity:.2f} %  [{humidity_status}]")
        print(f"Voltage     : {voltage:.2f} V  [{voltage_status}]")
        print(f"Current     : {current:.2f} A  [{current_status}]")

        print(f"\nTimestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        statuses = [
            temp_status,
            humidity_status,
            voltage_status,
            current_status
        ]

        if "CRITICAL" in statuses:
            overall_status = "CRITICAL"
        elif "WARNING" in statuses:
            overall_status = "WARNING"
        else:
            overall_status = "NORMAL"

        print(f"OVERALL STATUS: {overall_status}")

        print("\n--------------- ALERTS ----------------")

        if temp_status == "CRITICAL":
            print("CRITICAL: Temperature is dangerously high!")
        elif temp_status == "WARNING":
            print("WARNING: Temperature exceeds safe range.")

        if humidity_status == "CRITICAL":
            print("CRITICAL: Humidity is very high!")
        elif humidity_status == "WARNING":
            print("WARNING: Humidity exceeds safe range.")

        if voltage_status == "CRITICAL":
            print("CRITICAL: Voltage is dangerously high!")
        elif voltage_status == "WARNING":
            print("WARNING: Voltage exceeds safe range.")

        if current_status == "CRITICAL":
            print("CRITICAL: Current is dangerously high!")
        elif current_status == "WARNING":
            print("WARNING: Current exceeds safe range.")

    elif choice == "2":
        display_statistics()

    elif choice == "3":
        print("\nThank you for using Smart Sensor Monitoring System!")
        break

    else:
        print("\nInvalid choice. Please select 1, 2 or 3.")