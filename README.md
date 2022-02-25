**Movie Theater Seating Challenge**

**Language used:**  Python (v3.7 or above)

**Program Description:**

This program takes an input file via command line, reads line by line and processes the user requests for reserving seats in the movie theatre.

The algorithm is based on following rules/ideas:

1. Customers that come first will be allocated seats in the middle row.
2. Each group will be allocated seats in a single row. If the group is larger than the number of seats in the row, split the group and allocate as many seats available in that that row for few members and for others allocate in the other row.
3. Full fill as many requests as possible.
4. After scanning all the rows, if the theater is not able to allocate nearby (consecutive) seats to a group, then allocate seats wherever there is a vacant seat.
5. If the numbers of requested seats are not available in the theater then, inform the customer about insufficient seats.

**Assumptions:**

1. The theater cannot reserve seats for a group if the requested number of seats is greater than the available seats. In that case, the customers are informed about the insufficient number of available seats.
2. The reservation number(R###) will be in sequential order like (R001, R002, R003...) in the input file.
3. We have kept buffer of 3 seats between customers for public safety.

**How are the goals of the problem statement achieved?**

_Customer Satisfaction:_

1. Since customers are reserving seats for groups, they would prefer sitting next to each other. So the first priority will be to allocate seats for the group in a single row.
2. Since the middle seats give a better viewing experience in the movie theater, customers who come first will be allocated seats in the middle row.

_Public Safety:_

1. During this Covid times, Theatre are occupied with Social Distancing Measures in place. So as to follow that and keeping that situation in mind, we are keeping a gap of 3 seats per each customer.

_Maximum Theater Utilization:_

1. To make sure that we are able to accommodate as many groups as possible and also keep them satisfied by allocating consecutive seats, we start allocating seats from the first column. This will allow us to allocate seats for maximum number of groups in a single row.
2. In one or two cases if we are not able to accommodate a group in a single row, then we allocate the seats wherever there is a vacant seat in the theater.

**Steps for running**
1. Download and save the TheaterSeating folder in a directory.
2. Go to the Driver.py file and update the system path as accordingly with your machine.
3. Create Virtualenv using command: python -m venv <any_name where you want to activate> Ex: python -m venv mypy.
4. Then use **.\mypy\Scripts\activate** command to activate your environment. This creates a separate python environment which helps in keeping local python dependencies and your project dependencies separate.
5. Go to the command line inside the folder where you have stored the TheaterSeating folder and run the file using the following(Windows Machine):
   python driver/Driverdetails.py input.txt  
6. You will get output.txt as desired output along with Movie Theatre Analysis on command line for user viewing.
