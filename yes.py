import hashlib
from pathlib import Path
import time
import sys
firsttimecheck = ()
#first time setup
try:
                
                #If it does it prints it in text
                d = open('firsttimecheck','r').read()
                
                firsttimecheck = ('')
                
except IOError:
                #if there was not a file it says so
                
                firsttimecheck = ('1')
        


            
if firsttimecheck == ('1'):
    print ('I see this is your first time using this program')
    print ('')
    firsttimeusername = input("Admin Username: ")
    firsttimepassword = input('Admin Password: ')
    firsttimecode = input('Admin Code: ')

    hashedpassword =hashlib.sha256(str.encode(firsttimepassword)).hexdigest()
    hashedusername =hashlib.sha256(str.encode(firsttimeusername)).hexdigest()
    hashedadmincode =hashlib.sha256(str.encode(firsttimecode)).hexdigest()
    
    open('adminusername','w+').write(hashedusername)
    open('adminpassword','w+').write(hashedpassword)
    open('admincode','w+').write(hashedadmincode)
    open('firsttimecheck','w').write('2')
    open('loginattempts','w').write('')
    
    
#login system


usernameloop = True
passwordloop = True
adminloginuser = False


while usernameloop == True:
    
    userexist = (True)
    while userexist == (True):
        inputusername = input ("Input Username ")

        adminusername = open('adminusername','r').read()
        inputusername = hashlib.sha256(str.encode(inputusername)).hexdigest()
        
        if inputusername == (adminusername):                       
            username = ('')
            print ('admin user')
            adminloginuser = True
            userexist = False
        else:
            
            adminloginuser = False
            try:
                username = open(inputusername,'r').read()
                userexist = False
            except IOError:
                print ('User does not exist')
    
    if (inputusername) == (username) or adminloginuser == True:
        print ("correct")
        usernameloop = False
        
    else:
        print ("incorrect")
        
        usernameloop = True


while passwordloop == True:
    failedcheck = open('loginattempts','r').read()
    
             
    if failedcheck == ('5'):
        print ('you have failed to many times wait 1 minute')
        only = (0)
        
        taken = ('')
        while taken == (''):
            
            time.sleep(1)            
            only = only + 1            
            print (only)
            if only == (60):
                taken = ('i')
        taken = ('')
        print ('time is up have another go')
        open('loginattempts','w').write('')
        
    passwordexists = True
    Password = ('')
    inputpassword = ('')
    adminlogin = False

    
    inputpassword = input("Input Password ")
        
    inputpassword = hashlib.sha256(str.encode(inputpassword)).hexdigest()


    AdminPassword = open('adminpassword','r').read()
        
        
    if inputpassword == AdminPassword and adminloginuser == True:
        print ('adminlogin')
        passwordexists = False
        passwordloop = False
        adminlogin = True
    else:
        try:
            (Password) = open(inputpassword,'r').read()
            
            
            
        except IOError:
            print ('You were Incorrect')
            passwordexists = True
            
        
        
        
                    
        
        if (Password) == (inputpassword) or adminlogin == True:
            print ('correct')
            print (adminlogin)
            passwordexists = False
            passwordloop = False
            

    
        
        
        

        else:
            loginattempts = open('loginattempts','r').read()
        
            
            if loginattempts == ('1'):
                open('loginattempts','w+').write('2')
             
            elif loginattempts == ('2'):
                open('loginattempts','w+').write('3')
            elif loginattempts == ('3'):
                open('loginattempts','w+').write('4')
            elif loginattempts == ('4'):
                open('loginattempts','w+').write('5')
            else:
                open('loginattempts','w+').write('1')
            print ("incorrect")


        
        
        

#Menu from here you can go to view edit or create scores


menuactive = (True)

