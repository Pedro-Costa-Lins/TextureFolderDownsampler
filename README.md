# TextureFolderDownsampler
Python script for down sampling every image texture in a folder/dir.

Ideal for textures to be used in lower resolution assets since AmbientCG
exports textures from 1K up. 

Uses "os" and "cv2" libraries

## Image Support

PNG, JEPG, JPG, WEBP, HRD, EXR...

Should support any static image type that cv2 supports
As per the OpenCV2 doc(see: imread() [1/2]): [https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html](https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html)

## HOW TO:
  - Run downsampler.py on Python Terminal
  - Feed the folder/dir path with the textures to downsample
  - Choose a factor _f_ (how many times to cut it in half : x >= 1)
  - The script will create a copy of the folder with the new downsampled textures.
  - The copy will have the name extended with "_down_sampled_by_{ _f_ }x.{ _extension_ }"

WARNING: This will affect every image in the folder including the thumbnail found in many texture folders if supported.

## TO-DO:
  - Make it simpler to use (.exe?)
  - Make a rename interface
  - Mke file selection interface
  - More TO-DO?
