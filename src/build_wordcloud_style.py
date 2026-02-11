from wordcloud import WordCloud
import matplotlib.pyplot as plt

def make_wordcloud_figure(string_data, word_limit=50):
    wordcloud = WordCloud(
        width=2400,
        height=1600,
        relative_scaling=0.5,
        background_color="black",
        min_word_length= 4,
        max_words= word_limit,
        colormap="Blues",
        font_path=r"C:\Windows\Fonts\segoeui.ttf",
        collocations=False
    ).generate(string_data)
    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")

    return wordcloud