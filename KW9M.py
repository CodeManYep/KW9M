# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 11:09:43 2019

@author: Weizhen Zhang
Create a Chinese dataset, extract from the KB CN-DBpedia and we call it KW9M
for training on model TransE. 
 
First, we swap the position of relation and tail entity. 
Second, we extract head entity and relation and add index to them respectively. 
Third, we remove the duplicate entity and relation and at last obtain the dataset.
dataSource format:head entity relationship tail entity
   require format:head entity tail entity relationship
"""
import logging
import datetime

sourceFile = './Data/baike_triples.txt' #CN-DBpedia triple data
#trainFile = './Data/test.txt'
trainFile = './Data/Final/train.txt'
entity2idFile = './Data/Final/entityMul2id.txt'
reletion2idFile = './Data/Final/relationMul2id.txt'

#   Swap the position of relation and tail entit
def swapPosition():
    i = 0
    with open(sourceFile, encoding = 'utf-8') as sf:
        for line in sf:
            lineArr = line.strip().split('\t')
            headEntity = lineArr[0]
            relation = lineArr[1]
            tailEntity = lineArr[2]
            temp = relation
            relation = tailEntity
            tailEntity = temp
            line = headEntity + '\t' + relation + '\t' + tailEntity
            if i%10000 == 0:
                print(str(i) + ":" + line)
            with open(trainFile, 'a', encoding='utf-8') as tfw:
                tfw.write(line + '\n')
            i = i + 1
    return True
    
#   Extract head entity and relation and add index to them respectively
def getEntRelwithInd(trainFile):
    j = 0
    k = 0
    with open(trainFile, encoding='utf-8') as tf:
        for line in tf:
            entityAndRelArray = line.strip().split('\t')
            #headEntity
            entityH = entityAndRelArray[0]
            #tailEntity
            entityT = entityAndRelArray[1]
            #relationship
            relation = entityAndRelArray[2]
            if j%10000 == 0:
                print('%s:%s' %(str(j), line))

            with open(entity2idFile, 'a', encoding='utf-8') as efw:
                entityHStr = entityH+ '\t' + str(j) + '\n'
                efw.write(entityHStr)
                j = j + 1
                entityTStr = entityT+ '\t' + str(j) + '\n'
                efw.write(entityTStr)
                j = j + 1
            with open(reletion2idFile, 'a', encoding='utf-8') as rfw:
                relationStr = relation + '\t' + str(k) + '\n' 
                rfw.write(relationStr)
                k = k + 1
    return True

#   Remove the duplicate entity and relation
def removeDup():
    entityFile = './Data/Final/entity2id.txt'
    relationFile = './Data/Final/relation2id.txt'
    m = 0
    n = 0
    entitySet = set()
    relationSet = set()
    with open(entity2idFile, encoding='utf-8') as ef:
        for line in ef:
            line = line.strip().split('\t')[0]
            if line not in entitySet:
                if m%10000 == 0:
                    print('%d:%s' %(m,line))
                with open(entityFile, 'a', encoding='utf-8') as efw:
                    efw.write(line + '\t' + str(m) + '\n')
                entitySet.add(line)
                m = m + 1
                
    with open(reletion2idFile, encoding='utf-8') as rf:
        for line in rf:
            line = line.strip().split('\t')[0]
            if line not in relationSet:
                if n%10000 == 0:
                    print('%d:%s' %(n,line))
                with open(relationFile, 'a', encoding='utf-8') as rfw:
                    rfw.write(line + '\t' + str(n) + '\n')
                relationSet.add(line)
                n = n + 1
    return True
    
if __name__ == "__main__":
    program = "KW9M.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # start time...
    starttime = datetime.datetime.now()
    print('start time:' + str(starttime))
    swapPosition()
    print('--- first step done ---')
    getEntRelwithInd(trainFile)
    print('--- second step done ---')
    removeDup()
    print('--- third step done ---')
    print('running over...')
    # end time...
    endtime = datetime.datetime.now()
    print('end time:' + str(endtime))
    # running time...
    runAllTime = endtime - starttime
    print('running time:' + str(runAllTime))
