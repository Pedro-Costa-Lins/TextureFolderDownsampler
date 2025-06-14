# TextureFolderDownsampler
Python script for down sampling every image texture in a folder/dir.

Ideal for textures to be used in lower resolution assets since AmbientCG
exports textures from 1K up. 

Uses "os" and "cv2" libraries

Should support the following image file types:
- Windows bitmaps - *.bmp, *.dib (always supported)
- GIF files - *.gif (always supported)
- JPEG files - *.jpeg, *.jpg, *.jpe (see the Note section)
- JPEG 2000 files - *.jp2 (see the Note section)
- Portable Network Graphics - *.png (see the Note section)
- WebP - *.webp (see the Note section)
- AVIF - *.avif (see the Note section)
- Portable image format - *.pbm, *.pgm, *.ppm, *.pxm, *.pnm (always supported)
- PFM files - *.pfm (see the Note section)
- Sun rasters - *.sr, *.ras (always supported)
- TIFF files - *.tiff, *.tif (see the Note section)
- OpenEXR Image files - *.exr (see the Note section)
- Radiance HDR - *.hdr, *.pic (always supported)
- Raster and Vector geospatial data supported by GDAL (see the Note section)
As per the OpenCV2 doc(see: imread() [1/2]): [https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html](https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html)

## HOW TO:
  - Run downsampler.py on Python Terminal
  - Feed the folder/dir path with the textures to downsample
  - Choose a factor _f_ (how many times to cut it in half)
  - The script will create a copy of the folder with the new downsampled textures.
  - The copy will have the name extended with "_downsampled_by_{ _f_ }x.{ _extension_ }"

OBS: This will also affect the thumbnail image found in many texture folders

## TO-DO:
  - Make it simpler to use (.exe?)
  - More TO-DO?
