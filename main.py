
from fastbook import *
from fastai.imports import *
from fastai.vision import *
from fastai.metrics import error_rate
from fastai.interpret import *
from fastai.vision.widgets import *

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
base_dir = "/content/gdrive/My Drive/ML/raccoon_data/sorted"
path = Path(base_dir)

# Use this ! syntax to execute commandline commands in Google Collab
!pip install fastbook -Uqq

# This wraps the image data to be digested by the model
data = ImageDataLoaders.from_folder(path, train="train", valid="val", item_tfms=Resize(224))

# Display a batch of images
data.show_batch()

# Build a Convolutional Neural Network vision learner (pretrained model)
learn = cnn_learner(data, resnet34, metrics=error_rate)
# Fine tune the pretrained model
learn.fine_tune(4, 3e-3)

# Display a batch of results with model guess and correct answer
learn.show_results()

# Interpret the results and plot a confusion matrix
interp = ClassificationInterpretation.from_learner(learn)
interp.plot_confusion_matrix()

# Plot your models WORST predictions - will often identify mis-labelled data
interp.plot_top_losses (6, nrows=3)

# Uncomment the below line to use an interactive image cleaner
# cleaner=ImageClassifierCleaner(learn)

# Now have some fun giving challenging images to your model and see what it comes up with
test_img = "/content/gdrive/My Drive/ML/raccoon_data/tests/test1.jpeg"
test_path = Path(test_img)
learn.predict(test_path)
