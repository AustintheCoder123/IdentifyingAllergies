# Identifying Allergies with Jetson Nano and ChatGPT

Hello! Welcome to my project for the "AI and Machine Learning Academy with NVIDIA" class. For my project, I focused specifically on the problems concerning allergies when dining and many restaurants' failure to accomodate or show them. Within the U.S, restaurants and shops are not required to display the ingredients used in their food, and from where I'm from - Taiwan - it is extremely rare to know what ingredients are used in food and what actions can be taken by restaurants to accomodate for allergies or food preferences. Due to this, many people with allergies have to go out of their way and put in effort to find out the nutritional values and ingredients used in making food.

My project aims to completely remove the need for that effort. By using machine learning and ChatGPT, it can recognize what type of food is shown and send the result of that to ChatGPT, and asking it to list the ingredients used. Completely removing the need to ask for a waiter or seeking individual help when eating food. If implemented into daily life, this could GREATLY improve the quality of life for those with allergies or food preferences.

**This is a proof of concept, not a final version.**

## The Algorithm
! REMEMBER TO FILL IN !

## Running This Project
1. First, set up a connection to your Jetson Nano using an SSH connection, and starting up a functioning terminal.
2. Then, you will have to download the "jetson-inference" library. Follow the steps below to do so. If already completed, you can skip to step 14 to run the A.I. model.
3. In your terminal window, run `sudo apt-get update` to ensure that your installer is up to date.
4. Then, you have to install CMake. Run `sudo apt-get install git cmake`.
5. Then, clone the "jetson-inference" library by running `git clone --recursive https://github.com/dusty-nv/jetson-inference`.
6. Once that finishes cloning, go into your jetson-inference directory by running `cd jetson-inference`.
7. Then, update the modules inside the folder. Run `git submodule update --init`.
8. You also need to download some other necessary python packages for this to work. Run `sudo apt-get install libpython3-dev python3-numpy`.
9. Next, run `mkdir build` to make a folder called "build" inside of your current directory.
10. Move into the build directory using `cd build`
11. Run "make" to build the project. Run `cmake ../` then `make` separately.
12. Then, run `sudo make install` to install "make".
13. Now, configure it. Run `sudo ldconfig`.
14. 
