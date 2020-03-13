/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exercicicio01aed;

import java.util.Arrays;

/**
 *
 * @author Luiz Gustavo
 */
public class Queue {
    int queue[] = new int[5];
    int size;
    int front;
    int rear;
    String whoIAm = "I'm Queue Structure!";
    
    // function enqueue
    public void enqueue(int data)
    {
        queue[rear] = data;
        // The new rear gonna be the next data thats gonna come
        rear = (rear + 1)%5;
        // Important to when i gonna use the dequeue to remove the first element of queue
        size++;
    }
    
    // funtion dequeue
    public int deQueue()
    {
        int data = queue[front];
        front = (front + 1)%5;
        size--;
        return data;
    }

    // Function thats show the elements in the queue
    public void show ()
    {
         for(int i = 0;i<size;i++)
        {
            System.out.println(queue[(front+i)%5] + " ");
        }
    }
}
