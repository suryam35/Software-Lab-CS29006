/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication1;

/**
 *
 * @author Suryam Arnav Kalra - 19CS30050 - Assignment 0
 */
import java.util.*;
import java.text.*;

public class JavaApplication1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        ArrayList<Individual> individual = new ArrayList<>();
        ArrayList<Group> group = new ArrayList<>();
        ArrayList<Business> business = new ArrayList<>();
        ArrayList<Organisation> organisation = new ArrayList<>();
        Scanner obj = new Scanner(System.in);
        while(true) {
            System.out.println("************* Menu options ************");
            System.out.println("0. Show all nodes");
            System.out.println("1. Create a node");
            System.out.println("2. Delete a node");
            System.out.println("3. Search by name or type or birthday");
            System.out.println("4. Create and post content by a user");
            System.out.println("5. Print all nodes linked to a given node");
            System.out.println("6. Search for content by a user");
            System.out.println("7. Display all content posted by nodes linked to a given node");
            System.out.println("8. Exit the menu");
            System.out.println("**************************************");
            System.out.print("Enter a number from 0 to 8 : ");
            int x = obj.nextInt();
            obj.nextLine();
            if(x == 8) {
                break;
            }
            if(x == 0) {
                //print all nodes
                printall(individual , group , business , organisation);
            }
            if(x == 1) {
                System.out.print("Enter the type of node to create(individual/group/business/organisation) : ");
                String sc = obj.nextLine();
                if(sc.equals("individual")) {
                    individual.add(new Individual(obj));
                }
                if(sc.equals("group")) {
                    Group g = new Group(obj);
                    //check for links
                    System.out.print("How many links : ");
                    int num = obj.nextInt();
                    obj.nextLine();
                    for(int i = 0 ; i < num ; i++) {
                        System.out.print("Enter the id of business/indvidual you want to link : ");
                        int id = obj.nextInt() , index = -1;
                        obj.nextLine();
                        for(int j = 0 ; j < individual.size() ; j++) {
                            if(individual.get(j).id == id) {
                                index = j;
                                break;
                            }
                        }
                        if(index != -1) {
                            g.ind.add(individual.get(index));
                            continue;
                        }
                        for(int j = 0 ; j < business.size() ; j++) {
                            if(business.get(j).id == id) {
                                index = j;
                                break;
                            }
                        }
                        if(index != -1) {
                            g.bu.add(business.get(index));
                            continue;
                        }
                        if(index == -1) {
                            System.out.println("No user of this id found");
                        }
                    }
                    group.add(g);
                }
                if(sc.equals("business")) {
                    Business b = new Business(obj);
                    //check for links;
                    System.out.print("How many links : ");
                    int num = obj.nextInt();
                    obj.nextLine();
                    for(int i = 0 ; i < num ; i++) {
                        System.out.print("Enter the id of indvidual you want to link : ");
                        int id = obj.nextInt() , index = -1;
                        obj.nextLine();
                        for(int j = 0 ; j < individual.size() ; j++) {
                            if(individual.get(j).id == id) {
                                index = j;
                                break;
                            }
                        }
                        if(index != -1) {
                            b.ind.add(individual.get(index));
                        }
                        else {
                            System.out.println("No user of this id found");
                        }
                    }
                    business.add(b);
                }
                if(sc.equals("organisation")) {
                    Organisation org = new Organisation(obj);
                    //check for links
                    System.out.print("How many links : ");
                    int num = obj.nextInt();
                    obj.nextLine();
                    for(int i = 0 ; i < num ; i++) {
                        System.out.print("Enter the id of indvidual you want to link : ");
                        int id = obj.nextInt() , index = -1;
                        obj.nextLine();
                        for(int j = 0 ; j < individual.size() ; j++) {
                            if(individual.get(j).id == id) {
                                index = j;
                                break;
                            }
                        }
                        if(index != -1) {
                            org.ind.add(individual.get(index));
                        }
                        else {
                            System.out.println("No user of this id found");
                        }
                    }
                    organisation.add(org);
                }
            }
            if(x == 2) {
                System.out.print("Enter the id of the node to be deleted : ");
                int id = obj.nextInt() , index = -1;
                obj.nextLine();
                //delete a node
                for(int i = 0 ; i < individual.size() ; i++) {
                    if(individual.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    int index2 = -1;
                    individual.remove(index);
                    for(Business b : business) {
                        for(int j = 0 ; j < b.ind.size() ; j++) {
                             if(b.ind.get(j).id == id) {
                                 index2 = j;
                                 break;
                             }
                        }
                        if(index2 != -1) {
                            b.ind.remove(index2);
                            break;
                        }
                    }
                    index2 = -1;
                    for(Group b : group) {
                        for(int j = 0 ; j < b.ind.size() ; j++) {
                             if(b.ind.get(j).id == id) {
                                 index2 = j;
                                 break;
                             }
                        }
                        if(index2 != -1) {
                            b.ind.remove(index2);
                            break;
                        }
                    }
                    index2 = -1;
                    for(Organisation b : organisation) {
                        for(int j = 0 ; j < b.ind.size() ; j++) {
                             if(b.ind.get(j).id == id) {
                                 index2 = j;
                                 break;
                             }
                        }
                        if(index2 != -1) {
                            b.ind.remove(index2);
                            break;
                        }
                    }
                    continue;
                }
                for(int i = 0 ; i < group.size() ; i++) {
                    if(group.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    group.remove(index);
                    continue;
                }
                for(int i = 0 ; i < business.size() ; i++) {
                    if(business.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    int index2 = -1;
                    business.remove(index);
                    for(Group g : group) {
                        for(int j = 0 ; j < g.bu.size() ; j++) {
                            if(g.bu.get(j).id == id) {
                                index2 = j;
                                break;
                            }
                        }
                        if(index2 != -1) {
                            g.bu.remove(index2);
                            break;
                        }
                    }
                    continue;
                }
                for(int i = 0 ; i < organisation.size() ; i++) {
                    if(organisation.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    organisation.remove(index);
                    continue;
                }
                if(index == -1) {
                    System.out.println("No user found");
                }
            }
            if(x == 3) {
                System.out.println("1. Search by name");
                System.out.println("2. Search by type");
                System.out.println("3. Search by birthday");
                String sc = obj.nextLine();
                if(sc.equals("1")) {
                    System.out.println("Enter the name : ");
                    sc = obj.nextLine();
                    SearchbyName(sc , individual , group , business , organisation);
                }
                if(sc.equals("2")) {
                    System.out.println("Enter the type : ");
                    sc = obj.nextLine();
                    SearchbyType(sc , individual , group , business , organisation);
                }
                if(sc.equals("3")) {
                    System.out.println("Enter the birthday : ");
                    sc = obj.nextLine();
                    SearchbyBirthday(sc , individual);
                }
            }
            if(x == 4) {
                System.out.print("Enter the id of the user : ");
                int id = obj.nextInt() , index = -1;
                obj.nextLine();
                for(int i = 0 ; i < individual.size() ; i++) {
                    if(individual.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    int flag = 1;
                    System.out.print("Enter the content to be posted : ");
                    String sc = obj.nextLine();
                    for(String s : individual.get(index).content) {
                        if(s.equals(sc)) {
                            flag = 0;
                            break;
                        }
                    }
                    if(flag == 1) {
                        individual.get(index).content.add(sc);
                    }
                    continue;
                }
                for(int i = 0 ; i < group.size() ; i++) {
                    if(group.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    int flag = 1;
                    System.out.print("Enter the content to be posted : ");
                    String sc = obj.nextLine();
                    for(String s : group.get(index).content) {
                        if(s.equals(sc)) {
                            flag = 0;
                            break;
                        }
                    }
                    if(flag == 1) {
                        group.get(index).content.add(sc);
                    }
                    continue;
                }
                for(int i = 0 ; i < business.size() ; i++) {
                    if(business.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    int flag = 1;
                    System.out.print("Enter the content to be posted : ");
                    String sc = obj.nextLine();
                    for(String s : business.get(index).content) {
                        if(s.equals(sc)) {
                            flag = 0;
                            break;
                        }
                    }
                    if(flag == 1) {
                        business.get(index).content.add(sc);
                    }
                    continue;
                }
                for(int i = 0 ; i < organisation.size() ; i++) {
                    if(organisation.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    int flag = 1;
                    System.out.print("Enter the content to be posted : ");
                    String sc = obj.nextLine();
                    for(String s : organisation.get(index).content) {
                        if(s.equals(sc)) {
                            flag = 0;
                            break;
                        }
                    }
                    if(flag == 1) {
                        organisation.get(index).content.add(sc);
                    }
                    continue;
                }
                if(index == -1) {
                    System.out.println("No user found");
                }
            }
            if(x == 5) {
                System.out.print("Enter the id of the node : ");
                int id = obj.nextInt() , index = -1;
                obj.nextLine();
                //print all linked nodes to this id
                for(int i = 0 ; i < individual.size() ; i++) {
                    if(individual.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("No nodes linked to this individual");
                    continue;
                }
                for(int i = 0 ; i < group.size() ; i++) {
                    if(group.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("The businesses linked to this group id are : ");
                    for(Business b : group.get(index).bu) {
                        b.printobj();
                    }
                    System.out.println("The individuals linked to this group id are : ");
                    for(Individual u : group.get(index).ind) {
                        u.printobj();
                    }
                    continue;
                }
                for(int i = 0 ; i < business.size() ; i++) {
                    if(business.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("The individuals linked to this group id are : ");
                    for(Individual u : business.get(index).ind) {
                        u.printobj();
                    }
                    continue;
                }
                for(int i = 0 ; i < organisation.size() ; i++) {
                    if(organisation.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("The individuals linked to this group id are : ");
                    for(Individual u : organisation.get(index).ind) {
                        u.printobj();
                    }
                    continue;
                }
                if(index == -1) {
                    System.out.println("No user found");
                }
            }
            if(x == 6) {
                System.out.print("Enter the id of the node : ");
                int id = obj.nextInt() , index = -1;
                obj.nextLine();
                //print the content of this user
                for(int i = 0 ; i < individual.size() ; i++) {
                    if(individual.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("The content of this user are : ");
                    for(String s : individual.get(index).content) {
                        System.out.println(s);
                    }
                    continue;
                }
                for(int i = 0 ; i < group.size() ; i++) {
                    if(group.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("The content of this user are : ");
                    for(String s : group.get(index).content) {
                        System.out.println(s);
                    }
                    continue;
                }
                for(int i = 0 ; i < business.size() ; i++) {
                    if(business.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("The content of this user are : ");
                    for(String s : business.get(index).content) {
                        System.out.println(s);
                    }
                    continue;
                }
                for(int i = 0 ; i < organisation.size() ; i++) {
                    if(organisation.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("The content of this user are : ");
                    for(String s : organisation.get(index).content) {
                        System.out.println(s);
                    }
                    continue;
                }
                if(index == -1) {
                    System.out.println("No user found");
                }
            }
            if(x == 7) {
                System.out.print("Enter the id of the node : ");
                int id = obj.nextInt() , index = -1;
                obj.nextLine();
                //all content of nodes linked to this node , print it
                for(int i = 0 ; i < individual.size() ; i++) {
                    if(individual.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("No nodes linked to this individual");
                    continue;
                }
                for(int i = 0 ; i < group.size() ; i++) {
                    if(group.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("The content of businesses linked to this group id are : ");
                    for(Business b : group.get(index).bu) {
                        for(String s : b.content) {
                            System.out.println(s);
                        }
                    }
                    System.out.println("The content of individuals linked to this group id are : ");
                    for(Individual u : group.get(index).ind) {
                        for(String s : u.content) {
                            System.out.println(s);
                        }
                    }
                    continue;
                }
                for(int i = 0 ; i < business.size() ; i++) {
                    if(business.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("The content of individuals linked to this group id are : ");
                    for(Individual u : business.get(index).ind) {
                        for(String s : u.content) {
                            System.out.println(s);
                        }
                    }
                    continue;
                }
                for(int i = 0 ; i < organisation.size() ; i++) {
                    if(organisation.get(i).id == id) {
                        index = i;
                        break;
                    }
                }
                if(index != -1) {
                    System.out.println("The content of individuals linked to this group id are : ");
                    for(Individual u : organisation.get(index).ind) {
                        for(String s : u.content) {
                            System.out.println(s);
                        }
                    }
                    continue;
                }
                if(index == -1) {
                    System.out.println("No user found");
                }
            }
            if(x > 8 || x < 0) {
                System.out.println("Invalid number entered");
            }
        }
    }
    
    static void printall(ArrayList<Individual> i , ArrayList<Group> g , ArrayList<Business> b , ArrayList<Organisation> org) {
        for(Individual ind : i) {
            ind.printobj();
        }
        for(Group gr : g) {
            gr.printobj();
        }
        for(Business bu : b) {
            bu.printobj();
        }
        for(Organisation organ : org) {
            organ.printobj();
        }
    }
    
    static void SearchbyName(String name , ArrayList<Individual> i , ArrayList<Group> g , ArrayList<Business> b , ArrayList<Organisation> org) {
        int flag = 1;
        for(Individual ind : i) {
            if(ind.name.equals(name)) {
                ind.printobj();
                flag = 0;
            }
        }
        for(Group gr : g) {
            if(gr.name.equals(name)) {
                gr.printobj();
                flag = 0;
            }
        }
        for(Business bu : b) {
            if(bu.name.equals(name)) {
                bu.printobj();
                flag = 0;
            }
        }
        for(Organisation organ : org) {
            if(organ.name.equals(name)) {
                organ.printobj();
                flag = 0;
            }
        }
        if(flag == 1) {
            System.out.println("No user found");
        }
    }
    
    static void SearchbyType(String type , ArrayList<Individual> i , ArrayList<Group> g , ArrayList<Business> b , ArrayList<Organisation> org) {
        int flag = 1;
        if(type.equals("individual")) {
            for(Individual ind : i) {
                ind.printobj();
                flag = 0;
            }
        }
        else if(type.equals("group")) {
            for(Group gr : g) {
                gr.printobj();
                flag = 0;
            }
        }
        else if(type.equals("business")) {
            for(Business bu : b) {
                bu.printobj();
                flag = 0;
            }
        }
        else if(type.equals("organisation")) {
            for(Organisation or : org) {
                or.printobj();
                flag = 0;
            }
        }
        if(flag == 1) {
            System.out.println("No user found");
        }
    }
    
    static void SearchbyBirthday(String birth , ArrayList<Individual> i) {
        int flag = 1;
        for(Individual ind : i) {
            if(ind.birthday.equals(birth)) {
                ind.printobj();
                flag = 0;
            }
        }
        if(flag == 1) {
            System.out.println("No user found");
        }
    }
}

class Node {
    int id;
    String name;
    String date;
    ArrayList<String> content;
    public Node(Scanner obj) {
        System.out.print("Enter the id : ");
        this.id = obj.nextInt();
        obj.nextLine();
        System.out.print("Enter the name : ");
        this.name = obj.nextLine();
        System.out.print("Enter the creation date : ");
        this.date = obj.nextLine();
        this.content = new ArrayList<>();
    }
    
    void printobj() {
        System.out.println("Id : " +id);
        System.out.println("Name : " + name);
        System.out.println("Date : " + date);
        System.out.println("Content : ");
        for(int i = 0 ; i < content.size() ; i++) {
            System.out.println(content.get(i));
        }
    }
}

class Individual extends Node {
    String birthday;
    public Individual(Scanner obj) {
        super(obj);
        System.out.print("Enter the birthday : ");
        this.birthday = obj.nextLine();
    }
    void printobj() {
        super.printobj();
        System.out.println("Birthday : "+birthday);
    }
}

class Group extends Node {
    ArrayList<Individual> ind;
    ArrayList<Business> bu;
    public Group(Scanner obj) {
        super(obj);
        this.ind = new ArrayList<>();
        this.bu = new ArrayList<>();
    }
    void printobj() {
        super.printobj();
    }
}

class Business extends Node {
    int x , y;
    ArrayList<Individual> ind;
    public Business(Scanner obj) {
        super(obj);
        System.out.print("Enter the x -coordinate : ");
        this.x = obj.nextInt();
        System.out.print("Enter the y -coordinate : ");
        this.y = obj.nextInt();
        this.ind = new ArrayList<>();
    }
    void printobj() {
        super.printobj();
        System.out.println("Coordinates : (" + x + "," + y + ")");
    }
}

class Organisation extends Node {
    int x , y;
    ArrayList<Individual> ind;
    public Organisation(Scanner obj) {
        super(obj);
        System.out.print("Enter the x -coordinate : ");
        this.x = obj.nextInt();
        System.out.print("Enter the y -coordinate : ");
        this.y = obj.nextInt();
        this.ind = new ArrayList<>();
    }
    void printobj() {
        super.printobj();
        System.out.println("Coordinates : (" + x + "," + y + ")");
    }
}