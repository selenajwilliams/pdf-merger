import PyPDF2
import os

""" a simple script that merges & combines pdfs from an input_files folder
"""

def merge_pdfs(in_path, files, outfile):
    merger = PyPDF2.PdfMerger()

    print(f'list of files to merge:')
    [print(f) for f in files]
    print(f'merging files now...')
    # merge all the PDFs
    for pdf in files:
        with open(f'{in_path}{pdf}', 'rb') as f:
            merger.append(f)

    # write the merged PDF to a single output pdf
    # if the parent directory doesn't exist, create it 
    dir = os.path.dirname(outfile)
    if not os.path.exists(dir):
        os.makedirs(dir)

    with open(outfile, 'wb') as out:
        merger.write(out)
    
    print(f'Merged PDF saved as {outfile}')
    return outfile


def find_files(in_path) -> list[str]:
    if not os.path.exists(in_path):
        raise Exception(f'{in_path} does not exist.')

    files = []
    for file in os.listdir(in_path):
        files.append(file)
        
    if len(files) == 0:
        raise Exception(f'No files were found in {in_path}/ directory')
    return files

if __name__ == "__main__":
    in_path = "input_files/"
    out_path = "results"

    files = find_files(in_path) # a list of pdfs to merge
    files.sort()
    merged = merge_pdfs(in_path, files, f"{out_path}/biotech_lectures.pdf")