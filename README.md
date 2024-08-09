# Identifying Allergies with Jetson Nano and ChatGPT

Hello! Welcome to my project for the "AI and Machine Learning Academy with NVIDIA" class. For my project, I focused specifically on the problems concerning allergies when dining and many restaurants' failure to accomodate or show them. Within the U.S, restaurants and shops are not required to display the ingredients used in their food, and from where I'm from - Taiwan - it is extremely rare to know what ingredients are used in food and what actions can be taken by restaurants to accomodate for allergies or food preferences. Due to this, many people with allergies have to go out of their way and put in effort to find out the nutritional values and ingredients used in making food.

My project aims to completely remove the need for that effort. By using machine learning, it can recognize what type of food is shown, and show the ingredients used in that food. Completely removing the need to ask for a waiter or seeking individual help when eating food. If implemented into daily life, this could GREATLY improve the quality of life for those with allergies or food preferences.

**This is a proof of concept, not a final version.**

## The Algorithm
The machine that I am using, the Jetson Nano, is a machine specifically designed for machine learning. It uses a neural network to run simulations and act similarly to a human brain, therefore simulating intelligence, hence the name "artificial intelligece". The library that I used, the "food-11 Image Classification Dataset", was taken from Kaggle. Within it, there are multiple types of foods, along with a "train" folder and a "val" (validation) folder, with 900 images in the "train" folder and 100 in the "val" folder. This - however - is not the most optimal way for machine learning. With only training and validation sets, the model can not properly test the results of it's training. I had to take out another 100 images from the "training" folder of each type of food, and create a new folder called "test". The ratio of images in the "training" folder, the "validation" folder, and the "test" folder is 80:10:10; 80% of the images will be for training, 10% for validation, and 10% for testing. Utilizing the jetson-inference library, we can train the model using a pre-written script. After training it for around 100 epochs, it still isn't at the most optimal accuracy, but due to time constraints, I felt 100 epochs was more than acceptable for such a time-limited project.

The original plan after training was complete was to integrate the ChatGPT API as part of this project, where you take the output of the engine's image recognization and feed it to the API, and letting it return the ingredients. However, I was running short on time due to the sheer amount of images there were (over 10,000), so I had to put that idea aside for now and focus on completing the rest of the project. Although it might not be possible at the moment, the thought of integrating ChatGPT as part of this project is very intriguing, and I definitely plan on implementing that in the future.

The foods included in this dataset are:
> Applie pie
> Cheesecake
> Chicken curry
> French fries
> Fried rice
> Hamburgers
> Hotdogs
> Ice cream
> Omelette
> Pizza
> Sushi

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
14. Next, you'd want to open VS Code. If you do not have it installed, please install it from their website: https://code.visualstudio.com/download
15. Set up your Jetson Nano so that it is connected to the internet, and open an SSH connection to it using a Remote Window.
16. In the Explorer tab on the left, click "Open Folder" and click on the first option in the search bar at the top of the screen.
17. Download the file "resnet18.onnx" from this Github project and put it inside of jetson-inference/python/training/classification folder.
18. Also, download the "run.py" file and put it in the same folder as "resnet18.onnx"
19. Additionally, also download "labels.txt" and put it in the same directory as well.
20. Then, open a new terminal in VS Code, enter your Jetson Nano username and password if prompted.
21. Type in this command `cd jetson-inference/python/training/classification` to navigate to the classification directory.
22. Next, run `python3 run.py --model=resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=labels.txt [INPUT IMAGE PATH HERE] [OUTPUT IMAGE NAME].jpg`.
23. Remeber to change the last two fields to the correct ones, and try it out!
24. You can also freely customize the last two arguments; the first one is the input image, while the second one is the output. You can pick whatever image you want from the internet, you can download it, and put it into VS Code. Simply fill in "[INPUT IMAGE PATH HERE]" and you can run that through the A.I. model instead!

Have fun!

Dataset used: food-11 Image Classification Dataset, https://www.kaggle.com/datasets/imbikramsaha/food11
