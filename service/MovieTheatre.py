#imports
from collections import OrderedDict

class MovieTheatre:
    rows,cols = 10,20 #defined boundaries for the theatre
    numberOfSeats = rows * cols #maximum seats
    hm = OrderedDict()
    seats = [[ None for _ in range(20) ] for _ in range(10)] #Initially setting all the seats to none(empty)
    remainingSeats = [ 20 for _ in range(10)] #Setting all the seats initially as available.
    satisfaction, totalCustomers = 0, 0 #Set initial req and customers to 0

    def bookSeat(self, reservation): 
        '''
        Function is used for booking Seats for the customers as and when requests comes up.
        Args:
            reservation(str): space seperated request in the form of (R### 3) comes up for the seat booking.
        '''    
        ip = reservation.split()
        if not ip:      #check for handling blank lines in the input file.
            return -1
        rno = ip[0]     #Row Number
        count = int(ip[1]) #Number of seats to be booked per group.
        group = count
        op = None

        if count > 0:
            if self.numberOfSeats >= count:
                self.totalCustomers += count
                if group > 20:      #check if there is any group of more than 20 customers, then break them into groups of max 20.
                    while group > 20:
                        op = self.allocate(rno, 20)
                        group -= 20
                    op = self.allocate(rno, group)
                else:
                    op = self.allocate(rno, group)
                
                return op
            else:
                return -1
        else:
            return -1
        
    def allocate(self, rno, seatsToBook):
        '''
        Function is used to allocate number of seats and on which row to be booked.
        Args:
            rno(str): Which row is to be booked.
            seatsToBook(int): number of seats to be booked for a group
        '''
        counter = 1
        check = True
        r = (self.rows // 2) - 1 
        while r >= 0 and r < self.rows:
            if self.remainingSeats[r] >= seatsToBook:
                c = 0
                while c < 20 and seatsToBook > 0:
                    if self.seats[r][c] == None:
                        self.seats[r][c] = rno
                        if rno in self.hm:
                            self.hm[rno].append(chr(r+65) + str(c+1)) #converting to ascii letters
                        else:
                            self.hm[rno] = [chr(r+65) + str(c+1)]

                        self.remainingSeats[r] -= 1
                        self.numberOfSeats -= 1
                        seatsToBook -= 1
                        self.satisfaction += 1 #<20 //24
                    c += 3 #Just for social distancing else we can change it to #1 for Maximum allocation.
            if check:
                r += counter
                counter += 1
                check = False
            else:
                r -= counter
                counter += 1
                check = True
        
        if seatsToBook == 0:
            return 0
        else:
            counter = 1
            check = True
            i = (self.rows//2) - 1
            while i >= 0 and i < self.rows:
                if self.remainingSeats[i] > 0:
                    j = 19
                    while(self.seats[i][j] == None):
                        self.seats[i][j] = rno
                        if rno in self.hm:
                            self.hm[rno].append(chr(i+65) + str(j+1))
                        else:
                            self.hm[rno] = [chr(i+65) + str(j+1)]
                        
                        seatsToBook -= 1
                        self.numberOfSeats -= 1
                        self.remainingSeats[i] -= 1   
                        j -= 1
                if check:
                    i += counter
                    counter += 1
                    check = False
                else:
                    i -= counter
                    counter += 1
                    check = True
            return 0

    def getList(self, row, columnStart, columnEnd):
        '''
        Getting list of No of seats based on input
        '''
        ls = []
        c = columnStart
        while c <= columnEnd:
            ls.append(self.seats[row][c])
            c+=1
        return ls

    def getResults(self):
        '''
        Returning Ordered Dictionary.
        '''
        return self.hm

    def getNumberOfSeats(self):
        '''
        Return Number of Seats.
        '''
        return self.numberOfSeats
    
    def theatreAnalysis(self):
        '''
        Function which Displays Movie Theatre Analysis.
        '''
        print("Analysis")
        print("Total number of groups: ", len(self.hm))
        print("Total customers :", self.totalCustomers)
        print("Total number of Satisfied customers: ", self.satisfaction)
        print("Percentage of Satisfied Customers :", round((self.satisfaction * 100 / self.totalCustomers),3))
        print("Theater Utilization Percent: ", (self.satisfaction)/2)        
    
    def printLayout(self):
        '''
        Displaying how the seats are filled in each row.
        '''
        print("Reservations")
        for r in range(10):
            print(chr(r+65), "")
            for c in range(20):
                print("", self.seats[r][c])
            print()
    
    