# 
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#
# import the htmlparser module, you have to import from html.parser

from html.parser import HTMLParser

paragraphs = 0


# create a subclass of HTMLParser and override the handler methods
class MyHTMLParser(HTMLParser):
    # function to handle the processing of HTML comments
    def handle_comment(self, data):
        print("encountered comment:", data )
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    # function to handle an opening tag in the doc
    # this will be called when the closing ">" of the tag is reached
    def handle_starttag(self, tag, attrs):
        global paragraphs
        if tag == "p":
            paragraphs += 1

        print("emcountered a start tag, ", tag)
        pos = self.getpos()  # returns a tuple indicating line and character
        print("\tAt line: ", pos[0], " position ", pos[1])

        if attrs.__len__() > 0:
            print("attributes: ")
            for a in attrs:
                print(a[0], "=", a[1])

    # function to handle character and text data (tag contents)
    def handle_data(self, data):
        if data.isspace():
            return
        print("encountered some text data: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])


def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()

    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()  # read the entire file
        parser.feed(contents)


if __name__ == "__main__":
    main()
