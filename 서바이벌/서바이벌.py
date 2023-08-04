import pygame
import random
import enemy
import attack_1
import attack_2
import xp
import math
###############################################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 1900    # 가로 크기
screen_height = 1000   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# FPS
clock = pygame.time.Clock()

# 화면 타이틀 설정
pygame.display.set_caption("서바이벌")  # 게임 이름

###############################################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load(".\\테스트_배경.png")

character1 = pygame.image.load(".\\테스트_캐릭터.png")
character1_size = character1.get_rect().size
character1_width = character1_size[0]
character1_height = character1_size[1]
character1_x_pos = screen_width/2 - character1_width/2
character1_y_pos = screen_height/2 - character1_height/2
character1_speed = 0.8
character1_to_x = 0
character1_to_y = 0
character1_level = 1
character1_pre_level = 1
character1_max_hp = 50
character1_hp_lengh = 80
character1_hp = 50
character1_max_xp = character1_level*10
character1_xp_lengh = 80
character1_xp = 0
character1_attack_speed_level = 0
character1_attack_speed_max_level = 10
character1_bs_level = 0
character1_bs_max_level = 5
character1_speed_level = 0
character1_speed_max_level = 5
character1_hp_level = 0
character1_hp_max_level = 5
character1_attack_2_stack = 0
character1_attack_2_level = 0
character1_attack_2_max_level = 2

enemy_pos = []
enemy_list = []
enemy_spawn = 0
enemy_die = 0
enemy_new = 0
enemy_total = 5
enemy_new_spawn_num = 0
enemy_ticks = 0
enemy_pre_ticks = 0
enemy_num_up = False

xp_list = []
xp_width = 15
xp_height = 15

choose_background = pygame.image.load(".\\테스트_choose_background.png")
choose_background_size = choose_background.get_rect().size
choose_background_width = choose_background_size[0]
choose_background_height = choose_background_size[1]
choose_background_x_pos = screen_width/2 - choose_background_width/2
choose_background_y_pos = screen_height/2 - choose_background_height/2

choose_option = 1
choose_skill_num = -1
choose_list = []
choose_start_time = 0
choose_end_time = 0
choose_total_time = 0
choose_time = 0
choose_total_time_plus = False
flag_1 = False
flag_2 = False
choose_able_option = [1,2,3,4,5]
choose_option_max = 3
choose_option_remove_1 = False
choose_option_remove_2 = False
choose_option_remove_3 = False
choose_option_remove_4 = False
choose_option_remove_5 = False


now_time_m = 0
now_time_s = 0

choose_option_1 = pygame.image.load(".\\테스트_choose_option_1.png")
choose_option_2 = pygame.image.load(".\\테스트_choose_option_2.png")
choose_option_3 = pygame.image.load(".\\테스트_choose_option_3.png")
choose_option_4 = pygame.image.load(".\\테스트_choose_option_4.png")
choose_option_5 = pygame.image.load(".\\테스트_choose_option_5.png")

pause = False

die = False

win = False

character1_attack_1 = attack_1.Attack()
character1_attack_2 = attack_2.Attack()

info_game_font = pygame.font.Font(None,40)
game_font = pygame.font.Font(None, 100)

