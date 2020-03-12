/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exercicicio01aed;

/**
 *
 * @author Luiz Gustavo
 */
public class LinkedList {
    Node head; // the default value its null
    
    // insert to the end function
    public void insert(int data)
    {
        Node node = new Node();
        node.data = data;
        node.next = null;
        // testing if i have or no a head
        if(head==null)
        {
            head = node;
        }
        else 
        {
            Node n = head;
            // to travel into the list
            while(n.next!=null)
            {
                // gonna testing until i come the the last value thats gonna have the next as null
                n = n.next;
            }
            n.next = node; // gonna receive the data iqual to the data in the function and the next as null
        }
    }
    
    // insert to the start function
    public void insertAtStart(int data)
    {
        Node node = new Node();
        node.data = data;
        node.next = null;
        node.next = head; // the new node gonna to point to the older head
        head = node; // at the same time thats he's become the new head
    }
    
    //insert in some place by a index function
    public void insertAt(int index, int data)
    {
        // defining values to the node 
        Node node = new Node();
        node.data = data;
        node.next = null;
        
        if(index==0)
        {
            insertAtStart(data);
        } 
        else
        {
        // variable to travell
        Node n = head;
        // travelling
        for(int i = 0;i<index-1;i++)
        {
            // the 
            n = n.next;
        }        
        node.next = n.next; // pick up the old n.next that were in the head
        n.next = node; //The head gonna pickup the next new value
     }
    }
    
    // Show function
    public void show()
    {
        Node node = head;
        while(node.next!=null)
        {
            System.out.println(node.data);
            node = node.next;
        }
        // i use this cuz i'm travell until i getting null in the next, so i dont print the data of the next value
        System.out.println(node.data);
    }
    
    // function to delete
    public void deleteAt(int index)
    {
        if(index == 0)
        {
            head = head.next;
        } 
        else {
            Node n = head;
            Node n1 = null;
            for(int i=0;i<index-1;i++)
            {
                n = n.next;
            }
            n1 = n.next;
            n.next = n1.next;
            System.out.println("n1 " + n1.data);
            
        }
    }
        
}
