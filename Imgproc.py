 #import the classes from PIL
from PIL import Image, ImageDraw, ImageFont

punc = ['.', '!', '"', '\'', ',', '-', '?', ';', ' ']

class memeFormat:
	def __init__(self, memeName, memeLocName, memePicFormat):
		self.data = {}
		self.counter = 0
		self.name = memeName
		self.location = memeLocName
		self.picFormat = memePicFormat
		self.font = 'Roboto-Black.ttf'

	def addSlide(self, name, x, y, linesize, maxlines):
		self.data[self.counter] = { 	'name' : name,
					'x' : x,
					'y' : y,
					'linesize' : linesize,
					'maxlines' : maxlines}
		self.counter += 1

	def displayMeme(self):
		display = []
		display.append(self.name)
		display.append("\n")
		
		for template in self.data:
			display.append( "Name:\t" )
			display.append( self.data[template]['name'] )
			display.append( "\tMax. Chars:\t" )
			display.append( str(self.data[template]['linesize'] * self.data[template]['maxlines']) )
			display.append( "\n" )

		return ''.join(display)

	def doProc(self, template, userText, formatting = None):
		#userText = userText + ' '		
		if (len(userText) >= (self.data[template]['linesize'] * self.data[template]['maxlines'])):
			return ("ERROR: Too Long")
		TotalLines = []
		tempWord = []
		count = 0

		if (formatting != None):
			for i in range(0, len(userText), self.data[template]['linesize']):
				TotalLines.append(userText[i:i+self.data[template]['linesize']])
				
			print (TotalLines)

			self.printImage(TotalLines, template)
			return 1

		

		for i in range(0, len(userText), self.data[template]['linesize']):
			tempLine = userText[count:count+self.data[template]['linesize']]
			print (tempLine, type(tempLine))
			
			if (len(tempLine) < self.data[template]['linesize']):
				print (tempLine)
				TotalLines.append(tempLine)
				break

			if (tempLine[self.data[template]['linesize']-1] not in punc):
				j = self.data[template]['linesize']-1
				while (tempLine[j] not in punc):
					tempLine = tempLine[:-1]
					print(tempLine)
					j -= 1
				i = j
				count += i+1
				print (tempLine)
			else:
				count+=self.data[template]['linesize']
			print (len(tempLine))
			TotalLines.append(tempLine)
			print(TotalLines)
		print (TotalLines)

		"""while (len(userText) != 0):
			tempLine = userText[count:count+self.data[template]['linesize']]
			print (tempLine, len(tempLine))
			if (len(tempLine) < self.data[template]['linesize']):
				TotalLines.append(tempLine)
				break
			if (templine[self.data[template]['linesize']-1] not in punc):
			"""	 
				


		self.printImage(TotalLines, template)
		return 1
			

	def printImage(self, Lines, template):
		count = 0

		image = Image.open(self.location+"."+self.picFormat)
		font = ImageFont.truetype(str(self.font), size = 30)
		color = 'rgb(0,0,0)'
		
		draw = ImageDraw.Draw(image)

		for line in Lines:
			draw.text( (self.data[template]['x'], self.data[template]['y']+(30*count)), str(line), fill=color, font=font)
			count += 1

		image.save(self.location+"Modify."+self.picFormat)



drake = memeFormat("IminDanger", "imInDangerMeme", "png")
drake.addSlide("Lines", 30, 20, 35, 5)
#drake.addSlide("DrakeDown", 350, 290, 15, 6)
print (drake.displayMeme())

userText = str(input("Enter:"))

drake.doProc(0, userText)








#create the Image object (inputStarts)
"""image = Image.open("DrakeMeme.jpg")

#drawing context with image as background
draw = ImageDraw.Draw(image)

#sizein = int(input())

#font related stuff
font = ImageFont.truetype("Roboto-Black.ttf", size = 30)

#define color
color = 'rgb(0,0,0)'
"""







"""data

##########
Distracted:
red girl: 100,550
<!--
line_max = 25
max_lines=3
font-szie:30
-->
man: 500,350
3rd girl: 875,450

#########
Drake:
up :350,20
<!--
line_max = 15
max_lines = 6
font-size :30
-->
down: 350, 290

#########
ImInDanger:
<!--
start: 30,20
line_max = 35
max_lines = 5
font-size :30
-->

"""


