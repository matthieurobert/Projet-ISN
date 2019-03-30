class ARBot(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("sprite.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect = self.image.get_rect()
		#self.side = side
		#self.speed = 10
		self.state = "still"
		self.newpos = [0, 0]
		self.speed = [0, 2]
		self.update()

	
	def update(self):
		if self.rect.top < 0:
			self.newpos[1] = self.newpos[1] + self.speed[1]
			self.rect = self.rect.move(self.newpos)
		
		elif self.rect.bottom > 440:
			self.newpos[1] = self.newpos[1] - self.speed[1]
			self.rect = self.rect.move(self.newpos)
		
		else:
			self.newpos[1] = self.newpos[1] + self.speed[1]
			self.rect = self.rect.move(self.newpos)
		
		#print(self.speed)


class LRBot(pygame.sprite.Sprite):
	
	

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("sprite2.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect = self.image.get_rect()
		#self.side = side
		#self.speed = 10
		self.state = "still"
		self.newpos = [0, 0]
		self.speed = [2, 0]
		self.update()

	
	def update(self):
		if self.rect.left < 0:
			self.newpos[0] = self.newpos[0] + self.speed[0]
			self.rect = self.rect.move(self.newpos)
		
		elif self.rect.right > 440:
			self.newpos[0] = self.newpos[0] - self.speed[0]
			self.rect = self.rect.move(self.newpos)
		
		else:
			self.newpos[0] = self.newpos[0] + self.speed[0]
			self.rect = self.rect.move(self.newpos)
		
		#print(self.speed)

class RBot(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("sprite3.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect = self.image.get_rect()
		#self.side = side
		#self.speed = 10
		self.state = "still"
		self.newpos = [0, 0]
		self.speed = [2, ]
		self.update()

	
	def update(self):
		if self.rect.top < 0 and self.rect.left < 0:
			self.newpos[1] = self.newpos[1] + self.speed[1]
			self.newpos[0] = self.newpos[0] + self.speed[0]
			self.rect = self.rect.move(self.newpos)
		
		elif self.rect.bottom > 440 and self.rect.right > 440:
			self.newpos[1] = self.newpos[1] - self.speed[1]
			self.newpos[0] = self.newpos[0] - self.speed[0]
			self.rect=self.rect.move(self.newpos)
		elif self.rect.top < 0:
			self.newpos[1] = self.newpos[1] + self.speed[1]
			
			self.rect = self.rect.move(self.newpos)
		
		elif self.rect.bottom > 440:
			self.newpos[1] = self.newpos[1] - self.speed[1]
			
			self.rect = self.rect.move(self.newpos)

		elif self.rect.left < 0:
			self.newpos[0] = self.newpos[0] + self.speed[0]
			self.rect = self.rect.move(self.newpos)
		
		elif self.rect.right > 440:
			self.newpos[0] = self.newpos[0] - self.speed[0]
			self.rect = self.rect.move(self.newpos)
		
		else:
			self.newpos[1] = self.newpos[1] + self.speed[1]
			self.newpos[0] = self.newpos[0] + self.speed[0]
			self.rect = self.rect.move(self.newpos)
		
		#print(self.newpos)