import argparse
import os
class DigitRemover():
	def __init__(self,args):
		self.Args = args
	def main(self):
		path = self.Args.InputSRTFile
		ofile = f'{os.path.splitext(path)[0]}_touched.txt'
		os.system(f'rm -f {ofile}') 
		with open(path,'r') as sub:
			for line in sub:
				line = line.strip()
				with open(ofile, 'a') as file:
					try:file.write(line + '\n') if DigitRemover.not_digit(line[0]) and DigitRemover.not_digit(line[-1]) else None
					except IndexError: file.write('\n')
				file.close()
		sub.close()
	def not_digit(char): return not char.isdigit()
if __name__=='__main__':
	parser = argparse.ArgumentParser(description = "this script receives a srt file and deletes lines starting with time and numbers and outputs a text file containing only text")
	parser.add_argument("-InputSRTFile", "--InputSRTFile", type=str, required=True, dest="InputSRTFile")
	args = parser.parse_args()
	DigitRemover(args).main()
