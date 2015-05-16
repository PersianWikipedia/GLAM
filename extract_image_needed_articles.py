# -*- coding: utf-8  -*-

# (C) Amir Sarabadani 2015
# License: MIT
import pywikibot
from pywikibot import pagegenerators
from pywikibot.textlib import extract_templates_and_params as extract
import codecs
import sys
import re

city = pywikibot.input('City?')
site = pywikibot.Site('fa')
cat = pywikibot.Category(site, u'رده:بناهای تاریخی ' + city)
gen = pagegenerators.CategorizedPageGenerator(cat, True)
pregen = pagegenerators.PreloadingGenerator(gen)


def main():
    res = u''
    for page in pregen:
        image = None
        try:
            text = page.get()
        except:
            continue
        if re.search(ur'\[\[([Ff]ile|پرونده|تصویر|[Ii]mage)\:', text):
            continue
        for i in extract(text.split('\n==')[0]):
            if i[0] == u'جعبه جای‌های تاریخی ایران':
                image = i[1].get(u'تصویر', '').strip()
        if image:
            continue
        address = re.findall(
            ur'در \[\[%s\]\]، (.+?) واقع شده و این اثر' % city, text)
        res += u'*[[%s]]' % page.title()
        if address:
            res += u': %s' % address[0]
        res += '\n'
        with codecs.open('res_glam.txt', 'w', 'utf-8') as f:
            f.write(res)

if __name__ == "__main__":
    try:
        main()
    finally:
        pywikibot.stopme()

