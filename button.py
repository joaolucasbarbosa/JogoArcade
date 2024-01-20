import pygame.mixer

pygame.mixer.init()

click_sound = pygame.mixer.Sound("assets\\button_sound.wav")

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, play_click_sound=True):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.play_click_sound = play_click_sound

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if self.rect.collidepoint(position):
			if pygame.mouse.get_pressed()[0]:  # Verifica se o botão esquerdo do mouse está pressionado
				if self.play_click_sound:
					click_sound.play()  # Reproduz o som de "click" se ativado
				return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)