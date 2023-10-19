from PIL import Image

photo_image_path = "Hoenn_Route_119_E.png"
watermark_image_path = "RED.png"

image = Image.open(photo_image_path).convert('RGBA')
watermark = Image.open(watermark_image_path).convert('RGBA')
layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
layer.paste(watermark, (0, 0))
layer.paste(watermark, (32, 0))

# Create a copy of the layer
layer2 = layer.copy()

# Put alpha on the copy
layer2.putalpha(180)

# merge layers with mask
layer.paste(layer2, layer)


result = Image.alpha_composite(image, layer)

result.show()