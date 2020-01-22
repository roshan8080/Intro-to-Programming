/* Author: Roshan Rijal
   ## Due Date: November 16
   ## Class: CSCI 2000
   ## Instructor: Ms. Tyler Greer
   ## Program Assignment: 10
   ## Program Title: OrderTickets
   ## Program Description: This program create a simple user interface for
   ##                      the Cerebral Stage's website.
   ## Plagiarism Statement:
   ## I swear that I have not received or given aid on this program
   ## beyond guidelines of the course including giving or receiving
   ## specific code content.        */




import java.util.Scanner;    // Import Scanner class which is in util folder inside the java folder. 

public class OrderTickets
{
   public static void main(String [] args)
   {
      // Declaring variables
      String name;
      String show;
      String date;
      
      System.out.println("Welcome to the Cerebral Stage Online Ticket Service!");
      System.out.println("====================================================");
      System.out.println("\nEnter your information to start your ticket order.");
      System.out.println("--------------------------------------------------");
      
      Scanner scan= new Scanner(System.in);   // Creating object of class 'Scanner'
      
      System.out.print("\nEnter your fist and last name: ");    // Asking user for name
      name = scan.nextLine();    // Storing user input in variable 'name' 
      
      System.out.print("Enter the name of the show: ");         // Asking user for show
      show = scan.nextLine();   // Storing user input in varable 'show'
      
      System.out.print("Enter the date of the show: ");         // Asking user for date
      date = scan.nextLine();   // Storing user input in variable 'date'
       
      System.out.println("\nSeating Options");
      System.out.println("---------------");
      System.out.println("Section 1 - $20.00");
      System.out.println("Section 2 - $40.00");
      System.out.println("Section 3 - $60.00");
      
      System.out.print("\nEnter the section number of your choice: ");     // Asking user for section
      int section = scan.nextInt();    // storing user input in variable 'section'
      
      double selection =  section * 20;
      
      System.out.printf("\nYou selected Section %d for $%.2f per ticket.",section,selection);
      
      System.out.print("\n\nEnter the number of tickets you want to purchase: ");    // Asking user of no. of tickets
      int numberOfTickets = scan.nextInt();   // Storing user input in variable 'numberOfTickets'
      
      double price = selection * numberOfTickets;
      double tax = price * 0.11;
      double total = price + tax;
      
      System.out.println("\nTotal Cost");
      System.out.println("----------");
      
      System.out.printf("Price:  $%5.2f", price);
      System.out.printf("\nTax:    $%5.2f", tax);
      System.out.printf("\nTotal:  $%5.2f", total );
      
      System.out.println("\n\nPlease print out your 2 copies of the ticket below.");
      System.out.println("---------------------------------------------------");
      
      System.out.println("\n====================================================");
      
      String dash = "||";
      
      System.out.printf("%2s %15s %2s  %5s %-20s %2s ",dash,"Celebral Stage",dash,"Show:",show, dash);
      
      System.out.printf("\n%s                 %s                             %2s",dash,dash,dash);
      
      System.out.printf("\n%s     %s    %s  %s %-20s %s",dash,"Official",dash,"Name:",name,dash);
      
      System.out.printf("\n%s     %s      %s  %s %-20s %s",dash,"Online",dash,"Date:",date,dash); 
      
      System.out.printf("\n%s     %s      %s  %s %-17s %s",dash,"Ticket",dash,"Section:",section,dash);
      
      System.out.println("\n====================================================");
      
      System.out.println("\nEnjoy the show!");   

         
   
   }
   
   




}