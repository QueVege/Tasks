from os.path import splitext
import csv
import argparse
import pandas as pd


LINES_TO_READ = 5
TEXT = 'One\nTwo\nThree\nFour\nFive\nSix\nSeven\nEight\nNine\nTen'


def is_valid_extension(parser, file):
	extension = splitext(file)[1]
	if extension not in ['.txt', '.csv', '.xls']:
		parser.error(f'{extension} file extension is not supported.')
	else:
		return file


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
		elif extension == '.xls':
			return XlsHandler()
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
		rows = pd.read_csv(file_path, usecols=['Rows'], nrows=lines_count)
		print(rows)

	def to_write(self, file_path, text=TEXT):
		text_to_write = text.split('\n')

		df = pd.DataFrame({'Rows': text_to_write})
		df.to_csv(file_path)


class XlsHandler:
	def to_read(self, file_path, lines_count=LINES_TO_READ):
		rows = pd.read_excel(file_path, usecols=['Rows'], nrows=lines_count)
		print(rows)

	def to_write(self, file_path, text=TEXT):
		text_to_write = text.split('\n')

		df = pd.DataFrame({'Rows': text_to_write})
		df.to_excel(file_path)


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--mode', required=True, choices=['read', 'write'],
							help='file mode to handle the file')

	parser.add_argument('--file', required=True, type=lambda f: is_valid_extension(parser, f),
							help='path to the file for reading/writing')

	args = parser.parse_args()

	factory = HandlerFactory()
	handler = FileHandler()
	handler.handle(mode=args.mode, file=File(args.file))

