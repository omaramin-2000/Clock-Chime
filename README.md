# Clock Chime By Omar Amin

![Window](https://user-images.githubusercontent.com/65174210/130119833-be4aa502-6797-4af4-bfcd-977de9a9b1d2.jpeg)

- Download for Windows: <https://download-clock-chime.objectives.repl.co/Clock%20Chime.msi>

## Description

- This program is a chiming clock replicating the exact Big Ben chimes.
- Works with GUI (Tkinter) window.
- Can be set to ring every 15, 30, or 60 minutes.
- Also chimes can be set at specific hours.

## Requirements

 1. Python3 or above
 2. Pip package
 3. Playsound package: Can be installed using cmd: ``` pip install playsound ``` in windows, and in Linux using terminal: ``` pip3 install playsound ```
 4. Tkinter package: ``` pip install tk ```

    - You can install the requirements from the text file by using the command: ``` pip install -r requirements.txt ```

## Instructions

1. The program contains py files that connect to each other so they can work together, along with the text files in the "data" folder.

2. The "Clock Chime.pyw" file includes the Tkinter window, which's used to set the program so it saves to the data text files.

3. The "Main.pyw" file reads the text files as saved from the other py file (GUI) so the clock can chime, add this file to Startup, and set the correct path, so it can keep running infinitely whenever you boot your PC anytime.

## License

- This project is licensed under the MIT license.
