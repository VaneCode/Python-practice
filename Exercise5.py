# Write a program which repeatedly reads numbers until the user enters done.
# Once "done" is enterd, print out the total, count, and average of the numbers.
# If the users enters anything other than a number, detect their mistake using tyr and except.
# Print an error message and skip to the next number.
def repeatNums():
    inp = 0
    count = 0
    sum = 0.0
    while True:
        try:
            inp = input("Please enter a number: ")
            if inp == 'done':
              break
            else:
              inp = float(inp)
              count += 1
              sum += inp
        except ValueError:
            print("Ops, your input is not valid, try again")
    print('All done')   
    print('Total', sum)
    print('Count', count)
    print('Average',sum/count)

repeatNums()