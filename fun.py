# minimo = min('Gilberto')

# maximo = max('Gilberto')


# numeros = [1,2,3,4,5,6,7]

# numeroMaximo = max(numeros)
# print(minimo)

# print(maximo)

# numeros.append(8)

# print(numeroMaximo)

# a,b,c = 7,4,5

# print(a.bit_count())


# a = b
# b = 123

# print(a)

# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)

# a = int(0)
# f = float(1.0)

# fruit = 'banana'

# for f in range(1,10000):
#     print(f)


# print('please digit a name: ')

# name = input()
# print('Hello ' + name)

# palavra = 'Gilberto'

# print(palavra.isupper())

# print('Ola {}, seja bem vindo ao seu {}'.format('Gilberto', "Trabalho"))

# new_str = "The cow jumped over the moon."

# titulo = 'Top Gun Maverick'

# outro_titulo = 'e o vento levou'

# splitted = new_str.split()

# print(splitted)

# print( 'João'.isalpha())

# print(titulo.istitle())
# print(outro_titulo.istitle())

# print('BaseTestHook'.removesuffix('Hook'))

# try:
#     conteudo = open('test.txt').read()
#     print(conteudo)
# except: 
#     print('arquivo não encontrado')

# frutas = ['banana', 'maçã', 'uva','pera', 'melão']

# contatos = dict()

# contatos['gilberto'] = 988331247
# contatos['joselia'] = 972302904

# print(frutas)

# print(contatos)

# nomes = ['gil', 'jo', 'gil', 'joao', 'jo', 'gil']
# ocorrencias = {}

# for n in nomes:
#     if n not in ocorrencias:
#         ocorrencias[n] = 1
#     else: 
#         ocorrencias[n] +=1
    
# print(ocorrencias)

# for n in nomes:
#     ocorrencias[n] = ocorrencias.get(n,0) + 1

# print(ocorrencias)

# indices = [0,1,2,3,4,5,6,7,8,9]

# print(indices[2:5])

# print(indices[:7])

# print(indices[3:])

# eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
#                  'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
#                  'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
#                  'March 9, 2016']
                 
                 
# # TODO: Modify this line so it prints the last three elements of the list
# print(eclipse_dates[-3:])
# eclipse_dates.reverse()

# numeros=[10,9,8,7,6,5,4,3,2,1]

# # numeros.sort()
# # numeros.reverse()

# ordenados = sorted(numeros)

# print(ordenados)

# elements = {'carbon':1, 'oxygen':2}

# print(elements['hidrgen'])



# a = [1,1,1,1, 2, 3,2,2,2,2,3,3,3,3,3]

# setA = set(a)

# print(setA)

# len(setA)



# verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
# print(verse_dict, '\n')


# # find number of unique keys in the dictionary
# num_keys  = 0
# for i in verse_dict:
#     if(verse_dict[i] == 1): 
#         num_keys +=1

# print(num_keys)

# # find whether 'breathe' is a key in the dictionary
# contains_breathe = 'breathe' in verse_dict 
# print(contains_breathe)

# # create and sort a list of the dictionary's keys
# keys = list()
# for k in verse_dict:
#     keys.append(k)
    
# sorted_keys = sorted(keys)

# # get the first element in the sorted list of keys
# print(sorted_keys[0])

# # find the element with the highest value in the list of keys
# print(sorted_keys[len(sorted_keys) -1]) 

# faixa = list(range(1,2,3))
# print(faixa)

# cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
# capitalized_cities = []
# for index in range(len(cities)):
#     capitalized_cities.append(cities[index].title())
#     cities[index] = cities[index].title()
#     print(cities[index])
    
# #print(capitalized_cities)

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_count = dict()
# for word in book_title:
#     if word not in word_count: 
#         word_count[word] = 1
#     else: 
#         word_count[word] += 1

# for word in book_title:
#     print()
#     word_count[word] = word_count.get(word,0) + 1

# print(word_count)


# people = {'gilberto': 1, 'Joao':2, 'joselia': 3}

# # for key, value in people.items() :
# #     print(key)
# #     print(value)

# print(people.items())


# number to find the factorial of
# number = 6   

# # start with our product equal to one
# product = 1

# # write your for loop here
# for n in range(1,number+1):
#     product *= n


# # print the factorial of number
# print(product)

# letters = ['a', 'b', 'c']
# nums = [1, 2, 3]

# for letter, num in zip(letters, nums):
#     print("{}: {}".format(letter, num))


# some_list = [('a', 1), ('b', 2), ('c', 3)]
# letters, nums = zip(*some_list)

# print(letters)
# print(nums)


# data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

# data_transpose = tuple(zip(*data))
# print(data_transpose)


# lista_a = ['a','b','c']
# lista_b = ['1','2','3']

# dicionario = tuple(zip(lista_a,lista_b))
# print(dicionario)

# def obter_media(a,b,c):
#     x =(a+b+c) / 3
#     print(x)
#     return x

# media = obter_media(1,2,3)

# lista = [1,2,3,4]

# print(media)


how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)
