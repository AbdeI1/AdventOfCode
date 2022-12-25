import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day3Code{

    public static void main (String args[]){
        File inputText = new File("C:\\Users\\bluey\\Documents\\Coding Projects\\AdventOfCode\\Day 3\\Day3input.txt");
        String[] input = reader(inputText, 323);
        System.out.println(part2(input, 5, 1));
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

    public static int part1(String[] input){
        int trees = 0;
        int rightPos = 0;
        for(String s : input){
            if(s.charAt(rightPos) == '#'){
                trees++;
            }
            rightPos = (rightPos + 3)%s.length();
        }
        return trees;
    }

    public static int part2(String[] input, int slopeX, int slopeY){
        int trees = 0;
        int rightPos = 0;
        for(int i = 0; i < input.length; i+=slopeY){
            if(input[i].charAt(rightPos) == '#'){
                trees++;
            }
            rightPos = (rightPos + slopeX)%input[i].length();
        }
        return trees;
    }

}