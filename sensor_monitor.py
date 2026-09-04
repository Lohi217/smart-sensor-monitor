print("========================================")
print("     SMART SENSOR MONITORING SYSTEM")
print("========================================")

temperature = float(input("Enter Temperature (°C): "))
humidity = float(input("Enter Humidity (%): "))
voltage = float(input("Enter Voltage (V): "))
current = float(input("Enter Current (A): "))


def check_status(value, warning, critical):
    if value >= critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    else:
        return "NORMAL"


temp_status = check_status(temperature, 35, 40)
humidity_status = check_status(humidity, 70, 80)
voltage_status = check_status(voltage, 5.0, 5.5)
current_status = check_status(current, 1.0, 1.5)


print("\n----------- SENSOR READINGS ------------")
print(f"Temperature : {temperature} °C  [{temp_status}]")
print(f"Humidity    : {humidity} %   [{humidity_status}]")
print(f"Voltage     : {voltage} V    [{voltage_status}]")
print(f"Current     : {current} A    [{current_status}]")


print("\n-------------- ALERTS ------------------")

if temp_status == "CRITICAL":
    print("🚨 CRITICAL: Temperature is dangerously high!")
elif temp_status == "WARNING":
    print("⚠ WARNING: Temperature exceeds safe range.")

if humidity_status == "CRITICAL":
    print("🚨 CRITICAL: Humidity is very high!")
elif humidity_status == "WARNING":
    print("⚠ WARNING: Humidity exceeds safe range.")

if voltage_status == "CRITICAL":
    print("🚨 CRITICAL: Voltage is dangerously high!")
elif voltage_status == "WARNING":
    print("⚠ WARNING: Voltage exceeds safe range.")

if current_status == "CRITICAL":
    print("🚨 CRITICAL: Current is dangerously high!")
elif current_status == "WARNING":
    print("⚠ WARNING: Current exceeds safe range.")


statuses = [temp_status, humidity_status, voltage_status, current_status]

if "CRITICAL" in statuses:
    overall_status = "CRITICAL"
elif "WARNING" in statuses:
    overall_status = "WARNING"
else:
    overall_status = "NORMAL"

print("\n========================================")
print(f"       OVERALL SYSTEM STATUS: {overall_status}")
print("========================================")