import os
import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image

folders = os.listdir('.')
results = [] 
widths =[]
heights = []
for i in np.arange(0, len(folders)):
    try: 
        imgs = os.listdir(folders[i])
        results.append(len(imgs))
        for j in np.arange(0,len(imgs)):
            path = os.path.join(folders[i], imgs[j])
            img = Image.open(path)
            widths.append(img.size[0])
            heights.append(img.size[1])
    except: 
        pass
#class imbalance histogram
f1 = plt.figure()
plt.hist(np.array(results))
plt.ylabel('Number of classes')
plt.xlabel('Number of images')
plt.title('Class Imbalance Histogram')
plt.savefig('classimbalance_hist.png')

#Width histogram
f2 = plt.figure()
plt.hist(np.array(widths))
plt.ylabel('Number of images')
plt.xlabel('Image width')
plt.title('Histogram of Yoga-82 Image Widths')
plt.savefig('widths.png')

#height histogram
f3 = plt.figure()
plt.hist(np.array(heights))
plt.ylabel('Number of images')
plt.xlabel('Image height')
plt.title('Histogram of Yoga-82 Image Heights')
plt.savefig('heights.png')

#width and height overlayed 
f4 = plt.figure()
plt.hist(np.array(widths), label = 'Widths')
plt.hist(np.array(heights), label = 'Heights')
plt.ylabel('Number of images')
plt.xlabel('Dimension')
plt.title('Width and Height Distributions Overlayed')
plt.legend()
plt.savefig('heights_and_widths.png')

#class imbalance barplot
x = []
for i in np.arange(1,83):
    x.append(str(i))
f5 = plt.figure(figsize=(14, 6))
plt.bar(x, results)
plt.xticks(x, fontsize = 6)
plt.ylabel('Number of images in a class')
plt.xlabel('Yoga Class: numbers assigned alphabetically')
plt.title('Class Imbalance Plot')
plt.savefig('classimbalance_plot.png')