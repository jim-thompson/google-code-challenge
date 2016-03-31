# Author: Jim Thompson, jim.thompson@pobox.com

def answer(heights):
    # your code here

    # Here's how we compute the amount of pooled rainwater on the
    # rabbit hutches: Imagine the smallest grid that overlays all the
    # hutches; the grid will be as wide as the number of hutches and
    # as high as the highest stack of hutches. Now subtract from that
    # the number of hutches. This is the amount of water the hutches
    # would accumulate if there were no runoff. Or if - say - we were
    # accumulating snow instead of water.

    # We'll compute two runoff amounts - one for the left side of the
    # stack of hutches, and one for the right. Any square in the grid
    # will run off if it's "clear" to the edge. In other words, any
    # water that's higher than the maximum hutch height between it and
    # the edge.

    # Compute the size of the bounding grid
    hutchmax = max(heights)
    hutchlen = len(heights)
    gridcount = hutchlen * hutchmax

    # Compute the number of hutches
    hutchcount = sum(heights)

    # Compute the runoff of the left and then right sides of the stack
    # of hutches. Note that we can compute the runoff on the right
    # side simply by reversing the array and then running the same
    # runoff calculation
    leftrunoff = computerunoff(heights, hutchmax);
    rightrunoff = computerunoff(reversed(heights), hutchmax);

    # Finally, we can compute the amount of water pooled on the tops
    # of the hutches. We take the max possible pooled water (the
    # "snow" amount) and subtract the runoff on each side.
    return gridcount - hutchcount - leftrunoff - rightrunoff;


def computerunoff(heights, hutchmax):
    # Basic approach: we iterate over the columns of hutches from one
    # side inward. If we reach a column that's as high as the tallest
    # column of hutches, we can stop immediately, because no more
    # inward column of hutches can produce runoff.

    # At each column of hutches we compute the amount of water that
    # will run off. This amount is amount of water between the top of
    # the grid, and the height of the pooling water. The height of the
    # pooling water is always at least as high as the current column
    # of hutches. If the height of the current column is higher, then
    # that increases the pooling height for hutches further in (we're
    # working from one edge inward.

    # As we start the iteration, the pooling height is zero.
    columnpoolheight = 0

    # ...as is the amount of runoff
    thisrunoff = 0

    # Now we loop over the hutches.
    for h in heights:

        # If we've reached a column of hutches that's as high as the
        # maximum, then we can stop now. No more water further inward
        # can run off.
        if h == hutchmax:
            break

        # If this column of hutches is higher than the height of the
        # pooling water, then the pooling height increases.
        if h > columnpoolheight:
            columnpoolheight = h

        # Finally, for this column, the amount of water that will run
        # off is all the water between the top of the grid and the top
        # of the pool of water.
        thisrunoff += (hutchmax - columnpoolheight)

    # Return the amount of runoff we've calculated
    return thisrunoff

hutches = [4]
water = answer(hutches);
print "Total water =", water
print

hutches = [0]
water = answer(hutches);
print "Total water =", water
print

hutches = [50, 100]
water = answer(hutches);
print "Total water =", water
print

hutches = [100, 50]
water = answer(hutches);
print "Total water =", water
print

hutches = [100, 0, 100]
water = answer(hutches);
print "Total water =", water
print
    
hutches = [1, 4, 2, 5, 1, 2, 3]
water = answer(hutches)
print "Total water =", water
print

heights = [1, 2, 3, 2, 1]
water = answer(heights)
print "Total water =", water
print
