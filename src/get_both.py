from src.get_character import *
from src.get_image import *
import math

CHARACTERS = {}

def _segment(array, h0, w0, h1, w1):
    out = []
    #print(array.shape)
    #print(h0, w0, h1, w1)
    for i in range (h0, h1):
        temp = []
        for j in range (w0, w1-1):
            #print(i,j)
            temp += [array[i][j]]
        out += [temp]
    return np.array(out)

def segment(contour, shape, N, debug=False):
    h, w = shape
    temp_h, temp_w = h // N, w // N
    out = []
    for i in range (1, temp_h-1):
        row = []
        for j in range (1, temp_w-1):
            #print(i,j)
            temp = _segment(contour, (i-1)*N, (j-1)*N, i*N, j*N)
            row += [temp]
        out += [row]
    return np.array(out)

def compute(elem1, elem2):
    elem1, elem2 = elem1.flatten(), elem2.flatten()
    return np.average(np.absolute(elem1-elem2))

def process(segment):
    out = ' '
    error = math.inf
    if (segment == segment[0]).all():
        return out
    for char in CHARACTERS:
        score = compute(CHARACTERS[char], segment)
        if score < error:
            error = score
            out = char
    return out

def main(file, N = 25, debug=False):
    out = ''
    contour, shape = get_image_contour(file, debug)
    global CHARACTERS
    segments = segment(contour, shape, N, debug)
    CHARACTERS = get_alphabet_dictionary(segments.shape[2], segments.shape[3])
    if debug:
        print('Running in debug mode')
        figure, axes = plt.subplots(nrows=segments.shape[0], ncols=segments.shape[1])
    for i, row in enumerate(segments):
        for j, col in enumerate(row):
            if debug:
                print(col, i, j)
                axes[i, j].axis('off')
                axes[i, j].imshow(col)
            out+=process(col)
        print(out)
        out += '\n'
    return out