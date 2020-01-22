/* Author: Roshan Rijal
   ## Due Date: November 28
   ## Class: CSCI 2000
   ## Instructor: Ms. Tyler Greer
   ## Program Assignment: 12
   ## Program Title: FoodItem
   ## Program Description: This program design and implement a 
   ##                      class called FoodItem.                      
   ## Plagiarism Statement:
   ## I swear that I have not received or given aid on this program
   ## beyond guidelines of the course including giving or receiving
   ## specific code content.        */







/**
 * The FoodItem class stores and manipulates
 * data for a Pantry class.
 */
public class FoodItem
{
  
   // declaring instance variable
   private String food;
   private int calories;
   private int fatGrams;
  
  
   // Define the FoodItem constructor to accept and initialize instance data for name of the food item, calories and fatGrams.
   public FoodItem(String foodnew,int caloriesnew,int fatGramsnew)
   {
      food = foodnew;
      calories = caloriesnew;
      fatGrams = fatGramsnew;
   } 
   
    
     /**
  * The setName method accepts an argument
  * which is stored in the food field.
  */
   public void setName(String name)
   {
      food = name;
   }
  
    
     /**
  * The setCalories method accepts an argument
  * which is stored in the calories field.
  */
   public void setCalories(int calories1)
   {
      calories = calories1;
   }

     
     /**
  * The setFatGrams method accepts an argument
  * which is stored in the fatGrams field.
  */
   public void setFatGrams(int fat)
   {
      fatGrams = fat;
   }
  
     
     /**
  * The getName  method returns the value
  * stored in the food field.
  */
   public String getName()
   {
      return food;
   }
  
   
     /**
  * The getCalories  method returns the value
  * stored in the calories field.
  */
   public int getCalories()
   {
      return calories;
   }
  

     /**
  * The getFatGrams  method returns the value
  * stored in the fatGrams field.
  */
   public int getFatGrams()
   {
      return fatGrams;
   }
   
 
  // This method returns a one-line description of the item
   public String toString()
   {
      return (food + " contains " + calories + " calories and " + fatGrams + " fat grams."); 
   }
  
  
  // This method returns an integer with the number of calories that fat contributes to the total calories
   public int caloriesFromFat()
   {
      return fatGrams * 9;
   }
  
  
  // This method returns a double calculates the percentage of the calories that comes from fat
   public double percentFat()
   {
      return (caloriesFromFat() * 1.0 )/calories;
   }
  
}
  

