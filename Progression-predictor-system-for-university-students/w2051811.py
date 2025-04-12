"""
Software Develoment I - Coursework

Name: W.D.Chanith Ransika
IIT Student Number : 20231027

# I declare that my work contains no examples of misconduct, such as plagiarism, or 
collusion. 
# Any code taken from other sources is referenced within my code solution

"""

credit_values = [0, 20, 40, 60, 80, 100, 120]

credit_pass = 0
credit_defer = 0
credit_fail = 0

count_progress = 0
count_trailer = 0
count_retriever = 0
count_exclude = 0
outcomes = 0

all_outcome_list = []

f = open("inputdata.txt", "w")

while True:

        while True:

                while True:
                    try:
                        credit_pass = int(input("Please enter your credit at pass: "))
                        if credit_pass in credit_values:
                            break
                        else:
                            print("Out of range")

                    except ValueError:
                        print("Integer required")

                while True:
                    try:
                        credit_defer = int(input("Please enter your credit at defer: "))
                        if credit_defer in credit_values:
                            break
                        else:
                            print("Out of range")

                    except ValueError:
                        print("Integer required")

                while True:
                    try:
                        credit_fail = int(input("Please enter your credit at fail: "))
                        if credit_fail in credit_values:
                            break
                        else:
                            print("Out of range")

                    except ValueError:
                        print("Integer required")


                total_credit = credit_pass + credit_defer + credit_fail

                if total_credit == 120:
                    break
                else:
                    print("Total incorrect")

        if credit_pass == 120:
            print("Progress")
            count_progress += 1
            credit_user_input = f"Progress - {credit_pass}, {credit_defer}, {credit_fail}"
            all_outcome_list.append(credit_user_input)
            f.write(f"{credit_user_input}\n")

        elif credit_pass == 100:
            print("Progress (module trailer)")
            count_trailer += 1
            credit_user_input = f"Progress (module trailer) - {credit_pass}, {credit_defer}, {credit_fail}"
            all_outcome_list.append(credit_user_input)
            f.write(f"{credit_user_input}\n")

        elif credit_fail >= 80:
            print("Exclude")
            count_exclude += 1
            credit_user_input = f"Exclude - {credit_pass}, {credit_defer}, {credit_fail}"
            all_outcome_list.append(credit_user_input)
            f.write(f"{credit_user_input}\n")

        else:
            print("Do not progress - module retriever")
            count_retriever += 1
            credit_user_input = f"Module retriever - {credit_pass}, {credit_defer}, {credit_fail}"
            all_outcome_list.append(credit_user_input)
            f.write(f"{credit_user_input}\n")

        repeat = input("""Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: """).lower()
    
        while repeat not in ["y", "q"]:
            repeat = input("""Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: """).lower()

        if repeat == "q":
            break

outcomes = count_progress + count_trailer + count_retriever + count_exclude


from graphics import *

def main():

    win = GraphWin("Histogram", 800, 600)
    msg1 = Text(Point(225,30), "Histogram Results")
    msg1.setSize(18)
    msg1.setStyle("bold")
    msg2 = Text(Point(185,500), "Progress")
    msg3 = Text(Point(330,500), "Trailer")
    msg4 = Text(Point(470,500), "Retriever")
    msg5 = Text(Point(610,500), "Excluded")
    msg6 = Text(Point(225,540), f"{outcomes} outcomes in total.")
    msg6.setSize(15)
    msg7 = Text(Point(185,480 - count_progress * 15 - 10), count_progress)
    msg8 = Text(Point(330,480 - count_trailer * 15 - 10), count_trailer)
    msg9 = Text(Point(470,480 - count_retriever * 15 - 10), count_retriever)
    msg10 = Text(Point(610,480 - count_exclude * 15 - 10), count_exclude)
    h_line = Line(Point(70,480), Point(730,480))
    c1 = Rectangle(Point(130,480 - count_progress * 15), Point(250,480))
    c1.setFill("palegreen")
    c2 = Rectangle(Point(270,480 - count_trailer * 15), Point(390,480))
    c2.setFill('darkseagreen')
    c3 = Rectangle(Point(410,480 - count_retriever * 15), Point(530,480))
    c3.setFill("yellowgreen")
    c4 = Rectangle(Point(550,480 - count_exclude * 15), Point(670,480))
    c4.setFill("pink")
    h_line.draw(win)
    msg1.draw(win)
    msg2.draw(win)
    msg3.draw(win)
    msg4.draw(win)
    msg5.draw(win)
    msg6.draw(win)
    msg7.draw(win)
    msg8.draw(win)
    msg9.draw(win)
    msg10.draw(win)
    c1.draw(win)
    c2.draw(win)
    c3.draw(win)
    c4.draw(win)
    win.getMouse()
    win.close()

main()


for y in all_outcome_list:
    print(y)

f.close()