##### View on [gh-page](https://odelayio.github.io/FT232RQ-Breakout-Board/)

   
# FTDI FT232RQ Breakout Board with Variable LDO for VIO
<br>
<br>

![Layout](http://odelay.io/projects/FTDI_FT232RQ/Layout.jpg)

   
## Description:
This is a small form factor FTDI breakout board using the FT232RQ device.  In addition this board can be capable to adjust the VIO by an on board LM317 LDO.  The board has all pins of the FTDI chip routed to either a header pin or test pad while keeping the form factor below 1 square inch.

<br>
<br>

## Board Features:

-	On board LDO to adjust the VIO of the UART signals
-	Route the RTS and DTR to a header, so they could be used to configure microcontrollers directly (e.g. CC430F5137 chip)
-	Small form factor

<br>
<br>

## Documents:

Eagle_SCH_BRD_GERBER : Schematic, Layout and Gerber files
FTDI_EEPROM_Configuration.xml : Configuration file used to configure the FT232RQ device
Verify_Serial_Communications.py : Simple Python script to test the serial communications between a reference USB design and the Unit Under Test (UUT)

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
  - Gerber Zip Package is ready for fab
  - Gerber Zip Package is ready for fab

