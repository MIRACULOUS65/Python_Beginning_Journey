from PyPDF2 import PdfWriter

merger = PdfWriter()

pdf=[]
n= int (input("Enter number of pdf files to be merged: "))
for i in range(n):
    pdf.append(input(f"Enter name of pdf file {i+1}: "))

for i in pdf:
    merger.append(i)

merger.write("merged.pdf")
merger.close()