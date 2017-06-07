from time import sleep
import time
from threading import Thread
from multiprocessing.pool import ThreadPool
import re

import os

from Search import models

from Search.Utils.ActionBook import ActionBook
from Search.Utils.Amazon import Amazon
from Search.Utils.GoodReads import GoodReads
from Search.Utils.OverDrive import OverDrive
from Search.Utils.YouTube import YouTube
from Search.Utils.ProxyService import ProxyService

SUMMARYfh = "Search\\Utils\\Results\\Summary.txt"

def ReadData(model,book):
    results = model.objects.filter(name=book.lower())
    if results:
        return results[0].url

class AllUtils(object):
    """docstring for AllSummeries"""
    def __init__(self, arg):
        super(AllSummeries, self).__init__()
        self.arg = arg
        
    def getAllSummeries(query):
        start = time.time()
        # ProxyService.getProxies()

        results = {}

        pattern = re.compile('\b\d{3}[a-zA-Z]{3}\b')
        if not query:
            results['EmptyError'] = 'Enter a book title'
            return results
        if pattern.match(query):
            results['RegexError'] = 'You have done something naughty..'
            return results


        booklist = [query.lower().strip()]

        print('Working on it...')

        pool = ThreadPool(processes=8)

        goodlist = pool.map(GoodReads.SummaryService, booklist)
        actionlist = pool.map(ActionBook.SummaryService, booklist)
        overdrivelist = pool.map(OverDrive.SummaryService, booklist)
        youtubelist = pool.map(YouTube.SummaryService, booklist)

        blink = [ReadData(models.BlinkMod,book) for book in booklist]
        fourmin = [ReadData(models.FourMinMod,book) for book in booklist]
        bizsum = [ReadData(models.BizSumMod,book) for book in booklist]
        kirkus = [ReadData(models.KirkusMod,book) for book in booklist]
        readit = [ReadData(models.ReadItForMeMod,book) for book in booklist]


        results['RegexError'] = None
        results['EmptyError'] = None
        results['goodlist'] = goodlist[0] if goodlist else None
        results['actionlist'] = actionlist[0] if actionlist else None
        results['overdrivelist'] = overdrivelist[0] if overdrivelist else None
        results['youtubelist'] = youtubelist[0] if youtubelist else None
        results['blink'] = blink[0] if blink else None
        results['fourmin'] = fourmin[0] if fourmin else None
        results['bizsum'] = bizsum[0] if bizsum else None
        results['kirkus'] = kirkus[0] if kirkus else None
        results['readit'] = readit[0] if readit else None

        end = time.time()
        print(end - start)
        return results

       

        





