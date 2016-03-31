package com.google.challenges;

import java.util.*;

public class Answer {
  static String candidate;
  static int candidate_len;

  public static String answer(String chunk, String word) {
    int word_len = word.length();
    int chunk_len = chunk.length();

    candidate = chunk;
    candidate_len = chunk_len;

    recurse(chunk, chunk_len, word, word_len);
    return candidate;
  }

  static public void recurse(String chunk, int chunk_len, String word, int word_len) {
    //    int thiscount = 0;

    ArrayList<String> subchunks = new ArrayList<String>();

    int search_start = 0;

    while(true) {
      int found_loc = chunk.indexOf(word, search_start);
      if (found_loc < 0) {
	//	if (thiscount > 0) break;

	// We have a candidate
	if (chunk_len < candidate_len) {
	  candidate = chunk;
	  candidate_len = chunk_len;
	} else if ((chunk_len == candidate_len) && (chunk.compareTo(candidate) < 0)) {
	  candidate = chunk;
	  candidate_len = chunk_len;
	}

	break;
      }

      StringBuilder new_chunk_builder = new StringBuilder(20);
      new_chunk_builder.append(chunk.substring(0, found_loc));
      new_chunk_builder.append(chunk.substring(found_loc + word_len));
      String new_chunk = new_chunk_builder.toString();

      if (!subchunks.contains(new_chunk)) {
	subchunks.add(new_chunk);
	//        thiscount += 1;
      }

      search_start = found_loc + 1;
    }

    for (String s : subchunks) {
      recurse(s, chunk_len - word_len, word, word_len);
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
    test("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "x");
    test("aabb", "ab");
  }
}
