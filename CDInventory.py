#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# NJohnson, 2021-Aug-08, updated
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
dic = {}  
# TODO replace list of lists with list of dicts



strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[1] Load Inventory from File\n[2] Add CD\n[3] Display Current Inventory')
    print('[4] Delete CD from Inventory\n[5] Save Inventory to file\n[x] Exit')
    strChoice = input('1, 2, 3, 4, 5 or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break



    if strChoice == '1':
        with open('CDInventory.txt','r') as f:
           data = f.read()
           print (data)
            
        
     

        # TODO Add the functionality of loading existing data
        pass




    elif strChoice == '2':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        
        #populate dictionary
        dic[intID] =  {'title':strTitle, 'artist':strArtist}
       
     
    elif strChoice == '3':
        # 3. Display the current data to the user each time the user wants to display the data
        for intID in dic:
            print(intID, 
                  dic[intID]['title'], 
                  dic[intID]['artist'])





    elif strChoice == '4':
        rownumber = input('Enter number row you would like to delete: ')
        intID2 = int(rownumber)
        del dic[intID2]
        #TODO Add functionality of deleting an entry
        pass




    elif strChoice == '5':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        
       f= open('CDInventory.txt','w')
       f.write(str(dic))
       f.close()

    else:
        print('Please choose either 1, 2, 3, 4, 5 or x!')
