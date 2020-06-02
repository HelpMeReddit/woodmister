import pandas as pd 

data = pd.read_csv("C:\\Users\\dwood\\Desktop\\test_file.csv", header=1)

def passthru(df):

    for index, row in df.iterrows():
        if row['Email'] == "nan":
            break
        else:
            email = row['Email']
            f_name = row['First Name']
            location = row['Office']
            emerg = row['Emergency']
            nonemerg = row['Non- Emergency / Office Phone']
            position = row['Position']
            
            text = "{}\n\n Hey {},\n\n How are you doing in {}? \n\n This e-mail is to update your contact info, I have: \n Emergency: {}\n Non-emegency: {}\n Position: {}\n\n\n".format(email, f_name, location, emerg, nonemerg, position)
            
            print(text)
            
            with open("newfile.txt","a") as f:
                f.write("\n\n"+str(text))

passthru(data)
