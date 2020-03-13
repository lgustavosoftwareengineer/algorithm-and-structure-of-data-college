/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exercicicio01aed;
import java.lang.reflect.Array;
import java.util.*;
/**
 *
 * @author Luiz Gustavo
 */
// The stack its a LIFO - Last in first out
public class Stack {
   int stack[] = new int[5];
   int top = 0;
   String whoIAm = "I'm Stack Structure!";

   public void push(final int data)
   {
       stack[top] = data;
       top++;
   }
   public int pop()
   {
       top--;
       int data;
       data = stack[top];
       stack[top] = 0;
       return data;
   }
   public void show()
   {    
       //for(int i = 0;i < stack.length;i++)
       //{
       //    System.out.println( stack[i] + ", ");
       //}
       System.out.println(Arrays.toString(stack));
   }
   
    
}
