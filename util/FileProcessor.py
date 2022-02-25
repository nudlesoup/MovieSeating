class FileProcessor:

    fileName, noOfLines = "",0
    def __init__(self, input):
        '''
        Constructor which is invoked all the time.
        Args:
            input(str): user provided filename.
        '''
        self.fileName = input
        self.noOfLines = 0
    
    def readFile(self, inputFileName):
        '''
        Function is used for reading the inputFile which the user provides.
        Args:
            inputFileName(str): input filename for reading the contents.
        '''
        content = None
        try:
            with open(inputFileName,"r") as f:
                temp = f.readline()
                while(temp != None):
                    content += " " + temp
                    self.noOfLines += 1
        except(FileNotFoundError):
            print("Input File Not Found")
        except IOError:
            print("Some IO Error popped up.")
        return content

    def writeToFile(self, hm):
        '''
        Function is used to write the desired output in the provided filename.
        Args:
            hm(dict): ordered dictionary which stores the contents of the input filename.
        '''
        try:
            with open("output.txt","w+") as fp:
                for i in hm:
                    fp.write(str(i) +" " + ",".join(hm[i]) + "\n")
        except IOError:
            print("Some IO Error popped up.")
        print(hm)
