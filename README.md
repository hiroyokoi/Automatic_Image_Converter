# Automatic_Image_Converter

A script to automatically convert the images in a folder.  
*img_converter.py* file allows you to convert the file by resizing them to 256x256 and renaming them into "foldername-i.jpg" (i refers to the continuous number).  
  
This is useful when you download a number of images from website and want to use them for your deep learning model. This script reduces the file size and rename the files in a consistent manner. This will make you easy when conducting inference with a deep learning model.

## How to use
Mount the py file into the directory you want to convert, and run the py file in your commandline.
- Open Terminal/Command
- cd "parent path of the folder that you want to convert"
- python ./img_converter.py "FOLDER NAME"
    
The script will pass broken/corrupt images and will give you the result of how many images were converted.
