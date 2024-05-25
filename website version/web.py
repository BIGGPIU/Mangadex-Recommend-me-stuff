

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
from mainbackend import searchformanga
import webbrowser
 

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/recommend', methods=["GET"])
def helloworld():
    if request.method == "GET":
        if request.args.get("Password") == None:
            return render_template("tempfirstUI.html")
        

        elif(request.args.get("Username") == ""):
            return "<html><body> <h1> put in a Username loser</h1></body></html>"
        elif(request.args.get("Password") == ""):
            return render_template("reccstemp.html",name0="One piece",name1="One piece",name2="One piece",name3="One piece",name4="One piece",name5="One piece",name6="One piece",name7="One piece",name8="One piece",name9="One piece"
                                   ,id0="a2c1d849-af05-4bbc-b2a7-866ebb10331f",id1="a2c1d849-af05-4bbc-b2a7-866ebb10331f",id2="a2c1d849-af05-4bbc-b2a7-866ebb10331f",id3="a2c1d849-af05-4bbc-b2a7-866ebb10331f",id4="a2c1d849-af05-4bbc-b2a7-866ebb10331f",id5="a2c1d849-af05-4bbc-b2a7-866ebb10331f",id6="a2c1d849-af05-4bbc-b2a7-866ebb10331f",id7="a2c1d849-af05-4bbc-b2a7-866ebb10331f",id8="a2c1d849-af05-4bbc-b2a7-866ebb10331f",id9="a2c1d849-af05-4bbc-b2a7-866ebb10331f")
        else:
            password = request.args.get("Password")
            username = request.args.get("Username")
            api = request.args.get("API")
            secret = request.args.get("secret")
            ids,name = searchformanga(username,password,api,secret)
            a = ids[0]
            b = ids[1]
            c = ids[2]
            d = ids[3]
            e = ids[4]
            f = ids[5]
            g = ids[6]
            h = ids[7]
            i = ids[8]
            j = ids[9]
            aa = name[0]
            bb = name[1]
            cc = name[2]
            dd = name[3]
            ee = name[4]
            ff = name[5]
            gg = name[6]
            hh = name[7]
            ii = name[8]
            jj = name[9]
            return render_template("reccstemp.html",name0=aa,name1=bb,name2=cc,name3=dd,name4=ee,name5=ff,name6=gg,name7=hh,name8=ii,name9=jj
                                   ,id0=a,id1=b,id2=c,id3=d,id4=e,id5=f,id6=g,id7=h,id8=i,id9=j)


# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    webbrowser.open(f"http://127.0.0.1:5000/recommend",new=2)
    app.run()