runing = True 
while runing:
    dt = clock.tick(144) 

    now_time = pygame.time.get_ticks() - (choose_total_time + choose_time)

    enemy_ticks = int(now_time/7500)

    if enemy_pre_ticks != enemy_ticks:
        enemy_num_up = True
        enemy_pre_ticks = enemy_ticks
    
    if enemy_num_up:
        enemy_num_up = False
        enemy_total += enemy_ticks

    # set pos constantly
    while len(enemy_pos) < enemy_total:
        if len(enemy_pos) % 4 == 0:
            enemy_pos.append((random.randint(-40, screen_width), -50))
        elif len(enemy_pos) % 4 == 1:
            enemy_pos.append((screen_width+10, random.randint(-40, screen_height)))
        elif len(enemy_pos) % 4 == 2:
            enemy_pos.append((random.randint(-40, screen_width), screen_height+10))
        elif len(enemy_pos) % 4 == 3:
            enemy_pos.append((-50, random.randint(-40, screen_height)))
        enemy_new += 1

    # set enemies
    for i in range(enemy_spawn, enemy_spawn+enemy_new):
        enemy_list.append(enemy.Enemy(enemy_pos[i][0], enemy_pos[i][1], 0.3))
        enemy_spawn += 1
    enemy_new = 0

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                character1_to_x -= character1_speed
            if event.key == pygame.K_d:
                character1_to_x += character1_speed
            if event.key == pygame.K_w:
                character1_to_y -= character1_speed
            if event.key == pygame.K_s:
                character1_to_y += character1_speed
            if pause == True:
                if event.key == 13:
                    if choose_list[(choose_option-1) % len(choose_list)] == 1:
                        if character1_attack_2_level != character1_attack_2_max_level:
                            flag_2 = True
                    if choose_list[(choose_option-1) % len(choose_list)] == 2:
                        if character1_attack_speed_level != character1_attack_speed_max_level:
                            flag_2 = True
                    if choose_list[(choose_option-1) % len(choose_list)] == 3:
                        if character1_bs_level != character1_bs_max_level:
                            flag_2 = True
                    if choose_list[(choose_option-1) % len(choose_list)] == 4:
                        if character1_speed_level != character1_speed_max_level:
                            flag_2 = True
                    if choose_list[(choose_option-1) % len(choose_list)] == 5:
                        if character1_hp_level != character1_hp_max_level:
                            flag_2 = True

                if flag_2 == True:
                    pause = False
                    choose_skill_num = (choose_option-1)%3
                    flag_2 = False

                if event.key == pygame.K_UP:
                    choose_option -= 1
                if event.key == pygame.K_DOWN:
                    choose_option += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                character1_to_x = 0
            if event.key == pygame.K_d:
                character1_to_x = 0
            if event.key == pygame.K_w:
                character1_to_y = 0
            if event.key == pygame.K_s:
                character1_to_y = 0

    if pause == True:
        character1_to_x = 0
        character1_to_y = 0

    # 3. 게임 캐릭터 위치 정의
    character1_x_pos += character1_to_x
    if character1_x_pos <= 20:
        character1_x_pos = 20
    if character1_x_pos >= screen_width-character1_width-20:
        character1_x_pos = screen_width-character1_width-20
    character1_y_pos += character1_to_y
    if character1_y_pos <= 20:
        character1_y_pos = 20
    if character1_y_pos >= screen_height-character1_height-20:
        character1_y_pos = screen_height-character1_height-20

    # for e in enemy_list:
    #     if character1_x_pos + character1_width/2 - (e.x+e.width/2) >= 0:
    #         e.x += math.cos(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s
    #         e.y += math.sin(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s
    #     else:
    #         e.x -= math.cos(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s
    #         e.y -= math.sin(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s


    # 4. 충돌 처리
   
    character1_rect = character1.get_rect()
    character1_rect.left = character1_x_pos
    character1_rect.top = character1_y_pos

    for e in enemy_list:
        e.rect = e.img.get_rect()
        e.rect.left = e.x
        e.rect.top = e.y
        e.move = not pause

    for e in enemy_list:
        for k in enemy_list:
            if e.x == k.x and e.y == k.y:
                pass
            elif e.rect.colliderect(k.rect):
                d1 = ((character1_x_pos + character1_width/2) - (e.x+e.width/2))**2 + ((character1_y_pos + character1_height/2) - (e.y+e.height/2))**2
                d2 = ((character1_x_pos + character1_width/2) - (k.x+k.width/2))**2 + ((character1_y_pos + character1_height/2) - (k.y+k.height/2))**2
                if d2 >= d1:
                    k.move = False

                    # if ((character1_x_pos + character1_width/2) - (k.x+k.width/2))**2 > ((character1_y_pos + character1_height/2) - (k.y+k.height/2))**2:
                    #     if character1_x_pos + character1_width/2 - (k.x+k.width/2) >= 0:
                    #         k.y -= math.sin(math.atan((character1_y_pos + character1_height/2-(k.y+k.height/2))/(character1_x_pos + character1_width/2-(k.x+k.width/2)+ 1e-9))) * k.s
                    #     else:
                    #         k.y += math.sin(math.atan((character1_y_pos + character1_height/2-(k.y+k.height/2))/(character1_x_pos + character1_width/2-(k.x+k.width/2)+ 1e-9))) * k.s
                    # else:
                    #     if character1_x_pos + character1_width/2 - (e.x+e.width/2) >= 0:
                    #         k.x -= math.cos(math.atan((character1_y_pos + character1_height/2-(k.y+k.height/2))/(character1_x_pos + character1_width/2-(k.x+k.width/2)+ 1e-9))) * k.s
                    #     else:
                    #         k.x += math.cos(math.atan((character1_y_pos + character1_height/2-(k.y+k.height/2))/(character1_x_pos + character1_width/2-(k.x+k.width/2)+ 1e-9))) * k.s
                else:
                    e.move = False

                    # if ((character1_x_pos + character1_width/2) - (e.x+e.width/2))**2 > ((character1_y_pos + character1_height/2) - (e.y+e.height/2))**2:
                    #     if character1_x_pos + character1_width/2 - (e.x+e.width/2) >= 0:
                    #         e.y -= math.sin(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s
                    #     else:
                    #         e.y += math.sin(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s
                    # else:
                    #     if character1_x_pos + character1_width/2 - (e.x+e.width/2) >= 0:
                    #         e.x -= math.cos(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s
                    #     else:
                    #         e.x += math.cos(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s

    for e in enemy_list:
        if e.move:
            if character1_x_pos + character1_width/2 - (e.x+e.width/2) >= 0:
                e.x += math.cos(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s
                e.y += math.sin(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s
            else:
                e.x -= math.cos(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s
                e.y -= math.sin(math.atan((character1_y_pos + character1_height/2-(e.y+e.height/2))/(character1_x_pos + character1_width/2-(e.x+e.width/2)+ 1e-9))) * e.s

    
    for e in enemy_list:
        now_time = pygame.time.get_ticks() - (choose_total_time + choose_time)
        if character1_rect.colliderect(e.rect) and e.attack == True:
            character1_hp -= e.damage
            e.attack_time = now_time
            e.attack = False
        if character1_rect.colliderect(e.rect) and e.attack == False:
            if (now_time - e.attack_time)/1000 >= e.attack_ready_time:
                e.attack = True
        if character1_hp <= 0:
            die = True
            runing = False
            break
    
    now_time = pygame.time.get_ticks() - (choose_total_time + choose_time)
    if character1_attack_1.learn and not pause:
        character1_attack_1.rect = character1_attack_1.img.get_rect()
        character1_attack_1.rect.left = character1_attack_1.x
        character1_attack_1.rect.top = character1_attack_1.y
        if (now_time - character1_attack_1.attack_time)/1000 >= character1_attack_1.attack_ready_time:
            character1_attack_1.attack = True
            character1_attack_1.attack_motion = True
            character1_attack_2.attack = True
        if character1_attack_1.attack:
            for i in range(len(enemy_list)-1, -1, -1):
                if character1_attack_1.rect.colliderect(enemy_list[i].rect):
                    enemy_list[i].hp -= character1_attack_1.damage
                    if enemy_list[i].hp >= 0: 
                        character1_hp += (character1_attack_1.damage/10 * character1_bs_level) / 4
                    else:
                        character1_hp += ((character1_attack_1.damage + enemy_list[i].hp)/10 * character1_bs_level) / 4
                    if character1_hp > character1_max_hp:
                        character1_hp = character1_max_hp
            character1_attack_1.attack_time = now_time
            character1_attack_2_stack += 1
            character1_attack_1.attack = False

    if character1_attack_2.learn and  not pause and (character1_attack_2_stack % (4-character1_attack_2_level)) == 0:
        character1_attack_2.rect = character1_attack_2.img.get_rect()
        character1_attack_2.rect.left = character1_attack_2.x
        character1_attack_2.rect.top = character1_attack_2.y
        if character1_attack_2.attack:
            for i in range(len(enemy_list)-1, -1, -1):
                if character1_attack_2.rect.colliderect(enemy_list[i].rect):
                    enemy_list[i].hp -= character1_attack_2.damage
                    if enemy_list[i].hp >= 0:
                        character1_hp += (character1_attack_2.damage/10 * character1_bs_level) / 4
                    else:
                        character1_hp += ((character1_attack_2.damage + enemy_list[i].hp)/10 * character1_bs_level) / 4
                    if character1_hp > character1_max_hp:
                        character1_hp = character1_max_hp
            character1_attack_2.attack = False

    for i in range(len(enemy_list)-1, -1, -1):
        if enemy_list[i].hp <= 0:
            xp_list.append(xp.Xp(enemy_list[i].x + (enemy_list[i].width/2) - (xp_width/2), enemy_list[i].y + (enemy_list[i].height/2) - (xp_height/2)))
            enemy_list.pop(i)
            enemy_die += 1

    for i in range(len(xp_list)-1, -1, -1):
        if character1_rect.colliderect(xp_list[i]):
            character1_xp += 3
            xp_list.pop(i)
            if character1_xp >= character1_level*10:
                character1_xp = 0
                character1_level += 1

    if character1_level != character1_pre_level:
        pause = True
        character1_pre_level = character1_level


    # character1_to_enemy_min = 5000000
    # if character1_attack_1.attack_direction_check: 
    #     for e in enemy_list:
    #         if character1_to_enemy_min >= ((character1_x_pos + character1_width/2) - (e.x+e.width/2))**2 + ((character1_y_pos + character1_height/2) - (e.y+e.height/2))**2:
    #             character1_to_enemy_min = ((character1_x_pos + character1_width/2) - (e.x+e.width/2))**2 + ((character1_y_pos + character1_height/2) - (e.y+e.height/2))**2
    #             if character1_x_pos >= e.x:
    #                 character1_attack_1.attack_direction = 0
    #             else:
    #                 character1_attack_1.attack_direction = 1           
    # if character1_attack_1.attack_direction == 0:
    #     character1_attack_1.x = character1_x_pos - character1_attack_1.width
    #     character1_attack_1.y = character1_y_pos
    # elif character1_attack_1.attack_direction == 1:
    #     character1_attack_1.x = character1_x_pos + 30
    #     character1_attack_1.y = character1_y_pos
    # character1_attack_1.attack_direction_check = False

    character1_attack_1.x = (character1_x_pos+(character1_width/2)) - (character1_attack_1.width/2)
    character1_attack_1.y = (character1_y_pos+(character1_height/2)) - (character1_attack_1.height/2)

    character1_attack_2.x = (character1_x_pos+(character1_width/2)) - (character1_attack_2.width/2)
    character1_attack_2.y = (character1_y_pos+(character1_height/2)) - (character1_attack_2.height/2)

            
    # 5. 화면에 그리기


    screen.blit(background, (0,0))

    now_time = pygame.time.get_ticks() - (choose_total_time + choose_time)

    for x in xp_list:
        screen.blit(x.img, (x.x, x.y))

    if character1_attack_2.learn and character1_attack_1.attack_motion and (character1_attack_2_stack % (4-character1_attack_2_level)) == 0:
        screen.blit(character1_attack_2.img, (character1_attack_2.x, character1_attack_2.y))

    if character1_attack_1.attack_motion:
        screen.blit(character1_attack_1.img, (character1_attack_1.x, character1_attack_1.y))
        if (now_time - character1_attack_1.attack_time)/1000 >= character1_attack_1.attack_motion_remain_time:
            character1_attack_1.attack_motion = False

    screen.blit(character1, (character1_x_pos, character1_y_pos))


    # built enemies
    for e in enemy_list:
        screen.blit(e.img, (e.x, e.y))


    pygame.draw.rect(screen,(255,0,0), (character1_x_pos+character1_width/2-character1_hp_lengh/2,character1_y_pos+character1_height+7,(character1_hp/character1_max_hp)*character1_hp_lengh,10))
    pygame.draw.rect(screen,(255,255,255), (character1_x_pos+character1_width/2-character1_hp_lengh/2,character1_y_pos+character1_height+7,character1_hp_lengh,10),2)

    pygame.draw.rect(screen,(0,0,255), (character1_x_pos+character1_width/2-character1_hp_lengh/2,character1_y_pos+character1_height+20,(character1_xp/(character1_level*10))*character1_xp_lengh,10))
    pygame.draw.rect(screen,(255,255,255), (character1_x_pos+character1_width/2-character1_hp_lengh/2,character1_y_pos+character1_height+20,character1_xp_lengh,10),2)

    now_time = pygame.time.get_ticks() - (choose_total_time + choose_time)
    now_time_m = round(now_time/1000) // 60
    now_time_s = round(now_time/1000) - (now_time_m*60)
    if now_time_s < 10:
        now_time_s = f'0{now_time_s}'

    show_level = (f'Level : {character1_level}')
    show_kill = (f'kill : {enemy_die}')
    show_time = (f'{now_time_m} : {now_time_s}')
    show_level_msg = info_game_font.render(str(show_level), True, (0,0,0))
    show_kill_msg = info_game_font.render(str(show_kill), True, (0,0,0))
    show_time_msg = info_game_font.render(str(show_time), True, (255,255,255))

    screen.blit(show_level_msg, (20, 20))
    screen.blit(show_kill_msg, (20, 60))
    screen.blit(show_time_msg, (screen_width/2-60, 20))

    if len(choose_able_option) < 3:
        choose_option_max = len(choose_able_option)
    if pause == True:
        if len(choose_list) != 0:
            screen.blit(choose_background, (choose_background_x_pos, choose_background_y_pos))
        while len(choose_list) < choose_option_max:
            new_option = random.randint(1,5)
            if new_option in choose_list:
                continue
            elif new_option == 1:
                if character1_attack_2_level == character1_attack_2_max_level:
                    continue
            elif new_option == 2:
                if character1_attack_speed_level == character1_attack_speed_max_level:
                    continue
            elif new_option == 3:
                if character1_bs_level == character1_bs_max_level:
                    continue
            elif new_option == 4:
                if character1_speed_level == character1_speed_max_level:
                    continue
            elif new_option == 5:
                if character1_hp_level == character1_hp_max_level:
                    continue
            choose_list.append(new_option)

        choose_option_x_pos = choose_background_x_pos + 30
        choose_option_y_pos = choose_background_y_pos + 25
        for n in choose_list:
            if n == 1:
                screen.blit(choose_option_1, (choose_option_x_pos, choose_option_y_pos))
            if n == 2:
                screen.blit(choose_option_2, (choose_option_x_pos, choose_option_y_pos))
            if n == 3:
                screen.blit(choose_option_3, (choose_option_x_pos, choose_option_y_pos))
            if n == 4:
                screen.blit(choose_option_4, (choose_option_x_pos, choose_option_y_pos))
            if n == 5:
                screen.blit(choose_option_5, (choose_option_x_pos, choose_option_y_pos))
            if n == 6:
                pass
            choose_option_y_pos += 225

        if len(choose_list) != 0:
            choose_rec_x_pos = choose_background_x_pos + 30
            choose_rec_y_pos = choose_background_y_pos + 25 + 225*((choose_option-1)%len(choose_list))
            pygame.draw.rect(screen,(255,255,255), (choose_rec_x_pos, choose_rec_y_pos, 360, 200), 8)

        if len(choose_list) == 0:
            win = True
            runing = False
    
    if choose_skill_num != -1:
        if choose_list[choose_skill_num] == 1:
            character1_attack_2.learn = True
            character1_attack_2_level += 1
            if character1_attack_2_level > character1_attack_2_max_level:
                character1_attack_2_level = character1_attack_2_max_level

        elif choose_list[choose_skill_num] == 2:
            character1_attack_speed_level += 1
            if character1_attack_speed_level > character1_attack_speed_max_level:
                character1_attack_speed_level = character1_attack_speed_max_level
            character1_attack_1.attack_ready_time = 2.5 * ((10-character1_attack_speed_level/2)/10)

        elif choose_list[choose_skill_num] == 3:
            character1_bs_level += 1
            if character1_bs_level > character1_bs_max_level:
                character1_bs_level = character1_bs_max_level

        elif choose_list[choose_skill_num] == 4:
            character1_speed_level += 1
            if character1_speed_level > character1_speed_max_level:
                character1_speed_level = character1_speed_max_level
            character1_speed = 0.8 + (0.8/10) * 2 * character1_speed_level

        elif choose_list[choose_skill_num] == 5:
            character1_hp_level += 1
            if character1_hp_level > character1_hp_max_level:
                character1_hp_level = character1_hp_max_level
            character1_max_hp = round(50 + (50/10) * 2 * character1_hp_level)
            character1_hp += 10

        choose_skill_num = -1    
        choose_list = []
        choose_option = 1

    ### 코드 수정시 확일 필요 ###
    character1_attack_1.attack_ready_time = 2.5 * ((10-character1_attack_speed_level/2)/10)
    character1_speed = 0.8 + (0.8/10) * 2 * character1_speed_level
    character1_max_hp = round(50 + (50/10) * 2 * character1_hp_level)


    if choose_option_remove_1 == False and character1_attack_2_level == character1_attack_2_max_level:
        choose_able_option.remove(1)
        choose_option_remove_1 = True
    if choose_option_remove_2 == False and character1_attack_speed_level == character1_attack_speed_max_level:
        choose_able_option.remove(2)
        choose_option_remove_2 = True
    if choose_option_remove_3 == False and character1_bs_level == character1_bs_max_level:
        choose_able_option.remove(3)
        choose_option_remove_3 = True
    if choose_option_remove_4 == False and character1_speed_level == character1_speed_max_level:
        choose_able_option.remove(4)
        choose_option_remove_4 = True
    if choose_option_remove_5 == False and character1_hp_level == character1_hp_max_level:
        choose_able_option.remove(5)
        choose_option_remove_5 = True

    if pause == False:
        choose_start_time = pygame.time.get_ticks()
        if flag_1:
            choose_total_time_plus = True
            flag_1 = False
    if pause == True:
        choose_end_time = pygame.time.get_ticks()
        choose_time = choose_end_time - choose_start_time
        flag_1 = True
    if pause == False and choose_total_time_plus == True:
        choose_total_time += choose_time
        choose_time = 0
        choose_total_time_plus == False

    if win:
        win = ("!!!! win !!!!")
        play_time_num = round(now_time/1000)
        play_time = (f'Play Time :  {play_time_num}  second')
        win_msg = game_font.render(str(win), True, (0, 255, 0))
        play_time_msg = game_font.render(str(play_time), True, (0, 0, 255))
        screen.blit(win_msg, (screen_width/2 - 200 , screen_height*(1/3)-50)) 
        screen.blit(play_time_msg, (screen_width/2 - 370 , screen_height*(1/3)+50)) 

    if die:
        game_over = ("Game Over!!!")  
        play_time_num = round(now_time/1000)
        play_time = (f'Play Time :  {play_time_num}  second')
        game_over_msg = game_font.render(str(game_over), True, (0, 255, 0))
        play_time_msg = game_font.render(str(play_time), True, (0, 0, 255))
        screen.blit(game_over_msg, (screen_width/2 - 250 , screen_height*(1/3)-50)) 
        screen.blit(play_time_msg, (screen_width/2 - 370 , screen_height*(1/3)+50)) 

    pygame.display.update() # 개임화면을 다시 그리기

pygame.time.delay(3000)

pygame.quit()