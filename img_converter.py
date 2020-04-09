import os, shutil, argparse
from PIL import Image, ImageFile
import warnings
warnings.simplefilter("ignore")
ImageFile.LOAD_TRUNCATED_IMAGES = True

parser = argparse.ArgumentParser(description = 'Image Converter')
parser.add_argument('directory', type = str, help = 'Path to convert')
args = parser.parse_args()

def convert_image(directory):
    if os.path.isdir(directory + '_resized') == True:
        shutil.rmtree(directory + '_resized')
    os.makedirs(directory + '_resized')
    resized_dir = directory + '_resized'
    for idx, filename in enumerate(os.listdir(directory)):
        if filename == '.DS_Store':
            continue
        im = Image.open(os.path.join(directory, filename))
        rgb_im = im.convert('RGB')
        rgb_im_resize = rgb_im.resize((256, 256))
        rgb_im.save(os.path.join(resized_dir, directory + "-" + str(idx + 1) + ".jpg"))
    print('\n\tCONGRATULATIONS! WORK COMPLETED\n')
    print('\tOut of {} files, {} ({:.2f}%) were converted.\n'.format(len(os.listdir(directory)), len(os.listdir(resized_dir)), (len(os.listdir(resized_dir)) / len(os.listdir(directory)))*100))

if __name__ == "__main__":
    convert_image(args.directory)
