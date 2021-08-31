from os.path import splitext
import csv


LINES_TO_READ = 5
TEXT = 'One\nTwo\nThree\nFour\nFive\nSix\nSeven\nEight\nNine\nTen\n'


class FileHandler:

	def __init__(self, file_path):
		self.file_path = file_path
		self.file_root, self.file_extension = splitext(file_path)


	def to_read(self, lines_count=LINES_TO_READ):

		if self.file_extension == ".txt":
			line_num = 0

			with open(self.file_path) as f:
				for line in f:
					if line_num < lines_count:
						print(line, end='')
						line_num += 1

		elif self.file_extension == ".csv":
	
			row_num = 0

			with open(self.file_path) as f:
				reader = csv.reader(f)
				for row in reader:
					if row_num < lines_count:
						print(row[0], end='\n')
						row_num += 1

		else:
			raise RuntimeError("This file extension is not supported.")


	def to_write(self, text=TEXT):

		if self.file_extension == ".txt":

			with open(self.file_path, 'w') as f:
				f.write(text)


		elif self.file_extension == ".csv":

			text_to_write = text.split('\n')

			with open(self.file_path, 'w', newline='') as f:
				writer = csv.writer(f)

				for row in text_to_write:
					writer.writerow([row])
	
		else:
			raise RuntimeError("This file extension is not supported.")


if __name__ == '__main__':

	csv_file = FileHandler('my_file.csv')
	txt_file = FileHandler('my_file.txt')

	txt_file.to_write()
	txt_file.to_read()

	csv_file.to_write()
	csv_file.to_read()

