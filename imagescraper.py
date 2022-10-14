#Syntax to use commandline command in Google Collab
!pip install jmd_imagescraper -Uqq


from jmd_imagescraper.core import *
from pathlib import Path
from fastai.imports import *

# Connect to Google Drive
from google.colab import drive
drive.mount('/content/gdrive')

# Set path
root = Path("/content/gdrive/My Drive/ML/raccoon_data/")
print(root)

# Parameters for image scraping. This first dict is for all the raccoon images
params = {
    "max_results": 200,
    "img_size":    ImgSize.Cached, 
    "img_type":    ImgType.Photo,
    "img_layout":  ImgLayout.Square,
    "img_color":   ImgColor.All,
    "uuid_names": True
}
# This second dict will be used to select a smaller number of many different "Not Raccoon" images
params2 = {
    "max_results": 25,
    "img_size":    ImgSize.Cached, 
    "img_type":    ImgType.Photo,
    "img_layout":  ImgLayout.Square,
    "img_color":   ImgColor.All,
    "uuid_names": True
}
# Perform first search to collect images of raccoons
duckduckgo_search(root, "Raccoon", "Raccoon", **params)

# List of other items we will search for to train the model as "Not Raccoon"s
search_terms = ["Black bear", "cat", "dog", "human", "bird", "wolf", "reptile", "plant"]

# Iterate over list of search terms, perform an image scrape for each, and store them all in in the same folder
for term in search_terms:
  duckduckgo_search(root, "Not_Raccoon", term, **params2)

