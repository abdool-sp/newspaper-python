
import prep_news as pn
from prep_news import PrepareNews
import newspaper




## Listing available categories
categories = list()
categories = pn.categories()
i = 1
for category in categories:
    print(str(i) + ". " + category)
    i = i + 1



print()
print()
inp = input("Select category(By number):")
print("###########################################################################################################################")
ch = int(inp) - 1
print("Selected category: " + categories[ch] )

Article = PrepareNews(categories[ch])
Article.Fparse()
articles = Article.prepareArticle()



print()
print()

c = 0
for art in articles:
    c = c + 1
    print(str(c) + ". " + art.title)

print()
print()

selected_article = input("select Article(By Number): ")
selected_article = int(selected_article) - 1
print()
print()
print("###########################################################################################################################")
print(articles[selected_article].title)
print()
print(articles[selected_article].text)
