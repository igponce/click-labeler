# clickPOILabeler
Point-and-click POI labeler for images (needed before you want to train an algorithm or neural network)

So you want to train a neural network, and you have enough images. Great.
Problem is you need to label some features present in the images in order to train the algorithm... and that's not as easy as it sounds.

## Prerequisites

* Python3
* numPy
* openCV3

## How to use

```{bash}
click_labeler.py <image to label>.{png|jpg}
```
### Keys

To reset the points press 'r'.
To save changes press 's' or 'x' (save, exit).
To exit, press q.

If you try to save changes withot clicking any point, the program will end.

### Use in directiries

If you want to use the program to label *every* file in your directory, use the shell:

 ```{bash}
 for i in /path/to/directory/with/a/huge/amount/of/files.jpg ; do
    click_labeler.py -i $i
 done
 ```
 
### Output
The program will write a file with the same name as the image file with the "points".
This is a pipe-separated text file with the X, y coordinates ( from (0,0) on the top left corner to (1,1) on the bottom right) of each point.




