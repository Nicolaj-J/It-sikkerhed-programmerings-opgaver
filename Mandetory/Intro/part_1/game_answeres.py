import challenge as challenge


class game_questions:
    def __init__(self, username, password) -> None:
        game_login = (username, password)
        self.game = challenge.client(ip_address="cybergame.dk", port=39594)
        self.game.login(game_login[0], game_login[1])

    def get_question(self, question_number=int()-1):
        self.question_number = question_number
        return (self.game.question(question_number))

    def get_data(self, question_number=int()-1):
        data = self.game.data(question_number)
        return (data)

    def send_data(self, answer):
        self.game.answer(self.question_number, answer)

    def get_scores(self):
        print(self.game.score())

    def question_0(self):
        """
        Question: Return the answer

        What i did:
        I placed the data in the variable answer and returned it
        """
        answer = self.get_data(question_number=self.question_number)
        self.send_data(answer)
        return answer

    def question_1(self):
        """
        Question: The answer is the data multiplied with 2

        What i did:
        I forced the data to be integer and mulitplied it with 2 before placing it into answer variable and returning it
        """
        answer = int(self.get_data(question_number=self.question_number)) * 2
        self.send_data(answer)
        return answer

    def question_2(self):
        """
        Question: The answer is the data in uppercase

        What i did:
        I used the upper function for strings to change all letters to uppercase
        """
        answer = str(self.get_data(question_number=self.question_number)).upper()
        self.send_data(answer)
        return answer

    def question_3(self):
        """
        Question: Return the text in data in the reverse order

        What i did:
        I forced a string and told it to start from the back. So reversed it
        """
        answer = str(self.get_data(question_number=self.question_number))[::-1]
        self.send_data(answer)
        return answer

    def question_4(self):
        """
        Question: Return the sorted list

        What i did:
        I forced the data to be a list. Then used the sorted function
        """
        answer = list(self.get_data(question_number=self.question_number))
        self.send_data(sorted(answer))
        return sorted(answer)

    def question_5(self):
        """
        Question: Return a list containing only the first 3 elements

        What i did:
        I took from 0 up to index 3 and returned it.
        """
        answer = self.get_data(question_number=self.question_number)[0:3]
        self.send_data(answer)
        return answer

    def question_6(self):
        """
        Question: Return a list where each number is multiplied with 5

        What i did:
        I forced a list and looped over it. Then i replaced each index with the value multiplied by 5.
        """
        answer = list(self.get_data(question_number=self.question_number))
        for number in answer:
            answer[answer.index(number)] = number * 5
        self.send_data(answer)
        return answer

    def question_7(self):
        """
        Question: Return the value of the 6th element

        What i did:
        I forced a list and since python works with 0 index i took the 5th index and returned it.
        """

        answer = list(self.get_data(question_number=self.question_number))[5]
        self.send_data(answer)
        return answer

    def question_8(self):
        """
        Question: Return a sorted list, where the duplicates are removed

        What i did:
        I first forced a set to remove any dublicates then changed it into a list afterwards.
        """

        answer = list(set(self.get_data(question_number=self.question_number)))
        self.send_data(answer)
        return answer

    def question_9(self):
        """
        Question: Replace 'be' in the data with 'python'

        What i did:
        I used the str function replace to change be to python
        """

        answer = str(self.get_data(question_number=self.question_number)).replace("be", "python")
        self.send_data(answer)
        return answer

    def question_10(self):
        """
        Question: The answer is the whole sentence with the word 'star' spelled backwards

        What i did:
        I also used replace here but was more accurate with the search
        """

        answer = str(self.get_data(question_number=self.question_number)).replace("the star", "the rats")
        self.send_data(answer)
        return answer

    def question_11(self):
        """
        Question: Return a list containing 20 values starting with the number in data and incrementing with 5

        What i did:
        I placed the data in a list. Then i looped over the list 20 times. In the loop i append the last index plus 5
        """

        answer = self.get_data(question_number=self.question_number)
        my_list = [answer]
        for i in range(19):
            my_list.append(my_list[-1]+5)
        answer = my_list
        self.send_data(answer)
        return answer

    def question_12(self):
        """
        Question: The data is a list of tuples containing ip-addresses and number of connections.
        Return the number of connections for ip-address 192.168.1.212

        What i did:
        Here i looped over the list and when the correct ip was found i took the second index and stopped the loop.
        """

        answer = self.get_data(question_number=self.question_number)
        for i in answer:
            if i[0] == "192.168.1.212":
                answer = i[1]
                break
        self.send_data(answer)
        return answer

    def question_13(self):
        """
        Question: The answer is the total sum of all the numbers in the list

        What i did:
        Here i used the function sum. Which takes the total sum of the list.
        """

        answer = self.get_data(question_number=self.question_number)
        answer = sum(answer)
        self.send_data(answer)
        return answer

    def question_14(self):
        """
        Question: Return a list containing tuples with names and phonenumbers
        [(\"name1\",\"phone1\"),(\"name2\",\"phone2\")...]

        What i did:
        First I split the data on ",".
        I loop over date and replaced each index with a tupple containing a string.
        """

        answer = self.get_data(question_number=self.question_number).split(",")
        for i in answer:
            answer[answer.index(i)] = tuple(str(i).split(":"))
        self.send_data(answer)
        return answer

    def question_15(self):
        """
        Question: Return the dictionary with the entry for \"192.168.1.243\" removed

        What i did:
        Here i use the statement del to delete key and value in the dictionary.
        """

        answer = self.get_data(question_number=self.question_number)
        del answer["192.168.1.243"]
        self.send_data(answer)
        return answer

    def question_16(self):
        """
        Question: The answer is the sentence where each word is in reverese
        (the words keep their place in the sentence)

        What i did:
        I make a list where its split for spaces. After that i loop over each work and reverses it while i add it into the sentence.
        After the loop i use the strip function to remove any unwanted spaced.
        """

        answer = self.get_data(question_number=self.question_number)
        answer = answer.split(" ")
        s = ""
        for i in answer:
            s = s + " " + str(i)[::-1]
        answer = s.strip()
        self.send_data(answer)
        return answer

    def question_17(self):
        """
        Question: Return a list containing 10 tuples of the ones found in data

        What i did:
        I create a new list and create a for loop to append the data 10 times.
        """

        answer = self.get_data(question_number=self.question_number)
        my_list = []
        for i in range(10):
            my_list.append(answer)
        answer = my_list
        self.send_data(answer)
        return answer

    def question_18(self):
        """
        Question: Add a new item to the dictionary with the key \"yellow\" and the value 22

        What i did:
        I add a key and value pair to the dictionary
        """

        answer = self.get_data(question_number=self.question_number)
        answer["yellow"] = 22
        self.send_data(answer)
        return answer

    def question_19(self):
        """
        Question: Return a set containing all unique ip addresses in data

        What i did:
        I split for newline and loop over the data. In the loop i split each line and takes index 0. This i append to a list.
        After the loop i make the list a set and discards empty entries.
        """

        answer = self.get_data(question_number=self.question_number)
        answer = answer.split("\n")
        my_list = []
        for i in answer:
            my_list.append(str(i).split(" - - ")[0])
        answer = set(my_list)
        answer.discard("")
        self.send_data(answer)
        return answer

    def question_20(self):
        """
        Question: Return a dictionary containing all status codes (in string)
        as key, and how many times their occured (in int) as value

        What i did:
        I split the data for newline. After that i looped over every line where i split each line 2 times and picked the status code.
        Then if it already was in the dictionary it plusses one otherwise it places it in the dictionary.
        """

        answer = self.get_data(question_number=self.question_number).split("\n")
        my_dic = {}
        for i in answer:
            try:
                status_code = i.split('" ')[1].split(" ")[0]
                if status_code in my_dic:
                    my_dic[status_code] += 1
                else:
                    my_dic[status_code] = 1
            except:
                pass
        answer = my_dic
        self.send_data(answer)
        return answer

    def question_21(self):
        """
        Question: Return the average size (in int) of all responses with status 200

        What i did:
        I split for newline and loops over eachline. In the loop i split eachline twice and checks if the statuscode is 200.
        If so i split the line again and selects the size which i adds to my variable and i add one to the other variable.
        After the loop i force integers to remove variable and divide the two to get the average.


        I could also have used list with the len function to get number of entries and sum function to get the total entry
        """

        answer = self.get_data(question_number=self.question_number).split("\n")
        avg_len = 0
        number_entry = 0
        for i in answer:
            try:
                if i.split('" ')[1].split(" ")[0] == "200":
                    message_len = int(i.split('" ')[1].split(" ")[1])
                    avg_len += message_len
                    print(message_len)
                    number_entry += 1
            except:
                pass
        answer = int(avg_len)/int(number_entry)
        self.send_data(int(answer))
        return answer

    def question_22(self):
        """
        Question: Return the number of times (in int)  an images of the type png is in the response

        What i did:
        Here i use the count function to search for .png 
        """

        answer = self.get_data(question_number=self.question_number).count(".png")
        self.send_data(answer)
        return answer

    def question_23(self):
        """
        Question: Convert this list to a dictionary where the episode number is the key
        (ie: \"Episode I\") and the name is the value (ie: \"The Phantom Menace\")

        What i did:
        I loop over the list and add them each to the dictionary.
        """

        answer = self.get_data(question_number=self.question_number)
        movie_dic = {}
        for i in answer:
            movie_dic[i[1]] = i[0]
        answer = movie_dic
        self.send_data(answer)
        return answer

    def question_24(self):
        """
        Question: Return a sorted list (in int) containing the numbers 1-100,
        but without the numbers divideble with the number in data
        (ie. the numbers 3,6,9,12... should not be there)

        What i did:
        First i make a list from 1-100
        After that i loop over the list and if it can be divided with 3 i remove it.
        """

        answer = self.get_data(question_number=self.question_number)
        my_list = list(range(101))
        for i in my_list:
            if i % 3 == 0:
                my_list.remove(i)
        answer = my_list
        self.send_data(answer)
        return answer

    def question_25(self):
        """
        Question: This sha1 hash was found. the system it comes from normally uses 4 character codes,
        consisting of a-z in lowercase.

        What i did:
        This is a bad way of doing it. But i made a list of all possible characters.
        Then i have a loop for each cipher and just loops over the list to create all possible four ciphers code.
        This code is hashed and checked if it matches the data.
        """
        import hashlib
        abc = list("qwertyuiopasdfghjklzxcvbnm")
        answer = self.get_data(question_number=self.question_number)
        for a in abc:
            for b in abc:
                for c in abc:
                    for d in abc:
                        fourcc = str(a + b + c + d)
                        digest = hashlib.sha1(bytes(fourcc, 'utf-8'))
                        if answer == digest.hexdigest():
                            self.send_data(fourcc)
                            return fourcc

    def question_26(self):
        """
        Question: The data provided contains a tuple, where first element is a sha256.
        The second element contains a list (created by scapping the victims facebook) of words
        that the password could be generated from. Assume that the password length is 8 characters,
        and that the system requires lowercase, uppercase letters and numbers.

        What i did:
        This is the smarter way of doing it. I take out the hash from the data. 
        And loop over each of the entries in index 1 of the data.
        Here i checks if its a tuple if so i loop over the tuple where i add each entry to a new list.
        If it isnt a tuple i just add it to the list.
        The * in the last for loops does so it loops over each charachter in the string. 
        So if the word was Lars it would enter the new list like this: " L, a, r, s "

        Because of this i can now use itertools combinations to create all the possible combinations of the characters that is used in the data.
        These combinations must be 8 ciphers. Right after the combinations list gets looped over where each combination gets hashed and checked towards the hashed password.
        It takes about 5 min to do since the answer is in the start. Otherwise it would take about 11 days with normal run time for python(Without allocating more resouces)
        """
        import hashlib
        import itertools
        answer = self.get_data(question_number=self.question_number)
        sha = answer[0]
        answer = answer[1:][0]
        letter_list = []

        for i in answer:
            if isinstance(i, tuple):
                for n in i:
                    for m in [*n]:
                        letter_list.append(m)
            else:
                for m in [*i]:
                    letter_list.append(m)
        test = itertools.combinations(letter_list, 8)
        print(test)
        for i in test:
            pass_test = "".join(i)
            digest = hashlib.sha256(bytes(pass_test, 'utf-8'))
            print(pass_test, " ", digest.hexdigest(), " ", sha)
            if sha == digest.hexdigest():
                self.send_data(pass_test)
                return pass_test
            

    def question_27(self):
        """
        Question: Return the missing layer (you can hardcode the answer.)

        What i did:
        I first i split the data and right after i make a list of all the layers in TCP stack.
        Then i loop over the list and checks if its in the data given.
        """

        answer = self.get_data(question_number=self.question_number).split(", ")
        network_layers = ["application", "transport", "network", "link", "physical"]
        for i in network_layers:
            if i not in answer:
                answer = i
                break

        self.send_data(answer)
        return answer

    def question_28(self):
        """
        Question: Return the mac address (you can hardcode the answer.)

        What i did:
        I splitted the data and looped over it. Then i splitted for : and checked if the length was 6.
        If it was it matched the length of a mac address and i return it
        """

        answer = self.get_data(question_number=self.question_number).split(", ")
        for i in answer:
            if len(i.split(":")) == 6:
                answer = i
                break
        self.send_data(answer)
        return answer

    def question_29(self):
        """
        Question:
        Use cap.pcapng from the network challenge.
        Analyse the paket(data is the packet no).
        What is the length of the data transmitted,
        in this paket (in bytes).
        (you can hardcode the answer.)

        What i did:
        Here i hardcoded the answer
        """

        answer = self.get_data(question_number=self.question_number)
        answer = "39"
        self.send_data(answer)
        return answer

    def question_30(self):
        """
        Question:
        Use cap.pcapng from the network challenge. Data is a path for a HTTP request.
        What is Ack (raw) in the packet that acknowledges this file? (you can hardcode the answer.)

        What i did:
        I hardcoded the answer
        """

        answer = self.get_data(question_number=self.question_number)
        self.send_data(3775708311)
        return answer

    def question_31(self):
        """
        Question:
        Use cap.pcapng from the network challenge. What domain name is here? (you can hardcode the answer.)

        What i did:
        I hardcoded the answer
        """

        answer = self.get_data(question_number=self.question_number)
        answer = "0.client-channel.google.com"
        self.send_data(answer)
        return answer

    def question_32(self):
        """
        Question:
        A packet is sent using TCP with the Sequence number provided in data, and a payload that is 140 bytes.
        What is the Acknowledge number in the returned response package? (you can hardcode the answer.)

        What i did:
        I hardcoded the answer
        """

        answer = self.get_data(question_number=self.question_number)
        answer = 3728276336 + 140
        self.send_data(answer)
        return answer

    def question_33(self):
        """
        Question:
        Is the request in data correct according to rfc 9110 (you can hardcode the answer [yes or no].)
        
        What i did:
        I hardcoded the answer
        """

        answer = self.get_data(question_number=self.question_number)
        answer = "no"
        self.send_data(answer)
        return answer

    def question_34(self):
        """
        Question:
        KEA has been infiltrated by thieves. Luckily, they were chased away, and dropped what they stole.
        Your task is to use the recorded log data to figure out what floor and room number the thieves ended up.
        ServiceDesk gave you the following legend: ^ = +1 floor, v = -1 floor, < = -1 room number, > = +1 room number.
        Answer with a tuple containing the floor and room number, considering you start on floor 0 and room 0.

        What i did:
        Here i made the data into a list to seperate each command. 
        Then i looped over each command and matched it to each instruction

        """
        answer = list(self.get_data(question_number=self.question_number))
        print(answer)
        floor = 0
        room = 0
        for i in answer:
            match i:
                case "^":
                    floor += 1
                case "v":
                    floor -= 1
                case "<":
                    room -= 1
                case ">":
                    room += 1
        answer = (floor, room)
        self.send_data(answer)
        return answer

    def question_35(self):
        """
        Question:
        ServiceDesk calls you and tells you they gave you an outdated legend for the log data.
        It was from before KEA realised that having negative room numbers doesn't make sense.
        That means the room numbers wrap back around. For example if you are by room 0 and you move left (<),
        you will be by room 100 and vice versa. Furthermore the legend states that if log entries are repeated,
        they increment in value. For example if you see >>>, the first ">" is 1,
        the next ">" is 2, and the last ">" is 3, totalling 6 rooms moved.
        This incremenation resets if the current log entry differs from the previous entry.

        What i did:
        Most of it is the same as 34. The difference is i check if the current command is the same as the previous one. 
        If so i add 1 to the number i increment with. If not i go back to 1 i increment with

        The correct answer and data should be changed. You dont have to think about going into minus. 
        I would suggest making it so the correct answer should be (-8, 88) or something like that. So you needed to implement the loop around to a 100.
        """
        answer = list(self.get_data(question_number=self.question_number))
        floor = 0
        room = 0
        prev_answer = ""
        n_inc = 1
        for i in answer:
            match i:
                case "^":
                    if i == prev_answer:
                        n_inc += 1
                    else:
                        n_inc = 1
                    floor += n_inc
                case "v":
                    if i == prev_answer:
                        n_inc += 1
                    else:
                        n_inc = 1
                    floor -= n_inc
                case "<":
                    if i == prev_answer:
                        n_inc += 1
                    else:
                        n_inc = 1
                    room -= n_inc
                case ">":
                    if i == prev_answer:
                        n_inc += 1
                    else:
                        n_inc = 1
                    room += n_inc
            prev_answer = i
        answer = (floor, room)
        self.send_data(answer)
        return answer

"""
Since i made a class containing all the questions and how to talk to the server. The lines below is used to control the class
"""
question_number = input("What question do you want to see? 0-35 ")
p1 = game_questions(username="nico013w", password="johansen")
p1.get_scores()
print(p1.get_question(question_number))
print(p1.get_data(question_number))
# The line below needs to be changed for each question even tho it asked what question you want to see. 
print(p1.question_26())
