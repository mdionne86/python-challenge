# python-challenge

Please note, both scripts contain a reference to a csv file stored in a respective subdirectory "Resources" and writes the txt file to a respective subdirectory "analysis". Please ensure these are properly set before running the script.

# PyBank
This is relatively straight forward.

# PyPoll
This was difficult.

I initially had used set() to find and store a second list of just the unique names of candidates, then appended the unique list with counts from the big list. This returned the correct answers, however, I had noted that this approach lacked  procedurally generated variables, meaning that if you tried to run this script on a list with more than 4 candidates it would have omitted any candidates above 4. Back to the drawing board. I then tried for a long time to count them in the primary list + append the unique list with the counts. After a while I stumbled on Counter, and once I turned it into a dictionary it was extremely easy to perform the neccesary calculations. 