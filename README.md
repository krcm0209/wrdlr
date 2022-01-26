# WRDLR

## Usage

```bash
python wrdlr.py
```

The script will ask you to enter the result of each round. The result should be provided in the following format:

` , , , , `

Gray boxes should be entered as periods. For example, if you didn't get any hints or correct letters in a round, you would enter:

`., ., ., ., .`

Hints (yellow boxes) should be entered with a question mark. For example, if you didn't get any correct letters, but got a hint of the letter 'a' in the 4th position:

`., ., ., a?, .`

Correct letters should be entered as they appear. For example, if you entered `BRICK` but only the last three letters were correct, and there were no hints:

`., ., i, c, k`

## Example

```bash
python wrdlr.py
Enter the result of round 1: a?, ., r, ., .
Try "harps"
Enter the result of round 2: ., a?, r, ., s?
Try "scram"
Enter the result of round 3: s, c, r, a, .
Try "scrap"
```
