# Wordle Solver
### About: 
Wordle Solver allows one to mindlessly win wordle :-)

(in hard mode!!)

Uses weighted random choices. Vowels and non-repeating letters are favored.
### Usage:
To use, run  `python3 .\main.py`

At each round, you will be asked to input the result of the guess. Use the following legend:

| Symbol | Color  | Meaning                            |
|--------|--------|------------------------------------|
| `_`    | Grey   | Incorrect letter                   |
| `*`    | Yellow | Correct letter, incorrect location |
| `a-z`  | Greeen | Correct letter and location        |
#### Example: For this example, say the correct wordle answer is `rocky`. Upon entering the guess `wormy`, you would enter the input: `_o*_y`.

### Options:
The following flag(s) are available:

|    | Argument | Default | Note                                                                |
|----|----------|---------|---------------------------------------------------------------------|
| `-i` | `--init`   | `''`      | When value is not set, a randomized starting word will be selected. |

### Success Rate:
    Win: 97%

#### Breakdown
| Guesses | Occurence |
|---------|-----------|
| 1       | 0         |
| 2       | 0         |
| 3       | 9         |
| 4       | 14        |
| 5       | 8         |
| 6       | 3         |

Win frequency can be increased by starting with "optimal" words. Use `-i` to start with your favorite Wordle starting word.

### Drawbacks:
- Words in wordlist may not be comprehensive.
- Words in wordlist may include words that are not deemed "words" by wordle.