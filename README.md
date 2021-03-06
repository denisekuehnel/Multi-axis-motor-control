# Multi-axis-motor-control
Driver for [TMCM-6110](https://www.trinamic.com/products/modules/details/tmcm-6110/) as a multi-axis stepper motor controller.


The motivation behind this project is to be able to set up a device-independet system for multi-axis motor control, more specifically the conduction of combinatorial research. However, the implemented driver provides the base for that goal. There is no actual automation yet. Commands for the motor such as “move to position” have to be executed manually. <br />
For that purpose a GUI is included, which allows for the adaptation of base parameters, as well as carry out the “move to position”, “motor stop” and “reference search” commands. More about the commands the TMCM-6110 is capable of can be found in its [documentation](https://www.trinamic.com/fileadmin/assets/Products/Modules_Documents/TMCM-6110_TMCL-firmware_manual.pdf).

Before contributing to the project, please be aware of the suggestions for [contributing](CONTRIBUTING.md) to the project and the used [code of conduct](CODE_OF_CONDUCT.md) [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md).

## Necessary modules/ Installation
[PyQt5](https://doc.bccnsoft.com/docs/PyQt5/installation.html) <br />
[Python](https://www.python.org/downloads/)<br />
This project was implemented with Python 3.8.2.<br />
To run the early version of this project the [_execute](https://github.com/denisekuehnel/Multi-axis-motor-control/blob/main/multi-axis%20motor%20controller/_execute.bat) file can be used.


