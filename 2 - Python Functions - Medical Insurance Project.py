''' CREATING A FUNCTION 
Question 1
First, take a look at the code in script.py.

In this code, we estimate the medical insurance costs for two individuals, Maria and Omar, based on five variables:

    age: age of the individual in years
    sex: 0 for female, 1 for male
    bmi: individual’s body mass index
    num_of_children: number of children the individual has
    smoker: 0 for a non-smoker, 1 for a smoker

These variables are used in the following formula to estimate an individual’s insurance cost (in USD):

insurance_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500insurance\_cost = 250*age - 128*sex + 370*bmi + 425*num\_of\_children + 24000*smoker - 12500insurance_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500

Click “Save” to see the estimated insurance costs for Maria and Omar.

Question 2
The code used to estimate insurance costs for Maria and Omar looks quite similar – in both cases we calculate the insurance cost using the same formula and then print the output.

This code is a great candidate for a function because it involves repeating almost identical commands in multiple places.

Let’s start by defining a function called calculate_insurance_cost() on line 2. For now, your function should not have any parameters or output.

Question 3 
Let’s outline the behavior we want our function to have. Inside of calculate_insurance_cost(), do the following:

    Create a variable called estimated_cost. For now, set this variable equal to a value of 1000. You’ll add the full formula in the next step.
    Add a print statement that prints estimated_cost. You should output a message similar to: "The estimated insurance cost for this person is xxx dollars."
    Return estimated_cost
'''

''' ADDING PARAMETERS TO A FUNCTION 
Question 4
Nice job – you’ve created a simple Python function that we’ll use to estimate medical insurance costs.
However, the function currently returns a value of 1000. We want it to return our insurance cost formula instead.
Modify the function definition so that it contains five parameters:
    age
    sex
    bmi
    num_of_children
    smoker
Take a look at the hint if you need a reminder on how to add parameters to a function definition.

Question 5
Now that we have set up the function to take inputs for each of the values needed in the insurance formula, we can make use of them inside of our function.
In calculate_insurance_cost(), change the value of estimated_cost from 1000 to our formula for insurance cost.
Remember that the formula for insurance cost is:
250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

Question 6
The function is now properly set up to calculate an individual’s medical insurance costs based on the five variables passed into it. Let’s test this out!

Go to the section of code that estimates Maria’s insurance cost.

Rename insurance_cost as maria_insurance_cost and set it equal to calculate_insurance_cost() with the appropriate values for Maria as arguments.

Question 7
Now, remove the print statement for Maria since our function will take care of printing the estimated cost for us.

Additionally, remove the five lines of code defining the initial variables for Maria, as we are now passing in these values directly in the function call.

Question 8
Repeat steps 6-7 for Omar:
    Rename insurance_cost as omar_insurance_cost and set it equal to the calculate_insurance_cost() function, passing in the appropriate values as arguments.
    Remove the initial variables and print statement for Omar.
Notice how much cleaner our code is now! By utilizing a Python function, we were able to condense many lines of code into just a few.

Quesiton 9
Click “Save” to see the estimated insurance costs for Maria and Omar as calculated by your function.

In the output terminal, notice that it says "The estimated insurance cost for this person is..." but it does not specify the actual name of the person.

To fix this, begin by adding an additional parameter called name to the function definition.

Question 10
Next, modify the print statement in the function so that it includes the new name parameter, replacing "this person" with the actual name of the person.

Question 11
We must also update our function calls, passing in the name variable as an argument.

Update the function call for maria_insurance_cost, passing in name = "Maria" as an argument.

Do the same for Omar, passing in name = "Omar".

Now if you click “Save”, you’ll see that our function is able to write a more personalized message specifying the name of the individual it is estimating insurance costs for. Pretty neat, right?

Question 12
In this example, we calculated the insurance costs for two individuals, but with our new code we can easily extend this to thousands or even millions of individuals.

To illustrate, estimate your own insurance cost.
At the bottom of your code, create a new insurance_cost variable for yourself, similar to how we did it for Maria and Omar.
Set the variable equal to a function call to calculate_insurance_cost(), passing in your own name, age, sex, bmi, number of children, and smoker status.
Click “Save” to see the result.

'''

# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost

# Initial variables for Maria 
'''
age = 28
sex = 0  
bmi = 26.2
num_of_children = 3
smoker = 0  
'''

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria",28,0,26.2,3,0)

# Initial variables for Omar
'''
age = 35
sex = 1 
bmi = 22.2
num_of_children = 0
smoker = 1  
'''

# Estimate Omar's insurance cost 
insurance_cost =  calculate_insurance_cost("Omar", 35,1,22.2,0,1)

#Estimate your own insurance cost
insurance_cost = calculate_insurance_cost("Charles", 26,1,18.7,0,0)



