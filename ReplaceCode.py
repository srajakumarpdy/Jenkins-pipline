#!/usr/bin/python


class codeCorrection():
    
    def getPosition(self):
       
        with open('sample.cbl','rt+') as cf:
            data = cf.readlines()
            print(data)
            count = 0
            lc = 0
            w = 'PIC'
            for indx, line in enumerate(data):
                print(line, indx) 
                lc = lc + 1
                sc = 39
                npc = 0
                if w in line:
                    print("In IF")
                    pos = line.find('PIC')
                    count = count + 1
                    print(line)
                    print("The position of the word " +w+ " in line no " +str(lc)+" is ", str(pos)+"\n") 
                    
                    
                    spline = line.split('PIC')
                    spline[0] = spline[0].rstrip()
                    
                    nwpos = line.find(spline[0][-1])
                    #print(nwpos)
                    npc = sc - nwpos
                    #print (npc)

                    spline[1] = 'PIC' + spline[1]
                    
                    upline = spline[0] +npc*' '+ spline[1]
                    #print(line)
                    upos = upline.find('PIC')
                    print("The position of the word " +w+ " in line no " +str(lc)+" after correction is ", str(upos),"\n") 
                    #print(upline)
                    data[indx] = upline
                    print(data[indx])
                else:
                     pass
                    #print("In else")
                    #print(line)
            cf.seek(0)
            cf.writelines(data)
            print("The number of occurence of the word "+w+ " is ",count)

def main():
    c = codeCorrection()
    c.getPosition()
    
        
if __name__ == "__main__":
	main()

