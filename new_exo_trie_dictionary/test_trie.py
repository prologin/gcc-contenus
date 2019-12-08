from trie import Dict, Node


def test_node_init():
    node = Node('a')
    assert node
    assert node.char == 'a'
    assert node.children == []
    assert node.is_end_word == False

def test_node_add_at_single():
    node = Node('a')
    assert node
    assert node.children == []
    node.add_child_at(0, Node('b'))
    assert len(node.children) == 1
    assert type(node.children[0]) == Node
    assert node.children[0].char == 'b'

def test_node_add_at_front():
    node = Node('a')
    assert node
    assert node.children == []
    node.add_child_at(0, Node('b'))
    node.add_child_at(0, Node('c'))
    assert len(node.children) == 2
    assert type(node.children[0]) == Node
    assert type(node.children[1]) == Node
    assert node.children[0].char == 'c'
    assert node.children[1].char == 'b'

def test_node_add_at_end():
    node = Node('a')
    assert node
    assert node.children == []
    node.add_child_at(0, Node('b'))
    node.add_child_at(1, Node('c'))
    assert len(node.children) == 2
    assert type(node.children[0]) == Node
    assert type(node.children[1]) == Node
    assert node.children[0].char == 'b'
    assert node.children[1].char == 'c'

def test_node_add_at_middle():
    node = Node('a')
    assert node
    assert node.children == []
    node.add_child_at(0, Node('b'))
    node.add_child_at(0, Node('c'))
    node.add_child_at(1, Node('w'))
    assert len(node.children) == 3
    assert type(node.children[0]) == Node
    assert type(node.children[1]) == Node
    assert type(node.children[2]) == Node
    assert node.children[0].char == 'c'
    assert node.children[1].char == 'w'
    assert node.children[2].char == 'b'


def test_node_insert_char_single():
    node = Node('a')
    assert node
    assert node.children == []
    node.insert_char('b')
    assert len(node.children) == 1
    assert type(node.children[0]) == Node
    assert node.children[0].char == 'b'

def test_node_insert_char_front():
    node = Node('a')
    assert node
    assert node.children == []
    node.insert_char('p')
    node.insert_char('c')
    assert len(node.children) == 2
    assert type(node.children[0]) == Node
    assert type(node.children[1]) == Node
    assert node.children[0].char == 'c'
    assert node.children[1].char == 'p'

def test_node_insert_char_end():
    node = Node('a')
    assert node
    assert node.children == []
    node.insert_char('b')
    node.insert_char('c')
    assert len(node.children) == 2
    assert type(node.children[0]) == Node
    assert type(node.children[1]) == Node
    assert node.children[0].char == 'b'
    assert node.children[1].char == 'c'

def test_node_insert_char_middle():
    node = Node('a')
    assert node
    assert node.children == []
    node.insert_char('b')
    node.insert_char('e')
    node.insert_char('c')
    assert len(node.children) == 3
    assert type(node.children[0]) == Node
    assert type(node.children[1]) == Node
    assert type(node.children[2]) == Node
    assert node.children[0].char == 'b'
    assert node.children[1].char == 'c'
    assert node.children[2].char == 'e'

def test_node_insert_char_get():
    node = Node('a')
    assert node
    assert node.children == []
    nodeb = node.insert_char('b')
    nodee = node.insert_char('e')
    nodec = node.insert_char('c')
    assert nodeb == node.children[0]
    assert nodee == node.children[2]
    assert nodec == node.children[1]


def test_node_get_child():
    nodea = Node('a')
    nodeb = Node('b')
    nodec = Node('c')
    nodee = Node('e')
    nodea.children.append(nodeb)
    nodea.children.append(nodec)
    nodea.children.append(nodee)
    assert nodea.get_child('a') == None
    assert nodea.get_child('b') == nodeb
    assert nodea.get_child('c') == nodec
    assert nodea.get_child('d') == None
    assert nodea.get_child('e') == nodee


def test_node_print_chars_simple1(capsys):
    nodea = Node('a')
    nodeb = Node('b')
    nodeb.is_end_word = True
    nodea.children.append(nodeb)
    nodea.print_chars("")
    # get words
    array = capsys.readouterr().out.split('\n')[:-1]
    assert array == ["ab"]

