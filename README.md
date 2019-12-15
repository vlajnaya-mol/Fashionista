# Fashionista

### Mask RCNN & PSPNet
https://github.com/matterport/Mask_RCNN

https://github.com/divamgupta/image-segmentation-keras

10 manually selected images are placed into "10images" folder

script.py creates .csv with segments of these 10 images

.ipynb files were executed on Google Colaboratory (so you need to change task_path = "drive/My Drive/test_task/")
checkpoints are saved in "checkpoints" folder, but I decided to not include them in repo

**Train.ipynb** trains both models and saves checkpoints.

**Inference.ipynb** loads weights and predicts segmentations on some image (**img_name** variable). **Results** are shown below the notebook
