import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("COET Pantry")
icon = pygame.image.load("groceries.png")
pygame.display.set_icon(icon)

font = pygame.font.Font("KGHolocene.ttf", 36)
textX = 280
textY = 40
def show_text(x, y):
    text = font.render("COET Pantry", True, (0, 0, 0))
    screen.blit(text, (x, y))

font1= pygame.font.Font("KGHolocene.ttf", 12)
ins_textX = 20
ins_textY = 100
def show_instruction(x, y):
    ins = font1.render("Instruction: Press the first letter of the desired item to withdraw. (Example: Press S to get a sardine.)", True, (0, 0, 0))
    screen.blit(ins, (x, y))

font2 = pygame.font.Font("KGHolocene.ttf", 20)
textX2 = 105
textY2 = 375
def show_get(x, y):
    text1 = font2.render("You successfully withdrawed the items below:", True, (0, 0, 0))
    screen.blit(text1, (x, y))


font3 = pygame.font.Font("KGHolocene.ttf", 18)
textX3 = 75
textY3 = 150
def show_sardines(x, y):
    item1 = font3.render("Sardines :" + str(sardines_value), True, (0, 0, 0))
    screen.blit(item1, (x, y))

font4 = pygame.font.Font("KGHolocene.ttf", 18)
textX4 = 230
textY4 = 150
def show_coffee(x, y):
    item2 = font4.render("Coffee :" + str(coffee_value), True, (0, 0, 0))
    screen.blit(item2, (x, y))

font5 = pygame.font.Font("KGHolocene.ttf", 18)
textX5 = 370
textY5 = 150
def show_noodles(x, y):
    item3 = font5.render("Noodles :" + str(noodles_value), True, (0, 0, 0))
    screen.blit(item3, (x, y))

font6 = pygame.font.Font("KGHolocene.ttf", 18)
textX6 = 510
textY6 = 150
def show_rice(x, y):
    item4 = font6.render("Rice :" + str(rice_value), True, (0, 0, 0))
    screen.blit(item4, (x, y))

font7 = pygame.font.Font("KGHolocene.ttf", 18)
textX7= 620
textY7 = 150
def show_egg(x, y):
    item5 = font7.render("Egg :" + str(egg_value), True, (0, 0, 0))
    screen.blit(item5, (x, y))


font8 = pygame.font.Font("KGHolocene.ttf", 20)
textX8 = 75
textY8 = 410
def show_sardines1 (x, y):
    item6 = font8.render("Sardines :" + str(u_get_S_value), True, (0, 0, 0))
    screen.blit(item6, (x, y))

font9 = pygame.font.Font("KGHolocene.ttf", 20)
textX9 = 230
textY9 = 410
def show_coffee1 (x, y):
    item7 = font9.render("Coffee :" + str(u_get_C_value), True, (0, 0, 0))
    screen.blit(item7, (x, y))

font10 = pygame.font.Font("KGHolocene.ttf", 20)
textX10 = 370
textY10 = 410
def show_noodles1 (x, y):
    item8 = font10.render("Noodles :"+ str(u_get_N_value), True, (0, 0, 0))
    screen.blit(item8, (x, y))

font11 = pygame.font.Font("KGHolocene.ttf", 20)
textX11 = 510
textY11 = 410
def show_rice1(x, y):
    item9 = font11.render("Rice :" + str(u_get_R_value), True, (0, 0, 0))
    screen.blit(item9, (x, y))

font12 = pygame.font.Font("KGHolocene.ttf", 20)
textX12 = 620
textY12 = 410
def show_egg1 (x, y):
    item10 = font12.render("Egg :" + str(u_get_E_value), True, (0, 0, 0))
    screen.blit(item10, (x, y))


font13 = pygame.font.Font("KGHolocene.ttf", 40)
textX13 = 125
textY13 = 475
def show_msg(x, y):
    msg = font13.render("Thank you for coming!", True, (0, 0, 0))
    screen.blit(msg, (x, y))

iconImg = pygame.image.load('cart.png')
iconX = 320
iconY = 200

def icon():
    screen.blit(iconImg, (iconX, iconY))

sardines_value = 5
coffee_value = 5
noodles_value = 5
rice_value = 5
egg_value = 5

u_get_S_value = 0
u_get_C_value = 0
u_get_N_value = 0
u_get_R_value = 0
u_get_E_value = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                sardines_value -= 1
                u_get_S_value += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                noodles_value -= 1
                u_get_N_value += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                coffee_value -= 1
                u_get_C_value += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                rice_value -= 1
                u_get_R_value += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                egg_value -= 1
                u_get_E_value += 1

    screen.fill((223, 255, 127))
    icon()
    show_text(textX, textY)
    show_get(textX2, textY2)
    show_instruction(ins_textX, ins_textY)
    show_msg(textX13, textY13)

    show_sardines(textX3, textY3)
    show_coffee(textX4, textY4)
    show_noodles(textX5, textY5)
    show_rice(textX6, textY6)
    show_egg(textX7, textY7)

    show_sardines1(textX8, textY8)
    show_coffee1(textX9, textY9)
    show_noodles1(textX10, textY10)
    show_rice1(textX11, textY11)
    show_egg1(textX12, textY12)

    pygame.display.update()