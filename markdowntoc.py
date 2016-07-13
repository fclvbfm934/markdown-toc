def createtoc(fileName, *ignore):
    """createtoc(fileName, ignore) -> None
    Creates a file that has a markdown of a Table Of Contents
    ignores the ignore headers"""

    wikiFile = open(fileName, 'r')
    tocFile = open("TOC_" + fileName, 'w')
    
    tocFile.write("##Table of Contents\n\n") #Creates the heading for the TOC
    
    url = wikiFile.readline().strip() #the url should be at the top of the file 
    for line in wikiFile:
        numHashtags = 0 #this variable counts the number of "#" symbols 
        while(line[numHashtags] == "#"):
            numHashtags += 1
            
        if(numHashtags > 0 and line[numHashtags:].strip().lower() not in ignore):
            dashes = "" #only takes digits and letters, and puts a - for a space
            for char in line[numHashtags:].strip(): # we don't want the last \n character
                if(char == " "):
                    dashes += "-"
                elif char.isalpha():
                    dashes += char.lower()
                elif char.isdigit():
                    dashes += char.lower()
            stuffToWrite = "* [" + line[numHashtags:].strip() + "](" + url + "#" + dashes + ")\n"
            
            #This part here is temporary. It was used for my own purposes so that it would sequence properly
            if numHashtags == 4:
                numHashtags -= 1
            #Adds the proper spacing for indentation
            for i in range(numHashtags - 1):
                stuffToWrite = "    " + stuffToWrite
            stuffToWrite += "\n"
            tocFile.write(stuffToWrite)


