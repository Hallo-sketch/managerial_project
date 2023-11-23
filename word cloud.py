from wordcloud import WordCloud
import matplotlib.pyplot as plt

# List of phrases for the word cloud
phrases = [
    "Best PC graphics", "Best Adaptation or Use of License", "Best PC Game of 2011", "Best PC of 2011",
    "Studio of the Year (CD Projekt RED)", "Best PC Game of 2011", "Best PC Game of 2011", "Best PC Game",
    "Best Story", "Best European PC Game", "Best Game Design", "Best Gameworld", "Best Special Edition",
    "Best European Script", "Best Graphics Technology", "Best Looking Game", "Best Voice Acting",
    "Fanboy Award for Best PC Game", "Best European RPG Game", "Top 20 at Wired", "Best Graphics",
    "RPG of the Year", "Best RPG Narrative", "Best RPG Protagonist", "Best RPG Combat System",
    "Best Voice Cast", "Best Story", "Best RPG", "Best PC Game", "Game of the Year"
]

# Joining phrases into a single string with a newline character to keep each phrase separate
text_with_newlines = '\n'.join(phrases)

# Creating the word cloud with phrases as single elements
wordcloud_phrases = WordCloud(width=800, height=800, background_color='white', min_font_size=10, 
                              collocations=False, regexp=r"\w[\w' ]+").generate(text_with_newlines)

# Displaying the word cloud
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud_phrases, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.rcParams['pdf.fonttype'] = 42
plt.savefig('wordcloud.pdf', transparent=True)