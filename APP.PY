from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs=[]
n = int(input("how many pdfs you want to insert"))
for i in range(0,n):
    print("enter the name of the pdf")
    name = input(f"enter the name of the pdf {i+1}")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)
    

merger.write("merged-pdf.pdf")
merger.close()