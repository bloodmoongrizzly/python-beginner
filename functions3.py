def gradeTranslator(score):
        if score >= 90:
            grade="A"

        elif score >= 80:
            grade= "B"

        elif score >=70:
            grade="C"
            
        elif score >= 60:
            grade="D"
            
        else:
            grade="F"
            
        return grade

inScore = int(input("What is the score?: "))
outGrade =  gradeTranslator (inScore)
print("The Letter Grade is: ", outGrade)

        