def test_node_print_chars_simple2(capsys):
    nodea = Node('a')
    nodea.is_end_word = True
    nodeb = Node('b')
    nodea.children.append(nodeb)
    nodea.print_chars("")
    # get words
    array = capsys.readouterr().out.split('\n')[:-1]
    assert array == ["a"]

def test_node_print_chars_prefix(capsys):
    nodea = Node('a')
    nodea.is_end_word = True
    nodeb = Node('b')
    nodeb.is_end_word = True
    nodea.children.append(nodeb)
    nodea.print_chars("yes_")
    # get words
    array = capsys.readouterr().out.split('\n')[:-1]
    assert array == ["yes_a", "yes_ab"]

def test_node_print_chars_no_end(capsys):
    nodea = Node('a')
    nodeb = Node('b')
    nodea.children.append(nodeb)
    nodea.print_chars("")
    # get words
    array = capsys.readouterr().out.split('\n')[:-1]
    assert array == []

def test_node_print_chars_1st_level(capsys):
    nodea = Node('a')
    nodeb = Node('b')
    nodeb.is_end_word = True
    nodec = Node('c')
    nodec.is_end_word = True
    nodea.children.append(nodeb)
    nodea.children.append(nodec)
    nodea.print_chars("")
    # get words
    array = capsys.readouterr().out.split('\n')[:-1]
    assert array[0] == "ab"
    assert array[1] == "ac"
    assert len(array) == 2

def test_node_print_chars_2nd_level(capsys):
    nodea = Node('a')
    nodea.is_end_word = True
    nodeb = Node('b')
    nodec = Node('c')
    nodec.is_end_word = True
    nodee = Node('e')
    nodee.is_end_word = True
    nodea.children.append(nodeb)
    nodea.children.append(nodec)
    nodea.children.append(nodee)
    nodea.print_chars("")
    # get words
    array = capsys.readouterr().out.split('\n')[:-1]
    assert array[0] == "a"
    assert array[1] == "ac"
    assert array[2] == "ae"
    assert len(array) == 3


def test_dict_init():
    d = Dict()
    assert d
    assert d.root
    assert type(d.root) == Node
    assert d.root.char == ''


def test_dict_add_word_simple():
    d = Dict()
    assert d
    d.add_word("a")
    assert len(d.root.children) == 1
    assert d.root.children[0].char == 'a'
    assert d.root.children[0].is_end_word
    assert d.root.is_end_word == False
    assert d.root.children[0].children == []

def test_dict_add_word_double():
    d = Dict()
    assert d
    d.add_word("ab")
    assert len(d.root.children) == 1
    assert d.root.is_end_word == False
    assert d.root.children[0].char == 'a'
    assert d.root.children[0].is_end_word == False
    assert len(d.root.children[0].children) == 1
    assert d.root.children[0].children[0].char == 'b'
    assert d.root.children[0].children[0].is_end_word
    assert d.root.children[0].children[0].children == []

def test_dict_add_word_2():
    d = Dict()
    assert d
    d.add_word("ab")
    d.add_word("a")
    assert len(d.root.children) == 1
    assert d.root.is_end_word == False
    assert d.root.children[0].char == 'a'
    assert d.root.children[0].is_end_word
    assert len(d.root.children[0].children) == 1
    assert d.root.children[0].children[0].char == 'b'
    assert d.root.children[0].children[0].is_end_word
    assert d.root.children[0].children[0].children == []

def test_dict_add_word_3():
    d = Dict()
    assert d
    d.add_word("ab")
    d.add_word("ba")
    assert len(d.root.children) == 2
    assert d.root.is_end_word == False
    assert d.root.children[0].char == 'a'
    assert d.root.children[0].is_end_word == False
    assert d.root.children[1].char == 'b'
    assert d.root.children[1].is_end_word == False

    assert len(d.root.children[0].children) == 1
    assert d.root.children[0].children[0].char == 'b'
    assert d.root.children[0].children[0].is_end_word
    assert d.root.children[0].children[0].children == []
    assert len(d.root.children[1].children) == 1
    assert d.root.children[1].children[0].char == 'a'
    assert d.root.children[1].children[0].is_end_word
    assert d.root.children[1].children[0].children == []

