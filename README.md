## VIgenere SQuare GENerator

#### What is a Vigenere Square?

[The Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword. It is a form of polyalphabetic substitution.

#### What is VISQGEN?

visqgen is short for "Vigenere Square Generator". It is a command line tool written in Python that is designed to help create a Vigenere Square for the user.

#### How does it work?

The user is asked 3 questions. What values they want for the X-axis, what values they want for the Y-axis, and how much they want to shift the rows. Then visqgen builds the table for them. If the user wants the X-axis and the Y-axis to be the same with no shift at all, then they only need to enter in one set of values. Visqgen even allows the user to save their table into a .csv file to allow for easy importing to their spreadsheet program of choice for further table manipulation.

#### Short Examples

###### Example 1: Basic Table

`Please enter in the values you want on your X axis: abcdef`

`Please enter in the values you want on your Y axis (leave blank to input same values as X): <Enter>`

`How many places to the left do you want to initially shift the row? (leave blank for a default of 0): <Enter>`

Result:

||a|b|c|d|e|f|
|-|-|-|-|-|-|-|
|a|a|b|c|d|e|f|
|b|b|c|d|e|f|a|
|c|c|d|e|f|a|b|
|d|d|e|f|a|b|c|
|e|e|f|a|b|c|d|
|f|f|a|b|c|d|e|

###### Example 2: Basic Table with Shifting

`Please enter in the values you want on your X axis: abcdef`

`Please enter in the values you want on your Y axis (leave blank to input same values as X): <Enter>`

`How many places to the left you want to initially shift the row? (leave blank for a default of 0): 2`

Result:

| |a|b|c|d|e|f|
|-|-|-|-|-|-|-|
|a|c|d|e|f|a|b|
|b|d|e|f|a|b|c|
|c|e|f|a|b|c|d|
|d|f|a|b|c|d|e|
|e|a|b|c|d|e|f|
|f|b|c|d|e|f|a|

###### Example 3: Table with Special Characters

`Please enter in the values you want on your X axis: abc *!123`

`Please enter in the values you want on your Y axis (leave blank to input same values as X): <Enter>`

`How many places to the left do you want to initially shift the row? (leave blank for a default of 0): <Enter>`

| |a|b|c| |*|!|1|2|3|
|-|-|-|-|-|-|-|-|-|-|
|a|a|b|c| |*|!|1|2|3|
|b|b|c| |*|!|1|2|3|a|
|c|c| |*|!|1|2|3|a|b|
| | |*|!|1|2|3|a|b|c|
|*|*|!|1|2|3|a|b|c| |
|!|!|1|2|3|a|b|c| |*|
|1|1|2|3|a|b|c| |*|!|
|2|2|3|a|b|c| |*|!|1|
|3|3|a|b|c| |*|!|1|2|

#### Long Examples

There is no better way to learn how this program works than to just see the program in action. Since Vigenere squares can get quite large, the examples will be kept short, but hopefully with enough meat that you understand how the program works.

For this first example let us build a Vigenere square with the values of `abcdef` on the X-axis and the same values, `abcdef`, on the Y-axis.

Run the program and you will see the following prompt:

`Please enter in the values you want on your X axis:`

After this prompt we would enter into the keyboard `abcdef` as one string then press `<Enter>`

The next prompt is quite similar to the first one:

`Please enter in the values you want on your Y axis (leave blank to input same values as X):`

As we can see the prompt for the values that will go onto the Y-axis is identical to the prompt for the values on the X-axis. However, to save time from having to enter in identical values, if the user wants the X and Y axis to be the same, all they have to do is hit enter on this prompt and visqgen will copy the values of the X-axis to the Y-axis. Since that is what we are trying to accomplish in this example all we need to do is press `<Enter>`.

The last prompt is as follows:

`How many places to the left do you want to initially shift the row? (leave blank for a default of 0):`

We will cover shifting rows later on. For now all we need to do is press `<Enter>` and have our table built for us.

||a|b|c|d|e|f|
|-|--|-|-|-|-|-|
|a|a|b|c|d|e|f|
|b|b|c|d|e|f|a|
|c|c|d|e|f|a|b|
|d|d|e|f|a|b|c|
|e|e|f|a|b|c|d|
|f|f|a|b|c|d|e|

Voila! Just like that our table is built for us. Admittedly the table most likely won't look as good on your terminal screen as it does right here. Lucky our next prompt can help us out with that.

`Would you like to save this table in a .csv file? (y/n):`

This command line tool is helpful to build you a quick table, but for futher table manipulation, or more complex manipulation a spreadsheet program is better suited for the job. The easiest way to get the table you just made to the spreadsheet program of your choice is with a .csv file. Lets download our table into a .csv file by pressing `y`.

`Enter the name you want to save the file as (if blank it will be saved as 'visqgen-YYYY-MM-DD-HH:MM:SS.csv'):`

After pressing `y` the next prompt gives you the chance to name the file whatever you would like. If you have a certain name in mind all you need to do is enter it in. If you are in a hurry, or don't care what the name is, visqgen will name the file for you. Press `<Enter>`.

Just like that a .czv file with your table was saved into the current directory you are in.

`Would you like to create another table? (y/n):`

The last prompt asks if you would like to go again. If you press `y` you will go through the exact same process and be able to create another table. If you wish to stop simply press `n` and the program will terminate.

#### Shifting rows

For creation of more advanced tables a user might which to shift rows over. Visqgen allows users to do this. When asked how many rows visqgen should shift over in the third prompt, simply enter in how many are desired and it will move them over to the left that amount. For a visual see Example 2 under the Short Example section.

#### Installing

###### Native Python

If you already have Python on your machine, all you need to do is download the visqgen.py file. Visqgen uses the standard Python library so no additional requirements are needed. The only requirement is python3.6 or greater.

###### Docker

To avoid confliction with depednencies and for maximum cross platform support, Docker is the best way to go. In this project is a Dockerfile that will get you up and running as soon as possible

###### Docker: Linux
