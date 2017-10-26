#!/usr/bin/python
#-*- coding: utf-8 -*-

from apiclient.discovery import build

import efigie.config as config

def customSearch(theme):
  service = build("customsearch", "v1", developerKey=config.GOOGLE_DEVELOPER_KEY)
  res = service.cse().list(
    q=theme,
    cx= config.GOOGLE_CUSTOM_SEARCH,
    searchType= 'image',
    fileType='png',
    # imgSize Returns images of a specified size, where size can be one of: icon(256), small, medium, large, xlarge, xxlarge, and huge. (string)
    ).execute()
  return res
