
def minAreaRect(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    sqr=0
    for i in range(len(points)): 
        rect=[]       
        for j in range(i+1,len(points)):                    
            if points[i]!=points[j] and points[i][0]!=points[j][0] and points[i][1]!=points[j][1]:
                x1=k[0]
                y1=points[i][1]
                x2=points[i][0]
                y2=k[1]
                if [x1,y1] in points and [x2,y2] in points:
                    tmp=abs((x1-points[i][0])*(y2-points[i][1]))
                    if sqr==0:
                        sqr=tmp
                    elif tmp<sqr:
                        sqr=tmp
    return sqr


minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]) 
            


                

        