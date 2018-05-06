 #import the classes from PIL
from PIL import Image, ImageDraw, ImageFont
from time import sleep

punc = ['.', '!', '"', '\'', ',', '-', '?', ';', ' ']

version = '0.1.2'
print ("\n\n"+ str(version) +"\n\n")

class memeFormat:
	def __init__(self, memeName, memeLocName, memePicFormat):
		self.data = {}
		self.counter = 0
		self.name = memeName
		self.location = memeLocName
		self.picFormat = memePicFormat
		self.font = 'Roboto-Black.ttf'

	def addSlide(self, name, coordinates, linesize, maxlines):
				
		self.data[self.counter] = { 	'name' : name,
					'x' : coordinates[0],
					'y' : coordinates[1],
					'linesize' : linesize,
					'maxlines' : maxlines}
		self.counter += 1

	def displayMeme(self):
		display = []
		display.append( "Meme Name:\t" )
		display.append( self.name )
		display.append( "\nNumber of Templates:\t" )
		display.append( str(self.counter) + "\n\n\n" )
		count = 1
	
		for template in self.data:
			display.append( str(count) )
			count += 1
			display.append( ".\nName:\t" )
			display.append( self.data[template]['name'] )
			display.append( "\nMax. Chars:\t" )
			display.append( str(self.data[template]['linesize'] * self.data[template]['maxlines']) )
			display.append( "\n_________\n\n" )

		return ''.join(display)

	def memeControl(self, formatting = None):
		print (self.displayMeme())

		AllLines = []

		for template in range (0, self.counter, 1):
			print ("\nEnter Template:\t"+str(template+1))
			userText = str(input()) 

			if (len(userText) >= (self.data[template]['linesize'] * self.data[template]['maxlines'])):
				return ("ERROR: Too Long")
		
			TotalLines = []
			tempWord = []
			count = 0

			if (formatting != None):
				for i in range(0, len(userText), self.data[template]['linesize']):
					TotalLines.append(userText[i:i+self.data[template]['linesize']])
					
				print (TotalLines)
				break
				#self.printImage(TotalLines, template)
				#return 1

			while (len(userText) != 0):
				tempWord = (userText[:self.data[template]['linesize']])

				if (len(tempWord) < self.data[template]['linesize']):
					TotalLines.append(''.join(tempWord))
					userText = ''
					break

				if (tempWord[self.data[template]['linesize']-1] not in punc):
					if (userText[self.data[template]['linesize']] in punc):
						TotalLines.append(''.join(tempWord))
						userText = userText[self.data[template]['linesize']+1:]

					else:
						enum = 0
						referrer = self.data[template]['linesize']-1

						while (tempWord[referrer-enum] not in punc):
							tempWord = tempWord[:-1]							
							enum += 1	

						userText = userText[referrer-enum+1:]
						TotalLines.append(''.join(tempWord))

				else:
					TotalLines.append(''.join(tempWord))
					userText=userText[self.data[template]['linesize']:]

			AllLines.append(TotalLines)
		
		print (AllLines)
		
		self.printImage(AllLines)
		return 1
			

	def printImage(self, AllLines):
		image = Image.open(self.location+"."+self.picFormat)
		font = ImageFont.truetype(str(self.font), size = 30)
		color = 'rgb(0,0,0)'
		
		draw = ImageDraw.Draw(image)
		
		for template in range(0, self.counter, 1):
			count = 0
			for line in AllLines[template]:
				draw.text( (self.data[template]['x'], self.data[template]['y']+(30*count)), str(line), fill=color, font=font)
				count += 1

		image.save(self.location+"Modify."+self.picFormat)



drake = memeFormat("Drake Meme", "DrakeMeme", "jpg")
drake.addSlide("DrakeTop", (350, 20), 15, 6)
drake.addSlide("DrakeDown", (350, 290), 15, 6)


result = drake.memeControl()
if (result == 1):
	print ("Okie Dokie! DONE!")
else:
	print (result)

"""imInDanger = memeFormat("Im In Danger Meme", "imInDanger", "png")
imInDanger.addSlide("NormalLines", (30, 20), 35, 5)"""
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


