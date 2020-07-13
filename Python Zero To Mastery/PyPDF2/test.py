import PyPDF2

with open('new_pdf.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)

	with open('wtr.pdf', 'rb') as wtm_file:
		watermark = PyPDF2.PdfFileReader(wtm_file)
		watermark_page = watermark.getPage(0)
		
		writer = PyPDF2.PdfFileWriter()

		for page in reader.pages:
			page.mergePage(watermark_page)
			writer.addPage(page)

		with open('watermarked.pdf', 'wb') as output_file:
			writer.write(output_file)


# inputs = sys.argv[1:]

# def pdf_combiner(pdf_list):
# 	merger = PyPDF2.PdfFileMerger()
# 	for pdf in pdf_list:
# 		merger.append(pdf)
# 	merger.write('new_pdf.pdf')


# pdf_combiner(inputs)





# with open('original.pdf', 'rb') as file:
# 	reader = PyPDF2.PdfFileReader(file)
# 	page = reader.getPage(0)
# 	page.rotateCounterClockwise(180)
# 	writer = PyPDF2.PdfFileWriter()
# 	writer.addPage(page)
# 	with open('tilted.pdf', 'wb') as new_file:
# 		writer.write(new_file)
