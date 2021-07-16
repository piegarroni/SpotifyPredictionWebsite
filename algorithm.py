from flask import Flask, render_template, request
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier



app=Flask(__name__)

@app.route('/')

def main():
    return render_template('structure.html')

@app.route('/send', methods=['post'])

def send():

    if request.method=='POST':
            p1=request.form['p1']
            p2=request.form['p2']
            p3=request.form['p3']
            p4=request.form['p4']
            p5=request.form['p5']
            p6=request.form['p6']
            p7=request.form['p7']
            p8=request.form['p8']

            data= pd.read_csv("website_data.csv")
            #creating binary variable (popular/not popular)
        #    data=data[data["year"]>2019]
        #    data['bool_pop']=data['popularity']>60
            print(type(p8))
            if p8==[]:
                X=data[['danceability', 'instrumentalness', 'energy', 'acousticness', 'explicit', 'speechiness', 'valence']]
                song=[p1, p2, p3, p4, p5, p6, p7]
            else:
                X=data[['danceability', 'instrumentalness', 'energy', 'acousticness', 'explicit', 'speechiness', 'valence', 'popularity_artist' ]]
                song=[p1, p2, p3, p4, p5, p6, p7, p8]
            y=data["pop_three"]

            knn = KNeighborsClassifier(n_neighbors=1).fit(X, y)
            #'danceability', 'instrumentalness', 'energy', 'acousticness', 'explicit', 'speechiness', 'valence', 'popularity_artist'
      #list with eight entries from structure.html


            d=pd.Series(song).values.reshape(1, -1)  #reshaping and converting the list
            result=(knn.predict(d))

            print(type(result))
            print(result)

            if str(result)=='[1]':
                return render_template('structure.html', result="this song is probably not going to be a success")
            elif str(result)=='[2]':
                return render_template('structure.html', result="this song is maybe going to be a success (medium popularity)")
            elif str(result)=='[3]':
                return render_template('structure.html', result="this song is probably going to be a success (high popularity)")
            else:
                return render_template('structure.html', result="there was an error")


        #    if result=='1':
        #        return render_template('structure.html', result="this song is probably not going to be a success (low_popularity")

        #    elif result=='2':
        #        return render_template('structure.html', result="this song is maybe going to be a success (medium popularity)")
        #    elif result=='3':
        #        return render_template('structure.html', result="this song is probably going to be a success (high popularity)")
if __name__=='__main__':
    app.run(debug=True)
