# TextureDownsampler
Python script for down sampling every image texture in a folder/dir
Uses "os" and "cv2" libraries

Ideal for textures to be used in lower resolution assets since AmbientCG
exports textures from 1K up.

first draft:
  - Run downsampler.py on Python Terminal
  - Feed the folder/dir path with the textures to downsample
  - Choose a factor _f_(how many times to cut it in half)
  - The script will create a copy of the folder with the new downsampled textures.
  - The copy will have the name extended with "_downsampled_by_{ _f_ }x.{ _extension_ }"

OBS: This will also affect the thumbnail image found in many texture folders

TO-DO:
  - Make it simpler to use (.exe?)
  - 
