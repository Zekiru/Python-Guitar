# Python Guitar

## Contents
- [Setup](https://github.com/Zekiru/Python-Guitar/blob/main/README.md#setup)
- [Testing](https://github.com/Zekiru/Python-Guitar/blob/main/README.md#testing)
- [Running](https://github.com/Zekiru/Python-Guitar/blob/main/README.md#running)

## Setup

You will need to set up a **Python virtual environment**, which allows us to install Python packages without messing up the existing system Python installation. To do this, run the command:
```
python -m venv guitarenv
```
Now your project has its own virtual environment. Generally, before you start using it, you’ll first activate the environment by executing a script that comes with the installation:
- In Linux/macOS:
```
source guitarenv/bin/activate
```
- In Windows:
```
guitarenv\Scripts\activate
```
Once you can see the name of your virtual environment (*guitarenv* in this case) in your terminal, then you know that your virtual environment is active.

Next, install the packages used by this project by running the command:
```
pip install -r requirements.txt
```
This file lists the packages, and more importantly, their respective version numbers, which ensures consistency.

Verify that the packages have been installed correctly by running the command:
```
pip freeze
```
It should look something like this:
```
User@device ~/classes/csci30/projects/guitar
(guitarenv) % pip freeze
numpy==1.26.4
pygame==2.6.0
```

Provided as part of the starter files is the **stdaudio** library, which serves as a convenient wrapper for low-level audio synthesis functions from **PyGame**.

## Testing

**WARNING**: You may want to turn down the volume first since it may be loud.

To test whether the **stdaudio** library works in your machine, you can run the command:
```
python stdaudio.py
```
You should hear a short tune being played.

For macOS users, you may need to install **Homebrew** and the **Xcode Command Line Tools**, and you might also need to install the **SDL dependencies** required for **PyGame**.

Once you are done using the virtual environment, you can deactivate it by running the command:
```
deactivate
```
After executing the deactivate command, your terminal returns to normal.

This change means that you’ve exited your virtual environment. If you interact with ```Python``` or ```pip``` now, you’ll interact with your globally configured Python environment.

If you want to go back into a virtual environment that you’ve created before, you again need to run the activate script of that virtual environment.

## Running

Once you have your virtual environment active and have tested the functionality of the **stdaudio** library, you can finally run the *Guitar Simulation*.

To run the guitar client, simply run the command:
```
python guitar.py
```
This starts a client that plays the guitar in real-time, using the keyboard to input notes.

To play the guitar on your keyboard, press on any of the keys below, the program *plucks* the corresponding string.

<img width="750" alt="keyboard layout" src="https://github.com/user-attachments/assets/7971ac74-6030-4105-8351-40955df3700e" />
<br>
<br>

This keyboard arrangement imitates a piano keyboard:
- The *white keys* are on the **qwerty** row of the keyboard.
- The *black keys* on the **12345** row of the keyboard.
