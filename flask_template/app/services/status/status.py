import os
import json
import time
from flask import jsonify

class Status:
    def __init__(self) -> None:
        self._api_status = 200
        self._percentage = 0
        self._progress = 0
        self._total = 0
        
        self._detected_fails = 0
        self._process_status = None #self.process_status
        self._response = {} 
        self._ocr_process = None