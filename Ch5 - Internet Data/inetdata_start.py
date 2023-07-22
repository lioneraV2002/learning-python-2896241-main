# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#
import urllib.request


def main():
    # open a connection to a URL using urllib2
    # pass # this is a placeholder, do-nothing statement
    url = urllib.request.urlopen("https://www.google.com")
    # get the result code and print it
    print("result code: ", url.getcode())
    #
    # read the data from the URL and print it
    data = url.read()
    print(data)


if __name__ == "__main__":
    main()
