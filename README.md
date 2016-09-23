##### View on [gh-page](https://odelayio.github.io/FT232RQ-Breakout-Board/)

   
# FTDI FT232RQ Breakout Board with Variable LDO for VIO
<br>
<br>

## Board Features:

- Capability to configure microcontrollers directly (e.g. CC430F5137) 
-	Configurable VCCIO between 1.8V to 5V using on-board LDO
-	Data Rate Max 3,000,000 BAUD (FTDI FT232R Chip)
-	Route the RTS and DTR to a header for easy mode as a Programmer
-	Small form factor

## Final PCB:
![Layout](http://odelay.io/projects/FTDI_FT232RQ/Layout.jpg)
![Layout](http://odelay.io/projects/FTDI_FT232RQ/fab.jpg)

   
## Reflowing QFN-32 FTDI FT232RQ Chip:

First attempt to reflow a QFN-32 device to a board without purchasing expensive equipment.  I used a hot air gun that I purchased on Amazon for $14 ( TruePower 01-0712 Mini Heat Gun, Blue).  I also used solder paste that melts at 183C degrees.  

Applied the solder paste:
![Paste](http://odelay.io/projects/FTDI_FT232RQ/solder_paste.jpg)


Placed QFN-32 Device
![Placed](http://odelay.io/projects/FTDI_FT232RQ/pre_reflow.jpg)


Final Product being used to configure a CC430F5137 microcontroller
![Layout](http://odelay.io/projects/FTDI_FT232RQ/prog.jpg)

<br>
<br>

## Documents:

- Eagle_SCH_BRD_GERBER 
  * Schematic, Layout and Gerber files
-FTDI_EEPROM_Configuration.xml
  * Configuration file used to configure the FT232RQ device
-Verify_Serial_Communications.py 
  * Simple Python script to test the serial communications between a reference USB design and the Unit Under Test (UUT)

<br>
<br>

## Parts List

| Part               | Part Number        | Unit Price | Notes         | Link                                                                                                                         |
|--------------------|--------------------|------------|---------------|------------------------------------------------------------------------------------------------------------------------------|
| USB Mini Connector | 151-1206-1-ND      | $6.55      | 10 Connectors | http://www.digikey.com/product-detail/en/edac-inc/690-005-299-043/151-1206-1-ND/4312192                                      |
| FTDI FT232RQ       | 768-1008-1-ND      | $4.50      | 1             | http://www.digikey.com/product-detail/en/ftdi-future-technology-devices-international-ltd/FT232RQ-REEL/768-1008-1-ND/1836403 |
| LM317              | 768-1008-1-ND      | $0.77      | In stock      | http://www.digikey.com/product-detail/en/texas-instruments/LM317DCYR/296-12602-1-ND/443738                                   |
| 0.1uF, 0402, Cap   | 490-6328-1-ND      | $0.55      | 100 capacitor | http://www.digikey.com/product-detail/en/murata-electronics-north-america/GRM155R71C104KA88J/490-6328-1-ND/3845525           |
| 10uF, 0805, Cap    | 1276-6456-1-ND     | $0.78      | 10 capacitor  | http://www.digikey.com/product-detail/en/samsung-electro-mechanics-america-inc/CL21A106KPFNNNG/1276-6456-1-ND/5958084        |
| 143 ohm, 0402      | YAG2980CT-ND       | $0.48      | 100 resistors | http://www.digikey.com/product-detail/en/yageo/RC0402FR-07143RL/YAG2980CT-ND/5281845                                         |
| 240 ohm, 0402      | 311-240JRCT-ND     | $0.47      | 100 resistors | http://www.digikey.com/product-detail/en/yageo/RC0402JR-07240RL/311-240JRCT-ND/729393                                        |
| 392 ohm, 0402      | YAG3145CT-ND       | $0.48      | 100 resistors | http://www.digikey.com/product-detail/en/yageo/RC0402FR-07392RL/YAG3145CT-ND/5282010                                         |
| 1k ohm, 0402       | 311-1.0KJRCT-ND    | $0.47      | 100 resistors | http://www.digikey.com/product-detail/en/yageo/RC0402JR-071KL/311-1.0KJRCT-ND/729355                                         |
| Red LED            | SML-D12V1WT86CT-ND | $1.71      | 10 LEDs       | http://www.digikey.com/product-detail/en/rohm-semiconductor/SML-D12V1WT86/SML-D12V1WT86CT-ND/5843857                         |
| Yellow/Green LED   | SML-D12M1WT86CT-ND | $1.71      | 10 LEDs       | http://www.digikey.com/product-detail/en/rohm-semiconductor/SML-D12M1WT86/SML-D12M1WT86CT-ND/5843861                         |
| PCB Fab            | 2 layer prototype  | $5.00      | 3 copies      | http://docs.oshpark.com/services/two-layer/                                                                                  |
|                    |                    |            |               |                                                                                                                              |

<br>
<br>

## Additional Information:
- Fab board at [https://oshpark.com/](https://oshpark.com/)
  - Gerber Zip Package was used to fab board


