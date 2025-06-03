#!/usr/bin/env python3
from PIL import Image
import os

# Open the logo
logo = Image.open('content/images/filmz.png')

# Create favicon sizes
sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
favicon_images = []

for size in sizes:
    # Resize with high quality
    resized = logo.resize(size, Image.Resampling.LANCZOS)
    favicon_images.append(resized)

# Save as ICO with multiple sizes
favicon_images[0].save(
    'content/extra/favicon.ico',
    format='ICO',
    sizes=[(16, 16), (32, 32), (48, 48), (64, 64)],
    append_images=favicon_images[1:]
)

print("Favicon created successfully!")