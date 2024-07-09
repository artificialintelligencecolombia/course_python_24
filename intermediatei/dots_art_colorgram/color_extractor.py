# Extract all the colors from the art_dots.jpg image. Figure it out by using the colorgram library. Print the list of all the colors extracted. 
# The format for each color is T: (r, g, b)

# Import library
import colorgram 

file_path = 'C:\\Users\\damal\\repos\\course_python_24\\intermediate\\dots_art_colorgram\\art_dots.jpg'

def color_extractor(file):
    # Main function
    colors = colorgram.extract(file,100) 
    # Note: input a number big enough to get all the colors extracted

    color_list = []

    for color in colors:
        rgb_format = color.rgb # Output: Rgb(r=#, g=#, b=#) -> Object
        # Convert Rgb object to a tuple
        rgb_tuple = (rgb_format.r, rgb_format.g, rgb_format.b)
        color_list.append(rgb_tuple)
        
    return color_list

# Call the function
rgb_colors = color_extractor(file_path)