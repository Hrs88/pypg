"""
1.如果一个元胞是活的，且活的邻接元胞数少于2，那么它将死亡
2.如果一个元胞是活的，且活的邻接元胞数为2/3，那么它将存活
3.如果一个元胞是活的，且活的邻接元胞数大于3，那么它将死亡
4.如果一个元胞是死的，且活的邻接元胞数为3，那么它将复活
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("n",help="参数的描述信息") # 位置参数，必须按位置传入
parser.add_argument("-p",type=int) # 带 - 或者 -- 的参数，可选参数，传入前必须加上参数名 | 参数必须是int
parser.add_argument("-e",default=False) # 参数默认值为False
parser.add_argument("-d",required=True) # 只对可选参数有效，标识该参数是必须的
parser.add_argument("-f",action="store")
"""
定义参数的行为，常见的有:
    store 默认，存储参数的值
    store_true 如果参数存在，存储true,参数不存在存储false
    store_false 如果参数存在，存储true,参数不存在存储false
    append 如果参数多次出现，就用列表存储
    count 计算参数出现的次数
"""
parser.add_argument("-c",nargs=2) # 规定接收两个值 ?:0或1个值 *:0或多个值 +:1或多个值
parser.add_argument("-a",dest="a") # 分析出来后，用来存储参数的成员变量名
parser.add_argument("-b",choices=["x","y","z"]) # 限制参数只能是x、y、z其中的值。任意可迭代对象都可以传入
parser.add_argument("--version",action="version",version="%(prog)s 1.0")
# 显示版本信息,%(prog)s代表程序名称，即文件名
parser.add_argument("-j",action="store_true")





