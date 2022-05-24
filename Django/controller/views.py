from django.shortcuts import render, redirect
import RPi.GPIO as GPIO
import time 


GPIO.setmode(GPIO.BOARD)

ena = 11
in2 = 13
in1 = 15
in3 = 16 
in4 = 18
enb = 22

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)


def index(request):
    return render(request,'index.html')

def forword(request):
    print("Motorlar ileri gidiyor")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(ena,GPIO.HIGH)
    
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(enb,GPIO.HIGH) 
    
def back(request):
    print("Motorlar geri gidiyor")
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(ena,GPIO.HIGH)
    
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(enb,GPIO.HIGH) 
    
def left(request):
    print("Motorlar saga gidiyor")
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(ena,GPIO.HIGH)
    
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(enb,GPIO.HIGH) 
    
def right(request):
    print("Motorlar sola gidiyor")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(ena,GPIO.HIGH)
    
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(enb,GPIO.HIGH) 
    
def stop(request):
    print("Motorlar durdu.")
    GPIO.output(ena,GPIO.LOW)
    GPIO.output(enb,GPIO.LOW) 
    

def forward(request):
    return redirect('index')

