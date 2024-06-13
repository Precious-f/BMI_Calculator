print('Hi there, lets help you calculate your Body Weight Index')
print('')
user_input =input('Do you to continue ?(yes/no) ')
if user_input.lower()=='yes':   #.lower fuction to covert input into lowercase
    print('')
    print("Loading.........")
    print('')

    #Input weight and  height  using  in input  function
    weight=float(input('Input your weight in kilograms: '))
    height=float(input('Input your height in meters: '))

    print('')
    BMI=(weight/( height * height))
    BMI_2dp = round(BMI,2)
    
    # Classify the BMI as underweight, healthy, overweight, severely overweight, obese, or severely obese using nested if statement.
    print('Your body weight index is ',BMI_2dp )
    if  BMI_2dp < 18.5:
        print("You are underweight.")
    elif BMI_2dp <= 24.9:
        print("You are healthy.")    
    elif BMI_2dp <= 29.9:
        print("You are overweight.")    
    elif BMI_2dp <= 34.9:
        print("You are severly  overweight.")    
    elif BMI_2dp <= 39.9:
        print("You are obese.")    
    elif BMI_2dp > 40:
        print("You are severly obese.")
        print("you are adviced to go on a diet,and engage in execises that help burn fat!")
    



else:
    print('Program stopped')
    

