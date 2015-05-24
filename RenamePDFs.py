__author__ = 'Vlasev'
from PyPDF2 import PdfFileReader
import os

'''I collect and read through a lot of math/physics papers and they all come in fairly different naming formats
so I have to rename them to something more readable so I will know which is which. The following script
does just that - it opens pdfs and uses the PyPdf2 package to read off their titles. If they have titles
which are not just "" then we use them to rename the pdfs. Unfortunately for my selection of papers the success rate is
around 50% and the ones where it succeeds are often in a slightly unpleasant format or have irrelevant titles.
Nevertheless it's a useful scrip that allows be to cut my work by a factor of 2 roughly.'''

# uncomment if you want to rename them in a generic format.
# num = 0
# for filename in os.listdir("."):
# 	if filename.endswith(".pdf"):
# 		os.rename(filename, "PDF Number {}.pdf".format(str(num)))
# 		num += 1

for filename in os.listdir("."):
	if filename.endswith(".pdf"):  # Only pick out the pdfs
		file = open(filename, "rb")
		try:
			input1 = PdfFileReader(file)
			if input1.isEncrypted:  # Since some files are encrypted
				input1.decrypt('')
			try:
				info = input1.getDocumentInfo()  # We try to get the pdf info. Sometimes the pdf doesn't have it
				try:
					if "/Title" in info:  # Same here. Sometimes the pdf doesn't have a title attribute
						tit = info["/Title"]
						if tit != "":
							'''On windows we need to close the file before renaming.
							Some of the pdfs come from conversions from other formats
							and the titles reflect that by having .djvu or .dvi at the end'''
							file.close()
							if tit.endswith(".djvu"):
								os.rename(filename, tit[:-5]+".pdf")
							elif tit.endswith(".dvi"):
								os.rename(filename, tit[:-4]+".pdf")
							else:
								os.rename(filename, tit+".pdf")
				except (RuntimeError, ValueError, NameError, OSError, TypeError):  # Honestly all these are not necessary.
					print("Error 3 at "+filename)
					continue
			except (RuntimeError, ValueError, NameError, OSError):  # Honestly all these are not necessary.
				print("Error 2 at "+filename)
		except ValueError:
			print("Error 1 at "+filename)
		file.close()
