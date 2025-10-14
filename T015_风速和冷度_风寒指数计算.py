# 功能：根据风速和温度计算风寒指数
speed=int(input())
temp=int(input())
print(round(13.12+0.6215*temp-11.37*speed**0.16+0.3965*temp*speed**0.16))
