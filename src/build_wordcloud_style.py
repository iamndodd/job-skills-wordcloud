from wordcloud import WordCloud
import matplotlib.pyplot as plt
from config import FONT_DIR


def make_wordcloud_figure(string_data, word_limit=50):
    wordcloud = WordCloud(
        width=2400,
        height=1600,
        relative_scaling=0.5,
        background_color="black",
        min_word_length= 4,
        max_words= word_limit,
        colormap="Blues",
        #font_path=r"C:\Windows\Fonts\segoeui.ttf",
        collocations=False
    ).generate(string_data)
    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return wordcloud

def make_wordcloud_figure_dict(dict_data, word_limit=50, color="gist_yarg"):
    wordcloud = WordCloud(
        width=2400,
        height=2400,
        relative_scaling=0,
        background_color=None,
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