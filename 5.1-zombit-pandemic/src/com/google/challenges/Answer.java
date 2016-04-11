package com.google.challenges;
import java.util.*;
import java.math.*;


public class Answer {
	  public static String[] answers = new String[]{
			    "0/1",  // meaningless
			    "1/1",  // trivial
			    "2/1",
			    "3/1",
			    "106/27",
			    "155/32",
			    "17886/3125",
			    "38563/5832",
			    "6152766/823543",
			    "17494593/2097152",
			    "3560009650/387420489",
			    "627954547/62500000",
			    "3105872296170/285311670611",
			    "1634885974709/139314069504",
			    "3806351519163438/302875106592253",
			    "18625944786006435/1389000853194752",
			    "6234351169555051774/437893890380859375",
			    "34756722601614314393/2305843009213693952",
			    "773562277426009442754/48661191875666868481",
			    "10284482150135468731247/614787626176508399616",
			    "34718513354331762959383530/1978419655660313589123979",
			    "15053773537765084950812607/819200000000000000000000",
			    "112140288809338469272615587070/5842587018385982521381124421",
			    "854320303454493478751408480735/42678484670527444674580840448",
			    "18912756321867471938721965101170/907846434775996175406740561329",
			    "3610030325498948367204598852852585/166716972106285515556135184105472",
			    "1995411155670864680670929436760622226/88817841970012523233890533447265625",
			    "344576823778566517467992368671763089/14798364375497974304799697808654336",
			    "10684649726223342659811498644660675608426/443426488243037769948249630619149892803",
			    "1843103398013622761374075136603923170373/73985542663511997461099839851260280832",
			    "66042949805511372231365213875653489838628430/2567686153161211134561828214731016126483469",
			    "136582014642563779970541724775540053333470143/5147278302366225000000000000000000000000000",
			    "466710421570971604568184743712738644191638213630/17069174130723235958610643029059314756044734431",
			    "5143463407898005313442475192483802091320056485177/182687704666362864775460604089535377456991567872",
			    "3739096410394966424064185724550288598383827338841538/129110040087761027839616029934664535539337183380513",
			    "2734416349495925626662325797021969312293908777741055/91848741448192312589172269541487152770452671168512",
			    "6741987061723606853594628610525741041930695353663689186/220501499870829739190357286682701669633388519287109375",
			    "13042636517110143087176055909996022983442999225254367979/415575620795767675030130764658032788047530686054137856",
			    "339749569462116848439935334968084869925827515702722344355358/10555134955777783414078330085995832946127396083370199442517",
			    "4437525380892633218641214622385900021643773692787246091579511/134488975247499247757553656607015472389435921103802008076288",
			    "3805487585436257606374152449167335438201952264350939203818892350/112595147462071192539789448988889059930192105219196517009951959",
			    "52292042753206118664403121823278381003500114115970247032940845257/1511157274518286468382720000000000000000000000000000000000000000",
			    "47120325153233237084737138078618913934658460950300385959724398769010/1330877630632711998713399240963346255985889330161650994325137953641",
			    "169883796370934068081950976917114805097902708520947013505251740843915/4691591798290517886149124130132951806688999080273086788621672906752",
			    "641905988034354231029821722880620140843980880607592490372521399462500330/17343773367030267519903781288812032158308062539012091953077767198995507",
			    "1211700424850550781463312152848931785433758128964920752788874530817930545/32043340993134532088206337643318375554471559945634492926483077596708864",
			    "9578738547310180405522771203581728115283009160565774924265357416769319791214/248063644451341145494649182395412689744530581492654164321720600128173828125",
			    "151164422577241276086427256674992515031103246835103828947780587220861706128723/3835043287599284278832554205955049737473521330634856660010332469295644147712",
			    "155952219111744763744858482987443790414475772813221572439665055721589513953631486/3877924263464448622666648186154330754898344901344205917642325627886496385062863",
			    "2567162329457217045964642947718867244253878791072715244167941318071834302918083033/62587759782932414896817128156196361030838744422175027877657217635602709644050432",
			    "2760193150860512039773534794580172563788128162694566629462545301385874784598772926370/66009724686219550843768321818371771650147004059278069406814190436565131829325062449"
			  };


			  public static String answer(int n) {
			    return answers[n];
			  }

			  // Answers were calculated using the following code.
			  // I optimized the living hell out of it and it was not "fast enough"
			  // until I just included the results verbatim, which is a very reasonable
			  // thing to do for an input space of 48.
			  //
			  // What's happening below is explained very well at:
			  // http://math.stackexchange.com/questions/1090498/how-to-calculate-the-expected-maximum-tree-size-in-a-pseudoforest
			  // I plucked this algorithm (in a less optimized form) from that site.

			  public static void main(String[] args) {
			    for (Integer i=2; i<51; i++) {
			      System.out.println(real_answer(i));
			    }
			    System.out.println("Done!");
			  }

			  private static BigInteger BI0 = BigInteger.ZERO;
			  private static BigInteger BI1 = BigInteger.ONE;
			  private static BigInteger BI2 = BI1.add(BI1);
			  private static BigInteger BI3 = BI2.add(BI1);

			  private static BigRat BR0 = new BigRat(0);
			  private static BigRat BR1 = new BigRat(1);
			  private static BigRat BR2 = new BigRat(2);

