from cgi import test


Room_number= {'CS101':'3004',
             'CS102':'4501',
             'CS103':'6755', 
             'NT110': '1244',
             'CM241': '1411'}




Instructor= {'CS101':'Haynes',
             'CS102':'Alvarado',
             'CS103':'Rich', 
             'NT110': 'Burke',
             'CM241': 'Lee'}

Meeting_Times= {'CS101':'8:00 AM',
             'CS102':'9:00 AM',
             'CS103':'10:00 AM', 
             'NT110': '11:00 AM',
             'CM241': '1:00 PM'}


course_number = input('Enter a course number.')

if course_number in Room_number:
    print("Course Number:",course_number)
    print("Room Number:",Room_number[course_number])
    print("Instructor:",Instructor[course_number])
    print("Meeting Time:", Meeting_Times[course_number])

else:
    print('Course number is not found')



#Part 2

codes= {'A':'!','a': '@','B': '#','b': '$','C': '%','c': '^','D': '&','d': '*','E': '(','e': ')','F': '-','f': '_','G': '+','g': '=','H': '~','h': '`','I': '1','i': '2','J': '3','j': '4','K': '5','k': '6','L': '7','l': '8','M': '9','m': '0','N': 'Q','n': 'W','O': 'E','o': 'R','P': 'T','p': 'Y','Q': 'U','q': 'I','R': 'O','r': 'P','S': '[','s': ']','T': '{','t': '}','U': 'A','u': 'S','V': 'D','v': 'F','W': 'G','w': 'H','X': 'J','x': 'K','Y': 'L','y': 'C','Z': 'M','z': 'N'}

test ={'T':'!'}

#read the file
security = open('info_security.txt','r'


words = security.read()
words = str(security)

security.close()


#Create a new file
outfile = open("info_security_outfile.txt", "w")

#encryption
for letter in words:
    if letter in test:
        encrypt = test[letter]
    
        outfile.write(encrypt)
    else: 
        outfile.write(letter)

outfile.close()



