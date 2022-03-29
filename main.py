#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:10:07 2022

@author: dmytrenko.o
"""
import stanza

nlp = stanza.Pipeline(lang='en', processors='tokenize,sentiment')
doc = nlp('I love that they banned Mox Opal. Good. Bad.')
for i, sentence in enumerate(doc.sentences):
    print(i, sentence.sentiment)