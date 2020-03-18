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
        // O valor será adicionado na ultima posição da fila
        queue[rear] = data;
        // espécie de contador que serve para dizer quem será a proxima cauda
        rear = (rear + 1)%5;
        // importante para saber o valor o indice do elemento que foi adicionado/saber se a lista está cheia
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
