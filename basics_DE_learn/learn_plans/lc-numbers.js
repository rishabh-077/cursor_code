/**
 * LeetCode problem IDs for dsa-study-plan.html
 * Format: [id, slug, ...name aliases]
 */
const LC_ENTRIES = [
  [217, "contains-duplicate", "contains duplicate"],
  [485, "max-consecutive-ones", "find maximum in array"],
  [88, "merge-sorted-array", "merge sorted array"],
  [283, "move-zeroes", "move zeroes"],
  [26, "remove-duplicates-from-sorted-array", "remove duplicates from sorted array"],
  [66, "plus-one", "plus one"],
  [118, "pascals-triangle", "pascal's triangle", "pascals triangle"],
  [189, "rotate-array", "rotate array"],
  [442, "find-all-duplicates-in-an-array", "find all duplicates in an array"],
  [125, "valid-palindrome", "valid palindrome"],
  [242, "valid-anagram", "valid anagram"],
  [344, "reverse-string", "reverse string"],
  [387, "first-unique-character-in-a-string", "first unique character in a string"],
  [14, "longest-common-prefix", "longest common prefix"],
  [13, "roman-to-integer", "roman to integer"],
  [38, "count-and-say", "count and say"],
  [5, "longest-palindromic-substring", "longest palindromic substring"],
  [8, "string-to-integer-atoi", "string to integer", "string to integer (atoi)"],
  [1, "two-sum", "two sum"],
  [383, "ransom-note", "ransom note"],
  [771, "jewels-and-stones", "jewels and stones"],
  [205, "isomorphic-strings", "isomorphic strings"],
  [290, "word-pattern", "word pattern"],
  [49, "group-anagrams", "group anagrams"],
  [347, "top-k-frequent-elements", "top k frequent elements"],
  [128, "longest-consecutive-sequence", "longest consecutive sequence"],
  [560, "subarray-sum-equals-k", "subarray sum equals k"],
  [432, "all-oone-data-structure", "all o`one data structure", "all o'one data structure"],
  [977, "squares-of-a-sorted-array", "squares of a sorted array"],
  [167, "two-sum-ii-input-array-is-sorted", "two sum ii", "two sum ii (sorted array)"],
  [15, "3sum", "3sum"],
  [11, "container-with-most-water", "container with most water"],
  [19, "remove-nth-node-from-end-of-list", "remove nth node from end of list", "remove nth node from end"],
  [75, "sort-colors", "sort colors", "dutch national flag"],
  [18, "4sum", "4sum"],
  [42, "trapping-rain-water", "trapping rain water"],
  [643, "maximum-average-subarray-i", "maximum average subarray i"],
  [121, "best-time-to-buy-and-sell-stock", "best time to buy and sell stock"],
  [3, "longest-substring-without-repeating-characters", "longest substring without repeating characters"],
  [567, "permutation-in-string", "permutation in string"],
  [438, "find-all-anagrams-in-a-string", "find all anagrams in a string"],
  [424, "longest-repeating-character-replacement", "longest repeating character replacement"],
  [1004, "max-consecutive-ones-iii", "max consecutive ones iii"],
  [904, "fruit-into-baskets", "fruits into baskets"],
  [76, "minimum-window-substring", "minimum window substring"],
  [239, "sliding-window-maximum", "sliding window maximum"],
  [1480, "running-sum-of-1d-array", "running sum of 1d array"],
  [724, "find-pivot-index", "find pivot index"],
  [303, "range-sum-query-immutable", "range sum query", "range sum query — immutable"],
  [238, "product-of-array-except-self", "product of array except self"],
  [525, "contiguous-array", "contiguous array"],
  [2270, "number-of-ways-to-split-array", "number of ways to split array"],
  [20, "valid-parentheses", "valid parentheses"],
  [682, "baseball-game", "baseball game"],
  [225, "implement-stack-using-queues", "implement stack using queues"],
  [1047, "remove-all-adjacent-duplicates-in-string", "remove all adjacent duplicates in string"],
  [155, "min-stack", "min stack"],
  [739, "daily-temperatures", "daily temperatures"],
  [150, "evaluate-reverse-polish-notation", "evaluate reverse polish notation"],
  [735, "asteroid-collision", "asteroid collision"],
  [853, "car-fleet", "car fleet"],
  [503, "next-greater-element-ii", "next greater element ii"],
  [84, "largest-rectangle-in-histogram", "largest rectangle in histogram"],
  [227, "basic-calculator-ii", "basic calculator ii"],
  [232, "implement-queue-using-stacks", "implement queue using stacks"],
  [1700, "number-of-students-unable-to-eat-lunch", "number of students unable to eat lunch"],
  [622, "design-circular-queue", "design circular queue"],
  [994, "rotting-oranges", "rotting oranges"],
  [286, "walls-and-gates", "walls and gates"],
  [752, "open-the-lock", "open the lock"],
  [206, "reverse-linked-list", "reverse linked list"],
  [21, "merge-two-sorted-lists", "merge two sorted lists"],
  [141, "linked-list-cycle", "linked list cycle"],
  [234, "palindrome-linked-list", "palindrome linked list"],
  [876, "middle-of-the-linked-list", "middle of the linked list"],
  [83, "remove-duplicates-from-sorted-list", "remove duplicates from sorted list"],
  [142, "linked-list-cycle-ii", "linked list cycle ii"],
  [143, "reorder-list", "reorder list"],
  [2, "add-two-numbers", "add two numbers"],
  [138, "copy-list-with-random-pointer", "copy list with random pointer"],
  [24, "swap-nodes-in-pairs", "swap nodes in pairs"],
  [25, "reverse-nodes-in-k-group", "reverse nodes in k-group"],
  [146, "lru-cache", "lru cache"],
  [23, "merge-k-sorted-lists", "merge k sorted lists", "k-way merge"],
  [509, "fibonacci-number", "fibonacci number"],
  [231, "power-of-two", "power of two"],
  [1920, "build-array-from-permutation", "sum of digits"],
  [50, "powx-n", "pow(x, n)"],
  [22, "generate-parentheses", "generate parentheses"],
  [104, "maximum-depth-of-binary-tree", "maximum depth of binary tree"],
  [226, "invert-binary-tree", "invert binary tree"],
  [101, "symmetric-tree", "symmetric tree"],
  [112, "path-sum", "path sum"],
  [100, "same-tree", "same tree"],
  [572, "subtree-of-another-tree", "subtree of another tree"],
  [543, "diameter-of-binary-tree", "diameter of binary tree"],
  [102, "binary-tree-level-order-traversal", "binary tree level order traversal"],
  [199, "binary-tree-right-side-view", "binary tree right side view"],
  [1448, "count-good-nodes-in-binary-tree", "count good nodes in binary tree"],
  [236, "lowest-common-ancestor-of-a-binary-tree", "lowest common ancestor of bt", "lowest common ancestor of a binary tree"],
  [103, "binary-tree-zigzag-level-order-traversal", "binary tree zigzag level order"],
  [113, "path-sum-ii", "path sum ii"],
  [105, "construct-binary-tree-from-preorder-and-inorder-traversal", "construct bt from preorder and inorder"],
  [449, "serialize-and-deserialize-bst", "serialize and deserialize bst"],
  [124, "binary-tree-maximum-path-sum", "binary tree maximum path sum"],
  [297, "serialize-and-deserialize-binary-tree", "serialize and deserialize binary tree"],
  [700, "search-in-a-binary-search-tree", "search in a binary search tree"],
  [530, "minimum-absolute-difference-in-bst", "minimum absolute difference in bst"],
  [108, "convert-sorted-array-to-binary-search-tree", "convert sorted array to bst"],
  [98, "validate-binary-search-tree", "validate binary search tree"],
  [230, "kth-smallest-element-in-a-bst", "kth smallest element in a bst"],
  [701, "insert-into-a-binary-search-tree", "insert into a binary search tree"],
  [450, "delete-node-in-a-bst", "delete node in a bst"],
  [235, "lowest-common-ancestor-of-a-binary-search-tree", "lowest common ancestor of a bst"],
  [285, "inorder-successor-in-bst", "inorder successor in bst"],
  [315, "count-of-smaller-numbers-after-self", "count of smaller numbers after self"],
  [1971, "find-if-path-exists-in-graph", "find if path exists in graph"],
  [733, "flood-fill", "flood fill"],
  [463, "island-perimeter", "island perimeter"],
  [200, "number-of-islands", "number of islands"],
  [695, "max-area-of-island", "max area of island"],
  [133, "clone-graph", "clone graph"],
  [417, "pacific-atlantic-water-flow", "pacific atlantic water flow"],
  [547, "number-of-provinces", "number of provinces"],
  [127, "word-ladder", "word ladder"],
  [1091, "shortest-path-in-binary-matrix", "shortest path in binary matrix"],
  [207, "course-schedule", "course schedule"],
  [210, "course-schedule-ii", "course schedule ii"],
  [323, "number-of-connected-components-in-an-undirected-graph", "number of connected components in graph"],
  [130, "surrounded-regions", "surrounded regions"],
  [684, "redundant-connection", "redundant connection"],
  [1192, "critical-connections-in-a-network", "critical connections in a network"],
  [2115, "find-all-possible-recipes-from-given-supplies", "find all possible recipes from given supplies"],
  [310, "minimum-height-trees", "minimum height trees"],
  [269, "alien-dictionary", "alien dictionary"],
  [444, "sequence-reconstruction", "sequence reconstruction"],
  [1462, "course-schedule-iv", "course schedule iv"],
  [3052, "number-of-islands-ii", "number of islands ii"],
  [721, "accounts-merge", "accounts merge"],
  [947, "most-stones-removed-with-same-row-or-column", "most stones removed with same row or column"],
  [704, "binary-search", "binary search (basic)"],
  [35, "search-insert-position", "search insert position"],
  [278, "first-bad-version", "first bad version"],
  [374, "guess-number-higher-or-lower", "guess number higher or lower"],
  [69, "sqrtx", "sqrt(x)"],
  [153, "find-minimum-in-rotated-sorted-array", "find minimum in rotated sorted array"],
  [33, "search-in-rotated-sorted-array", "search in rotated sorted array"],
  [875, "koko-eating-bananas", "koko eating bananas"],
  [1011, "capacity-to-ship-packages-within-d-days", "capacity to ship packages within d days"],
  [162, "find-peak-element", "find peak element"],
  [74, "search-a-2d-matrix", "search a 2d matrix"],
  [981, "time-based-key-value-store", "time based key-value store"],
  [4, "median-of-two-sorted-arrays", "median of two sorted arrays"],
  [410, "split-array-largest-sum", "split array largest sum"],
  [1046, "last-stone-weight", "last stone weight"],
  [703, "kth-largest-element-in-a-stream", "kth largest element in a stream"],
  [215, "kth-largest-element-in-an-array", "kth largest element in an array"],
  [973, "k-closest-points-to-origin", "k closest points to origin"],
  [621, "task-scheduler", "task scheduler"],
  [767, "reorganize-string", "reorganize string"],
  [295, "find-median-from-data-stream", "find median from data stream"],
  [502, "ipo", "ipo"],
  [407, "trapping-rain-water-ii", "trapping rain water ii"],
  [784, "letter-case-permutation", "letter case permutation"],
  [401, "binary-watch", "binary watch"],
  [78, "subsets", "subsets"],
  [90, "subsets-ii", "subsets ii"],
  [46, "permutations", "permutations"],
  [47, "permutations-ii", "permutations ii"],
  [39, "combination-sum", "combination sum"],
  [40, "combination-sum-ii", "combination sum ii"],
  [17, "letter-combinations-of-a-phone-number", "letter combinations of a phone number"],
  [79, "word-search", "word search"],
  [51, "n-queens", "n-queens"],
  [52, "n-queens-ii", "n-queens ii"],
  [37, "sudoku-solver", "sudoku solver"],
  [212, "word-search-ii", "word search ii"],
  [70, "climbing-stairs", "climbing stairs"],
  [746, "min-cost-climbing-stairs", "min cost climbing stairs"],
  [198, "house-robber", "house robber"],
  [1137, "n-th-tribonacci-number", "n-th tribonacci number"],
  [213, "house-robber-ii", "house robber ii"],
  [322, "coin-change", "coin change"],
  [518, "coin-change-ii", "coin change ii"],
  [55, "jump-game", "jump game"],
  [45, "jump-game-ii", "jump game ii"],
  [139, "word-break", "word break"],
  [300, "longest-increasing-subsequence", "longest increasing subsequence"],
  [152, "maximum-product-subarray", "maximum product subarray"],
  [91, "decode-ways", "decode ways"],
  [416, "partition-equal-subset-sum", "partition equal subset sum"],
  [140, "word-break-ii", "word break ii"],
  [871, "minimum-number-of-refueling-stops", "minimum number of refueling stops"],
  [62, "unique-paths", "unique paths"],
  [64, "minimum-path-sum", "minimum path sum"],
  [63, "unique-paths-ii", "unique paths ii"],
  [1143, "longest-common-subsequence", "longest common subsequence"],
  [718, "maximum-length-of-repeated-subarray", "longest common substring"],
  [583, "delete-operation-for-two-strings", "delete operation for two strings"],
  [494, "target-sum", "target sum"],
  [97, "interleaving-string", "interleaving string"],
  [72, "edit-distance", "edit distance"],
  [10, "regular-expression-matching", "regular expression matching"],
  [44, "wildcard-matching", "wildcard matching"],
  [312, "burst-balloons", "burst balloons"],
  [208, "implement-trie-prefix-tree", "implement trie"],
  [211, "design-add-and-search-words-data-structure", "design add and search words data structure"],
  [648, "replace-words", "replace words"],
  [677, "map-sum-pairs", "map sum pairs"],
  [720, "longest-word-in-dictionary", "longest word in dictionary"],
  [336, "palindrome-pairs", "palindrome pairs"],
];

