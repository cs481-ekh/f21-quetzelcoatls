# CS481 F21 - Quetzelcoatls

### Project Description

A membrane stretcher is controlled by two Python scripts running on a Raspberry Pi. Each script takes a command line input to specify the number of steps forward or backwards. The process of running each script was tedious for the end user and does not provide useful historical data. This project focused on engineering a user friendly interface that combines the functionality of both scripts and implemented a logger to track previous inputs.

### How it works

The final product is a simple GUI application that can run on any platform, and can easily interface with the sponsor's provided control scripts. This is the basic stack:

 - Python 3.8+
 - [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
 - A homebrew testing framework that allows mocking PySimpleGUI in a headless environment.

The code for this project is available here: [github.com/cs481-ekh/f21-quetzelcoatls](https://github.com/cs481-ekh/f21-quetzelcoatls).

### Screenshots

![Screenshot 1](/screenshot1.png)

### Team Members

 - Adrianna Mickel
 - Kelton Christopher
 - Parker Erway 