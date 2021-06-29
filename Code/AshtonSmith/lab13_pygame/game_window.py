import pygame

###########################GAME####CLASS################################
class game_main():
 #background
    #initalization    
    def __init__(self):
        self.root = pygame.init()
        self.screen = pygame.display.set_mode((800,600)) #args: height, width
        self.background = pygame.image.load('background.png')
        self.player_img = pygame.image.load('player.png')
        self.title_and_icon()
        self.player_x = 150
        self.player_y = 150



    #blit the player
    def player(self):
        self.screen.blit(self.player_img,(self.player_x, self.player_y))

    #this function uses the py gamefunction blit to set the icon
    def title_and_icon(self):
        pygame.display.set_caption('Tic-Tac-Toe')
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)



    # #this function uses the py gamefunction blit to draw the player
    # #   args: x coordinate, y coordinate 
    # def player(player_img, player_x, player_y):
    #     self.screen.blit(player_img, (player_x,player_y))



    #this function determines what to do when an event occurs, event meaning there was input from the player
    def key_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player_x_change = -.3
                print('key pressed Left')
            if event.key == pygame.K_RIGHT:
                self.player_x_change = .3
                print('key pressed right')

            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        print('key released')
                        self.player_x_change = 0
            
    # Game loop: this loop is ran continously while the game is open
    def game_loop(self):
        running = True
        player_x_change = 0
        player_y_change = 0
        
        while running:
            self.screen.blit(self.background,(0,0))   
            
            player_speed = .25 

            #Check for events:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):#if window closed
                    running = False
                if event.type == pygame.KEYDOWN:#key is pressed
                    if event.key == pygame.K_UP:
                        player_y_change = -player_speed
                        print('up')
                    elif event.key == pygame.K_DOWN:
                        player_y_change = player_speed
                        print('down')
                    if event.key == pygame.K_RIGHT:
                        player_x_change = player_speed
                        print('right')
                    elif event.key == pygame.K_LEFT:
                        print('left')
                        player_x_change = -player_speed
                if event.type == pygame.KEYUP:#key is let go
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        print('key released')
                        player_x_change = 0
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        player_y_change = 0
            
            self.player_x +=  player_x_change 
            self.player_y +=  player_y_change 
            self.player()
            pygame.display.update()



        #if player is within region range
        #args: player(x, y) boundary(x,y)
        #the regionswitch is used to determine what to multiply x and y by for the region
        def player_within_region(self, player_x, player_y, bound_x, bound_y, regionswitch):
            
            #used to determine what to multiply x and y by enorder to not require a function for each region
            region_key = {
                #0:1,#key: 
                1:90,#need to find what to multiply by for each region
                2:180,
                3:270,
                4:360,
            }
            #need to dertmine the paramaters for each region to select that region .. (the place on the screen) = the choice for tictactoe
            option = player_x < bound_x *regionswitch
            something = 'placeholder'
            if option == something:
                return True
            else:
                return False
                
#my object
my_obj = game_main()
my_obj.game_loop()

########################################################################