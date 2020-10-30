Given an array of integers, find if the array contains any duplicates.

 1. Your output should print `true` if any value appears at least twice in the array.
 2. The output should return `false` if every element appears once.

 Example 1:

    Input: [4,5,4,3]
    Output: true

 Example 2:

    Input: [2,9,0,4]
    Output: false

###Extra credit 1:
    There may be instances where the number appears the same more than 2 times. In this situation your output should return `a number appears more than twice`

Example 3:

Input: [1,3,8,3,3,4,3,2,5,2]
Output: true

###Extra credit 2:
    There may be instances where the number appears the sae more than 2 times and also appears has a different set of numbers appearing only twice. In this situation your output should return:
    `{specificNumber} appears more than twice`
    `{specificNumber} appearstwice`
Where specifc number is the specific number.

Example 4:

Input: [1,3,8,3,3,4,3,2,4,2]
Output:
    3 appears more than twice.
    4 appears twice.
    2 appears twice.
