#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:06:44 2024

@author: chinaraazizova
"""

import pandas as pd
import numpy as np
import os
import PyPDF2
# pip install PyMuPDF

import fitz  # PyMuPDF

def convert_pdf_to_text(pdf_path, text_path):
    text = ""
    with fitz.open(pdf_path) as pdf_file:
        for page_num in range(pdf_file.page_count):
            page = pdf_file.load_page(page_num)
            text += page.get_text()
    with open(text_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

def main():
    # Directory containing PDF files
    pdf_directory = '/Users/chinaraazizova/Desktop/mpr'
    # Directory to store text files
    text_directory = '/Users/chinaraazizova/Desktop/mpr'

    for filename in os.listdir(pdf_directory):
        if filename.lower().startswith('da') or filename.lower().startswith('mpr'):
            if filename.lower().endswith('.pdf'):
                pdf_path = os.path.join(pdf_directory, filename)
                text_filename = filename.replace('.pdf', '.txt')
                text_path = os.path.join(text_directory, text_filename)
                convert_pdf_to_text(pdf_path, text_path)

if __name__ == "__main__":
    main()






def remove_text_after_keyword(file_path, keyword):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the index of the line containing the keyword
    index = None
    for i, line in enumerate(lines):
        if keyword in line:
            index = i
            break

    if index is not None:
        # Slice the lines list to keep only lines before the keyword
        lines = lines[:index]

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)


def remove_text_before_keyword(file_path, keyword):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the index of the line containing the keyword
    index = None
    for i, line in enumerate(lines):
        if keyword in line:
            index = i
            break

    if index is not None:
        # Slice the lines list to keep only lines starting from the keyword
        lines = lines[index:]

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)




def process_files(directory):
    # Iterate over files in the directory
    for filename in os.listdir(directory):
        if filename.startswith('da') and filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            remove_text_before_keyword(file_path, 'Ontario')
            remove_text_after_keyword(file_path, 'Information note')


# Specify the directory containing your text files
directory = '/Users/chinaraazizova/Desktop/mpr'

# Process the files in the directory
process_files(directory)






