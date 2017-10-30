import newspaper
import feedparser


rssurl = ""
news = list()


L = ['Entertainment', 'Science and Technology', 'Politics', 'Business']
def categories():
    ## This are the categories present in the __init__ method. if any category should be added, both method should nbe altered accordingly
    L = ['Entertainment', 'Science and Technology', 'Politics', 'Business']
    return L


class PrepareNews:

    ## can substitute the rss url with one's choice and add categories accordingly
    def getCategories(self):
        L = ['Entertainment', 'Science and Technology', 'Politics', 'Business']
        return L

    def __init__(self, category):
        global rssurl
        if category == "Entertainment":
            rssurl = 'http://feeds.skynews.com/feeds/rss/entertainment.xml'
        if category == "Science and Technology":
            rssurl = 'http://rss.cnn.com/rss/edition_technology.rss'
        if category == "Politics":
            rssurl = 'http://feeds.bbci.co.uk/news/politics/rss.xml?edition=uk'
        if category == "Business":
            rssurl = 'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/business/rss.xml'




    def Fparse(self):
        global Links
        Links = list()
        feed = feedparser.parse(rssurl)
        entries = feed.entries

        for entry in entries:
            Links.append(entry.link)

    def prepareArticle(self):
        global news
        downloadedArticles = list()
        news = list()
        for link in Links:
            news.append(newspaper.Article(link,language = 'en'))
        i = 0
        for News in news:
            News.download()
            i = i + 1
            try:
                News.parse()
                downloadedArticles.append(News)
            except:
                 print("could not download link " + str(i))




        return downloadedArticles

