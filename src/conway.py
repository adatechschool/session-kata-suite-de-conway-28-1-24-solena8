from itertools import groupby


class Conway:
    def __init__(self, given_string: str, nb_of_conway_loop: int):
        self.given_string: str = given_string
        self.nb_of_conway_loop: int = nb_of_conway_loop
        # string to add each line describing the previous
        self.new_line = ''
        # int counting how many times a single letter or number is repeated
        self.conway_result = ''


    def conway_suite(self):
        # add given string for reference
        self.conway_result += self.given_string
        # iterating the given number of times
        while self.nb_of_conway_loop > 0:
            # using groupby to split the given string into groups of similar caracters in a list
            splitted_string = ["".join(group) for ele, group in groupby(self.given_string)]
            # looping over the list
            for i in range(len(splitted_string)):
                # getting the caracter we're currenttly inspecting
                caracter = splitted_string[i][0]
                # getting the nb of times it is repeated
                nb_occurences = len(splitted_string[i])
                # turning the nb into a string
                str_occurences = str(nb_occurences)
                # adding the nb of times + the caracter to the new line
                self.new_line += str_occurences
                self.new_line += caracter
            #     adding the new line to the result + go to line
            self.conway_result += "\n"
            self.conway_result += self.new_line
            # new line will be the next given string
            self.given_string = self.new_line
            # resetting new line to an empty string
            self.new_line = ""
            # subtract 1 from the loop count
            self.nb_of_conway_loop -= 1
        return self.conway_result

test = Conway("1aaa",3)
print(test.conway_suite())

test2 = Conway("b",7)
print(test2.conway_suite())