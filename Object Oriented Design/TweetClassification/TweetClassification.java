import java.util.*;
import java.io.File;
import java.io.IOException;
import java.io.FileReader;
import java.lang.String;

/**
 * Write a description of class TweetClassification here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class TweetClassification
{
    public static void main(String[] args) throws IOException{
        int wordCount = 0, posCount = 0, negCount = 0;
        int neg = 0, pos = 4, neutral = 2;
        int correctClass = 0, wrongClass = 0, tweetNum = 0;
        double accuracy = 0;
        boolean correct = true;
        
        Scanner kbInput = new Scanner(System.in);
        System.out.println("Provide the file path and extension for the positive word file.");
        
        String fName = kbInput.nextLine();
        File file = new File(fName);
        System.out.println();
        
        while (!file.exists()) {
            System.out.println("Current pathway does not lead to a file.");
            System.out.println("Please check and re-enter the pathway.");
            
            fName = kbInput.nextLine();
            file = new File(fName);
            System.out.println();
        }
        
        Scanner positiveFile = new Scanner(new FileReader(file));
        
        HashSet<String> positive = new HashSet<String>();
        
        while (positiveFile.hasNextLine()) {
            String word = positiveFile.nextLine();
            if (word.length() > 0) {
                if (!word.startsWith(";")) {
                    positive.add(word);
                    wordCount++;
                }
            }
        }
        
        System.out.println("Positive word file has been read.");
        System.out.println("Number of words read: " + wordCount + "\n");
        wordCount = 0;
        
        System.out.println("Provide the file path and extension for the negative word file.");
        
        fName = kbInput.nextLine();
        file = new File(fName);
        System.out.println();
        
        while (!file.exists()) {
            System.out.println("Current pathway does not lead to a file.");
            System.out.println("Please check and re-enter the pathway.");
            
            fName = kbInput.nextLine();
            file = new File(fName);
            System.out.println();
        }
        
        Scanner negativeFile = new Scanner(new FileReader(file));
        
        HashSet<String> negative = new HashSet<String>();
        
        while (negativeFile.hasNextLine()) {
            String word = negativeFile.nextLine();
            if (word.length() > 0) {
                if(!word.startsWith(";")) {
                    negative.add(word);
                    wordCount++;
                }
            }
        }
        
        System.out.println("Negative word file has been read.");
        System.out.println("Number of words read: " + wordCount + "\n");
        wordCount = 0;
        
        System.out.println("Provide the file path and extension for the Twitter file.");
        
        fName = kbInput.nextLine();
        file = new File(fName);
        System.out.println();
        
        while (!file.exists()) {
            System.out.println("Current pathway does not lead to a file.");
            System.out.println("Please check and re-enter the pathway.");
            
            fName = kbInput.nextLine();
            file = new File(fName);
            System.out.println();
        }
        
        Scanner tweetFile = new Scanner(new FileReader(file));
        String line = null;
        ArrayList<Integer> csvClassification = new ArrayList<Integer>();
        ArrayList<Integer> progClassification = new ArrayList<Integer>();
        
        while (tweetFile.hasNextLine()) {
            line = tweetFile.nextLine();
            
            String[] temp = line.split("\",\"");
            
            String tweet = temp[5];
            if (temp.length > 6) {
                for (int i = 6; i < temp.length; i++) {
                    tweet += " " + temp[i];
                }
            }
            
            temp[0] = temp[0].replaceAll("\"", "");
            temp[5] = temp[5].replaceAll("\"", "");
            csvClassification.add(Integer.parseInt(temp[0]));
            
            tweet = tweet.replaceAll("\\p{Punct}","").toLowerCase();
            String[] tweetComp = tweet.split("\\s");
            
            for (int i = 0; i < tweetComp.length; i++) {
                if (positive.contains(tweetComp[i])) 
                    posCount++; 
                else if (negative.contains(tweetComp[i])) 
                    negCount++; 
            }
            
            if (posCount == 0 && negCount == 0)
                progClassification.add(neutral);
            else if (posCount > negCount)
                progClassification.add(pos);
            else if (negCount > posCount)
                progClassification.add(neg);
            else if (negCount == posCount)
                progClassification.add(neg);
                
            posCount = 0;
            negCount = 0;
            
            System.out.println("Tweet: \n" + temp[5]);
            System.out.println("Real label: " + csvClassification.get(tweetNum));
            System.out.println("Predicted label: " + progClassification.get(tweetNum));
            
            if (csvClassification.get(tweetNum).equals(progClassification.get(tweetNum))) {
                correctClass++;
                correct = true;
                System.out.println("Correctly classified: " + correct + "\n");
            }
            else {
                wrongClass++;
                correct = false;
                System.out.println("Correctly classified: " + correct + "\n");
            }
            tweetNum++;
        }
        
        System.out.println("Correctly Classified Tweets: " + correctClass);
        System.out.println("Incorrectly Classified Tweets: " + wrongClass + "\n");
        
        accuracy = ((float)correctClass / tweetNum) * 100;
        if (wrongClass == 0) {
            accuracy = 100.00;
        }
        
        System.out.print("Accuracy: ");
        System.out.printf("%.2f", accuracy);
        System.out.println("%");
    }
}
