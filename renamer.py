import os

def renamer(front=0,end=0,source="file",target="final"):
        #generate a list of the texts needs to be changed
        word_list=[]
        try:
                with open(source+'.txt', 'r') as file:
                        for line in file:
                                word = line.strip()  # Remove leading/trailing whitespace, if any
                                word_list.append(word)
        except FileNotFoundError:
                print("the source file has not been found, please check the file and it's name and try again.")
                        
        #generate a list of modified texts
        final_list=[]
        if(len(word_list)>0):
                for word in word_list:
                        final_list.append(word[int(front):-int(end)])
        else:
                print("the text file you provided was empty.")
                return
        
        final_list_line_by_line= '\n'.join(final_list)

        # import final sentences in final file
        with open(target+'.txt', 'w') as file:
                file.write(final_list_line_by_line)

        print("Final file has been modified and created successfully!")

renamer(5,4,'file','final')
