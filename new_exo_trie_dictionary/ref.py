class Node:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.is_end_word = False


    def add_child_at(self, index, child):
        if index > len(self.children):
            return False
        self.children.insert(index, child)
        return True


    def insert_char(self, char):
        nb_children = len(self.children)

        for i in range(nb_children):
            if char == self.children[i].char:
                return self.children[i]

            if char < self.children[i].char:
                # insert the char
                self.add_child_at(i, Node(char))
                return self.children[i]

        # at the end
        self.add_child_at(nb_children, Node(char))
        return self.children[nb_children]


    def get_child(self, char):
        for child in self.children:
            if child.char == char:
                return child
        return None


    def print_chars(self, prefix):
        word = prefix + self.char

        if self.is_end_word:
            print(word)

        for child in self.children:
            child.print_chars(word)


    def __repr__(self):
        return self.char


class Dict:
    def __init__(self):
        self.root = Node('')


    def add_word(self, word):
        current_node = self.root

        for letter in word:
            node_letter = current_node.get_child(letter)
            if not node_letter:
                node_letter = current_node.insert_char(letter)

            current_node = node_letter
        current_node.is_end_word = True


    def exists(self, word):
        current_node = self.root

        for letter in word:
            current_node = current_node.get_child(letter)
            if not current_node:
                return False

        return current_node.is_end_word


    def print_words(self):
        self.root.print_chars("")


def main():
    d = Dict()
    while True:
        word = input("Entrez votre commande: ")
        if word == "exit" or word == "quit":
            break

        if word == "add":
            word = input("Quel mot dois-je ajouter au dictionnaire ?\n")
            d.add_word(word)

        elif word == "test" or word == "exist":
            word = input("Quel mot dois-je tester ?\n")
            if d.exists(word):
                print("Ce mot appartient bien au dictionnaire.")
            else:
                print("Ce mot n'est pas dans le dictionnaire.")

        elif word == "print":
            d.print_words()

        else:
            print("Mauvaise commande: utilisez \"exit\", \"add\", \"test\", \"print\"")


if __name__ == "__main__":
    main()
