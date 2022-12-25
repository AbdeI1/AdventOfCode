import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Day7Code {

    static String[] input;

    public static int part1(){
        int count = 0;
        for(String s : input){
            if(containsGold(lineOf(s.substring(0, s.indexOf("bags") - 1)))){
                count++;
            }
        }
        return count - 1;
    }

    public static int part2(){
        return numberContained("shiny gold");
    }

    public static int numberContained(String color){
        String line = input[lineOf(color)];
        String[] colors = colorsContained(color);
        int count = 0;
        for(String s : colors){
            int num = Character.getNumericValue(line.charAt(line.indexOf(s) - 2));
            count += num;
            count += num * numberContained(s);
        }
        return count;
    }

    public static boolean containsGold(int lineNumber){
        String line = input[lineNumber];
        if(line.indexOf("shiny gold") > -1){
            return true;
        } else if (line.indexOf("no other bags") > - 1){
            return false;
        } else {
            String[] colors = colorsContained(line.substring(0, line.indexOf("bags") - 1));
            boolean result = false;
            for(String color : colors){
                result = result || containsGold(lineOf(color));
            }
            return result;
        }
    }

    public static String[] colorsContained(String color){
        String line = input[lineOf(color)];
        String colors = line.substring(line.indexOf("contain") + 8);
        int count = 0;
        if(line.indexOf("no other bags") == -1){
            count++;
            while(line.indexOf(",") > -1){
                count++;
                line = line.substring(line.indexOf(",") + 1);
            }
        }
        String[] result = new String[count];
        for(int i = 0; i < result.length; i++){
            result[i] = colors.substring(colors.indexOf(" ") + 1, colors.indexOf("bag") - 1);
            if(i != result.length - 1) {
                colors = colors.substring(colors.indexOf("bag") + 6);
            }
        }
        return result;
    }

    public static int lineOf(String color){
        for(int i = 0; i < input.length; i++){
            String line = input[i];
            String lineColor = line.substring(0, line.indexOf("bags") - 1);
            if(color.equals(lineColor)){
                return i;
            }
        }
        throw new IllegalArgumentException("color not in list");
    }

    public static void main(String args[]){
        File inputText = new File("C:\\Users\\bluey\\Documents\\Coding Projects\\AdventOfCode\\Day 7\\Day7input.txt");
        input = reader(inputText, 594);
        String line = input[1];
        System.out.println(part2());
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
