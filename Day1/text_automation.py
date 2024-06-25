import pyautogui
import time

def Greet(name):
  greeting_message = f'Hello, {name}! How are you doing?'
  return greeting_message

# List of names
names = ["Yaman", "Corey", "Adam", "Steve", "Rick", "Thomas", "John", "Adam", "Steve", "Rick", "Thomas", "John", "Adam", "Steve", "Rick", "Thomas", "John", "Adam", "Steve", "Rick", "Thomas"]

# looping through the list, for each name in names do smth,
for name in names:
  greet_message = Greet(name)
  time.sleep(2)
  pyautogui.write(greet_message)
  pyautogui.press('enter')

  """
  How would i code the same in Javascript??
  function Greet(name){
  console.log(`Hello, ${name}! How are you doing?`);
  }

  names = ["Yaman", "Corey", "Adam", "Steve", "Rick", "Thomas"];

  names.forEach((name)=>{
  Greet(name);
  })
  """