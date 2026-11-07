# Project Overview

This is a Python script that resizes images from the `input` directory and saves them to the `output` directory. It uses the `Pillow` library for image manipulation.

# Building and Running

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place the images you want to resize in the `input` directory.
3. Run the script:
   ```bash
   python main.py
   ```
4. The resized images will be in the `output` directory, ready to be copied into `content/images/posts/YYYY/`.

# Development Conventions

- The script uses a `MAXSIZE` of (1024, 1024) to resize the images.
- The DPI of the resized images is set to (300, 300).
- Input images are read from the `input` directory.
- Output images are saved to the `output` directory.
