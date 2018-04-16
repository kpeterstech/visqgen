## VIgenere SQuare GENerator


### Table of Contents
1. [What is a Vigenere Square](#whatis)
2. [What is VISQGEN?](# What is VISQGEN)
3. [How does it work?](# How does it work?)
4. [Short Examples](# Short Examples)

  a. [Example 1: Basic Table](# Example 1: Basic Table)

  b. [Example 2: Basic Table with Shifting](######Example 2: Basic Table with Shifting)

  c. [Eample 3: Table with Special Characters](###### Example 3: Table with Special Characters)

5. [Long Example](#### Long Example)

6. [Shifting Rows](#### Shifting Rows)

7. [Installing](#### Installing)

  a. [Native Python](###### Native Python)

  b. [Docker](###### Docker)

  c. [Docker: Linux](###### Docker: Linux)

  d. [Docker: Windows](###### Docker: Windows)



#### What is a Vigenere Square? <a name="whatis"></a>

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

#### Long Example

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

Just like that a .csv file with your table was saved into the current directory you are in. Go ahead and import to the spreadsheet program of your choice.

`Would you like to create another table? (y/n):`

The last prompt asks if you would like to go again. If you press `y` you will go through the exact same process and be able to create another table. If you wish to stop simply press `n` and the program will terminate.

#### Shifting Rows

For creation of more advanced tables a user might which to shift rows over. Visqgen allows users to do this. When asked how many rows visqgen should shift over in the third prompt, simply enter in how many are desired and it will move them over to the left that amount. For a visual see Example 2 under the Short Example section.

#### Installing

###### Native Python

If you already have Python on your machine, all you need to do is download the visqgen.py file. Visqgen uses the standard Python library so no additional requirements are needed. The only requirement is python3.6 or greater.

###### Docker

To avoid confliction with depednencies and to maximize cross platform support, Docker is the best way to go. In this project is a Dockerfile that will get you up and running as soon as possible

###### Docker: Linux

First you need to install docker. These steps will be for Ubuntu 16.04. If you are not using a distro that is within the Ubuntu family then some changes might need to be made.

1) First, add the GPG key for the official Docker repository to the system:

`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

2) Add the Docker repository to APT sources:

`sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`

3) Update

`sudo apt-get update`

4) Install Docker-ce

`sudo apt-get install -y docker-ce`


Once Docker is installed navigate to the directory you wish to save visqgen and either clone it with git or download the zip file

Clone:

`git clone https://github.com/kpeterstech/visqgen.git`

Zip:

`wget 'https://github.com/kpeterstech/visqgen/archive/master.zip'`

`unzip -x master.zip`

`cd visqgen-master`

Once inside insure that visqgen.py has execute privileges with `chmod +x visqgen.py`

Make sure that the visqgen image is built with:

`docker build -t visqgen .`

To run visqgen with docker run the following command from you shell

`docker run -it --rm -v "$PWD":/app:rw visqgen`

###### Docker: Windows

To install Docker on Windows first download the "Docker for Windows.exe". Official step by step instructions can be found at [the docker website](https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows). If you wish to download the .exe directly copy and paste the following link in your browser.

`https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe`

Once the .exe is downloaded install docker by double clicking on it and follow the install wizard.

Once installation is complete open up either Command Prompt or Powershell and run `docker --version` to make sure docker was installed correctly. If docker has installed correctly you should see output similar to `> Docker version 18.03.0-ce, build 0520e24`

If docker was installed correctly, download visqgen by clicking on the green button on the top of this page that says "Clone or download". After clicking on the button select download zip.

Extract the .zip. You should see a folder named `visqgen-master`. Make sure this folder is in your `Downloads` folder. Once you make sure it is placed there run the following command in Command prompt. Make sure to replace `<username>` with your username.

`cd C:\Users\<username>\Downloads\visqgen-master`

Once there run

`docker build -t visqgen .`

Then

`docker run -it --rm -v C:\Users\<username>\Downloads\visqgen-master:/app:rw visqgen`

You should now be using visqgen.
