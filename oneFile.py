from lxml import etree
import os
import pprint
from NLTKPreprocessor import NLTKPreprocessor

def main():
    pp = pprint.PrettyPrinter()
    cwd = os.getcwd()
    filePath = os.path.join(cwd, "positive_examples_anonymous/train_subject96.xml")

    root = etree.parse(filePath).getroot()
    userId = root[0].text

    userText = ''
    for post in root.findall('.//TITLE') + root.findall('.//TEXT'):
        post = post.text.strip()
        if post != '':
            userText += ' ' + post
    

    preprocessor = NLTKPreprocessor()
    print(preprocessor.transform([userText]))

if __name__ == '__main__':
    main()