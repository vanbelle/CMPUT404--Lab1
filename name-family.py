class Student:
    
    courseMarks={}
    name=""
    family=""
    
    def __init__(self, name, family):
        self.name = name
        self.family = family
    
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
        
    def average(self):
        total = len(self.courseMarks)
        sum_marks = 0
        for key, val in self.courseMarks.iteritems:
            sum_marks += val
        
        return sum_marks / total
        

def main():
    student = Student("Raman", "Dhatt")
    student.addCourseMark("CMPUT174", 100)
    student.addCourseMark("CMPUT175", 80)
    
    print "Average grade: {0}", str(student.average())

if __name__ == "__main__":
    main()
