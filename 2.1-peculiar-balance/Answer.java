package com.google.challenges;

import java.lang.Math;

public class Answer {

  // This class provides the solution to the second Google code challenge.
  // The key to this solution is the fact that a base-3 representation of the
  // given value can be modified in a way that lets us read the solution
  // directly from the modified representation.
  //
  // The base-3 representation divides the input value up into "digits", dig[n],
  // where each digit's value is dig[n] * (3**n) for nonzero dig[n]. The sum
  // of these values for nonzero dig[n] is equal to the input value.
  //
  // These values could be directly translated into weights to be added to the
  // right hand of the scale, except that we are only given one set of weights
  // corresponding to the powers of 3. However, we are able to place weights
  // into the LEFT side of the scale. These would correspond to negative
  // digits in the base-3 representation.
  //
  // Digit values are changed as follows: 0 or 1 are left unmodified. Digit
  // values of 2 (for example, the value 6 is represented in base 3 as 20),
  // are modified as follows: for digit n with value 2, add 1 to the digit
  // corresponding to the next greater power of 3: dig[n + 1], and subtract 3
  // from the digit dig[n]. In the language of the challenge, this would be
  // putting a weight of 3**n in the right-hand pan while putting a weight of
  // 3**(n+1) in the left-hand pan: the two cancel out to form a net value of
  // 2*3**n.
  //
  // Once the values are transformed, they're mapped into the values required
  // for the challenge solution as follows:
  //     0 ==> "-" Weight not used
  //     1 ==> "R" Weight placed on right-hand of scale
  //     -1 ==> "L" Weight placed on left-hand of scale
  //
  // Author: Jim Thompson, jtoftx@gmail.com or jim.thompson@pobox.com

  public static String[] answer(int x) { 
      // Your code goes here.
      String[] answerStrings = solve(x);
      return answerStrings;
    }

  static String[] solve(int leftHandWeight) {
    // Figure out how many weight placements we need to account for.
    double lhwlog3 = log3(leftHandWeight);
    int ceil = ((int) Math.floor(lhwlog3)) + 1;

    // New get the digits in the Base-3 representation of the value passed in.
    int[] digits = getDigits(leftHandWeight, ceil);

    // Next we redstribute the digits so that instead of each digit being 0,
    // 1, or 2, each digit is now -1, 0, or 1. This can be done simply and in
    // a way that ensures that the valueToBeDecomposed is preserved.
    int[] reDistDigits = reDistribute(digits);

    // Finally, map the digit values to strings. We interpret the digits as
    // follows: -1 indicates that the corresponding weight should be placed on
    // the left side of the balance, 1 indicates that the corresponding weight
    // should be placed on the right side of the balance, and 0 indicates that
    // the corresponding weight is unused.
    String[] answerString = reMap(reDistDigits);

    // One last thing we have to do. This algorithm sometimes leaves "-"
    // (weight not used) in the higher valued weights. The challenge notes
    // explicitly forbid this, so we have to find and return the useful
    // (legal) part of the array of strings.
    answerString = normalize(answerString);

    return answerString;
  }

  static String[] normalize(String[] answerString) {
    // Chop of any "-" not-used values from the heavy end of the arary.

    int i;

    // Loop through the array looking for strings indicating the weight is unused.
    for (i = answerString.length - 1; i >= 0; i--) {
      if (answerString[i] != "-") break;
    }

    // If we skipped any part of the array, copy the remainder into a new
    // array.
    if (i != answerString.length) {
      String[] newAnswers = new String[i + 1];
      for (; i >= 0; i--)
	newAnswers[i] = answerString[i];

      answerString = newAnswers;
    }

    // Return the copied array.
    return answerString;
  }

  static String[] reMap(int[] digits) {

    // Loop through the array mapping digits to strings. This is a simple
    // transformation.
    String[] weightPlacements = new String[digits.length];

    for (int i = 0; i < digits.length; i++) {
      switch (digits[i]) {
      case 0: weightPlacements[i] = "-"; break;	    // Not used
      case 1: weightPlacements[i] = "R"; break;	    // Right-hand side
      case -1: weightPlacements[i] = "L"; break;    // Left-hand side
      default: weightPlacements[i] = "X"; break;    // Illegal value, but this
						    // should never happen.
      }
    }

    // Return the re-mapped array.
    return weightPlacements;
  }

