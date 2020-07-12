import requests
from lxml import etree
import lxml.html
import csv

domain = "https://euler.jakumo.org/problems/view/"
filePath = 'problems/problems.txt'

def parse(url):
    #Data extraction
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    title = tree.xpath('//*[@class="probTitle"]/text()')
    problem = tree.xpath('//*[@class="problem_content"]/p/text()')

    #Formation of a string from the received data
    output = title[0] + '\n'
    for i in problem:
        output += i
    return output
 
def main():
    print('STARTING PARSING')

    #Open file
    f = open(filePath, 'a', encoding="utf-8")

    #Search of pages
    i = 1
    while i < 700:
        print(i)
        f.write(str(i) + ') ' + parse(domain + str(i) + '.html') + '\n\n\n')
        i += 1
        
    f.close()
    print('DONE')

if __name__ == "__main__":
    main()
