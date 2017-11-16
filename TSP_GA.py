# -*- encoding: utf-8 -*-

import random
import math
from ga.GA import GA
import  matplotlib.pyplot as plt

class TSP(object):
      def __init__(self, aLifeCount = 300,):
            self.initCitys()
            self.lifeCount = aLifeCount
            self.ga = GA(aCrossRate = 0.7, 
                  aMutationRage = 0.02, 
                  aLifeCount = self.lifeCount, 
                  aGeneLenght = len(self.citys), 
                  aMatchFun = self.matchFun())

      def initCitys(self):
            self.citys = []
            self.citys.append((3507,1633))
            self.citys.append((3394,1357))
            self.citys.append((3429,2092))
            self.citys.append((3780,1788))
            self.citys.append((3007,2030))
            self.citys.append((2545,1643))
            self.citys.append((3326,2444))
            self.citys.append((2381,2324))
            self.citys.append((2562,2244))
            self.citys.append((2788,2509))
            self.citys.append((2935,760))
            self.citys.append((1304,1688))
            self.citys.append((1332,3305))
            self.citys.append((2778,1174))
            self.citys.append((2370,1025))
            self.citys.append((3140,450))
            self.citys.append((2771,3238))
            self.citys.append((4196,2996))
            self.citys.append((4312,3210))
            self.citys.append((4386,3430))
            self.citys.append((3488,2465))
            self.citys.append((3639,2685))
            self.citys.append((3676,1422))
            self.citys.append((3712,2601))
            self.citys.append((3715,2322))
            self.citys.append((3918,1821))
            self.citys.append((4177,1756))
            self.citys.append((4061,1630))
            self.citys.append((4029,1162))
            self.citys.append((3439,799))
            self.citys.append((4263,1069))

            
      def distance(self, order):
            distance = 0.0
            for i in range(-1, len(self.citys) - 1):
                  index1, index2 = order[i], order[i + 1]
                  city1, city2 = self.citys[index1], self.citys[index2]
                  distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
            return distance

      def matchFun(self):
            return lambda life: 1.0 / self.distance(life.gene)

      def run(self, n = 0):
            x=[]
            y=[]
            while n > 0:
                  self.ga.next()
                  distance = self.distance(self.ga.best.gene)

                  print (("%d : %f") % (self.ga.generation, distance))
                  n -= 1
                  x.append(self.ga.generation)
                  y.append(distance)
            print(self.ga.best.gene)
            plt.plot(x,y , marker='')
            plt.title(u'GA-C-TSP')
            plt.xlabel('The number of iterations')
            plt.ylabel('Loop distance')
            plt.show()

def main():
      tsp = TSP()
      tsp.run(1800)

if __name__ == '__main__':
      main()


