# import requests
#
# try:
#     # Attempt to connect to IMDb's homepage
#     response = requests.get('https://www.imdb.com')
#
#     # Check if the connection was successful
#     if response.status_code == 200:
#         print("Connection successful. Status Code:", response.status_code)
#     else:
#         print(f"Connection failed. Status Code: {response.status_code}")
#
# except requests.exceptions.RequestException as e:
#     # If an error occurred (like a timeout or network issue), it will be printed here
#     print(f"Error connecting to IMDb: {e}")

from tkinter import *
import imdb
from tkinter import messagebox

###########Functionality part
def search():
    if movieEntry.get()=='':
        messagebox.showerror('Error','Please type a movie name')
    else:


     root1=Toplevel()

    root1.geometry('890x600+200+50')
    root1.title('Movie information')
    root1.config(bg='#1E1E2F')

    titlelabel=Label(root1,text='Title', font=('cooper black', 30, 'bold'),fg='white', bg='#1E1E2F')
    titlelabel.place(x=60, y=30)

    titlenamelabel=Label(root1,text='', font=('algerian', 20, 'bold'), fg='white', bg='#1E1E2F')
    titlenamelabel.place(x=300, y=30)


    directorlabel=Label(root1,text='Director', font=('cooper black', 30, 'bold'),fg='white', bg='#1E1E2F')
    directorlabel.place(x=60, y=100)

    directornamelabel=Label(root1,text='', font=('algerian', 20, 'bold'), fg='white', bg='#1E1E2F')
    directornamelabel.place(x=300, y=100)


    yearlabel=Label(root1,text='Year', font=('cooper black', 30, 'bold'),fg='white', bg='#1E1E2F')
    yearlabel.place(x=60, y=170)

    yearnamelabel=Label(root1,text='', font=('algerian', 20, 'bold'), fg='white', bg='#1E1E2F')
    yearnamelabel.place(x=300, y=170)


    runtimelabel=Label(root1,text='Runtime', font=('cooper black', 30, 'bold'),fg='white', bg='#1E1E2F')
    runtimelabel.place(x=60, y=240)

    runtimenamelabel=Label(root1,text='', font=('algerian', 20, 'bold'), fg='white', bg='#1E1E2F')
    runtimenamelabel.place(x=300, y=240)


    genrelabel=Label(root1,text='Genres', font=('cooper black', 30, 'bold'),fg='white', bg='#1E1E2F')
    genrelabel.place(x=60, y=310)

    genrenamelabel=Label(root1,text='', font=('algerian', 20, 'bold'), fg='white', bg='#1E1E2F')
    genrenamelabel.place(x=300, y=310)


    ratinglabel=Label(root1,text='Ratings', font=('cooper black', 30, 'bold'),fg='white', bg='#1E1E2F')
    ratinglabel.place(x=60, y=380)

    ratingnamelabel=Label(root1,text='', font=('algerian', 20, 'bold'), fg='white', bg='#1E1E2F')
    ratingnamelabel.place(x=300, y=380)


    castlabel=Label(root1,text='Cast', font=('cooper black', 30, 'bold'),fg='white', bg='#1E1E2F')
    castlabel.place(x=60, y=450)

    castnamelabel=Label(root1,text='', font=('algerian', 20, 'bold'), fg='white', bg='#1E1E2F', wraplength=615
                        ,justify=LEFT)
    castnamelabel.place(x=300, y=450)


    imdbobject=imdb.IMDb()
    movie_name=movieEntry.get()
    movies=imdbobject.search_movie(movie_name)
    index=movies[0].getID()
    movie=imdbobject.get_movie(index)

    title=movie['title']
    titlenamelabel.config(text=title)

    year=movie['year']
    yearnamelabel.config(text=year)

    rating=movie['rating']
    ratingnamelabel.config(text=rating)

    genre=movie['genre']
    genrenamelabel.config(text=genre)

    if 'director' in movie:
        for director in movie['director']:
            directornamelabel.config(text=director)
    else:
        directornamelabel.config(text="Director information not available")

    for runtime in movie['runtime']:
        hours=int(runtime)//60
        minutes=int(runtime)%60
        runtimenamelabel.config(text=f'{hours} hour {minutes} minutes')

    cast=movie['cast']
    castlist=list(map(str,cast))
    slicelist=castlist[:10]
    strr=''
    for i in slicelist:
        if i==slicelist[9]:
           strr=strr+i+'.'
        else:
            strr=strr+i+',' +' '
    castnamelabel.config(text=strr)
    root1.mainloop()

###########GUI part
root=Tk()

root.geometry('1057x650+100+30')
root.title('Movie Insight')
root.resizable(False, False)

bgpic=PhotoImage(file='pic.png')

bgLabel=Label(root, image=bgpic)
bgLabel.place(x=0, y=0)

movieLabel=Label(root,text='Movie Name:', font=('algerian', 30, 'bold' ), bg='#dedcdd')
movieLabel.place(x=200, y=570)

movieEntry=Entry(root, font=('FELIX TITLING', 20, 'bold'), bd=5, relief=GROOVE, justify=CENTER)
movieEntry.place(x=490, y=575)
movieEntry.focus_set()

moviesearchButton=Button(root, text='SEARCH', font=('FELIX TITLING', 20, 'bold'),bd=5, relief=GROOVE
                         ,command=search)
moviesearchButton.place(x=880, y=565)

root.mainloop()