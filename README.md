# Markdown Table of Contents

A simple Python script that makes a table of contents for a markdown file. A simple usage would be making a table of contents for your GitHub 
wiki page! 

In your *.md file (or whatever text file), have your markdown in that file. Then, make the first line the URL of the page. That way, the 
Python program can properly append the fragment. 

To use it, simply have the Python script and the fileName.md file in the same directory. Use the function defined in markdowntoc.py and a TOC_fileName.md file will 
be created. That's your table of contents! 

Note that currently it's very specific to my own github wikis, so I have yet to generalize the code to work on most other markdown pages. 
