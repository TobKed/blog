import pathlib

from PIL import Image

MAXSIZE = (1024, 1024)
DPI = (300, 300)

INPUT_PATH = "input"
OUTPUT_PATH = "output"


for input_img_path in pathlib.Path(INPUT_PATH).iterdir():
    output_img_path = str(input_img_path).replace(INPUT_PATH, OUTPUT_PATH)
    try:
        with Image.open(input_img_path) as im:
            im.thumbnail(MAXSIZE)
            im.save(output_img_path, dpi=DPI)
            print(f"processing file {input_img_path} done...")
    except Exception as e:
        print(f"\t{e}")
