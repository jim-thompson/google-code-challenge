package com.google.challenges;

import java.util.Arrays;
import java.util.Comparator;

public class Answer {

  // This challenge has a fairly straightforward solution using Java's
  // sort capabilities. So we don't have to design the sort algorithm, we just
  // have to define a function that compares two strings using the criteria
  // given in the challenge.

  public static String[] answer(String[] names) {
    // Your code goes here.
    Arrays.sort(names, bunnyNameComparator);

    return names;
  }

  static Comparator<String> bunnyNameComparator = new Comparator<String>() {
    public int compare(String s1, String s2) {

      // Compare two strings given in s1 and s2. Although the challenge
      // description said that the characters would all be lower case, let's
      // make sure. (This allows testing of the values given in the
      // description as "Annie", "Earz", "AL", and "CJ".
      s1 = s1.toLowerCase();
      s2 = s2.toLowerCase();

      // Get the value of each string according to the professor's way of
      // scoring.
      int value1 = stringVal(s1);
      int value2 = stringVal(s2);

      // Compute the comparison value of the two strings.
      int compareValue = value2 - value1;

      // If the two strings are equal, resort to a lexical comparison. The
      // String.compareTo function is such a comparison.
      if (compareValue == 0) {
        compareValue = s2.compareTo(s1);
      }

      // Return the comparison value.
      return compareValue;
    }

    int stringVal(String s) {
      // Compute the 'value' of a string by adding up the values of its
      // constituent characters - A = 1, B = 2, C = 3, ..., Z = 26, etc.

      // Wanted to use
      // StringCharacterIterator iter = new StringCharacterIterator(s);
      // This didn't work - the verify function wouldn't allow the use of
      // StringCharacterIterator, claiming it was a "restricted class".

      int value = 0;

      // Loop over every character in the string.
      for (int index = 0; index < s.length(); index++)
        {
          char c = s.charAt(index);

          // Get the character's value relative to 'a'. Adding one isn't
          // strictly necessary - the comparisons will be the same either way
          // - but this lets us compare the values of strings to values given
          // in the challenge text.
          int i = c - 'a' + 1;
          value += i;
        }

      // Return the sum of the character values
      return value;
    }
  };

  public static void main(String[] args) {

    String[] input0 = { "Annie", "Earz", "AL", "CJ" };
    String[] input1 = { "a", "ab", "abc" };
    String[] input2 = { "annie", "bonnie", "liz" };
    String[] input3 = { "abcdefg", "vi" };

    testRun(input0);
    testRun(input1);
    testRun(input2);
    testRun(input3);
  }

  static void testRun(String[] strings) {
    System.out.println();
    printStrings(strings, "input");
    Arrays.sort(strings, bunnyNameComparator);
    printStrings(strings, "output");
  }

  static void printStrings(String[] strings, String label) {
    System.out.println(label + ":");
    System.out.print("    (string list) [\"" + strings[0]);
    for (int i = 1; i < strings.length; i++) System.out.print("\", \"" + strings[i]);
    System.out.println("\"]");
  }
}