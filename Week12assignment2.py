#Name: Nick Wolf
#Date: 4/19/2021
#program name: Week 12 assignment 2

#Function 1
def function1 ():
     #open file
    names_file = open ('Scoobynames.txt', 'r')

    #read file
    names_contents = names_file.read()

    #close file
    names_file.close

    #print
    print (name_contents)

#Function 2
def function2 ():
    #open file
    names_file = open ('Scoobynames.txt', 'r')

    #Read lines
    line1 = names_file.readline()
    line2 = names_file.readline()
    line3 = names_file.readline()

    #close file
    names_file.close()

    #print statemnt
    print (line1)
    print (line2)
    print (line3)


#body
print ("Function 1\n")
function1 ()
print ("Function 2\n")
function2 ()
   

