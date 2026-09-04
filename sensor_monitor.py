from datetime import datetime
import csv

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


# FEATURE 1: Better Sensor Dashboard
def display_dashboard():
    print("\n========================================")
    print("          SENSOR DASHBOARD")
    print("========================================")

    if not any(readings.values()):
        print("No sensor data available.")
        return

    latest = {
        "temperature": readings["temperature"][-1],
        "humidity": readings["humidity"][-1],
        "voltage": readings["voltage"][-1],
        "current": readings["current"][-1]
    }

    temp_status = check_status(latest["temperature"], 35, 40)
    humidity_status = check_status(latest["humidity"], 70, 80)
    voltage_status = check_status(latest["voltage"], 5.0, 5.5)
    current_status = check_status(latest["current"], 1.0, 1.5)

    print(f"Temperature : {latest['temperature']:.2f} °C [{temp_status}]")
    print(f"Humidity    : {latest['humidity']:.2f} %  [{humidity_status}]")
    print(f"Voltage     : {latest['voltage']:.2f} V  [{voltage_status}]")
    print(f"Current     : {latest['current']:.2f} A  [{current_status}]")

    statuses = [
        temp_status,
        humidity_status,
        voltage_status,
        current_status
    ]

    if "CRITICAL" in statuses:
        overall = "CRITICAL"
    elif "WARNING" in statuses:
        overall = "WARNING"
    else:
        overall = "NORMAL"

    print("----------------------------------------")
    print(f"OVERALL SYSTEM STATUS: {overall}")
    print("========================================")


# FEATURE 2: Smart Alert Summary
def display_alert_summary():
    print("\n========================================")
    print("           SMART ALERT SUMMARY")
    print("========================================")

    if not any(readings.values()):
        print("No sensor data available.")
        return

    sensors = [
        ("Temperature", readings["temperature"][-1], 35, 40, "°C"),
        ("Humidity", readings["humidity"][-1], 70, 80, "%"),
        ("Voltage", readings["voltage"][-1], 5.0, 5.5, "V"),
        ("Current", readings["current"][-1], 1.0, 1.5, "A")
    ]

    critical_count = 0
    warning_count = 0

    for name, value, warning, critical, unit in sensors:
        status = check_status(value, warning, critical)

        if status == "CRITICAL":
            print(f"CRITICAL: {name} = {value:.2f} {unit}")
            critical_count += 1

        elif status == "WARNING":
            print(f"WARNING : {name} = {value:.2f} {unit}")
            warning_count += 1

    if critical_count == 0 and warning_count == 0:
        print("ALL SENSORS NORMAL")

    print("----------------------------------------")
    print(f"Critical Alerts : {critical_count}")
    print(f"Warning Alerts  : {warning_count}")
    print("========================================")


# FEATURE 3: CSV Data Logging
def save_reading_to_csv(temperature, humidity, voltage, current):
    file_name = "sensor_data.csv"

    file_exists = False

    try:
        with open(file_name, "r"):
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Temperature",
                "Humidity",
                "Voltage",
                "Current"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            temperature,
            humidity,
            voltage,
            current
        ])

    print("Sensor data saved to sensor_data.csv")


# FEATURE 4: Trend Analysis
def analyze_trends():
    print("\n========================================")
    print("             TREND ANALYSIS")
    print("========================================")

    for sensor, values in readings.items():

        if len(values) < 2:
            print(f"{sensor.capitalize()} : Not enough data")
            continue

        previous = values[-2]
        current = values[-1]

        if current > previous:
            trend = "INCREASING"
        elif current < previous:
            trend = "DECREASING"
        else:
            trend = "STABLE"

        change = current - previous

        print(
            f"{sensor.capitalize():12} : "
            f"{trend:10} "
            f"(Change: {change:+.2f})"
        )

    print("========================================")


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
    print("3. View Dashboard")
    print("4. Smart Alert Summary")
    print("5. Trend Analysis")
    print("6. Exit")

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

        # Save reading to CSV
        save_reading_to_csv(
            temperature,
            humidity,
            voltage,
            current
        )

        temp_status = check_status(temperature, 35, 40)
        humidity_status = check_status(humidity, 70, 80)
        voltage_status = check_status(voltage, 5.0, 5.5)
        current_status = check_status(current, 1.0, 1.5)

        print("\n----------- CURRENT STATUS ------------")

        print(
            f"Temperature : {temperature:.2f} °C "
            f"[{temp_status}]"
        )

        print(
            f"Humidity    : {humidity:.2f} % "
            f"[{humidity_status}]"
        )

        print(
            f"Voltage     : {voltage:.2f} V "
            f"[{voltage_status}]"
        )

        print(
            f"Current     : {current:.2f} A "
            f"[{current_status}]"
        )

        print(
            f"\nTimestamp: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

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
        display_dashboard()

    elif choice == "4":
        display_alert_summary()

    elif choice == "5":
        analyze_trends()

    elif choice == "6":
        print("\nThank you for using Smart Sensor Monitoring System!")
        break

    else:
        print("\nInvalid choice. Please select 1, 2, 3, 4, 5 or 6.")