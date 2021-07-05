
if __name__ == "__main__":

    import requests
    from bs4 import BeautifulSoup

    Udemy_HomePage = BeautifulSoup(requests.get("https://www.udemy.com/").text, features = "lxml")
    Text           = Udemy_HomePage.get_text()

    if 'through' in Text:
        start = Text.find('through') - 23
        end = Text[start:].find('.')
        print(Text[start : start+end])
        option = input(" Shall I open the Udemy site for you? (y/n): ")

        if option == "y":
            webbrowser.open("https://www.udemy.com/")
        else:
            pass

    else:
        print("No Udemy sale right now.")       
