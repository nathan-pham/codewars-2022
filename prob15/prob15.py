import os

__dirname = os.path.dirname(__file__)

def read_digital_letters():
    letters = """
    ####
#  #
####
#  #
#  #=A

####
#  #
####
#  #
####=B

####
#   
#   
#   
####=C

### 
#  #
#  #
#  #
### =D

####
#   
### 
#   
####=E

####
#   
####
#   
#   =F

####
#   
# ##
#  #
####=G

#  #
#  #
####
#  #
#  #=H

####
 #  
 #  
 #  
####=I

####
  # 
  # 
# # 
### =J

#  #
# # 
##  
# # 
#  #=K

#   
#   
#   
#   
####=L

#   #
## ##
# # #
#   #
#   #=M

#   #
##  #
# # #
#  ##
#   #=N

####
#  #
#  #
#  #
####=O

####
#  #
####
#   
#   =P

#### 
#  # 
#  # 
# ## 
### #=Q

#### 
#  # 
#### 
# #  
#   #=R

####
#   
####
   #
####=S

####
 #  
 #  
 #  
 #  =T

#  #
#  #
#  #
#  #
####=U

#   #
#   #
 # # 
 # # 
  #  =V

#   #
#   #
# # #
## ##
#   #=W

#   #
 # # 
  #  
 # # 
#   #=X

#   #
 # # 
  #  
  #  
  #  =Y

#####
   # 
  #  
 #   
#####=Z

#
#
#
 
#=!

 
 
 
 
#=.
    """.strip().split('\n\n')

    return [(letter[:-2], letter[-1]) for letter in letters]

with open(os.path.join(__dirname, "./input.txt")) as file:
    digital_letters = read_digital_letters()
    letters = file.read().strip()

    assembled_letters = []
    

    for i in range(len(letters)):
        letter = letters[i]
        for digital_letter in digital_letters:
            if letter == digital_letter[1]:
                assembled_letters.append(digital_letter[0].split('\n'))

                if i != len(letters) - 1: assembled_letters.append([" "] * 5)

    # print each letter horizontally
    for i in range(len(assembled_letters[0])):
        for j in range(len(assembled_letters)):
            print(assembled_letters[j][i], end='')
        print()