const LC_BY_KEY = {};
for (const [id, slug, ...aliases] of LC_ENTRIES) {
  const meta = { id, slug };
  for (const alias of aliases) {
    LC_BY_KEY[normalizeLcKey(alias)] = meta;
  }
}

function normalizeLcKey(name) {
  return String(name)
    .toLowerCase()
    .replace(/\(.*?\)/g, " ")
    .replace(/[—–-].*$/g, " ")
    .replace(/[`'']/g, "'")
    .replace(/\s+/g, " ")
    .trim();
}

/** Resolve LeetCode meta from question object or name string */
function resolveLc(q) {
  if (!q) return null;
  if (q.lc) {
    const id = q.lc;
    const slug = q.slug || `problem-${id}`;
    return { id, slug };
  }
  const name = typeof q === "string" ? q : q.name;
  if (!name) return null;
  const key = normalizeLcKey(name);
  if (LC_BY_KEY[key]) return LC_BY_KEY[key];
  for (const [k, meta] of Object.entries(LC_BY_KEY)) {
    if (key.includes(k) || k.includes(key)) return meta;
  }
  return null;
}

function lcProblemUrl(meta) {
  return `https://leetcode.com/problems/${meta.slug}/`;
}

function formatLcLabel(q) {
  const meta = resolveLc(q);
  if (!meta) return "";
  return `<a class="lc-num" href="${lcProblemUrl(meta)}" target="_blank" rel="noopener" title="Open on LeetCode">#${meta.id}</a>`;
}
