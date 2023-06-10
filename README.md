<h1>Valve Controller</h1>

<p>PCB Revision: 3.1</p>
<p>PCB Part No: L0005</p>
<p>The liquid engine's valve controller (L0005) contains the processor responsible for managing valve actuation commands issued by the liquid engine controller (L0002). The board contains opto-isolated solid state relays for solenoid actuation and a Pulse Width Modulation interface for issuing stepper motor commands that initiate actuation of the liquid engine's main propellant valves. The board contains an STM32H7 ARM Cortex-M7 microcontroller for processing, programmed using an STLink/V2 with a 20-pin IDC cable connection. The board is powered from the 5V buck converter on L0002, which is also used to power the photogate sensors used for valve position calibration. In order to allow the controller to know the true actuation state of the solenoids even in the event of a power failure, the board contains an AC power supply monitoring circuit which produces an indication signal read by the MCU when AC power is available for solenoid actuation. </p>

<p><b>Working Directory Structure:</b></p>

<p>
   cad: 3d models

   doc: documentation

   img: images of circuit/footprints for github display 

   lib: libraries for schematic symbols and footprints

   production: files needed for pcb fabrication, e.g. gerbers, profile, drill file

   sim: simulation models/files 

   src: source design files, e.g. schematic and PCB layout files
</p>

<h2>3D Model: </h2>
<img src='img/L0005-Rev3_1-TOP.png'>
<img src='img/L0005-Rev3_1-BOTTOM.png'>
