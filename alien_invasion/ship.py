import pygame
import settings

class Ship():
	
	def __init__(self, ai_settings, screen):
		self.screen=screen
		self.ai_settings = ai_settings
		
		#loading ship image and getting rectangle
		self.image=pygame.image.load('ship.jpg')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
				
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom-(int(70))
		
		self.center = float(self.rect.centerx)
		
		self.moving_right=False
		self.moving_left=False
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		self.rect.centerx=self.center
		
	
	def blitme(self):
		#drawing at current position		
		self.screen.blit(self.image, self.rect)
		
	
		

		
