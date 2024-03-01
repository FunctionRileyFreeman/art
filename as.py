def generate_intermediate_minimalist_art(width=800, height=600, elements=20):
    """
    Generates a piece of modern art that is more minimalist than the previous version but still features some complexity.

    Parameters:
    - width: Width of the final image.
    - height: Height of the final image.
    - elements: Number of shapes to draw, aiming for a balance between minimalism and detail.
    """
    # Create a new image with a neutral background
    img = Image.new('RGB', (width, height), '#eeeeee')
    draw = ImageDraw.Draw(img)

    for _ in range(elements):
        # Balance between simple and slightly complex shapes
        shape_type = random.choice(['rectangle', 'ellipse', 'line'])
        start_x = random.randint(0, width)
        start_y = random.randint(0, height)
        end_x = random.randint(0, width)
        end_y = random.randint(0, height)
        color = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))  # Muted colors

        if shape_type == 'rectangle':
            draw.rectangle([start_x, start_y, end_x, end_y], fill=color, outline=None)
        elif shape_type == 'ellipse':
            draw.ellipse([start_x, start_y, end_x, end_y], fill=color, outline=None)
        elif shape_type == 'line':
            draw.line([start_x, start_y, end_x, end_y], fill=color, width=3)

    return img


# Generate and show the intermediate minimalist art
intermediate_minimalist_art = generate_intermediate_minimalist_art()
intermediate_minimalist_art.show()
