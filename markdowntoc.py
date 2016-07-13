def createtoc(fileName, *ignore):
    """createtoc(fileName, ignore) -> None
    Creates a file that has a markdown of a Table Of Contents
    ignores the ignore headers"""
    #print(ignore)
    wikiFile = open(fileName, 'r')
    tocFile = open("TOC_" + fileName, 'w')
    
    tocFile.write("##Table of Contents\n\n")
    
    url = wikiFile.readline().strip() #the url should be at the top of the file 
    for line in wikiFile:
        numHashtags = 0
        while(line[numHashtags] == "#"):
            numHashtags += 1
        if(numHashtags > 0 and line[numHashtags:].strip().lower() not in ignore):
            dashes = ""
            for char in line[numHashtags:].strip():
                if(char == " "):
                    dashes += "-"
                elif char.isalpha():
                    dashes += char.lower()
                elif char.isdigit():
                    dashes += char.lower()
            stuffToWrite = "* [" + line[numHashtags:].strip() + "](" + url + "#" + dashes + ")\n"
            if numHashtags == 4:
                numHashtags -= 1
            for i in range(numHashtags - 1):
                stuffToWrite = "    " + stuffToWrite
            stuffToWrite += "\n"
            tocFile.write(stuffToWrite)


            
createtoc("Polynomial.md", "parameters", "returns")