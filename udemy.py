
if __name__ == "__main__":

    import requests
    from bs4 import BeautifulSoup

    Udemy_HomePage = BeautifulSoup(requests.get("https://www.udemy.com/").text, features = "lxml")
    Text           = Udemy_HomePage.get_text()

    if 'through' in Text:
        start = Text.find('through') - 23
        end = Text[start:].find('.')
        print(Text[start : start+end])
    
    else:
        print("No Udemy sale right now.")    
    
    
    

    
