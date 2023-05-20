def calculate_bmi() -> None:
    """
    Function that computes the body mass index of an individual
    
    Parameters:
        None
    
    Returns:
        None: Only prints output to the scree
    """
    
    # Prompt the user to enter their weight in kilograms
    weight = float(input("Enter your weight (in kilograms): "))

    # Prompt the user to enter their height in meters
    height = float(input("Enter your height (in meters): "))

    # Calculate the BMI using the formula: BMI = weight / height**2
    bmi = weight / height**2

    # Determine the BMI category and associated health risks
    if bmi < 18.5:
        category = "Underweight"
        risks = "You may have an increased risk of nutritional deficiency and osteoporosis."
    elif bmi < 25:
        category = "Normal weight"
        risks = "You have a generally healthy weight range."
    elif bmi < 30:
        category = "Overweight"
        risks = "You may have an increased risk of developing various health issues such as heart disease."
    else:
        category = "Obese"
        risks = "You may have a significantly higher risk of developing serious health conditions such as diabetes and cardiovascular diseases."

    # Display the calculated BMI, BMI category and associated health risks
    print("Your BMI is: {:.2f}".format(bmi))
    print("BMI Category: {}".format(category))
    print("Health Risks: {}".format(risks))



# Call the function to calculate the BMI
calculate_bmi()
