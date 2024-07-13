#import python libraries to use them in code;
#Make sure the libraries you want to use are installed in your Python environment. 
# If not, you can install them using pip, Python's package installer. For example:
# used this command in terminal - pip install <library name>.
# Eg. --> pip install pandas

import os
import PyPDF2

# Specify the folder path containing the PDF files
folder_path = "pdf"  # Replace with your folder path

# Specify the output filename for the merged PDF
output_filename = "result.pdf"

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# List all files in the directory
pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

# Sort the files by name
pdf_files.sort()

# Loop through all the PDF files and append them to the merger
for pdf_file in pdf_files:
    pdf_path = os.path.join(folder_path, pdf_file)
    merger.append(pdf_path)

# Write the merged PDF to the output file
with open(output_filename, 'wb') as output_file:
    merger.write(output_file)

print(f"All PDFs merged into {output_filename}")