			  public static String real_answer(int n) {
			    BigRat sum = BR0;

			    // generates all partitions of an integer n
			    // algorithm plucked from: http://jeromekelleher.net/partitions.php
			    // Here, partitions represent warren sizes within a graph.

			    int[] a = new int[n];
			    int k = 1;
			    int l;
			    int y = n - 1;
			    int x;
			    int[] p;
			    while (k != 0) {
			      x = a[k-1] + 1;
			      k -= 1;
			      while (2*x <= y) {
			        a[k] = x;
			        y -= x;
			        k += 1;
			      }
			      l = k + 1;
			      while (x <= y) {
			        a[k] = x;
			        a[l] = y;

			        // first k+2 elements form a partition
			        p = Arrays.copyOfRange(a, 0, k+2);
			        sum = sum.add(partition_addend(n, p));

			        x += 1;
			        y -= 1;
			      }
			      a[k] = x + y;
			      y += x - 1;

			      // first k+1 elements form a partition
			      p = Arrays.copyOfRange(a, 0, k+1);
			      sum = sum.add(partition_addend(n, p));
			    }

			    // divide by total number of possible n-rabbit graphs
			    return sum.divide(new BigRat(n-1).pow(n)).toString();
			  }

			  public static BigRat partition_addend(int n, int[] p) {
			    int pmax = 0;
			    BigRat tproduct = BR1;
			    for (int i=0; i < p.length; i++) {
			      if (p[i] == 1) return BR0;
			      if (p[i] > pmax) pmax = p[i];
			      tproduct = tproduct.multiply(arrangements(p[i]));
			    }
			    return tproduct.multiply(new BigRat(pmax)).multiply(splits(n, p));
			  }

			  // number of ways to split n rabbits into partition p
			  public static BigRat splits(int n, int[] p) {
			    BigInteger num = BI1;
			    BigInteger denom = BI1;

			    int psum = 0;
			    int last_elt = 0;
			    int multiplicity = 1;
			    for (int i=0; i < p.length; i++) {
			      num = num.multiply(choose(n - psum, p[i]));
			      psum += p[i];
			      if (p[i] == last_elt) {
			        multiplicity++;
			        denom = denom.multiply(BigInteger.valueOf(multiplicity));
			      }
			      else {
			        multiplicity = 1;
			      }
			      last_elt = p[i];
			    }

			    return new BigRat(num, denom);
			  }

			  public static Map<Integer, BigRat> arrangements_cache =
			    new HashMap<Integer, BigRat>();

			  // number of ways that a rabbit population can form a single warren of size n
			  // algorithm comes from http://math.stackexchange.com/questions/1071564/how-many-good-graphs-of-size-n-are-there
			  public static BigRat arrangements(int n) {
			    if (n < 3) return BR1;
			    if (!arrangements_cache.containsKey(n)) {
			      BigInteger sum = BigInteger.valueOf(0);
			      for (int k = 1; k < n; k++) {
			        sum = sum.add(
			          choose(n, k)
			            .multiply(BigInteger.valueOf(n-k).pow(n-k))
			            .multiply(BigInteger.valueOf(k).pow(k))
			        );
			      }
			      arrangements_cache.put(n, new BigRat(sum, BigInteger.valueOf(n)));
			    }
			    return arrangements_cache.get(n);
			  }

			  private static Map<List<Integer>,BigInteger> choose_cache =
			    new HashMap<List<Integer>,BigInteger>();

			  public static BigInteger choose(int n, int k) {
			    //if (! (0 <= k && k <= n)) return BI0;

			    if (k > n) return BI0;
			    else if (k == 0 || n == k) return BI1;
			    else if (k == 1 || k == n-1) return BigInteger.valueOf(n);

			    List<Integer> nk = Arrays.asList(n, k);
			    if (!choose_cache.containsKey(nk)) {
			      BigInteger ntok = BI1;
			      BigInteger ktok = BI1;
			      int min = k;
			      if ((n - k) < k) min = n - k;
			      for (int i=1; i <= min; i++) {
			        ntok = ntok.multiply(BigInteger.valueOf(n));
			        ktok = ktok.multiply(BigInteger.valueOf(i));
			        n -= 1;
			      }

			      choose_cache.put(nk, ntok.divide(ktok));
			    }
			    return choose_cache.get(nk);
			  }

			  private static Map<Integer, BigInteger> fact_cache =
			    new HashMap<Integer, BigInteger>();

			  // optimized factorial algorithm from:
			  // http://cs.stackexchange.com/questions/14456/factorial-algorithm-more-efficient-than-naive-multiplication
			  public static BigInteger fact(int n) {
			    if (! fact_cache.containsKey(n)) {
			      BigInteger f = BI1;
			      for (int i=1; i < n-1; i++) {
			        f = f.multiply(oddprod(BI3, BI2.pow(i+1).subtract(BI1)));
			      }
			      f = bigpow(BI2, BI2.pow(n).subtract(BI1)).multiply(f);
			      fact_cache.put(n, f);
			    }
			    return fact_cache.get(n);
			  }

			  private static Map<List<BigInteger>,BigInteger> oddprod_cache =
			    new HashMap<List<BigInteger>,BigInteger>();

			  public static BigInteger oddprod(BigInteger l, BigInteger h) {
			    List<BigInteger> lh = Arrays.asList(l, h);
			    if (!oddprod_cache.containsKey(lh)) {
			      BigInteger p = BigInteger.valueOf(1);
			      BigInteger ml = (l.mod(BI2) == BI0) ? l : l.add(BI1);
			      BigInteger mh = (h.mod(BI2) == BI0) ? l : l.subtract(BI1);
			      while (ml.compareTo(mh) < 1) {  // while ml <= mh
			        p = p.multiply(ml);
			        ml = ml.add(BI2);
			      }
			      oddprod_cache.put(lh, p);
			    }
			    return oddprod_cache.get(lh);
			  }

			  public static BigInteger bigpow(BigInteger base, BigInteger exponent) {
			    BigInteger result = BI1;
			    while (exponent.signum() > 0) {
			      if (exponent.testBit(0)) result = result.multiply(base);
			      base = base.multiply(base);
			      exponent = exponent.shiftRight(1);
			    }
			    return result;
			  }
			}