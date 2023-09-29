"""
# File: books.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  Open a file and search.
"""
max_chapters=-1
max_book=""
option=input("What book are you interested: ")

with open("books_and_chapters.txt") as file:
    for line in file:
        clean=line.strip()
        
        lines=clean.split(":")
        book=lines[0]
        chapter=int(lines[1])
        testa=lines[2]

        #print(book)
        # print(f"Scripture: {testa}, Book: {book}, Chapters: {chapter}")

        # #finding the largest nimber of chapters

        # if chapter>max_chapters:
        #     max_chapters=chapter
        #     max_book=book

   # print(f"The largest number of chapters in the scriptures is: {max_chapters} from: {max_book}") 
    #     if testa=="Book of Mormon":
    #         testa="Book of Mormon"
    #         morbook=book
    # #print(f"The books of the Boooks of Mormon are: {morbook}")   
    #         if chapter>max_chapters:
    #           max_chapters=chapter
    #           max_book=morbook
    # print(f"The book from the Book of Mormon that has the largest number of chapter is: {max_book}")                 
  
  
  #ask the user
        if option.lower()==testa.lower():
            testa=option
            if chapter>max_chapters:
                max_chapters=chapter
                max_book=book
    print(f"The book in {option}  that has the largest number of chapters is: {max_book}.")     
