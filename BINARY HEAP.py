# BINARY HEAP
class Heap:
    def __init__(self,size):
        self.customList=(size+1)*[None]
        self.heapSize=0
        self.maxsize=size+1

def peekofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.custom[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])  

def heapifyTreeInsert(rootNode,index,heapType):
    parentIndex=int(index/2)
    if index<=1:
        return
    if heapType=="Min":
        if rootNode.customList[index]<rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp    
        heapifyTreeInsert(rootNode,parentIndex,heapType) 
    elif heapType=="Max":
        if rootNode.customList[index]>rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp    
        heapifyTreeInsert(rootNode,parentIndex,heapType) 

def insertNode(rootNode,nodeValue,heapType):
    if rootNode.heapSize+1==rootNode.maxsize:
        return"The Binary Heap is full"
    rootNode.customList[rootNode.heapSize+1]=nodeValue
    rootNode.heapSize+=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType)
    return"The Value has been succefully completed"

def heapifyTreeExtrack(rootNode,index,heapType):
    leftIndex=index*2
    rightIndex=index*2+1
    swapChild=0
    if rootNode.heapSize<leftIndex:
        return
    elif rootNode.heapSize==leftIndex:
        if heapType=="Min":
            if rootNode.customList[index]>rootNode.customList[leftIndex]:
                temp=rootNode.customList[index]    
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
            return
        else:  
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp=rootNode.customList[index]    
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp 
            return
    else:
        if heapType=="Min":
            if rootNode.customList[leftIndex]<rootNode.customList[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if rootNode.customList[index]>rootNode.customList[swapChild]:
                temp=rootNode.customList[index]    
                rootNode.customList[index]=rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp        
        else:
            if rootNode.customList[leftIndex]>rootNode.customList[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if rootNode.customList[index]<rootNode.customList[swapChild]:
                temp=rootNode.customList[index]    
                rootNode.customList[index]=rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp   
    heapifyTreeExtrack(rootNode,swapChild,heapType)

def extractNode(rootNode,heapType):
    if rootNode.heapSize==0:
        return
    else:
        extrecktedNode=rootNode.customList[1]
        rootNode.customList[1]=rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize]=None
        rootNode.heapSize-=1
        heapifyTreeExtrack(rootNode,1,heapType)
        return extrecktedNode

def deleteEntireBH(rootNode):
    rootNode.custom=None        


  

newHeap=Heap(5)
insertNode(newHeap,4,"Max")
insertNode(newHeap,5,"Max")
insertNode(newHeap,2,"Max")
insertNode(newHeap,1,"Max")
extractNode(newHeap,"Max")
levelorderTraversal(newHeap)  
print(deleteEntireBH(newHeap))                     