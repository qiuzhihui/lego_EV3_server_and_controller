'''
Author: Zhihui Qiu
Email:  zhihui.qiu@tufts.edu
Data:   2015.07.24
Have fun
'''

import collections
from Tkinter import *
import tkFont
import urllib2
import json
import httplib



def robot_handle():
	url = e1.get()
	index=url.index(':')
	addr=url[: index]
	port=url[index+1 :]
	conn = httplib.HTTPConnection(addr, port)
	conn.request("GET", "/")
	r1 = conn.getresponse()
	html = r1.read()
	print html


def run_handle():
	a='haha';

def stop_handle():
	url = e1.get()
	url_post='http://' + url + '/'
	data = {"device":"motor","motor0":str(s1.get()),"motor1":str(s2.get()),"motor2":str(s3.get()),"motor3":str(s4.get()),"cmd":"stop"}
	data = json.dumps(data)
	r = urllib2.Request(url_post, data,headers={'Content-Type': 'application/xml'})
	u = urllib2.urlopen(r)

def LED_handle():
	url = e1.get()
	url_post='http://' + url + '/'
	data = {"device":"led","led1":str(s11.get()),"led2":str(s12.get()),"led3":str(s13.get()),"led4":str(s14.get())}
	data = json.dumps(data)
	r = urllib2.Request(url_post, data,headers={'Content-Type': 'application/xml'})
	u = urllib2.urlopen(r)
	

def sensor_handle():

	url = e1.get()
	url_post='http://' + url + '/'
	data = {"device":"sensor"}
	data = json.dumps(data)
	r = urllib2.Request(url_post, data,headers={'Content-Type': 'application/xml'})
	u = urllib2.urlopen(r)
	response = u.read()
	j = json.loads(response)
	e14.delete(0, END)
	e14.insert(0,j['type']+ ': ' +j['port'])


def motor_update(val):
	url = e1.get()
	url_post='http://' + url + '/'
	data = {"device":"motor","motor0":str(s1.get()),"motor1":str(s2.get()),"motor2":str(s3.get()),"motor3":str(s4.get()),"cmd":"run"}
	data = json.dumps(data)
	print data
	r = urllib2.Request(url_post, data,headers={'Content-Type': 'application/xml'})
	u = urllib2.urlopen(r)
	


if __name__ == "__main__":

	#Tkinter initialization 
	root = Tk()
	root.geometry("1000x700")
	root.title("EV3 Control")




	#Title of controller
	label=Label(root, text="Ev3Dev Controller",height=3,font=("Helvetica",20,"bold")).grid(row=0,column=2,sticky=S+W+N+E)
	Label(root, text="Robot IP:Port",height=5,font=("Helvetica",15)).grid(row=1,column=0)
	e1=Entry(root,width=20)
	e1.grid(row=1,column=1)
	e1.insert(10,"192.168.2.3:8000")
	Button(root, text='Rock it', width=8,command=robot_handle,font=(10)).grid(row=1,column=2)


	



	#Motor Control
	label=Label(root, text="Motor Control",font=("Helvetica",15)).grid(row=2,column=0,sticky=S)
	label=Label(root, text="Motor Speed",font=("Helvetica",15)).grid(row=2,column=2,sticky=S)

	Label(root, text="Motor A:").grid(row=3,column=0,sticky=S)
	s1=Scale(root, from_=-100, to=100, length=300,orient=HORIZONTAL,takefocus=100,command=motor_update)
	s1.grid(row=3,column=1)
	s1.set(0)
	Entry(root,width=5).grid(row=3,column=2,sticky=S)

	Label(root, text="Motor B:").grid(row=4,column=0,sticky=S)
	s2=Scale(root, from_=-100, to=100, length=300,orient=HORIZONTAL,command=motor_update)
	s2.grid(row=4,column=1)
	s2.set(0)
	Entry(root,width=5).grid(row=4,column=2,sticky=S)

	Label(root, text="Motor C:").grid(row=5,column=0,sticky=S)
	s3=Scale(root, from_=-100, to=100, length=300,orient=HORIZONTAL,command=motor_update)
	s3.grid(row=5,column=1)
	s3.set(0)
	Entry(root,width=5).grid(row=5,column=2,sticky=S)

	Label(root, text="Motor D:").grid(row=6,column=0,sticky=S)
	s4=Scale(root, from_=-100, to=100, length=300,orient=HORIZONTAL,command=motor_update)
	s4.grid(row=6,column=1)
	s4.set(0)
	Entry(root,width=5).grid(row=6,column=2,sticky=S)

	
	Button(root, text='run', width=8,command=motor_update).grid(row=7,column=0,sticky=N)
	Button(root, text='stop', width=8,command=stop_handle).grid(row=7,column=1,sticky=W+N)






	#LED control
	Label(root, text="LED control",font=("Helvetica",15)).grid(row=2,column=3,padx=150,sticky=S)

	s11=Scale(root, from_=0, to=100, length=150,orient=HORIZONTAL)
	s11.grid(row=3,column=3,padx=50)
	s11.set(20)

	s12=Scale(root, from_=0, to=100, length=150,orient=HORIZONTAL)
	s12.grid(row=4,column=3)
	s12.set(20)

	s13=Scale(root, from_=0, to=100, length=150,orient=HORIZONTAL)
	s13.grid(row=5,column=3)
	s13.set(20)

	s14=Scale(root, from_=0, to=100, length=150,orient=HORIZONTAL)
	s14.grid(row=6,column=3)
	s14.set(20)

	Button(root, text='update', width=8,command=LED_handle).grid(row=7,column=3,sticky=W,padx=110)
	





	#Sensor Reading:
	Label(root, text="Sensor Readings",height= 3,font=("Helvetica",15)).grid(row=8,column=0,ipady=5,sticky=S)

	Label(root, text="Port1").grid(row=9,column=0)
	e11=Entry(root,width=20)
	e11.grid(row=9,column=1,sticky=W)

	Label(root, text="Port2").grid(row=10,column=0)
	e12=Entry(root,width=20)
	e12.grid(row=10,column=1,sticky=W)

	Label(root, text="Port3").grid(row=11,column=0)
	e13=Entry(root,width=20)
	e13.grid(row=11,column=1,sticky=W)

	Label(root, text="Port4").grid(row=12,column=0)
	e14=Entry(root,width=20)
	e14.grid(row=12,column=1,sticky=W)


	Button(root, text='get', width=8,command=sensor_handle).grid(row=13,column=0)
	

	root.mainloop()