scorechecker = ()
while menuactive == True:        
    print ("")
    print ("")
    print ("main menu")
    print ("")
    print ("press 1 to view scores")
    print ("press 2 to add new scores")
    if adminlogin == True:
        print ("press 3 to add a new teacher")
    print ('press enter to exit the program')

    
    chosen = input('')

    if chosen == ('1'):
        yearchosen = ('')
        classchosen = ('')
        subjectchosen = ('')
        testname = ('')
        name = ('')
        txt = ('')
        #View scores
        viewer = ('')

        #checks the class
        classchosen = input('Class Name: ')
        viewer = viewer + classchosen
        
        addsubjectcheck = True
        
        while addsubjectcheck == True:
            addaccesscode = input('Access Code: ')
            addaccesscode = hashlib.sha256(str.encode(addaccesscode)).hexdigest()
            admincode = open('admincode','r').read()
            if addaccesscode == admincode:
                admincode1 = True
                print ('Admin Access')
                addsubjectcheck = False
                codesubjects = ()

            else:
                
                try:
                    codesubjects = open(addaccesscode,'r').read()
                    addsubjectcheck = False
                
                except IOError:
                    print ('make sure you put in the code correctly')
                    addsubjectcheck = True
        subject = True
        accessgranted = False
        while subject == True:
            print ('type in the subject that you wish to view')
            print ('or enter 1 to go to menu')
            subjectchosen = input('')
            if (subjectchosen) in (codesubjects) or admincode1 == True:
                
                subject = False
                accessgranted = True
            elif subjectchosen == ('1'):
                subject = False
                accessgranted = False
            else:
                print ('make sure you put in the subject right')
                
        if  accessgranted == True:

            
            viewer = viewer + subjectchosen
            #choose your test that you want to view
            print ('1 for autumn assesment')
            print ('2 for december assesment')
            print ('3 for january assesment')
            print ('4 for spring assesments')
            print ('5 for end of year assesments')
            print ('either use the following as a guideline for some of the assesments  you have done or type in the neame you gave when scoring')
            testname = input ('')
            viewer = viewer + testname

            #Now the pupils name
            viewperson = True
            while viewperson == True:
                print ('')
                print('now the pupil in the format')
                print ('firstname.lastname')
                print ('or type average for a class average')
                name = input('')
                viewernamed = viewer + name
            
            
            
            
        
       
                #checks whether the file exists
                try:
                    z = open(viewernamed,'r').read()
                
                    fileexists2 = ('')
                
                except IOError:
                    #if there was not a file it says so
                    fileexists2 = ('1')

                if fileexists2 == ('1'):
                    print('File does not exist, make sure you put in the information correctly or that the test has already been scored')
                    print ('')
                    print ('')
                    viewperson = False
                    
                elif fileexists2 == (''):
                    tempaccess = open(viewernamed,'r').read()
                    print (tempaccess,'%')
                    print ('press enter to view another student ')
                    print ('type 1 to go to menu')
                    homeornot = input('')
                    if homeornot == ('1'):
                        viewperson = False
                
                                
                
                
            
    elif chosen == ('2'):
        viewer = ('')
        yearchosen = input('which year do you want to add to ')
        viewer = viewer + yearchosen
        classchosen = input('which class do you want to view (just the ending e.g for 9m  just m)')
        viewer = viewer + classchosen
        addsubjectcheck = True
        while addsubjectcheck == True:
            addaccesscode = input('Access Code: ')
            addaccesscode = hashlib.sha256(str.encode(addaccesscode)).hexdigest()
            accessgranted = False
            try:
                codesubjects = open(addaccesscode,'r').read()
                addsubjectcheck = False
                
            except IOError:
                print ('make sure you put in the code correctly')
                addsubjectcheck = True
        subject = True
        while subject == True:
            print ('type in the subject that you wish to view')
            print ('or enter 1 to go to menu')
            subjectchosen = input('')
            if (subjectchosen) in (codesubjects):
                print ('go ahead')
                subject = False
                accessgranted = True
            elif subjectchosen == ('1'):
                subject = False
                accessgranted = False
            else:
                print ('make sure you put in the subject right')
                
        if  accessgranted == True:
                        
            viewer = viewer + subjectchosen
            print ('1 for autumn assesment')
            print ('2 for december assesment')
            print ('3 for january assesment')
            print ('4 for spring assesments')
            print ('5 for end of year assesments')
            print ('either use the following as a guideline for some of the assesments  you have done or type in the neame you gave when scoring')
            testname = input ('')
        

            viewer = viewer + testname
            testagain = True
            average = (0)
            averagenumber = (0)
            while testagain == True:
                print ('')
            
                print('now the pupil in the format')
                print ('firstname.lastname')
                name = input('')
                viewernamed = viewer + name
            
            
                percentagecheck = True
                while percentagecheck == True:
                    averagenumber = averagenumber + 1
                    print ('what percentage did they get')
                    try:
                    
                        tempscore = input ()
                        average = average + int(tempscore)
                        percentagechecker = True
                    
                    except ValueError:
                        print ('There was an error')
                        percentagechecker = False
                    if percentagechecker == True:
                        percentagecheck = False
                    
                open(viewernamed,'w+').write(tempscore)
                
            
            
            
                print ('1 to go to menu')
                print ('or press enter to score again')
                scoreagain = input('')
                if scoreagain == ('1'):
                    chosen = ('')
                    vieweraverage = viewer + ('average')
                    testagain = False
                    averagesaved = average/averagenumber
                    open(vieweraverage,'w+').write(str(averagesaved))
                    exit
                else:
                    viewernamed = viewer
                    exit
            
    elif chosen == (''):
        sys.exit()

    elif chosen == ('3') and adminlogin == True:
        print ('here you add new Accounts')

        newusername = input('Username? ')
        newpassword = input ('Password? ')
        subjectcode = input ('This code gives them access to only the subjects they should have access to ')
        hashedusername = hashlib.sha256(str.encode(newusername)).hexdigest()
        hashedpassword = hashlib.sha256(str.encode(newpassword)).hexdigest()
        hashedcode = hashlib.sha256(str.encode(subjectcode)).hexdigest()
        

        print ('which of the following subjects do you want this teacher to have')

        print ('geography')
        print ('maths')
        print ('english')
        print ('it')
        print ('art')
        print ('awe')
        print ('citizenship')
        print ('business studies')
        print ('drama')
        print ('dt')
        print ('foodtech')
        print ('geography')
        print ('history')
        print ('spanish')
        print ('german')
        print ('french')
        print ('music')
        print ('pe')
        print ('rs')
        print ('science')
        print ('physics')
        print ('chemistry')
        print ('bilogy')
        print ('')

        SubjectAgain = True
        Subjects10 = ('')
        SubjectAgain100 = ('')

        while SubjectAgain == True:
            

            print ('enter to add subject')
            print ('1 to finalise account creation')
            SubjectAgain1 = input('')
            
            
            
            if SubjectAgain1 == (''):
                SubjectAgain = True
                print ('')
                SubjectAgain100 = input('Subject? ')
                Subjects10 = Subjects10 + ('') + (SubjectAgain100)
            elif SubjectAgain1 == ('1'):
                open(hashedcode,'w+').write(Subjects10)
                open(hashedusername,'w+').write(hashedusername)
                open(hashedpassword,'w+').write(hashedpassword)
                SubjectAgain = False
                
                exit
