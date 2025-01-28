from itertools import groupby


class Conway:
    def __init__(self, given_string: str, nb_of_conway_loop: int):
        self.given_string: str = given_string
        self.nb_of_conway_loop: int = nb_of_conway_loop
        # string to add each line describing the previous
        self.new_line: str = ""
        self.conway_result: list = []

    def split_string(self, string):
        splitted_string: list = ["".join(group) for ele, group in groupby(string)]
        return splitted_string

    def conway_translation(self, splitted_string_element):
        # Get the character
        caracter:int = splitted_string_element[0]
        # getting the nb of times it is repeated
        nb_occurrences: int = len(splitted_string_element)
        # turning the nb into a string
        return f"{nb_occurrences}{caracter}"  # Return count and character as a string


    def conway_suite(self):
        # Add the initial string to the result list
        self.conway_result.append(self.given_string)
        current_string = self.given_string
        for _ in range(self.nb_of_conway_loop - 1):
            # Split the string into groups of identical characters
            splitted_string = self.split_string(current_string)
            # Use map() to apply conway_translation to each group
            mapped_result = map(self.conway_translation, splitted_string)
            # Join the mapped results into a new string
            current_string = "".join(mapped_result)
            # Append the new string to the result list
            self.conway_result.append(current_string)

    def print_conway(self):
        # print the result in the expected format
        for line in self.conway_result:
            print(line)


test = Conway("1aaa", 3)
test.conway_suite()
test.print_conway()

# test2 = Conway("b", 4)
# test2.print_conway()

# test2.conway_suite()
#
# test3 = Conway("1aaa2a223bb2b", 2)
# test3.conway_suite()
# test3.print_conway()

# splitter en objet avec un objet qui contient le caractere et le nb de recurence
# récursif ?
