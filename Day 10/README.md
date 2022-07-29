# Functions with Outputs

For the [example](example.py) file you will find a function called "days_in_month_by_year" tha prints the number of days in a selected month depending if the year is a leap year or not.

For the [main](main.py) file, i make a program that simulates a calculator.

It was created following the next structure.

```mermaid
graph TD;
A(Start)-->B(Presentation of the calculator);
B-->C(Input of the first number);
C-->D(Pick a operation);
D-->H(Input the other number);
H-->E(Print the result);
E-->F(Ask if the user wants to coninue with another operation with the previous result);
F--Yes-->D;
F--No-->G(Clean the screen and start again the program);
G-->A;
```