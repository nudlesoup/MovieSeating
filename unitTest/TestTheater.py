from service.MovieTheatre import MovieTheatre


class TestTheater:
    def __init__(self):
        self.mt = MovieTheatre()

    def testMovieTheatre(self, testTheatre):
        '''
        Function which calls different tests.
        '''
        print("****Testing****")
        self.mt = testTheatre
        self.checkReservationWithZeroTickets()
        self.checkFirstCustomerSeat()
        self.checkConsecutiveSeats()
        self.checkInsufficientSeats()
        self.checkGroupUnableToAccomodateInRow()
        self.checkGroupAccomodationOfSizeLargerSize()

    def checkReservationWithZeroTickets(self):
        '''
        Test to check whether 0 seats can be booked or not.
        '''
        if self.mt.bookSeat("R001 0") != 1:
            print("Test 1 Passed : No seat reserved for Reservation Id R001 with requirement of zero seats.")
        else:
            print("Test 1 Failed : Reservation made for R001 with zero requirement of seats.")

    def checkFirstCustomerSeat(self):
        '''
        Test to check 5 seats are booked for the first customer in the Middle row or not.
        '''
        self.mt.bookSeat("R002 5")
        cusList = ["E1", "E2", "E3", "E4", "E5"]
        if (self.mt.getResults()["R002"] == cusList):
            print("Test 2 Passed : 5 Seats successfully reserved for first customer at the middle row.")
        else:
            print("Test 2 Failed: Failed to reserve seats for first customer in the middle row.")

    def checkConsecutiveSeats(self):
        '''
        Test to check whether consecutive seats are booked or not.
        '''
        cusList = ["R002", "R002", "R002", "R002", "R002"]
        if self.mt.getList(4, 0, 4) == cusList:
            print("Test 3 Passed : 5 Consecutive seats successfully reserved for first customer row E.")
        else:
            print("Test 3 Failed : Failed to reserve consecutive seats.")

    def checkInsufficientSeats(self):
        '''
        Test to check whether customer request is not exceeding the maximum capacity of theatre.
        '''
        self.mt.bookSeat("R003 250")
        if (self.mt.getNumberOfSeats() - 250) < 0:
            print("Test 4 Passed : Failed to allocate seats when the request was greater than the available seats.")
        else:
            print("Test 4 Failed : Allocated as many seats as possible.")

    def checkGroupUnableToAccomodateInRow(self):
        '''
        Test to check whether below mentioned tickets can be booked in the desired Row.
        '''
        result = self.mt.bookSeat("R004 24")
        if result > 0:
            print(
                "Test 5 Passed : Successfully allocated seats to a large group that could not be accomodated in a single row.")
        else:
            print("Test 5 Failed : Failed to allocate seats to a large group.")

    def checkGroupAccomodationOfSizeLargerSize(self):
        '''
        Test to validate such large number of seats canbe booked in a single row or not.
        '''
        curList = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "F13", "F14", "F15",
                   "F16", "F17", "F18", "F19", "F20", "E6", "E7", "E8", "E9"]
        if self.mt.getResults()["R004"] == curList:
            print("Test 6 Passed : Successfully accomodated a group that could not be accomodated in a single row.")
        else:
            print("Test 6 Failed : Failed to accomodate the group that could not be accomodated in a single row.")
