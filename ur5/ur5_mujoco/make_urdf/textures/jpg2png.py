from PIL import Image

name = "liviooil_0"
im = Image.open("%s.jpeg"%name)
im.save("%s.png"%name)
print("Saved %s.png"%name)
