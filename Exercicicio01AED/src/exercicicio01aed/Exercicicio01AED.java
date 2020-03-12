/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exercicicio01aed;
import java.util.*;
import exercicicio01aed.Stack;
import exercicicio01aed.Queue;
import exercicicio01aed.LinkedList;
public class Exercicicio01AED {
   
    public static void main(final String[] args) {
        // Stack Struture
        Stack s = new Stack();
        s.push(1);
        s.push(2);
        s.push(3);
        s.show();
        System.out.println(s.pop()+" Valor retirado");
        s.show();
        // Queue Struture
        Queue q = new Queue();
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        q.enqueue(4);
        q.enqueue(5);
        
        q.deQueue();
        q.deQueue();
        
        q.enqueue(1);
        q.enqueue(1);
        
        q.deQueue();
        q.show();

        // LinkedList Struture
        final LinkedList l = new LinkedList();
        System.out.println("including elements using the insert function: ");
        l.insert(5);
        l.insert(2);
        System.out.println("including elements using the insertAt function: ");
        l.insertAt(1, 10);
        System.out.println("Deleting elements using the delete function: ");
        l.deleteAt(1);
        System.out.println("Showing elements using the show function: ");
        l.show();
        
    }
    
}
