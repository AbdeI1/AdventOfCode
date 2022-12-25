import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Day12{

    static String[] input;
    static char[] directions = {'N', 'E', 'S', 'W'};

    public static void part1(){
        int NS = 0;
        int EW = 0;
        int direction = 1;
        for(String s : input){
            char code = s.charAt(0);
            int num = Integer.parseInt(s.substring(1));
            switch(code){
                case 'N':
                    NS += num;
                    break;
                case 'E':
                    EW += num;
                    break;
                case 'S':
                    NS -= num;
                    break;
                case 'W':
                    EW -= num;
                    break;
                case 'R':
                    int turn = num/90;
                    direction = (direction + turn)%4;
                    break;
                case 'L':
                    int turn2 = 4 - (num/90);
                    direction = Math.abs((direction + turn2)%4);
                    break;
                case 'F':
                    switch(directions[direction]){
                        case 'N':
                            NS += num;
                            break;
                        case 'E':
                            EW += num;
                            break;
                        case 'S':
                            NS -= num;
                            break;
                        case 'W':
                            EW -= num;
                            break;
                        default:
                            break;
                    }
                    break;
                default:
                    break;
            }
        }
        System.out.println(Math.abs(NS) + Math.abs(EW));
    }

    public static void part2(){
        int NS = 0;
        int EW = 0;
        int[] waypoint = {1, 10};
        for(String s : input){
            char code = s.charAt(0);
            int num = Integer.parseInt(s.substring(1));
            switch(code){
                case 'N':
                    waypoint[0] += num;
                    break;
                case 'E':
                    waypoint[1] += num;
                    break;
                case 'S':
                    waypoint[0] -= num;
                    break;
                case 'W':
                    waypoint[1] -= num;
                    break;
                case 'R':
                    int turn = (num/90)%4;
                    switch(turn){
                        case 0:
                            break;
                        case 1:
                            int temp = waypoint[0];
                            waypoint[0] = -waypoint[1];
                            waypoint[1] = temp;
                            break;
                        case 2:
                            waypoint[0] = -waypoint[0];
                            waypoint[1] = -waypoint[1];
                            break;
                        case 3:
                            int temp2 = waypoint[0];
                            waypoint[0] = waypoint[1];
                            waypoint[1] = -temp2;
                            break;
                        default:
                            break;
                    }
                    break;
                case 'L':
                    int turn2 = (num/90)%4;
                    switch(turn2){
                        case 0:
                            break;
                        case 1:
                            int temp2 = waypoint[0];
                            waypoint[0] = waypoint[1];
                            waypoint[1] = -temp2;
                            break;
                        case 2:
                            waypoint[0] = -waypoint[0];
                            waypoint[1] = -waypoint[1];
                            break;
                        case 3:
                            int temp = waypoint[0];
                            waypoint[0] = -waypoint[1];
                            waypoint[1] = temp;
                            break;
                        default:
                            break;
                    }
                    break;
                case 'F':
                    NS += num * waypoint[0];
                    EW += num * waypoint[1];
                    break;
                default:
                    break;
            }
        }
        System.out.println(Math.abs(NS) + Math.abs(EW));
    }

    public static void main(String args[]){
        File inputText = new File("C:\\Users\\bluey\\Documents\\Coding Projects\\AdventOfCode\\Day 12\\Day12input.txt");
        input = reader(inputText, 788);
        part2();
    }

    public static String[] reader(File input, int lines){
        String[] result = new String[lines];
        try {
            Scanner reader = new Scanner(input);
            for (int i = 0; i < result.length; i++){
                result[i] = reader.nextLine();
            }
        } catch (FileNotFoundException x){
            System.out.println("File not found");
        }
        return result;
    }

}