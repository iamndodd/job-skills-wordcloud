from wordcloud import WordCloud
import matplotlib.pyplot as plt
from config import FONT_DIR
from PIL import Image
from config import FIGURE_DIR
import numpy as np
import matplotlib.pyplot as plt

## Debug / check image mask is working
# mask = np.array(Image.open(FIGURE_DIR / "circle.png"))
# mask = np.array(Image.open(FIGURE_DIR / "cloud_shape.png"))
# plt.imshow(mask, cmap="gray")
# plt.title("Mask Preview")
# plt.show()

def make_wordcloud_figure(string_data, word_limit=50):
    mask = np.array(Image.open(FIGURE_DIR / "circle.png"))
    wordcloud = WordCloud(
        mask=mask,
        width = mask.shape[1],
        height = mask.shape[0],
        scale=5,
        relative_scaling=0.2,
        background_color="black",
        min_word_length= 4,
        max_words= word_limit,
        colormap="Blues",
        font_path=FONT_DIR/ "LEMONMILK-Light.otf",
        collocations=False,
        mode="RGBA",
    ).generate(string_data)
    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return wordcloud



def make_wordcloud_figure_dict(dict_data, word_limit=50, color="copper"):
    mask = np.array(Image.open(FIGURE_DIR / "cloud_shape.png"))
    wordcloud = WordCloud(
        mask=mask,
        width=mask.shape[1],
        height=mask.shape[0],
        scale= 1,
        relative_scaling=0,
        background_color="black",
        min_word_length= 4,
        font_step=3,
        max_words= word_limit,
        colormap=color, #alts "copper" , "bone" "RdGy_r" "binary
        font_path=FONT_DIR/ "LEMONMILK-Light.otf",
        collocations=False,
        mode="RGBA",
    ).generate_from_frequencies(dict_data)
    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return wordcloud