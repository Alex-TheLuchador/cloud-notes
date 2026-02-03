# Return Mismatched Words

This is an exercise provided by Meta as part of their hiring preparation.

## Summary
Given an input of two strings consisting of english letters (a-z; A-Z) and spaces, complete a function that returns a list containing all the mismatched words (case sensitive) between them.

You can assume that a word is a group of characters delimited by spaces.

A mismatched word is a word that is only in one string but not the other.

Add mismatched words from the first string before you add mismatched words from the second string in the output array.

<strong>Signature</strong>

```
static String[] returnMismatched(String str1, String str2)
```

<strong>Input</strong>
- str1: a string
- str2: a string
- <strong>Note:</strong> You can only expect valid english letters (a-z; A-Z) and spaces.

<strong>Output</strong>

An array containing all words that do not match between str1 and str2.

<strong>Examples</strong>

```
str1: "Firstly this is the first string"

str2: "Next is the second string"

output: ["Firstly", "this", "first", "Next", "second"]
```
```
str1: ""

str2: ""

output: []
```
```
str1: ""
str2: "This is the second string"
output: ["This","is","the","second","string"]
```
```
str1: "This is the first string" 
str2: "This is the second string" 
output: ["first", "second"]
```
```
str1: "This is the first string extra" 
str2: "This is the second string" 
output: ["first", "extra", "second"]
```
```
str1: "This is the first text" 
str2: "This is the second string" 
output: ["first", "text", "second", "string"]
```