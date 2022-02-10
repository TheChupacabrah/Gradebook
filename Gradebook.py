#Gradebook
#John Hatch

lloyd = {'name' : 'lloyd', 'hw' : [90.0, 97.0, 75.0, 92.0] , 'q' : [88.0, 40.0, 94.0] , 't' : [75.0, 90.0] }
alice = {'name' : 'alice', 'hw' : [09.0, 17.0, 67.0, 33.0] , 'q' : [24.0, 75.0, 44.0] , 't' : [13.0, 66.0] }
tyler = {'name' : 'tyler', 'hw' : [99.0, 97.0, 00.0, 100.0] , 'q' : [88.0, 95.0, 94.0] , 't' : [98.0, 90.0] }

students = [lloyd, alice, tyler]

#for x in students:
    #print(x)

def average(num):
    total = float(sum(num))
    avg = total / len(num)
    return avg
    
def get_average(student):
    hw = student['hw']
    q = student['q']
    t = student['t']
    avg = average(hw)*0.1 + average(q)*0.3 + average(t)*0.6
    return avg

#name = input('What is the student name ')



def get_letter_grade(score):
    if score >= 90:
        return('A')
    elif score >=80:
        return('B')
    elif score >=70:
        return ('C')
    elif score >=60:
        return('D')
    elif score <60:
        return('F')

def class_avg(students):
    results = []
    for x in students:
        results.append(get_average(x))
    return average(results)
    
    
print('Student average is ' + str(get_average(lloyd)))    
print('Student letter grade is ' + str(get_letter_grade(get_average(lloyd))))    
print('Class average is ' + str(class_avg(students)))
print('Class letter grade is ' + str(get_letter_grade(class_avg(students))))
    