from fastai.imports import *

# This is a great little package for splitting your images into a structure your model can digest
!pip install split-folders[full]

# You need to connect to Google Collab if that is where your images are
from google.colab import drive
drive.mount('/content/gdrive')

# Set paths
root_dir = "/content/gdrive/My Drive/ML/raccoon_data"
output_dir = root_dir + "/sorted"
root_path = Path(root_dir)
output_path = Path(output_dir)

import splitfolders
# Instruct the plugin on ratio of training to validation images
splitfolders.ratio(root_path, output=output_path, seed=1337, ratio=(.8, .2), group_prefix=None) # default values
