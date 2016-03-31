package com.google.challenges;

import java.util.Arrays;
import java.util.Comparator;

public class Answer {

  public static int[] answer(int[][] minions) {

    // Your code goes here.
    convertMinions(minions);
    Arrays.sort(minions, minionComparator);

    int[] answer = new int[minions.length];
    for (int i = 0; i < answer.length; i++) {
      answer[i] = minions[i][1];
    }

    return answer;
  }

  // Comparing minions is as simple as subtracting the expected ktimes.
  static Comparator<int[]> minionComparator = new Comparator<int[]>() {
    public int compare(int[] a1, int[] a2) {
      return a1[0] - a2[0];
    }
  };

  static void convertMinions(int[][] minions) {
    // Convert each minion specification in place (keeping us from having to
    // gen up a new class/structure mixing doubles and ints).
    // Each converted minion has a "ktime" value, which is 1000 times the
    // expected time divided by the probability of a correct password answer.
    // Ktime is stored in the 0th position in each minion array. Index is
    // stored in the 1st position in each minion array.
    int index = 0;
    for (int[] minion : minions) {
      minion[0] = (1000 * minion[0] * minion[2]) / minion[1];
      minion[1] = index;
      index += 1;
    }
  }

  static void printMinions(int[][] minions, String label) {

    System.out.println(label);

    for (int[] minion : minions) {
      System.out.println("time: " + minion[0] + ", num: " + minion[1] + ", den: " + minion[2]);
    }
  }

  static void printAnswer(int[] ints, String label) {
    System.out.println(label + ":");
    System.out.print("    (int list) [\"" + ints[0]);
    for (int i = 1; i < ints.length; i++) System.out.print("\", \"" + ints[i]);
    System.out.println("\"]");
  }

  public static void main(String[] args) {
    int[][] testset0 = {{ 5, 1, 5 }, {10, 1, 2 }};
    printMinions(testset0, "test set 0");
    int[] answer0 = answer(testset0);
    printAnswer(answer0, "answer 0");

    int[][] testset1 = {{ 390, 185, 624 },
			{ 686, 351, 947 },
			{ 276, 1023, 1024 },
			{ 199, 148, 250 }};
    printMinions(testset1, "test set 1");
    int[] answer1 = answer(testset1);
    printAnswer(answer1, "answer 1");
 }
}