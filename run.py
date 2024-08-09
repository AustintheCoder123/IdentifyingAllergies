import sys
import argparse

from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput, cudaFont, Log


# parse the command line
parser = argparse.ArgumentParser(description="Classify a live camera stream using an image recognition DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, 
                                 epilog=imageNet.Usage() + videoSource.Usage() + videoOutput.Usage() + Log.Usage())

parser.add_argument("input", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="googlenet", help="pre-trained model to load (see below for options)")
parser.add_argument("--topK", type=int, default=1, help="show the topK number of class predictions (default: 1)")


try:
	args = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)


# load the recognition network
net = imageNet(args.network, sys.argv)

# note: to hard-code the paths to load a model, the following API can be used:
# net = imageNet(model="model/resnet18.onnx", labels="model/labels.txt", input_blob="input_0", output_blob="output_0")
# create video sources & outputs

input = videoSource(args.input, argv=sys.argv)
output = videoOutput(args.output, argv=sys.argv)
font = cudaFont()

# process frames until EOS or the user exits
while True:
    # capture the next image
    img = input.Capture()

    if img is None: # timeout
        continue  

    # classify the image and get the topK predictions
    # if you only want the top class, you can simply run:
    #   class_id, confidence = net.Classify(img)
    predictions = net.Classify(img, topK=args.topK)

    # draw predicted class labels
    for n, (classID, confidence) in enumerate(predictions):
        classLabel = net.GetClassLabel(classID)
        confidence *= 100.0

        StrClass = str(classLabel)
        print(f"imagenet:  {confidence:05.2f}% class #{classID} ({classLabel})")
        if StrClass.strip() == "apple_pie":
            print("The ingredients for apple pie are: apples, butter, salt, lard, granulated sugar, brown sugar, flour, cinnamon, nutmeg, lemon, egg.")
        if StrClass.strip() == "cheesecake":
            print("The ingredients for cheesecake are: graham crackers, butter, powdered sugar, cream cheese, eggs, vanilla, dairy sour cream, and possibly cherries, blueberries, or strawberries.")
        if StrClass.strip() == "chicken_curry":
            print("The ingredients for chicken curry are: olive oil, small onion, cloved garlic, curry powder, ground cinammon, paprika, white sugar, salt, chicken, tomato paste, plain yoghurt, coconut milk, juiced lemon, cayenne pepper.")
        if StrClass.strip() == "french_fries":
            print("The ingredients for french fries are: vinegar, salt, starchy potatoes.")
        if StrClass.strip() == "fried_rice":
            print("The ingredients for fried rice are: white rice, butter, eggs, assorted vegetables, soy sauce, sesame oil, green onions, and possibly oyster sauce.")
        if StrClass.strip() == "hamburger":
            print("The ingredients in hamburgers are: beef, salt, pepper, sesame seeds, bread buns, lettuce, tomatoes, onions, pickles, cheese. There could possibly also be bacon, avocado, guacamole, fried egg, jalapenos. There could also possibly be ketchup, mustard or mayonnaise as condiments.")

        font.OverlayText(img, text=f"{confidence:05.2f}% {classLabel}", 
                         x=5, y=5 + n * (font.GetSize() + 5),
                         color=font.White, background=font.Gray40)
        

     
                         
    # render the image
    output.Render(img)

    # update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS".format(net.GetNetworkName(), net.GetNetworkFPS()))

    # print out performance info
    net.PrintProfilerTimes()

    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break


