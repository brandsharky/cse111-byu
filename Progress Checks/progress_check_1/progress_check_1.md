# Playlist Stats

## Overview

Your goal is to write a Python program that analyzes a playlist of songs based
on various factors. The program will read a CSV file containing song data and
perform several calculations to provide insights about the playlist. You will
then print these insights to the console.

### Sample Execution

```text
% python3 playlist_stats.py
Enter the filename of the playlist in .csv format: test_files/playlist1.csv
The playlist has 40 songs.
The first song is Concerning Hobbits by Howard Shore.
The last song is Bring Him Home by Colm Wilkinson.
Overture to Candide was played the most times at 33 plays.
The playlist is 3:12:05 long.
```

### Input

The playlist will always be input as a CSV file with the following columns:

```text
Title,Artist,Album,Duration,Genre,Plays
```

For example,

```text
Baba Yetu,Christopher Tin,Calling All Dawns,3:30,Classical,26
```

## Rubric

| Grade Level   | Required standards                                                                                                                                                                                                                                |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Core**      | - Program prompts user for the playlist file<br/>- Number of songs in the playlist is correctly calculated and displayed<br/>- The first and last songs in the playlist are correctly displayed                                                   |
| **Advanced**  | - Most popular song is correctly displayed<br/>- Variable names are clear, informative, and match the course naming conventions<br/>- There is no unused code                                                                                     |
| **Excellent** | - Code correctly calculates and displays the playlist duration<br/>- Code is broken down into functions with no large sections of duplicate code<br/>- Code is easy to read<br/>- Code meets all course code quality standards outlined on Canvas |

## Tasks

### Task 1: Playlist Length

Count the number of songs in the playlist.

Your output for this task should be written in one line:

```text
The playlist has 38 songs.
```

### Task 2: Display Song Titles and Artists

After reading the CSV file, print the title and artist of the first and last
songs in the playlist.

Your output for this task should be written in two lines, with the first line
showing the first song and the second line showing the last song:

```text
The first song is Zoltraak by Evan Call.
The last song is You Can Call Me Al by Paul Simon.
```

### Task 3: Most Popular Song

Find the song that has been played the most times. If there is a tie, return the
**first song** in the list with that play count. The song title and number of
plays should both be output:

```text
Defying Gravity was played the most times at 31 plays.
```

### Task 4: Playlist Duration

Calculate the total length of the playlist in hours, minutes, and seconds (e.g.
`3:05:56` for 3 hours, 5 minutes, and 56 seconds).

Your output for this task should be written in one line:

```text
The playlist is 3:05:56 long.
```

## Testing Your Code

You can test your code and run all the pytests by running one of these two
commands in your terminal:

```sh
python3 -m pytest -vv .
```

or

```sh
python -m pytest -vv .
```

To test just a specific tier, you can add one of the following flags to the
above commands:

- **Core**: `-m "tier(tier_name='Core')"`
- **Advanced**: `-m "tier(tier_name='Advanced')"`
- **Excellent**: `-m "tier(tier_name='Excellent')"`

## Feeling Stuck?

Here are a few hints to help you during this progress check:

- How to open a file for reading (option 1): `with open(<filename>, "r") as <variable name>:`
- How to open a file for reading (option 2): `<variable name> = open(<filename>, "r")`, close with `<variable name>.close()`
- How to change a string to an integer: `int(<number as a string>)`

## Turn In Your Work

Submit your `playlist_stats.py` file to Gradescope through Canvas.
