from turtle import *
import time,datetime
import random

#主程序
title('猜数字游戏')
bgpic(r'D:\猜数字游戏\未标题-2.png')
f=r'D:\猜数字游戏\times.txt'
word=0
ke=0
dg=0
vmware=0
abcd=0
cvc=0
wd=[]
k=[]
d=[]
yx=0
score=[]
try:
    f=r'D:\猜数字游戏\desktop.txt'
    file=open(f,'r',encoding='utf-8')
    str1=file.read()
    str(str1)
except:
    f=r'D:\猜数字游戏\desktop.txt'
    file=open(f,'w',encoding='utf-8')
    file.write('none')
    str1="none"
win_times=0
all_times=0


L=1
try:
    while 1:
            if str1[3:] == str(datetime.datetime.today())[:11]:    
                try:
                
                    sybols=['+',"-","*",]
                    a=f'''{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}
                    {random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}
                    {random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}
                    {random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}
                    {random.randint(1,100)}'''
                    v=textinput('请完成下列题目',a)
                    if v == eval(a):
                        pass
                    else:
                        f=r'D:\猜数字游戏\desktop.txt'
                        file=open(f,'w',encoding='utf-8')
                        file.write(f'30 {str(datetime.datetime.today())[:11]}')
                        file.close() 
                        write('错误',font=('瑞美加张清平硬笔行书',20),align="center")
                        time.sleep(1)
                        exit()

                except:
                    f=r'D:\猜数字游戏\desktop.txt'
                    file=open(f,'w',encoding='utf-8')
                    file.write(f'30 {str(datetime.datetime.today())[:11]}')
                    file.close() 
                    write('错误',font=('瑞美加张清平硬笔行书',20),align="center")
                    time.sleep(1)
                    exit()
            if all_times == 30:
                try:
                
                    sybols=['+',"-","*",]
                    a=f'''{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}
                    {random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}
                    {random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}
                    {random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}{random.randint(1,100)}{random.choice(sybols)}
                    {random.randint(1,100)}'''
                    v=textinput('请完成下列题目',a)
                    if v == eval(a):
                        pass
                    else:
                        f=r'D:\猜数字游戏\desktop.txt'
                        file=open(f,'w',encoding='utf-8')
                        pd()
                        write('错误',font=('瑞美加张清平硬笔行书',20),align="center")
                        file.write(f'30 {str(datetime.datetime.today())[:11]}')
                        file.close() 
                        time.sleep(1)
                        exit()
                except:
                    f=r'D:\猜数字游戏\desktop.txt'
                    file=open(f,'w',encoding='utf-8')
                    file.write(f'30 {str(datetime.datetime.today())[:11]}')
                    file.close() 
                    write('错误',font=('瑞美加张清平硬笔行书',20),align="center")
                    time.sleep(1)
                    exit()

            try:
                a=int(textinput("要登录(1),注册(2),还是查询(3)","输入数字"))
            except:
                pu()
                goto(0,-300)
                write('您没有输入正确，系统认为您并不需要服务，已自动退出',font=('瑞美加张清平硬笔行书',20),align='center')
                time.sleep(1)
                exit()

            try:
                if a==1:
                    dd=0
                    b=textinput("请写入账号","")
                    c=textinput("请写入密码","")
                    if len(wd)==0 and len(k)==0:
                            write("您还没有注册",font=('瑞美加张清平硬笔行书',20),align="center")
                            time.sleep(1)
                            clear()
                    yxi=-1
                    for i in k:
                        yxi+=1
                        for cc in wd:
                            if b==i and c==cc:
                                a=write(f"您好，{d[yxi]}，猜数字游戏马上开始",font=('瑞美加张清平硬笔行书',20),align='center')
                                time.sleep(1)
                                clear()
                                
                                number=random.randint(1,100)
                                number_guss=0
                                yx=1
                                if win_times<7:
                                    number_tme=25
                                    L=2
                                elif win_times<15:
                                    number_tme=17
                                    L=3
                                elif win_times<22:
                                    number_tme=15
                                    L=4
                                else:
                                    number_tme=10
                                    L=5
                                while number_guss<number_tme:   
                                        x=1
                                        if x==1:
                                            if number_tme != 10:
                                                write(f"本次你有{number_tme}次机会",font=('瑞美加张清平硬笔行书',20),align="center")
                                                time.sleep(0.7)
                                                clear()
                                                x=0
                                            else:
                                                write("这次你只有10次机会，你赶快放弃吧！哈哈哈哈哈",font=('瑞美加张清平硬笔行书',20),align="center")    
                                                x=0                                        
                                            guess=textinput("猜一个1~100的整数","输入数字")
                                        try:
                                            guess=int(guess)
                                            guess_now=1
                                            if guess>=1 and guess<=100:
                                                if guess==number and guess_now==1:
                                                    if number_tme==10:
                                                        guess_now=0
                                                        pu()
                                                        goto(0,0)
                                                        write("真棒",font=('瑞美加张清平硬笔行书',20),align="center")
                                                        score.append(number_guss)
                                                        vmware=1
                                                        time.sleep(1)
                                                        clear() 
                                                        win_times += 1 
                                                        all_times += 1                                                
                                                    else:
                                                        guess_now=0
                                                        pu()
                                                        goto(0,0)
                                                        write("真棒",font=('瑞美加张清平硬笔行书',20),align="center")
                                                        score.append(number_guss)
                                                        vmware=1
                                                        time.sleep(1)
                                                        clear()
                                                        win_times += 1
                                                        all_times += 1
                                                    break
                                                if guess<number and guess_now==1:
                                                    guess_now=0
                                                    goto(0,0)
                                                    write("太小了",font=('瑞美加张清平硬笔行书',20,),align="center")
                                                    time.sleep(1)
                                                    clear()
                                                if guess>number and guess_now==1:
                                                    guess_now=0
                                                    goto(0,0)
                                                    write("太大了",font=('瑞美加张清平硬笔行书',20),align="center")
                                                    time.sleep(1)
                                                    clear()

                                                number_guss+=1
                                                goto(0,-25)
                                                write(f'你还有{number_tme-number_guss}次机会',font=('瑞美加张清平硬笔行书',20),align="center")
                                                time.sleep(1)
                                                clear()
                                                if number_tme-number_guss == 0:
                                                    write(f'你没有机会了，正确数字是{number}',font=('瑞美加张清平硬笔行书',20),align="center")
                                                    time.sleep(1)
                                                    clear()   
                                                    all_times += 1                                                 
                                                    

                                            else:
                                                write(f'1~100哦！',font=('瑞美加张清平硬笔行书',20),align="center")       
                                                time.sleep(1)
                                                clear()                                 
        
                                        except ValueError:
                                            write('这不是整数')
                                if vmware == 0:
                                    goto(0,-250)
                                    write('您（你的朋友）未进入（退出了）游戏，没有记录',font=('瑞美加张清平硬笔行书',20),align="center")
                                    goto(0,-300)
                                    write('按Ctrl+C退出...',font=('瑞美加张清平硬笔行书',20),align="center")
                                    time.sleep(1)
                                    clear()                                                                       
                    if yx==0:
                        write('这个账号不存在',font=('瑞美加张清平硬笔行书',20),align="center")   
                        clear() 
                elif a==2:
                    dd=0
                    ke=textinput("新账号？(不为0)","")
                    ab=textinput("昵称？(不为0)","")
                    word=textinput("新密码？(不为0)","")
                    k.append(ke)
                    d.append(ab)
                    wd.append(word)
                elif a==3:
                    dd=0
                    c=0
                    while cvc==0:
                        try:
                            what_to=int(textinput('想要查询什么？（可查询：1.最少次数，2.最多次数（成功），3.平均次数','输入数字'))
                            cvc=1
                            try:
                                while abcd==0:
                                    if what_to == 1:
                                        write(min(score),font=('瑞美加张清平硬笔行书',20),align="center")
                                        abcd=1
                                        time.sleep(1)
                                        clear()
                                    if what_to == 2:
                                        write(max(score),font=('瑞美加张清平硬笔行书',20),align="center")
                                        abcd=1
                                        time.sleep(1)
                                        clear()
                                    if what_to == 3:
                                        for vbvb in score:
                                            c+=vbvb
                                        write(c/len(score),font=('瑞美加张清平硬笔行书',20),align="center")
                                        abcd=1
                                        time.sleep(1)
                                        clear()
                                    else:
                                        write('请输入正确回答。',font=('瑞美加张清平硬笔行书',20),align="center")
                                        abcd=1
                                        time.sleep(1)
                                        clear()
                            except:
                                pu()
                                goto(0,-250)
                                write('您（你的朋友）未进入（退出了）游戏，没有记录',font=('瑞美加张清平硬笔行书',20),align="center")
                                goto(0,-300)
                                write('按Ctrl+C退出...',font=('瑞美加张清平硬笔行书',20),align="center")
                                time.sleep(1)
                                clear()
                        except ValueError:
                            write('输入数字!!!')
                else:
                    pu()
                    goto(0,-300)                    
                    write('您没有输入正确，系统认为您并不需要服务，已自动退出',font=('瑞美加张清平硬笔行书',20),align='center')
                    time.sleep(0.4)
                    exit()

            except NameError:
                break
except KeyboardInterrupt or Terminator:
    exit()
