# -*- coding: utf-8 -*-
import os
import random
import codecs
import pickle
import markdown
import webbrowser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


"""
Impress.py is a tool to make impress.js slides by text.
author: lihui
email: withlihui@gmail.com
website: withlihui.com
"""


part1 = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=1024" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <title>My SimpleWords</title>
    <link href="css/impress-demo.css" rel="stylesheet" />
    <link rel="apple-touch-icon" href="apple-touch-icon.png" />
"""

part2 = """
</head>
<body class="impress-not-supported">
    <div class="fallback-message">
        <p>很抱歉，你的浏览器不支持所需的特性，请更换至最新的<b>Chrome</b>, <b>Safari</b> 或 <b>Firefox</b>。</p>
        <p>Your browser <b>doesn't support the features required</b> by SimpleWords, please use the latest <b>Chrome</b>, <b>Safari</b> or <b>Firefox</b> browser.</p>
    </div>
    <div id="impress">
"""

part3 = """
    </div>
    <script src="js/jquery.min.js"></script>
    <script src="js/impress.js"></script>
    <script>impress().init();</script>
</body>
</html>
"""

os.chdir(os.getcwd())

class SimpleWords(object):
    def __init__(self):
        self.slides = []
        self.slide_html = "slides.html"
        self.file = open(self.slide_html, mode='w')          
        self.slide_txt = open("words.txt")

    def create(self, word, x, classname="step"): # classname: step or step slide
        slide = """
        <div class="%s" align="center" data-x="%d">
          %s
        </div>
        """ % (classname, x, word)
        self.slides.append(slide)

    def slide(self):
        self.pages = self.slide_txt.read().split("-----") # use ----- as separator
        length = len(self.pages)
        if length == 1: # use \n as separator (one line one page)
            self.pages = [line for line in open('words.txt').readlines() if len(line) != 1]
            length = len(self.pages)
        if "$$" in self.pages[0]:
            self.set_bgcolor(self.pages[0][2:].strip())
            print self.pages[0][2:].strip()
            self.pages.pop(0)
        else:
            self.color = " "
        pos_x = [x for x in range(-2000*length, 0, 2000)]
        for page in self.pages:
            page = markdown.markdown(page.decode('GBK', 'ignore').encode('utf-8'))
            self.create(page, pos_x.pop(0))

    def set_bgcolor(self, color):
        color_html = """
    <style>
      body {
        background: %s;
      }
    </style>""" % color
        self.color = color_html

    def save(self):
        self.file.write(part1 + "\n")
        self.file.write(self.color + "\n" + part2 +"\n")
        self.file.writelines(self.slides)
        self.file.write(part3)

    def preview(self):
        """
        open the slides in default browser
        """
        webbrowser.open("file:///" + os.getcwd() + "/" + self.slide_html)

    
if __name__ == "__main__":
    my_slide= SimpleWords()
    my_slide.slide()
    my_slide.save()
    my_slide.preview()
