import pytesseract
from pdf2image import convert_from_path
from app.utils.utils import Utils
import os
import PIL.Image
from pdf2image.exceptions import (
    PDFPageCountError,
)
from PIL import Image
import shutil

PIL.Image.MAX_IMAGE_PIXELS = None
os.environ["OMP_THREAD_LIMIT"] = "1"


class Ocr_Process(Utils):
    
    def __init__(self):
        print("constructor")

    def optical_character_recognition(self, file_name):
        try:
            path_results_txt = os.path.join(os.environ["GENERAL_PATH"],os.environ["OUTPUT_RESULTS_PATH"])
            is_file_exist = self.files_exist(file_name, os.environ["FILES_INPUT_PATH"])
            if is_file_exist:
                format_file = self.get_document_type(file_name)
                if "pdf" in format_file:
                    print("File processing: ", file_name)
                    type_file_result = ".txt"
                    is_file_exist_txt = self.files_exist(file_name + type_file_result, path_results_txt)
                    if is_file_exist_txt == False:
                        entire_path = os.path.join(os.environ["GENERAL_PATH"],os.environ["FILES_INPUT_PATH"])
                        pages = convert_from_path(entire_path + "/" + file_name,dpi=300,last_page=50,thread_count=5)
                        text = []
                        for page_num,img_blob in enumerate(pages):
                            text.append(
                                pytesseract.image_to_string(img_blob, lang="eng")
                            )
                        self.write_document(path_results_txt,file_name,text,"w")
                        print("Files Processed: ", file_name)
                    else:
                        print("txt already exists: ", file_name)
                else:
                    print("Format not accept: ", file_name)
            else:
                print("files does not exist: ", file_name)
        except PDFPageCountError as ex:
            print("Method failed with status code :" + str(ex))
    