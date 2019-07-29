import time
# stonenumber=int(input('几个宝石？'))
#
# if stonenumber>=6:
#     print('你拥有了毁灭宇宙的力量')
# else:
#     print('不够！')

# for i in range(10):
#     if i == 11:
#         print('1')
#         break
# else:
#     print('2')

# print('22')
# time.sleep(2)
#
# print('33')
# time.sleep(2)

# studysocre = int(input('你的成绩：'))
#
# if studysocre>=60:
#     print('good')
#     if studysocre>=80:
#         print('perfer')
#     else:
#         print('well')
# else:
#     print('shit')
# print('bye')

# scores = {'dd':33,'cc':33,'ff':55}
# print(scores['cc'])
#
# for i in range(4):
#     print('dd')

import time,random

# 存放玩家和怪物信息
#player_list = ['低级剑士','中级剑士','高级剑师','魔法学徒','魔法士','魔法师','魔法使']
player_list = ['刘大毛','刘二毛','刘三毛','刘四毛','刘五毛','刘六毛','傻逼毛毛']
enemy_list = ['蝴蝶怪','鲤鱼精','咸鱼王','蜻蜓怪','小火虫','大沙雕','放屁虫','犀牛精','牛魔王']
# 调用随机调取函数调取玩家和怪物名字
players = random.sample(player_list,3)
enemys = random.sample(enemy_list,3)
# 空字典存放玩家和怪物血量攻击
playler_info = {}
enemys_info = {}

#随机生成生命个攻击力的函数
def rang_info():
    life = random.randint(100, 200)
    attack = random.randint(30, 60)
    return life,attack


#d打印玩家个怪物信息的函数
def show_info():
    for i in range(3):
        # 给空字典添加属性，角色列表players的第0个元素为键，变量life为值
        playler_info[players[i]] = rang_info()
        enemys_info[enemys[i]] = rang_info()

    print('----------展示玩家信息----------')
    print('你的玩家：')
    for i in range(3):
         print('%s 血量： %d  攻击： %d' %(players[i],playler_info[players[i]][0],playler_info[players[i]][1]))
    print('-------------------------------')
    print('----------展示怪物信息----------')
    print('对面怪物：')
    for i in range(3):
        print('%s 血量： %d  攻击： %d' % (enemys[i], enemys_info[enemys[i]][0], enemys_info[enemys[i]][1]))
    print('-------------------------------')
    input('按快车前进')

#安排出厂顺序的函数
def order_role():
    global players
    #新的字典暂时存放确定的顺序
    order_dict = {}
    for i in range(3):
        order = int(input('你想%s第几个上'%players[i]))
        #order为新的顺序，绑定元数据的位置，
        order_dict[order] = players[i]
    #将原字典清空，将新的顺序填充
    players = []
    for i in range(1,4):
        players.append(order_dict[i])
    #打印出顺序表
    print('我方出场顺序：%s %s %s'%(players[0],players[1],players[2]))

#pk的安排
def pk_info():
    round = 1
    score = 0
    for i in range(3):
        player_name = players[i]
        player_life = playler_info[players[i]][0]
        player_attack = playler_info[players[i]][1]
        enemy_name = enemys[i]
        enemy_life = enemys_info[enemys[i]][0]
        enemy_attack = enemys_info[enemys[i]][1]
        print('-------------第%d局----------'% round)
        print('玩家角色：%s vs 敌方角色：%s ' % (player_name, enemy_name))
        print('%s 血量：%d  攻击：%d' % (player_name, player_life, player_attack))
        print('%s 血量：%d  攻击：%d' % (enemy_name, enemy_life, enemy_attack))
        print('--------------------------------------------')
        input('请按回车键继续。\n')
        while player_life > 0 and enemy_life > 0:
            enemy_life = enemy_life - player_attack
            player_life = player_life - enemy_attack
            print('%s发起了攻击，%s剩余血量%d' % (player_name, enemy_name, enemy_life))
            print('%s发起了攻击，%s剩余血量%d' % (enemy_name, player_name, player_life))
            print('--------------------------------------------')
            time.sleep(1)
        else:  # 每局的战果展示，以及分数score和局数的变化。
            print(show_result(player_life, enemy_life)[1])
            # 调用show_result()函数，打印返回元组中的第一个元素result。
            score += int(show_result(player_life, enemy_life)[0])
            # 调用show_result()函数，完成计分变动。
            round += 1
    input('\n点击回车，查看比赛的最终结果\n')
    if score > 0:
        print('【最终结果：你赢了！】\n')
    elif score < 0:
        print('【最终结果：你输了！】\n')
    else:
        print('【最终结果：平局！】\n')

    # 返回单局战果和计分法所加分数。
def show_result(player_life, enemy_life):  # 注意：该函数要设定参数，才能判断单局战果。
    if player_life > 0 and enemy_life <= 0:
        result = '\n敌人死翘翘了，你赢了！'
        return 1, result  # 返回元组(1,'\n敌人死翘翘了，你赢了！')
    elif player_life <= 0 and enemy_life > 0:
        result = '\n悲催，敌人把你干掉了！'
        return -1, result
    else:
        result = '\n哎呀，你和敌人同归于尽了！'
        return 0, result

def main():
    show_info()
    order_role()
    pk_info()



main()









# def info(plays,player_life,player_attack,enemys,enemy_life,enemy_attack):
#     print('[%s] \n血量:%s\n攻击力：%s'%(players,player_life,player_attack))
#     print('-------------------------')
#     time.sleep(1)
#     print('[%s] \n血量:%s\n攻击力：%s'%(enemys,enemy_life,enemy_attack))
#     print('-------------------------')
#     time.sleep(1)

# def pk_role(player_life,player_attack,enemy_life,enemy_attack):
#     while player_life > 0 and enemy_life > 0:
#         player_life = player_life - enemy_attack
#         enemy_life = enemy_life - player_attack
#         time.sleep(0.5)
#         if player_life > 0 and enemy_life > 0 :
#             print('你发起攻击，敌人剩余血量：' + str(enemy_life))
#             print('敌人发起攻击，玩家剩余血量：' + str(player_life))
#             print('-------------------------')



# pr_resoult(player_life,enemy_life)

# def pr_resoult(player_life,enemy_life):
#     time.sleep(0.5)
#     if (player_life <= 0) and (enemy_life > 0):
#         print('你发起攻击，敌人剩余血量：' + str(enemy_life))
#         print('敌人发起攻击，你剩余血量为0.\n你输了！')
#     elif player_life >= 0 and enemy_life < 0:
#         print('你发起致命一击，敌人剩余血量：0')
#         print('你赢了。')
#     else:
#         print('平局!')


#
# def main(player_life,player_attack,enemy_life,enemy_attck):
#     info(player_life,player_attack,enemy_life,enemy_attck)
#     pk_role(player_life,player_attack,enemy_life,enemy_attck)


