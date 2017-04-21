import urllib

def read_text():
    quotes = open('/Users/Emerson/Documents/workspace/LocalServer/movie_quotes.text')
    content = quotes.read()
    print(content)
    quotes.close()
    check_text(content)

def check_text(text):
    connection = urllib.urlopen(' http://www.wdylike.appspot.com/?q='+text)
    output = connection.read()
    print(output)
    connection.close()

read_text()