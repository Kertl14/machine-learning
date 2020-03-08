from urllib.request import urlopen

def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    
    for line in story:
        line = line.decode('utf8')
        line_words = line.split()
        for word in line_words:
            story_words.append(word)
            
    story.close()
    
    for word in story_words:
        print(word)
        
if __name__ == '__main__':
    fetch_words()



    


