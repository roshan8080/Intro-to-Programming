/* Author: Roshan Rijal
   ## Due Date: November 20
   ## Class: CSCI 2000
   ## Instructor: Ms. Tyler Greer
   ## Program Assignment: 11
   ## Program Title: Circle
   ## Program Description: This program design and implement a 
   ##                      class called Circle.                      
   ## Plagiarism Statement:
   ## I swear that I have not received or given aid on this program
   ## beyond guidelines of the course including giving or receiving
   ## specific code content.        */




/**
 * The Circle class stores and manipulates
 * data for a circle.
 */
public class Circle
{
   private double radius;
   
   
    /**
  * The setRadius method accepts an argument
  * which is stored in the radius field.
  */
   public void setRadius(double r)
   {
      radius = r;
   }
   
   
    /**
  * The getRadius  method returns the value
  * stored in the radius field.
  */
    public double getRadius()
   {
      return radius;
   
   }

  
   /**
  * The getArea method returns the value of the
  * PI field times the square of radius field.
  */
   public double getArea()
   {
      return Math.PI * Math.pow(radius,2);
   
   }

  
   /**
  * The getCircumference method returns the value of the
  * 2 times PI field times the radius field.
  */
   public double getCircumference()
   {
      return 2 * Math.PI * radius;
   }

}









