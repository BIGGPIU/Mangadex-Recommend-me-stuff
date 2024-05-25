import requests
from time import sleep
from collections import Counter
import random
import wget
import os
#NOTE the manga link is formatted like this: 
#mangadex.org/title/ID
#when I think about it why is #NOTE blue 



def maincall(USERNAME,PASSWORD,API,SECRET):
    permgenre = []
    permmanga = []

    creds = {
        "grant_type": "password",
        "username": f"{USERNAME}",
        "password": f"{PASSWORD}",
        "client_id": f"{API}",
        "client_secret": f"{SECRET}"
    }

    request1 = requests.post(
        "https://auth.mangadex.org/realms/mangadex/protocol/openid-connect/token",
        data=creds
    )
    r1_json = request1.json()

    access_token = r1_json["access_token"]
    refresh_token = r1_json["refresh_token"]

    #print(f"\n{access_token}\n")

    if (request1.status_code) == 200:
        ##print (f"\n HTTP Response: {request1.status_code}\n")
        pass
    
 #heyy me in the future make sure you make it toggleable to get reccs based on what you dont have in your completed folder
    request1 = requests.get( 
        "https://api.mangadex.org/manga/status", headers= {
            "accept":'application/json',
            "Authorization":f"Bearer {access_token}"
        }        
        )
    readingstatus = str(request1.json())
    readingstatus = readingstatus.replace("'reading'","")
    readingstatus = readingstatus.replace("'completed'","")
    readingstatus = readingstatus.replace("'plan_to_read'","")
    readingstatus = readingstatus.replace("'re_reading'","")
    readingstatus = readingstatus.replace("'dropped'", "")
    readingstatus = readingstatus.replace("'on_hold'","")
    readingstatus = strip(readingstatus)
    readingstatus = readingstatus.replace(":","")
    readingstatus = readingstatus.replace(" ","")
    if "result ok" in readingstatus:
        ##print ("\nALL GOOD!\n")
        pass
    readingstatus = readingstatus.split(",")
    readingstatus.pop(1)
    readingstatus.pop(0)
    i = 0
    while i != len(readingstatus):
        ##print(readingstatus[i])
        
        i += 1
    if i == len(readingstatus):
        ##print (f"\nTotal: {i}\n")
        pass

    i = 0
    
    while i != len(readingstatus):
        #print (f"Fetching item {i+1}/{len(readingstatus)}")
        #sleep(1)
        hold = str(readingstatus[i])

        request2 = requests.get(
            f"https://api.mangadex.org/manga/{hold}?includes%5B%5D=", headers= {
                "accept":"application/json"
            }
        )
        supertemp = (request2.json())
        temp = str(request2.json())
        hold3 = str(supertemp["data"]["attributes"]["tags"])
        hold3 = hold3.split("{")
        ii=0
        while ii != len(hold3):
            if "'en':" in hold3[ii]:
                ii+=1
            else:
                hold3.remove(hold3[ii])
        ii=0
        genres = []
        iii=0
        while iii != len(hold3):
            hold4 = hold3[iii]
            hold4 = strip(hold4)
            hold4 = hold4.replace(": ","")
            hold4 = hold4.replace("en","")
            hold4 = hold4.replace(", description","")
            if hold4 == "Alis":
                hold4 = "Aliens"
            if hold4 == "Advture":
                hold4 = "Adventure"
            if hold4 == "Gderswap":
                hold4 = "Genderswap"
            if hold4 == "Delinquts":
                hold4 = "Delinquents"
            if hold4 == "Sexual Violce":
                hold4 = "Sexual Violence"
            genres.append(hold4)
            iii+=1
            
        #print (f"\n{genres}")   
        temp = strip(temp)
        #print (temp)
        temp = temp.split(",")

        temp2 = (temp[4])
        temp2 = temp2.replace("attributes: title: en: ","")
        #print(hold2)

        permmanga.append(temp2)
        permgenre.append(genres)
        ##print (temp2)
        i+=1
    
    return permgenre, permmanga


