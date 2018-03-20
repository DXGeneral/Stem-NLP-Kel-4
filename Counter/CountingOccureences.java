import java.util.*;
import java.util.stream.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class CountingOccureences {
  public static void main(String[] args) {
    
	// Grab test input file:
	String testInput = "", fileName = args[0];
	BufferedReader br = null;
	try {
		String currentLine;
		br = new BufferedReader(new FileReader(fileName));
		while ((currentLine = br.readLine()) != null)
			testInput += " " + currentLine;
		br.close();
	} catch (IOException e) {
		e.printStackTrace();
	}
	
	String clearString = testInput.replaceAll("\\p{P}", " ").toLowerCase();
	
    // String example = "The quick brown fox jumps over the lazy dog, the dog catches the fox";
    
    // System.out.println(countOccurences(example.replaceAll("\\s", ""), "")); 
    // output: {a=3, b=1, c=3, d=3, e=6, f=2, g=2, h=5, i=1, j=1, k=1, l=1, m=1, n=2, o=6, p=1, q=1, r=2, s=2, t=5, u=2, v=1, w=1, x=2, y=1, z=1}
    // System.out.println(countOccurences(example, " "));
    // output: {over=1, the=4, quick=1, and=1, lazy=1, catches=1, jumps=1, brown=1, dog=2, fox=2}
	
	System.out.println(countOccurences(clearString, " "));

  }
  
  public static Map<String, Long> countOccurences(String s, String delim){
    return Arrays.stream(s.split(delim))
                 .collect(Collectors.groupingBy(String::toLowerCase, Collectors.counting()));
  }

}