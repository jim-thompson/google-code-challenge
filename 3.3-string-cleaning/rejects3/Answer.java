package com.google.challenges;

import java.util.*;

public class Answer {
  static String candidate;

  public static String answer(String chunk, String word) {
    candidate = chunk;
    recurse(chunk, word);
    return candidate;
  }

  static public void recurse(String chunk, String word) {
    int thiscount = 0;
    int chunk_len = chunk.length();
    int word_len = word.length();

    ArrayList<String> subchunks = new ArrayList<String>();

    int search_start = 0;

    while(true) {
      int found_loc = chunk.indexOf(word, search_start);
      if (found_loc < 0) {
	if (thiscount > 0) break;

	// We have a candidate
	if (chunk.length() < candidate.length()) {
	  candidate = chunk;
	} else if ((chunk.length() == candidate.length()) && (chunk.compareTo(candidate) < 0)) {
	  candidate = chunk;
	}

	break;
      }

      String new_chunk = chunk.substring(0, found_loc) + chunk.substring(found_loc + word_len);

      if (!subchunks.contains(new_chunk)) {
	subchunks.add(new_chunk);
        thiscount += 1;
      }

      search_start = found_loc + 1;
    }

    for (String s : subchunks) {
      recurse(s, word);
    }
  }

  static void test(String chunk, String word) {
    String s = answer(chunk, word);
    System.out.println("Answer: " + s);
  }

  public static void main(String[] argv) {
    test("lolol", "lol");
    test("lololololo", "lol");
    test("goodgooogoogfogoood", "goo");
    test("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxy", "x");
  }
}
