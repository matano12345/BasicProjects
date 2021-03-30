using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SevenBoom
{
    class Program
    {
        public static int GetValidNumber(int minimum)
        {
            /* This function is responsible for having the user input a valid integer number.
             * minimum - defines the lowest acceptable int value
             * return: a valid integer number which is equal or bigger than the minimum number */
            int validNumber;
            string input;
            while (true)
            {
                input = Console.ReadLine();
                if (int.TryParse(input, out int number))
                {
                    if (number >= minimum)
                    {
                        validNumber = number;
                        break;
                    }
                    else
                        Console.WriteLine("Please enter a number that is equal or bigger than {0}",minimum);
                }
                else
                    Console.WriteLine("Please enter a valid integer number");
            }
            return validNumber;
        }

        public static void PrintStartScreen(int numbers, int errors)
        {
            /*This function is responsible for printing the welcome message after recieving the amount of numbers the user want to play
             * and the errors he is willing to make.
             * numbers - how many numbers the user want to play.
             * errors - how many errors the user is willing to make before losing. */
            string line = " Let the game begin! You chose to play till " + numbers + " and your max errors is set to " + errors + ". ";
            string mark = "~",space="+"; //mark is set as the outer edge of the frame and space is set as the inside edge of the frame
            int lineLength = line.Length + 4;
            Console.WriteLine();
            for (int i = 0; i < lineLength; i++)
                Console.Write(mark);
            Console.WriteLine();
            Console.Write(mark);
            for (int i = 0; i < lineLength - 2; i++)
                Console.Write(space);
            Console.Write(mark);
            Console.WriteLine();
            Console.WriteLine(mark + space + line + space + mark);
            Console.Write(mark);
            for (int i = 0; i < lineLength - 2; i++)
                Console.Write(space);
            Console.WriteLine(mark);
            for (int i = 0; i < lineLength; i++)
                Console.Write(mark);
            Console.WriteLine(); Console.WriteLine();
        }
        public static bool RelatedToSeven(int num)
        {
            /* This function is responsible for checking whether or not a number is divided by 7 or has 7 in the unit digit
             * return: true if number is related to 7, false otherwise */
            return (num % 7 == 0 || num % 10 == 7);
        }
        static void Main(string[] args)
        {
            int mistakes = 0, gamelimit = 0, errorsAllowed,i=1 ;
            string number,result,wrongNumbers="";
            Console.WriteLine("Hello Champ! How many numbers would you like us to play?");
            gamelimit = GetValidNumber(2);
            Console.WriteLine("How many errors are you allowed to make if I may ask?");
            errorsAllowed = GetValidNumber(0);
            PrintStartScreen(gamelimit, errorsAllowed);
            while(mistakes <= errorsAllowed && i<=gamelimit)
            {
                if (i % 2 == 0) //Computer's turn
                {
                    Console.Write("My Turn: ");
                    if (RelatedToSeven(i))
                        Console.WriteLine("Boom");
                    else
                        Console.WriteLine(i);
                }
                else //Human's turn
                {
                    Console.Write("Your turn: ");
                    number = Console.ReadLine();
                    if (RelatedToSeven(i))
                    {
                        if (number != "Boom")
                        {
                            mistakes++;
                            if(mistakes<errorsAllowed)
                                wrongNumbers += i+",";
                            else
                                wrongNumbers += i + ".";
                        }
                    }  
                    else
                    {
                        if (i + "" != number)
                        {
                            mistakes++;
                            if (mistakes < errorsAllowed) 
                                wrongNumbers += i + ",";
                            else
                                wrongNumbers += i + ".";
                        }
                    }   
                }
                i++;
            }
            if (mistakes > errorsAllowed)
                result = "PC Win!";
            else
                result = "You Win!";
            if (wrongNumbers != "")
                result += "\nWrong numbers were " + wrongNumbers;
            Console.WriteLine(result);
        }
    }
}
