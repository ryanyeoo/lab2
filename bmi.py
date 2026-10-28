
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    if (bmi<18.5):
        print("under weight")
    elif(bmi<=25):
            print("normal weight")
    else:
            print("over weight")

calculate_bmi(weight=67, height=1.73)

