# -*- coding: utf-8 -*-
#Client 3: A Product

import matplotlib.pyplot as plt
import numpy as np
import PIL
#import os.path              



def make_logo1(rows, columns, stripe_width):
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
            if (row)/stripe_width % 2 == 0: 
                
                image[row] = [255, 255, 0, 255]             
            else:
                
                image[row] = [0, 0, 0, 255] 
    return image
    
if __name__ == "__main__":
    image = make_logo1(100,100,20)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.show() 
def make_logo2(rows, columns, stripe_width):
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
            if (row)/stripe_width % 2 == 0: 
                
                image[row] = [255, 0, 0, 255]             
            else:
                
                image[row] = [0, 0, 0, 255] 
    return image
    
if __name__ == "__main__":
    image = make_logo1(100,100,20)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.show()      
#Caused Kernel to crash
# Open the files in the same directory as the Python script
#directory = os.path.dirname(os.path.abspath(__file__))  
#background_file = os.path.join(directory, 'border.png')

# Open and show the student image in a new Figure window
#background_img = PIL.Image.open(background_file)
#fig, axes = plt.subplots(1, 2)
#axes[0].imshow(background_img, interpolation='none')

# Display student in second axes and set window to the right eye
#axes[1].imshow(background_img, interpolation='none')
#axes[1].set_xticks(range(1050, 1410, 100))
#axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
#axes[1].set_ylim(1100, 850)
#fig.show()

# Open, resize, and display earth
#logo_file = os.path.join(directory, 'figure_1.png')
#logo_img = PIL.Image.open(logo_file)
#logo_small = logo_img.resize((89, 87))
#fig2, axes2 = plt.subplots(1, 2)
#axes2[0].imshow(logo_img)
#fig2.show()

# Paste earth into right eye and display
# Uses alpha from mask
#background_img.paste(logo_small, (1162, 966), mask=logo_small) 
# Display
#fig3, axes3 = plt.subplots(1, 2)
#axes3[0].imshow(background_img, interpolation='none')
#axes3[1].imshow(background_img, interpolation='none')
#axes3[1].set_xlim(500, 1500)
#axes3[1].set_ylim(1130, 850)
#fig3.show()
