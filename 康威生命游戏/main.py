"""
1.如果一个元胞是活的，且活的邻接元胞数少于2，那么它将死亡
2.如果一个元胞是活的，且活的邻接元胞数为2/3，那么它将存活
3.如果一个元胞是活的，且活的邻接元胞数大于3，那么它将死亡
4.如果一个元胞是死的，且活的邻接元胞数为3，那么它将复活
"""
import argparse
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation
def GetRandomGrid(N):
    """获取随机矩阵"""
    return np.random.choice([0,1], N*N, p=[0.5,0.5]).reshape(N,N)
def update(frames,img,grid,n):
    newGrid = grid.copy()
    for i in range(n):
        for j in range(n):
            total = (grid[(i-1)%n,(j-1)%n] + grid[(i-1)%n,j] + grid[(i-1)%n,(j+1)%n] +
                     grid[i,(j-1)%n] + grid[i,(j+1)%n] +
                     grid[(i+1)%n,(j-1)%n] + grid[(i+1)%n,j] + grid[(i+1)%n,(j+1)%n])
            if newGrid[i,j] == 1:
                if total == 2 or total == 3: pass
                else: newGrid[i,j] = 0
            else:
                if total == 3: newGrid[i,j] = 1
                else: pass
    img.set_data(newGrid)  # 更新数据
    grid[:] = newGrid[:]
    return img,
def main():
    # 接收参数并分析参数
    parser = argparse.ArgumentParser()
    parser.add_argument("-n",default=10, type=int,required=False,dest="n",help="正方形网格的边长")
    parser.add_argument("-i",default=500,type=int,required=False,dest="i",help="时间刻长度")
    args = parser.parse_args()
    # 创建随机矩阵
    grid = GetRandomGrid(args.n)
    # 设置动画
    fig, ax = plt.subplots()
    img = ax.imshow(grid)
    ani = animation.FuncAnimation(fig,update,fargs=(img,grid,args.n),frames=10,interval=args.i)
    plt.show()
if __name__ == '__main__':
    main()
