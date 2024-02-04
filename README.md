# Project FAST
**Field Artillery Safety Trainer**
*A web application that provides a testing/practice suite for manual artillery gunnery*


## Overview
One of the most formative experiences of a young artilleryman's career is completing the manual gunnery
unit during Field Artillery Basic Officer Leader's Course. This unit culminates in the dreaded "safety test"; a measure of whether or not you have a deep enough understanding of artillery to safely operate in a Fire Direction Center (FDC) or on the gunline.

These tests are verified by hand or in some cases through sophisticated excel workbooks that double check the the calculations made. However, this limits the amount of practice students may get since they are limited to those released by their instructors and the creation of the exams and study materials is a time consuming process.

What if students were able to login to a website, select what type of safety problems they would like to practice
and have example safety worksheets generated for them to complete. What if instructors could login and generate
safety exams for students to practice and view their performance immediately.

My aim in developing this web application is to assist instructors at the US Army Field Artillery School (USAFAS) instruct and evaluate gunnery,
assist Master Gunners (MGs) throughout the force teach, practice, and evaluate Soldiers during recertification and assist in improving the
technical competence of the Field Artillery branch.\

KING OF BATTLE!

## Project Structure

The project has three main folders.

django - This folder contains the relevant files for the django backend. It looks like a normal django project in this folder

react - This folder contains the relevant files for the react frontend. It looks like a normal react app within this folder

etc - This folder contains anything not in the first two folders, mostly admin files. I originally created a technical design doc for some practice but I don't think it's particularly necessary for this project and project overhead sucks the fun out of development, so it's just coding from now on.

## Updates 
 I spent some time putting more research into setting this project up the right way and want to make note of my next steps here. I am going to use Django with Django-Rest-Framework to interact with the react frontend and send requests with Axios. My first effort will be implementing users and a registration/login since that won't be much technical challenge on the Django side and will let me experiment with React and Axios to call the API.

I created working Dockerfiles and a docker-compose for the react and django apps so they can be run all at once.

 