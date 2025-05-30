---
comments: true
difficulty: Easy
rating: 1231
source: Weekly Contest 254 Q1
tags:
    - Array
    - String
---

<!-- problem:start -->

# [1967. Number of Strings That Appear as Substrings in Word](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word)

## Description

<!-- description:start -->

<p>Given an array of strings <code>patterns</code> and a string <code>word</code>, return <em>the <strong>number</strong> of strings in </em><code>patterns</code><em> that exist as a <strong>substring</strong> in </em><code>word</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> patterns = [&quot;a&quot;,&quot;abc&quot;,&quot;bc&quot;,&quot;d&quot;], word = &quot;abc&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong>
- &quot;a&quot; appears as a substring in &quot;<u>a</u>bc&quot;.
- &quot;abc&quot; appears as a substring in &quot;<u>abc</u>&quot;.
- &quot;bc&quot; appears as a substring in &quot;a<u>bc</u>&quot;.
- &quot;d&quot; does not appear as a substring in &quot;abc&quot;.
3 of the strings in patterns appear as a substring in word.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> patterns = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;], word = &quot;aaaaabbbbb&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong>
- &quot;a&quot; appears as a substring in &quot;a<u>a</u>aaabbbbb&quot;.
- &quot;b&quot; appears as a substring in &quot;aaaaabbbb<u>b</u>&quot;.
- &quot;c&quot; does not appear as a substring in &quot;aaaaabbbbb&quot;.
2 of the strings in patterns appear as a substring in word.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> patterns = [&quot;a&quot;,&quot;a&quot;,&quot;a&quot;], word = &quot;ab&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> Each of the patterns appears as a substring in word &quot;<u>a</u>b&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= patterns.length &lt;= 100</code></li>
	<li><code>1 &lt;= patterns[i].length &lt;= 100</code></li>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>patterns[i]</code> and <code>word</code> consist of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

Traverse each string $p$ in the array $\textit{patterns}$ and check if it is a substring of $\textit{word}$. If it is, increment the answer by one.

After traversing, return the answer.

The time complexity is $O(n \times m)$, and the space complexity is $O(1)$. Here, $n$ and $m$ are the lengths of $\textit{patterns}$ and $\textit{word}$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)
```

#### Java

```java
class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int ans = 0;
        for (String p : patterns) {
            if (word.contains(p)) {
                ++ans;
            }
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int ans = 0;
        for (auto& p : patterns) {
            ans += word.find(p) != string::npos;
        }
        return ans;
    }
};
```

#### Go

```go
func numOfStrings(patterns []string, word string) (ans int) {
	for _, p := range patterns {
		if strings.Contains(word, p) {
			ans++
		}
	}
	return
}
```

#### TypeScript

```ts
function numOfStrings(patterns: string[], word: string): number {
    return patterns.filter(p => word.includes(p)).length;
}
```

#### Rust

```rust
impl Solution {
    pub fn num_of_strings(patterns: Vec<String>, word: String) -> i32 {
        patterns.iter().filter(|p| word.contains(&**p)).count() as i32
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
