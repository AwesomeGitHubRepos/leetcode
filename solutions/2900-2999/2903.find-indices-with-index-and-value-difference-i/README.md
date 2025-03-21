---
comments: true
difficulty: Easy
rating: 1157
source: Weekly Contest 367 Q1
tags:
    - Array
    - Two Pointers
---

<!-- problem:start -->

# [2903. Find Indices With Index and Value Difference I](https://leetcode.com/problems/find-indices-with-index-and-value-difference-i)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> having length <code>n</code>, an integer <code>indexDifference</code>, and an integer <code>valueDifference</code>.</p>

<p>Your task is to find <strong>two</strong> indices <code>i</code> and <code>j</code>, both in the range <code>[0, n - 1]</code>, that satisfy the following conditions:</p>

<ul>
	<li><code>abs(i - j) &gt;= indexDifference</code>, and</li>
	<li><code>abs(nums[i] - nums[j]) &gt;= valueDifference</code></li>
</ul>

<p>Return <em>an integer array</em> <code>answer</code>, <em>where</em> <code>answer = [i, j]</code> <em>if there are two such indices</em>, <em>and</em> <code>answer = [-1, -1]</code> <em>otherwise</em>. If there are multiple choices for the two indices, return <em>any of them</em>.</p>

<p><strong>Note:</strong> <code>i</code> and <code>j</code> may be <strong>equal</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
<strong>Output:</strong> [0,3]
<strong>Explanation:</strong> In this example, i = 0 and j = 3 can be selected.
abs(0 - 3) &gt;= 2 and abs(nums[0] - nums[3]) &gt;= 4.
Hence, a valid answer is [0,3].
[3,0] is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1], indexDifference = 0, valueDifference = 0
<strong>Output:</strong> [0,0]
<strong>Explanation:</strong> In this example, i = 0 and j = 0 can be selected.
abs(0 - 0) &gt;= 0 and abs(nums[0] - nums[0]) &gt;= 0.
Hence, a valid answer is [0,0].
Other valid answers are [0,1], [1,0], and [1,1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3], indexDifference = 2, valueDifference = 4
<strong>Output:</strong> [-1,-1]
<strong>Explanation:</strong> In this example, it can be shown that it is impossible to find two indices that satisfy both conditions.
Hence, [-1,-1] is returned.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>0 &lt;= indexDifference &lt;= 100</code></li>
	<li><code>0 &lt;= valueDifference &lt;= 50</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers + Maintaining Maximum and Minimum Values

We use two pointers $i$ and $j$ to maintain a sliding window with a gap of $indexDifference$, where $j$ and $i$ point to the left and right boundaries of the window, respectively. Initially, $i$ points to $indexDifference$, and $j` points to $0$.

We use $mi$ and $mx$ to maintain the indices of the minimum and maximum values to the left of pointer $j$.

When pointer $i$ moves to the right, we need to update $mi$ and $mx$. If $nums[j] \lt nums[mi]$, then $mi$ is updated to $j$; if $nums[j] \gt nums[mx]$, then $mx$ is updated to $j$. After updating $mi$ and $mx$, we can determine whether we have found a pair of indices that satisfy the condition. If $nums[i] - nums[mi] \ge valueDifference$, then we have found a pair of indices $[mi, i]$ that satisfy the condition; if $nums[mx] - nums[i] >= valueDifference$, then we have found a pair of indices $[mx, i]$ that satisfy the condition.

If pointer $i$ moves to the end of the array and we have not found a pair of indices that satisfy the condition, we return $[-1, -1]$.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int
    ) -> List[int]:
        mi = mx = 0
        for i in range(indexDifference, len(nums)):
            j = i - indexDifference
            if nums[j] < nums[mi]:
                mi = j
            if nums[j] > nums[mx]:
                mx = j
            if nums[i] - nums[mi] >= valueDifference:
                return [mi, i]
            if nums[mx] - nums[i] >= valueDifference:
                return [mx, i]
        return [-1, -1]
```

#### Java

```java
class Solution {
    public int[] findIndices(int[] nums, int indexDifference, int valueDifference) {
        int mi = 0;
        int mx = 0;
        for (int i = indexDifference; i < nums.length; ++i) {
            int j = i - indexDifference;
            if (nums[j] < nums[mi]) {
                mi = j;
            }
            if (nums[j] > nums[mx]) {
                mx = j;
            }
            if (nums[i] - nums[mi] >= valueDifference) {
                return new int[] {mi, i};
            }
            if (nums[mx] - nums[i] >= valueDifference) {
                return new int[] {mx, i};
            }
        }
        return new int[] {-1, -1};
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<int> findIndices(vector<int>& nums, int indexDifference, int valueDifference) {
        int mi = 0, mx = 0;
        for (int i = indexDifference; i < nums.size(); ++i) {
            int j = i - indexDifference;
            if (nums[j] < nums[mi]) {
                mi = j;
            }
            if (nums[j] > nums[mx]) {
                mx = j;
            }
            if (nums[i] - nums[mi] >= valueDifference) {
                return {mi, i};
            }
            if (nums[mx] - nums[i] >= valueDifference) {
                return {mx, i};
            }
        }
        return {-1, -1};
    }
};
```

#### Go

```go
func findIndices(nums []int, indexDifference int, valueDifference int) []int {
	mi, mx := 0, 0
	for i := indexDifference; i < len(nums); i++ {
		j := i - indexDifference
		if nums[j] < nums[mi] {
			mi = j
		}
		if nums[j] > nums[mx] {
			mx = j
		}
		if nums[i]-nums[mi] >= valueDifference {
			return []int{mi, i}
		}
		if nums[mx]-nums[i] >= valueDifference {
			return []int{mx, i}
		}
	}
	return []int{-1, -1}
}
```

#### TypeScript

```ts
function findIndices(nums: number[], indexDifference: number, valueDifference: number): number[] {
    let [mi, mx] = [0, 0];
    for (let i = indexDifference; i < nums.length; ++i) {
        const j = i - indexDifference;
        if (nums[j] < nums[mi]) {
            mi = j;
        }
        if (nums[j] > nums[mx]) {
            mx = j;
        }
        if (nums[i] - nums[mi] >= valueDifference) {
            return [mi, i];
        }
        if (nums[mx] - nums[i] >= valueDifference) {
            return [mx, i];
        }
    }
    return [-1, -1];
}
```

#### Rust

```rust
impl Solution {
    pub fn find_indices(nums: Vec<i32>, index_difference: i32, value_difference: i32) -> Vec<i32> {
        let index_difference = index_difference as usize;
        let mut mi = 0;
        let mut mx = 0;

        for i in index_difference..nums.len() {
            let j = i - index_difference;

            if nums[j] < nums[mi] {
                mi = j;
            }

            if nums[j] > nums[mx] {
                mx = j;
            }

            if nums[i] - nums[mi] >= value_difference {
                return vec![mi as i32, i as i32];
            }

            if nums[mx] - nums[i] >= value_difference {
                return vec![mx as i32, i as i32];
            }
        }

        vec![-1, -1]
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
