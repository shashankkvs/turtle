from turtle import *

def arrow_c(size=None):
    global sc
    sc=Screen()
    sc.bgcolor("black")
    
if __name__ == "__main__":
        pointer = Turtle()
        pointer.color(input("enter color:"))
        arrow_c()
        while True:
           x=input()
           if "d" in x: pointer.fd(100)
           elif x=="q": break

