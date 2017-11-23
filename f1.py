import os
from gtts import gTTS

#Downloading the RSS
os.system("del \"rss.xml@edition=uk\"")
os.system("del speech.mp3")

os.system("wget64.exe http://feeds.bbci.co.uk/sport/formula1/rss.xml?edition=uk")
print("State: Downloading the RSS feed.")

#Modifying the file
def cleanFile(fileName):
    print("State: Start cleaning file.")
    f = open(fileName,'r+')
    lines = f.readlines()
    newLines = []
    newLines2 = []
    megaString = ''
    for i in lines:
        if("<title>" in i):
            newLines.append(str.strip(i)[16:])
        if("<description>" in i):
            newLines.append(str.strip(i)[22:])
    for j in newLines:
        if ("</title>" in j):
            newLines2.append(j.strip("]]></title>"))
        if ("</description>" in j):
            newLines2.append(j.strip("]]></description>"))
    newLines2.pop(0)
    newLines2.pop(0)
    newLines2.pop(0)
    for k in newLines2:
        megaString += k
        megaString += ": "
    print("State: Finish cleaning file.")
    return(megaString)

def textToSpeech(string):
#Using the text to speech engine and playing the file
    language = "en"
    print("State: Sending data to gTTS.")
    machine = gTTS(text=string,lang=language,slow=False)
    machine.save("speech.mp3")
    print("State: Finished downloading speech file, playing.")
    os.system("start speech.mp3")

if __name__=="__main__":
    megaString = cleanFile("rss.xml@edition=uk")
    textToSpeech(megaString)

