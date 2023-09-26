import os

def renamer(front,end,source,target):
        
        #generate a list of the texts needs to be changed
        word_list=[]
        with open('your_file.txt', 'r') as file:
                for line in file:
                        word = line.strip()  # Remove leading/trailing whitespace, if any
                        word_list.append(word)
                        
        #generate a list of modified texts
        final_list=[]
        for word in word_list:
                final_list.append(word[57:])
        
        final_list_line_by_line= '\n'.join(final_list)

        # import final sentences in final file
        with open('final.txt', 'w') as file:
                file.write(final_list_line_by_line)

        print("Final file has been modified and created successfully!")

renamer()