  static int[] reDistribute(int[] digits) {

    // Loop through the digits in the base-3 representation of the input
    // value, to map values of 2 into 1 and -1.
    for (int i = 0; i < (digits.length - 1); i++) {

      // It's only the digit 2 that we have to handle. The explanation for
      // this is given in the header comments, but basically: 2 weights in the
      // right-hand side of the scale is the same as the next-higher weight
      // in the right-hand side of the scale, and one weight in the left-hand
      // side of the scale.
      if (digits[i] >= 2) {
	digits[i] -= 3;
	digits[i + 1] += 1;
      }
    }

    return digits;
  }

  static int[] getDigits(int valueToBeDecomposed, int power) {

    // Decompose i into multiples of powers of 3 beginning with the p-th power
    // of 3. The decompisition starts at the p-th power of 3 and works
    // downward through smaller values of p. This corresponds to finding the
    // base 3 representation of the value.

    //Note that this algorithm will NOT work for bases other than 3.
    int[] digits = new int[power + 1];

    while (power >= 0) {

      int digitAtPower = findDigitAtPower(valueToBeDecomposed, power);

      int deletedValue =  (int) (digitAtPower * (Math.pow(3, power)));
      valueToBeDecomposed -= deletedValue;

      digits[power] = digitAtPower;

      power -= 1;
    }

    return digits;
  }

  static int findDigitAtPower(int valueToBeDecomposed, int power)
  {
    // We're going to take a naiive approach to this because naiive is easy
    // for powers of 3 -- and in the context of the challenge, 3 is the only
    // base that works.

    int powerPart = (int) (Math.pow(3, power));

    if ((valueToBeDecomposed - (powerPart + powerPart)) >= 0)
      {
	return 2;
      }
    else if ((valueToBeDecomposed - powerPart) >= 0)
      {
	return 1;
      }
    else
      {
	return 0;
      }
  }

  // Return the log base 3 of x. This function uses the equivalence
  // logY(X) = log(X)/log(Y).
  private static final double log3(double x) {
    return Math.log10(x) / Math.log10(3);
  }

  // The following functions were used in developing the code, and are left
  // here as a diagnostic aid for future maintainers.
  public static void main(String[] argv) {
    test(1);
    test(10);
    test(100);
    test(1000);

    test(1);
    test(3);
    test(9);
    test(27);
    test(81);
    test(243);
    test(729);

    test(24);
    test(56);

    test(4);

    // These are the test cases given in the assignment.
    test(2);
    test(8);
  }

  static void test(int value) {
    double dvalue = value;
    double l = log3(dvalue);
    int ceil = ((int) Math.floor(l)) + 1;
    //    System.out.println("\n==============================================================================");
    //    System.out.println("Test for value " + dvalue + " is " + l + " and " + ceil);

    int[] digits = getDigits(value, ceil);
    recompose(value, digits);

    reDistribute(digits);
    recompose(value, digits);

    String[] answer = solve(value);
    answer = normalize(answer);

    for (int j = answer.length; j > 0; j--) {
      int power = j - 1;
      //System.out.println(" Weight " + Math.pow(3, power) + ": " + answer[power]);
    }


    System.out.println();
    System.out.println("inputs:");
    System.out.println("    (int) " + value);
    System.out.println("outputs:");
    System.out.print("    (string list) [\"" + answer[0]);
    for (int i = 1; i < answer.length; i++) System.out.print("\", \"" + answer[i]);
    System.out.println("\"]");
  }

  static void recompose(int originalValue, int[] digits) {
    int value = 0;

    // Let's test recomposing the value.
    for (int j = digits.length; j > 0; j--) {
      int power = j - 1;
      value += digits[power] * Math.pow(3, power);
    }

    if (value == originalValue) {
//       System.out.println("Success! Recomposed to " + value);
    } else {
      System.out.println("*** ERROR! Original value " + originalValue + " recomposed to " + value);
    }
  }
}
