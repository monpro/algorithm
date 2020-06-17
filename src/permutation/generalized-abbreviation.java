package permutation;

import java.util.*;

class AbbrWord {
    StringBuilder str;
    int start;
    int count;

    public AbbrWord(final StringBuilder str, final int start, final int count) {
        this.str = str;
        this.start = start;
        this.count = count;
    }
}

class Solution {
    /**
     * @param word: the given word
     * @return: the generalized abbreviations of a word
     */

    public List<String> generateAbbreviations(final String str) {
        final List<String> result = new ArrayList<String>();
        final Queue<AbbrWord> queue = new LinkedList<>();
        final int length = str.length();
        queue.offer(new AbbrWord(new StringBuilder(), 0, 0));

        while (!queue.isEmpty()) {
            final AbbrWord word = queue.poll();
            if (word.start == length) {
                if (word.count != 0) {
                    word.str.append(word.count);
                }
                result.add(word.str.toString());
            } else {
                queue.offer(new AbbrWord(new StringBuilder(word.str), word.start + 1, word.count + 1));
                if (word.count != 0) {
                    word.str.append(word.count);
                }
                queue.offer(
                        new AbbrWord(new StringBuilder(word.str).append(str.charAt(word.start)), word.start + 1, 0));

            }
        }
        return result;
    }
}