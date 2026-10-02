
import psutil
import sys
import os
def PlatFormServillance(FolderName):
    Border="-"*5
    ret=False
    ret=os.path.exists(FolderName)
    if(ret==True):
        ret=os.path.isdir(FolderName)
        if(ret==False):
            print("unable to procced as directory name is existing but its not a directory ")
            return
    else:
        os.mkdir(FolderName)
        print("directory for log file gets succesfully")


def main():
    Border="-"*5
    print(Border)
    print("------MArvellouse platform servilence system------")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("this automation script is used to perform")
            print("1:it fetch information of running processess ")
            print("2:it fetch the information about primary storage as RAM")
            print("3:if fetch the information about scondary storage as HDD")
            print("4:it fetch the information about microprecessor")
            print("5:it gets")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("use the automation script as :")
            print(f"python {sys.argv[0]} time_Interval Folder_name")
            print("time_Interval:Time in minutes for periodic execution")
            print("folder_name: name of  folder of log file")

    elif(len(sys.argv)==3):
        pass
    else:
        print('invalid number of argument')
        print("unable proceed as argument are not matching")
        print("please use --h or --u flage for getting more details")

    print(Border)
    print("-----Thank you for using our automation system-----")
    print(Border)

    
        
if __name__=="__main__":
    main()


    #2 MarvellousLog
