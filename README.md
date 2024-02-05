# Project FAST
**Field Artillery Safety Trainer**\
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
I am now developing this through a Docker Compose which you can find in the repository. I changed the names in Django for some added clarity. My next steps will be expanding the Django code for some added User functionality within the API and then interacting with the API through the React front end which up to this point has not been touched.

 