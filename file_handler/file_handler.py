from os.path import splitext
import csv


LINES_TO_READ = 5
TEXT = 'One\nTwo\nThree\nFour\nFive\nSix\nSeven\nEight\nNine\nTen'


class File:
	def __init__(self, file_path):
		self.path = file_path
		self.root, self.extension = splitext(file_path)

	def to_read(self, handler):
		handler.to_read(self.path)

	def to_write(self, handler):
		handler.to_write(self.path)


class HandlerFactory:
	def get_handler(self, extension):
		if extension == '.txt':
			return TxtHandler()
		elif extension == '.csv':
			return CsvHandler()
		else:
			raise RuntimeError(f"{extension} file extension is not supported.")


class FileHandler:
	def handle(self, mode, file):
		handler = factory.get_handler(file.extension)
		if mode == 'read':
			file.to_read(handler)
		elif mode == 'write':
			file.to_write(handler)


class TxtHandler:
	def to_read(self, file_path, lines_count=LINES_TO_READ):
		line_num = 0

		with open(file_path) as f:
			for line in f:
				if line_num < lines_count:
					print(line, end='')
					line_num += 1

	def to_write(self, file_path, text=TEXT):
		with open(file_path, 'w') as f:
			f.write(text)


class CsvHandler:
	def to_read(self, file_path, lines_count=LINES_TO_READ):
		row_num = 0

		with open(file_path) as f:
			reader = csv.reader(f)
			for row in reader:
				if row_num < lines_count:
					print(row[0], end='\n')
					row_num += 1

	def to_write(self, file_path, text=TEXT):
		text_to_write = text.split('\n')

		with open(file_path, 'w', newline='') as f:
			writer = csv.writer(f)

			for row in text_to_write:
				writer.writerow([row])


if __name__ == '__main__':

	factory = HandlerFactory()

	txt_file = File('txt_file.txt')
	csv_file = File('csv_file.csv')

	handler = FileHandler()

	handler.handle(mode='write', file=csv_file)
	handler.handle(mode='read', file=csv_file)


