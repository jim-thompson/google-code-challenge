package com.google.challenges;
import java.util.*;
import java.math.*;

public class BigRat {
	  public BigInteger num = null;
	  public BigInteger denom = null; public BigRat(int n) { num = BigInteger.valueOf(n);
	    denom = BigInteger.valueOf(1);
	  }

	  public BigRat(BigInteger n) {
	    num = n;
	    denom = BigInteger.valueOf(1);
	  }

	  public BigRat(BigInteger n, BigInteger d) {
	    num = n;
	    denom = d;
	  }

	  public BigRat reduce() {
	    BigInteger gcd = num.gcd(denom);
	    return new BigRat(num.divide(gcd), denom.divide(gcd));
	  }

	  public BigRat multiply(BigRat b) {
	    BigInteger n = b.num.multiply(num);
	    BigInteger d = b.denom.multiply(denom);
	    return new BigRat(n, d);
	  }

	  public BigRat divide(BigRat b) {
	    BigInteger n = b.denom.multiply(num);
	    BigInteger d = b.num.multiply(denom);
	    return new BigRat(n, d);
	  }

	  public BigRat add(BigRat b) {
	    BigInteger n = b.num.multiply(denom).add(num.multiply(b.denom));
	    BigInteger d = b.denom.multiply(denom);
	    return new BigRat(n, d);
	  }

	  public BigRat subtract(BigRat b) {
	    return this.add(new BigRat(b.num.negate(), b.denom));
	  }

	  public BigRat pow(int n) {
	    BigRat acc = new BigRat(1);
	    for (int i=0; i < n; i++) {
	      acc = acc.multiply(this);
	    }
	    return acc;
	  }

	  public String toString() {
	    BigRat r = this.reduce();
	    return r.num.toString() + "/" + r.denom.toString();
	  }
}
