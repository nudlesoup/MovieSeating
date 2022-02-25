import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from util.FileProcessor import FileProcessor
from service.MovieTheatre import MovieTheatre
from unitTest.TestTheater import TestTheater
def main():
    '''
    Initiator Function which asks user to provide input file and does the seat booking.
    '''
    if len(sys.argv) > 0:
        fp = FileProcessor(sys.argv[0])
        mt = MovieTheatre()
        try:
            with open(sys.argv[1],"r") as f:
                temp = f.readline()
                while (temp != ""):
                    output = mt.bookSeat(temp)
                    if output == 1:
                        print("Invalid number of Seats")
                    if output == -1:
                        print("Sorry, cannot process request due to Insufficient seats")
                    
                    temp = f.readline()
                fp.writeToFile(mt.getResults())
                mt.printLayout()
                mt.theatreAnalysis()

                #Test Methods
                test = TestTheater()
                testObject = MovieTheatre()
                test.testMovieTheatre(testObject)
        except FileNotFoundError:
            print("Input File Not Found.")
            exit()
        except IOError:
            print("Some IO Error popped up.")
        except Exception as e:
            print(e, "Exception Occurred")

if __name__=="__main__":
    main()

