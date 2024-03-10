
import streamlit as st

def calculate_tax(income):
    income = int(input("Please enter your Salary: "))
    if income < 250000:
        print(f"You will be exempted{income}.")
        print("Thank you for filing your ITR")
    elif income >= 250000 and income < 300000:
        print(f'Old regime tax tax is {round(income/12)}: ', income *5/100)
        print(f"You will be exempted, as your salary is {round(income/12)}.")
    elif income > 300000 and income < 500000 :
        print(f'Old regime tax amount is {round(income/12)}: ', income *5/100)
        print(f"You are New regime tax amount is :", income *5/100)
    elif income > 500000 and income < 600000 :
        print(f'Old regime tax amount is {round(income/12)}: ', income *20/100)
        print(f"You are New regime tax amount is {round(income/12)} :", income *5/100)
    elif income > 600000 and income < 900000 :
        print(f' your old regime tax amount is:', round(income*20/100))
        print(f' You liable to pay {round(income*10/100)}, as you have choosen new regime tax')
    elif income > 900000 and income < 100000:
        print('old regime tax: ', income* 20/100)
        print('New regime tax: ', income * 15/100)
    elif income > 100000 and income < 1200000:
        print('old regime tax: ', income * 30*100)
        print('New regime tax: ', income *15/100)
    elif income > 1200000 and income < 1500000:
        print("old regime tax (30%)", income * 30/100)
        print("New regime tax ( 20%)", income *20/100)
    else:
        print(f' your old regime tax amount is {income*30/100} for salary of 15 lakhs')
        print(f' You liable to pay {income*30/100} for salary of 15 lakhs')


def main():
    st.title("Income tax calculator")
    income = st.number 