# pixelizer
Do its best to pixelize an image

## Simple Example

This is a very simple example of how the script can be used.

```
python pixelizer --input my_image.png \
                 --output pixelized_image.png \
                 --resolution 64x64
```

## Techniques being studied

* Change constrast
* Find edges
* Quantize
* Posterize
* Draw a grid

### Draw a grid

The aim of this technique is to divide the image in X blocks.

```
python draw_grid.py --input ../imgs/mona.webp --output output.png --step-size 20
```

Original Picture                  |  Grid picture
:--------------------------------:|:---------------------------------------------:
![](https://github.com/mesarpe/pixelizer/blob/main/tests/ground-truth/mona.webp?raw=true)  |  ![](https://github.com/mesarpe/pixelizer/blob/main/tests/ground-truth/mona-grid.png?raw=true)


### Draw a grid

Change the size of an image. You have the option to increase or reduce the size. To decrease the size, simply use a `0 < number < 1`. To increase bigger than 1.

```
python resize.py --input ../tests/ground-truth/mona.webp --output ../tests/ground-truth/mona-small.png --ratio 0.5
```

Original Picture                  |  Grid picture
:--------------------------------:|:---------------------------------------------:
![](https://github.com/mesarpe/pixelizer/blob/main/tests/ground-truth/mona.webp?raw=true)  |  ![](https://github.com/mesarpe/pixelizer/blob/main/tests/ground-truth/mona-small.png?raw=true)




