# Week 1.2, Session 2: Task 6
import datetime



machineTemp = int(input("Enter machine temperature in Degrees Celsius: "))
machinePressure = int(input("Enter machine's pressure in PSI: "))
machineOpStatus = int(input("Enter machine's operational status 0 (off) or 1 (on)"))

actionsTaken = ""


if(machineTemp >80):
    print("Machine temperature is too high! Shut down recommended.")
    actionsTaken = actionsTaken + "Shut Down, "
elif(50 <= machineTemp <= 80):
    print("Machine Temperature is safe...    for now :)")
else:
    print("Machine temperature is low no action requiered.")


if(machinePressure > 100):
    print("Machine pressure high! Maintenance recommended.")
    actionsTaken = actionsTaken + "Maintenance done, "
elif(70 <= machinePressure <= 100):
    print("Machine pressure is stable...    for now :)")
else:
    print("Machine pressure is low. ALl systems operating normally.")


if(machineOpStatus == 1 and (machinePressure > 100 or machineTemp >80)):
    print("Machine conditions unsafe! Shut down recommended.")
    actionsTaken = actionsTaken + "Shut Down!"
elif(machineOpStatus == 0):
    print("Machine not in operation")
else:
    print("Machine conditions normal...    for now :)")

time = datetime.datetime.now()
with open("machine_log.txt", "a") as machineLogs:
  machineLogs.write(f"Date/Time: {time} \n Machine Pressure: {machineTemp} \n Machine Pressure: {machinePressure} \n Machine Operation Satus: {machineOpStatus} \n Actions Taken: {actionsTaken}")


