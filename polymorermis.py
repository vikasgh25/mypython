class Bird :
     def speak(self):
        print("i am singer")
class parrot(Bird):
      def speak(self):
         print("i am not singer")
obj = parrot()
obj.speak() 
