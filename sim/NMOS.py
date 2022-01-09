### Name: nMOS 
### 
### Description: MOSFET selection for stepper motor
###      driver 5V logic interface. MOSFET acts as 
###      an open-drain digital output connecting 
###      driver LED to 5V supply
### 
### Author: Colton Acosta
### 
### Date: 1/8/2022

# Libraries
import math

# Function: calcCurrent
# Inputs: Threshold voltage Vth, NMOS Constant kn
# Output: NMOS current
# Description: Calculates MOSFET current and checks 
#         the NMOS state
def calcCurrent(Vth, kn):
    # Overdrive voltage
    Vov = Vg - Vth

    # Check for cutoff condition
    if (Vth >= Vg):
        return(0)

    # Assume saturation
    i = 0.5*kn*Vov**2
    Vd = Vdd - Vf - i*R

    # Check for contradiction
    if (Vd > 0 and Vd > Vov): # Sat assumption is correct
        return(i)
    else: # NMOS is in triode
        # solve quadratic equation for Vd
        a = 0.5*kn*R
        b = -(1+kn*R*Vov)
        c = Vdd-Vf
        Vd1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        Vd2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    
        # Determine which current is correct
        if (Vd1 > 0 and Vd1 < Vov): 
            i1 = kn*(Vov*Vd1 - 0.5*Vd1**2)
            return(i1)
        else: 
            i2 = kn*(Vov*Vd2 - 0.5*Vd2**2)
            return(i2)

# Circuit constants
R = 0.27  # kOhm, Driver series resistance
Vf = 1.3 # V, Driver LED forward voltage
Vdd = 5 # V, Power supply
Vg = 3.3 # V, Gate Voltage from MCU

# MOSFET Input Parameters
kn = input("Enter the kn value (mA/V^2): ")
kn = float(kn)
Vth = input("Enter the threshold voltage (V): ")
Vth = float(Vth)

# Calculate logic current
i = calcCurrent(Vth, kn) 

# Round to three decimal points
i = round(1000*i)/1000

# Display Result
print()
print(f'Resultant Current: {i} mA')
