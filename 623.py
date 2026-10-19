cameras = [
    {"model": "Sony Alpha", "price": 95000, "megapixels": 33, "rating": 4.8},
    {"model": "Canon EOS", "price": 88000, "megapixels": 30, "rating": 4.7},
    {"model": "Nikon Z", "price": 105000, "megapixels": 45, "rating": 4.9},
    {"model": "Fujifilm X", "price": 72000, "megapixels": 26, "rating": 4.6},
    {"model": "Panasonic Lumix", "price": 68000, "megapixels": 24, "rating": 4.5}
]

best_camera = max(( camera for camera in cameras 
                  if camera["megapixels"] >= 30 and camera["rating"] >= 4.7) , key=lambda camera : camera["price"] )

print(best_camera)