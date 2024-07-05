# Find Fivers

finds five-letter long words in a textfile given as input parameter (positional, first. default value: "lorem.txt", str). 
Word-length can also be given as 2nd parameter (positional parameter, second, default value: 5, int). 
Type "python -m findfivers -h" on the cli for help
The output is a text file, each word in a new line

## usage

both source filename and word-length can be given as parameter. However, there are default values for both.

### run with no parameters given

`python -m findvivers`
in this case the app is looking for the 'magyar-szavak.txt' in the directory where the script is run
(generally, the source file is always supposed to be in the project/script directory, where we initiate the app run)
and the word length is 5 - the app is searching for five-letter words. 

### run with parameters

`python -m findfivers lorem.txt`
there is a positional parameter, filename, which is the source file - the app expects a file named 'lorem.txt' to be found in the main/script directory

`python -m findfivers lorem.txt -l 9`
beside the source filename, a word-length parameter is given. This is an optional parameter. In this case the app will try to find nine-letter words in the lorem.txt file

`python -m findfivers -l 8`
using just the word-length parameter, the app will search the default file ('magyar-szavak.txt') for words of length specified (8 in this case)

## docker 

docker build -t fivers --rm .
docker build -t bajni37/fivers:0.4.0 --rm .
docker run -v ./:/app -v ./findfivers/data:/app/findfivers/data -it --rm --name fiveo fivers
docker run -v ./:/app -v ./findfivers/data:/app/findfivers/data -it --rm --name fiveo bajni37/fivers:0.4.0