def getmostpopular(USERNAME,PASSWORD,API,SECRET):
    permgenre = str(maincall(USERNAME,PASSWORD,API,SECRET))
    permgenre = permgenre.replace("[","")
    permgenre = permgenre.replace("]","")
    permgenre = permgenre.replace("'","")
    permgenre = permgenre.replace('"',"")
    permgenre = permgenre.replace("\n","")
    permgenrelist = permgenre.split(",")
    genredict = Counter(permgenrelist)
    mostpopular = sorted(genredict, key=genredict.get, reverse=True)[:5]
    i = 0
    while i != 5:
        hold = mostpopular[i]
        mostpopular[i] = hold.replace(" ","",1)
        i+=1
    return mostpopular #this is a list


def searchformanga(USERNAME,PASSWORD,API,SECRET):
    order = {
    "rating": "desc"}
    included_tag_names = getmostpopular(USERNAME,PASSWORD,API,SECRET) #I'm just straight stealing this from the mangadex documentation I see no reason to do otherwise
    #print (included_tag_names)
    base_url = "https://api.mangadex.org"
    tags = requests.get(
    f"{base_url}/manga/tag"
    ).json()

    # ["391b0423-d847-456f-aff0-8b0cfc03066b", "423e2eae-a7a2-4a8b-ac03-a8351462d71d"]
    included_tag_ids = [
        tag["id"]
        for tag in tags["data"]
        if tag["attributes"]["name"]["en"]
        in included_tag_names
    ]
    ##print (included_tag_ids)
    r = requests.get(
    f"{base_url}/manga",
    params={
        "includedTags[]": included_tag_ids,
        },
    )

    #print([manga["id"] for manga in r.json()["data"]])
    idforlinks = ([manga["id"] for manga in r.json()["data"]]) #this is a list
    nameforlinks = [] #this will be in the same order as idforlinks

    try:
        prune("website version\static\styles",".png")
    except:
        pass
    try:
        prune("website version\static\styles",".jpg")
    except:
        pass

    i=0
    while i != len(idforlinks):
        hold = idforlinks[i]
        if i == 0:
            request2 = requests.get(
                    f"https://api.mangadex.org/manga/{hold}?includes%5B%5D=cover_art", headers= {
                        "accept":"application/json"
                    }
                )
            holdddd = (request2.json())
            z = 0
            while True:
                try:
                    cover = (holdddd["data"]["relationships"][z]["attributes"]["fileName"])
                    coverpath = downloadcover(idforlinks[0],cover)
                    break
                except:
                    z +=1
        else:
            request2 = requests.get(
                    f"https://api.mangadex.org/manga/{hold}?includes%5B%5D=", headers= {
                        "accept":"application/json"
                    }
                )
        supertemp = (request2.json())
        x = 0
        y = 1
        reasonablelangs = ["en","jp","ko"] #this also functions as a priority list for names. prioritizing english names over jp names and jp names over ko names

        while y != 0:
            try:
                hold2 = str(supertemp["data"]["attributes"]["title"][f"{reasonablelangs[x]}"])
                y = 0         
                #print (hold2)
            except:
                x+=1
                if x == 3:
                    hold2 = "NAME ERROR"

        nameforlinks.append(hold2)   


        if i == 0:
            pass   
            
        i +=1
    return idforlinks, nameforlinks



def downloadcover(ID,link) -> str:
    url = f"https://mangadex.org/covers/{ID}/{link}"
    #print (url)
    if ".png" in url:
        end = ".png"
    else:
        end = ".jpg"
    response = wget.download(url,out=f"website version\static\styles\\cover{end}")

    path = f"{ID}{end}"
    return path

def prune(PATH,extension):
    hold = os.listdir(PATH)
    i=0
    while i != len(hold):
        if extension in hold[i]:
            os.remove(f"{PATH}/{hold[i]}")
            i+=1
        else:
            i+=1

    pass

def strip(string):
    string = string.replace("{","")
    string = string.replace("}","")
    string = string.replace("'","")
    return string

if __name__ == "__main__":
    searchformanga()