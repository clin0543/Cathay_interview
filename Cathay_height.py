"""
從100cm高度放下, 每次反彈一半高度
1. 第十次落地時經歷多少cm
2. 第十次反彈多高
"""
class Ball():
    def __init__(self, height):
        self.height = height

    def countCM(self, times):
        totalCM = self.height #frist landing, so times-1
        for x in range(times-1):
            totalCM += self.height/2**x
            print(f'第{x+2}落地時總共經歷了:', totalCM, 'CM') #second landing, so x+2

        print(f'第{times}落地時總共經歷了:', totalCM, 'CM')

    def rebound(self, times):
        print(f'第{times}次反彈的高度為:', self.height/2**times, 'CM')

if __name__ == '__main__':
    Ball = Ball(100)
    Ball.countCM(10)
    Ball.rebound(10)
    # -----Another way-----

    # def ballDetail(height, times):
    #     print(f'第{times}次反彈的高度為:',height/2**times,'CM')
    #     print(f'第{times}落地時總共經歷了:',  height+sum([(height/2**x) for x in range(times-1)]),'CM')

    # ballDetail(100,10)