def test_dict_add_word_4():
    d = Dict()
    assert d
    word = "qwertyuiopasdfghjklzxcvbnm"
    d.add_word(word)
    assert len(d.root.children) == 1
    assert d.root.is_end_word == False
    node = d.root.children[0]
    for i in range(len(word) - 1):
        assert node.char == word[i]
        assert node.is_end_word == False
        assert len(node.children) == 1
        node = node.children[0]
    assert node.char == "m"
    assert node.is_end_word
    assert node.children == []

def test_dict_add_word_4():
    d = Dict()
    assert d
    word = "qtyuiopasdfghjklzxcvbnm"
    d.add_word(word)
    word = "qtxy"
    d.add_word(word)
    assert len(d.root.children) == 1
    assert d.root.is_end_word == False
    assert d.root.children[0].char == 'q'
    assert len(d.root.children[0].children) == 1
    assert d.root.children[0].is_end_word == False
    assert d.root.children[0].children[0].char == 't'
    assert len(d.root.children[0].children[0].children) == 2
    assert d.root.children[0].children[0].is_end_word == False
    assert d.root.children[0].children[0].children[0].char == 'x'
    assert len(d.root.children[0].children[0].children[0].children) == 1
    assert d.root.children[0].children[0].children[0].is_end_word == False
    assert d.root.children[0].children[0].children[1].char == 'y'
    assert len(d.root.children[0].children[0].children[1].children) == 1
    assert d.root.children[0].children[0].children[1].is_end_word == False
    assert d.root.children[0].children[0].children[0].children[0].char == 'y'
    assert d.root.children[0].children[0].children[0].children[0].children == []
    assert d.root.children[0].children[0].children[0].children[0].is_end_word
    assert d.root.children[0].children[0].children[1].children[0].char == 'u'
    assert len(d.root.children[0].children[0].children[1].children[0].children) == 1
    assert d.root.children[0].children[0].children[1].children[0].is_end_word == False


def test_dict_exists():
    d = Dict()
    assert d
    d.root.children.append(Node('a'))
    d.root.children[0].children.append(Node('m'))
    d.root.children[0].children[0].children.append(Node('e'))
    d.root.children[0].children[0].children[0].children.append(Node('l'))
    d.root.children[0].children[0].children[0].children[0].children.append(Node('i'))
    d.root.children[0].children[0].children[0].children[0].children[0].children.append(Node('e'))
    d.root.children[0].children[0].children[0].children[0].children[0].children[0].is_end_word = True
    d.root.children.append(Node('e'))
    d.root.children[1].is_end_word = True
    d.root.children[1].children.append(Node('t'))
    d.root.children[1].children[0].is_end_word = True
    d.root.children.append(Node('f'))
    assert d.exists("a") == False
    assert d.exists("b") == False
    assert d.exists("c") == False
    assert d.exists("e")
    assert d.exists("f") == False
    assert d.exists("am") == False
    assert d.exists("ame") == False
    assert d.exists("amel") == False
    assert d.exists("ameli") == False
    assert d.exists("amelie")
    assert d.exists("et")
    assert d.exists("eta") == False
    assert d.exists("epita") == False
    assert d.exists("") == False


def test_dict_print_words(capsys):
    d = Dict()
    assert d
    d.root.children.append(Node('a'))
    d.root.children[0].children.append(Node('m'))
    d.root.children[0].children[0].children.append(Node('e'))
    d.root.children[0].children[0].children[0].children.append(Node('l'))
    d.root.children[0].children[0].children[0].children[0].children.append(Node('i'))
    d.root.children[0].children[0].children[0].children[0].children[0].children.append(Node('e'))
    d.root.children[0].children[0].children[0].children[0].children[0].children[0].is_end_word = True
    d.root.children.append(Node('e'))
    d.root.children[1].is_end_word = True
    d.root.children[1].children.append(Node('t'))
    d.root.children[1].children[0].is_end_word = True
    d.root.children.append(Node('f'))

    d.print_words()
    array = capsys.readouterr().out.split('\n')[:-1]
    assert len(array) == 3
    assert array[0] == "amelie"
    assert array[1] == "e"
    assert array[2] == "et"
