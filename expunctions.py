import os
import subprocess

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# Before running this program, the system must also have installed:
# Tesseract OCR     - https://github.com/UB-Mannheim/tesseract/wiki
# ImageMagick       - https://imagemagick.org/script/download.php
# GhostScript       - https://www.ghostscript.com/releases/index.html

def pdf_to_text():
    for root, dirs, files in os.walk('.', topdown=True):
        for this_dir in dirs:
            os.chdir(this_dir)
            os.path.join(root, this_dir)

#            print("This dir is {}".format(os.path.join(root, this_dir)))
            this_files = os.listdir()
            for this_pdf in this_files:
                if this_pdf.endswith('pdf'):
#                    print("This PDF is {}".format(this_pdf))
                    file_prefix = this_pdf.removesuffix('.pdf')
#                    print("File Prefix:  {}".format(file_prefix))
                    magick_cmd = 'magick convert -density 200 \"' + this_pdf + '\" \"' + file_prefix + '.jpg\"'
#                    print("Command line is: {}".format(cmd))
                    # TODO: this only works for single-page PDFs
                    if not os.path.exists(file_prefix + '.jpg'):
                        subprocess.run(magick_cmd)
                    else:
                        print("{} exists, skipping ImageMagick".format(file_prefix + '.jpg'))
            this_files = os.listdir()
            for this_jpg in this_files:
                if this_jpg.endswith('.jpg'):
                    jpg_prefix = this_jpg.removesuffix('.jpg')
#                    print("Does {} exist: {}".format(jpg_prefix + '.txt', os.path.exists(jpg_prefix + '.txt')))
                    if not os.path.exists(jpg_prefix + '.txt'):
                        tesseract_cmd = 'tesseract \"' + this_jpg + '\" \"' + jpg_prefix + '\"'
                        subprocess.run(tesseract_cmd)
                    else:
                        print("{} exists, skipping Tesseract".format(jpg_prefix + '.txt'))

def search():
#    os.chdir('../')
    search_list = open('expungeScan.searchlist', "r")

    for root, dirs, files in os.walk('.', topdown=True):
        for this_dir in dirs:
            os.chdir(this_dir)
            this_files = os.listdir()
#            print("This files: {}".format(this_files))
            for this_jpg in this_files:
                if this_jpg.endswith('.jpg'):
#                    print("Searching {}".format(this_jpg))
                    jpg_text = pytesseract.image_to_string(Image.open(this_jpg))
#                    print("Image to text is: \n{}".format(jpg_text))
                    for search_line in search_list:
                        search_terms = search_line.split()
#                        print("Search terms: {}".format(search_terms))
                        if all(search_term in jpg_text for search_term in search_terms):
                            print("Match of {} found in {}".format(search_terms, this_jpg))
                    search_list.seek(0) # move file pointer to top of file again
    search_list.close() # close our search list file

#scan_and_move()
pdf_to_text()
search()
