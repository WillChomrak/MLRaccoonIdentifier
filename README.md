# MLRaccoonIdentifier
A Machine Learning algorithm trainer that I used to identify raccoons

This was a fun experiment with Machine Learning Image classification.  Everyone does cats and dogs when playing with these classifiers, so I decided to train my model to differntiate between Raccoons and everything else!

The ancillary files (imagescrape.py and organizeimages.py) are pretty straight forward. I'll just add a little info here about the main.py file to help with understanding and to include some screenshots of outputs.

I create and ImageDataLoader (using fastbook) to prep my images for consumption by the model. We ask the image loader to display a sample batch.

<img width="522" alt="Screen Shot 2022-10-14 at 3 11 36 PM" src="https://user-images.githubusercontent.com/45401483/195923886-e928d798-207e-4ccf-aa54-ea661b860d33.png">

Next we load a pre-trained model and give it a little bit of a fine tune.

It prints som train_loss data:

<img width="575" alt="Screen Shot 2022-10-14 at 2 29 39 PM" src="https://user-images.githubusercontent.com/45401483/195924262-9b96f6be-6f53-4aaf-b919-a2bf884dc510.png">

Not too shabby for only a few lines of code.

We ask it to give a little peek at a batch the model classified:

<img width="522" alt="Screen Shot 2022-10-14 at 2 29 12 PM" src="https://user-images.githubusercontent.com/45401483/195924616-8a21358d-6d50-4a9e-84af-d520caa3252b.png">

It got the Wolf! Thats pretty impressive. Not perfect though.. we missed at least one in there. Lets take a look at what caused the confusion with a confusion matrix:

<img width="285" alt="Screen Shot 2022-10-14 at 2 29 17 PM" src="https://user-images.githubusercontent.com/45401483/195925475-38c394c5-8cdc-412a-8056-71385fab04dd.png">

And look at the least confident guesses the model made:

<img width="491" alt="Screen Shot 2022-10-14 at 2 29 22 PM" src="https://user-images.githubusercontent.com/45401483/195925759-f776d711-4237-4a03-b1a5-46e9453e45d3.png">

The sleeping wolf tricked our poor unsuspecting model! The angle of the snout disguises the longer wolf nose. And the different limb shapes aren't visable. Well played wolf.

We run the model through a bit of a cleaning and then give it its greatest test yet:

![adult-realistic-raccoon-costume-main-2](https://user-images.githubusercontent.com/45401483/195926257-9b9e0710-e683-470a-9e38-3758e8a6a8e4.jpeg)

SUCCESS! 

<img width="585" alt="Screen Shot 2022-10-14 at 2 29 32 PM" src="https://user-images.githubusercontent.com/45401483/195926452-acea6d83-80c3-4ea8-8b39-f1662fb71ca1.png">

Not a bad little model.





