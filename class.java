// hii, i am nagsen waghmare
//here i created two classes with two diffrent methods  
//and inside first  class named Bike declared main method in which i called the method  named changeSpeed

class Bike{
   String Size ;
   int cost;
    static void changeSpeed(int cost){
    System.out.println("cost");
   }
   public static void main(String args[]){
       changeSpeed();
       Bike s1 = new Bike();
       s1.cost = 10000;
        s1.Size = "Big";
        System.out.println(s1.cost+" "+s1.Size);
   }

}
class Car{
   int Mileage;
   int NumberofGears;
   int MaxSpeed;
     static void turn(int MaxSpeed){
       
         System.out.println("MaxSpeed");
     }
}

// Answer to Q.1 ==
// I learned how to create classes and how to declare methods in java
// initialize and access objects in class;
