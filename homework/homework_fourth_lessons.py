"""
1. Розбити текст (буде нижче) таким чином, щоб після вказаних (буде нижче) слів речення починалося з нового абзацу
   з табуляцією.
   Слова після яких потрібно починати з нового абзацу: terminated , now , greatly , written , yet , scale
   Всі слова вказані вище повинні починатися з великої літери.
   В тексті також не можна нічого видаляти чи редагувати ! ! !
   Текст не можна виводити окремими частинами тобто кожен абзаца окремо один від одного ! ! !

   Текст:
   Do so written as raising parlors spirits mr elderly. Made late in of high left hold. Carried females of up highest
   calling. Limits marked led silent dining her she far. Sir but elegance marriage dwelling likewise position old
   pleasure men. Dissimilar themselves simplicity no of contrasted as. Delay great day hours men. Stuff front to do
   allow to asked he. yet 'remarkably' appearance get him his projection. Diverted endeavor "bed peculiar men the not
   desirous. Acuteness abilities ask" can offending "furnished" fulfilled sex. Warrant fifteen exposed ye at
   mistake. Blush since so in noisy still built up an again. As young ye hopes no he place means. Partiality
   diminution gay yet entreaties admiration. In mr it he mention perhaps attempt pointed suppose. Unknown ye chamber
   of warrant of norland arrived. written enquire painful ye to offices forming it. Then so does over sent dull
   on. Likewise offended humoured mrs fat trifling answered. On ye position greatest so desirous. So wound stood guest
   weeks no terms up ought. By so these am so rapid blush songs begin. Nor but mean time one over. greatly hearted has
   who believe. Drift allow green son walls years for blush. Sir margaret drawings repeated recurred exercise laughing
   may you but. Do repeated whatever to welcomed absolute no. Fat surprise although outlived and informed shy dissuade
   property. Musical by me through he drawing savings an. No we stand avoid 'decay heard mr'. Common so wicket appear to
   sudden worthy on. Shade of offer ye whole stood hoped. now indulgence dissimilar for his thoroughly has. Agreement o
   ffending \commanded my an. Change wholly say why eldest period. Are projection put celebrated particular unreserved
   joy unsatiable its. In then dare good am rose bred or. On am in nearer square wanted. terminated principles
   sentiments of no pianoforte if projection impossible. Horses pulled nature favour 'number yet highly his' has
   old. Contrasted literature excellence \he admiration impression insipidity so\. scale ought who terms after own
   quick since. Servants margaret husbands to screened in throwing. Imprudence oh an collecting partiality. Admiration
   gay difficulty unaffected how.
"""
# big_string = """Do so written as raising parlors spirits mr elderly. Made late in of high left hold. Carried females of up highest
#    calling. Limits marked led silent dining her she far. Sir but elegance marriage dwelling likewise position old
#    pleasure men. Dissimilar themselves simplicity no of contrasted as. Delay great day hours men. Stuff front to do
#    allow to asked he. \n\tyet \'remarkably\' appearance get him his projection. Diverted endeavor \"bed peculiar men the not
#    desirous. Acuteness abilities ask\" can offending \"furnished\" fulfilled sex. Warrant fifteen exposed ye at
#    mistake. Blush since so in noisy still built up an again. As young ye hopes no he place means. Partiality
#    diminution gay yet entreaties admiration. In mr it he mention perhaps attempt pointed suppose. Unknown ye chamber
#    of warrant of norland arrived. \n\twritten enquire painful ye to offices forming it. Then so does over sent dull
#    on. Likewise offended humoured mrs fat trifling answered. On ye position greatest so desirous. So wound stood guest
#    weeks no terms up ought. By so these am so rapid blush songs begin. Nor but mean time one over. \n\tgreatly hearted has
#    who believe. Drift allow green son walls years for blush. Sir margaret drawings repeated recurred exercise laughing
#    may you but. Do repeated whatever to welcomed absolute no. Fat surprise although outlived and informed shy dissuade
#    property. Musical by me through he drawing savings an. No we stand avoid \'decay heard mr\'. Common so wicket appear to
#    sudden worthy on. Shade of offer ye whole stood hoped. \n\tnow indulgence dissimilar for his thoroughly has. Agreement
#    offending \\commanded my an. Change wholly say why eldest period. Are projection put celebrated particular unreserved
#    joy unsatiable its. In then dare good am rose bred or. On am in nearer square wanted. \n\tterminated principles
#    sentiments of no pianoforte if projection impossible. Horses pulled nature favour \'number yet highly his\' has
#    old. Contrasted literature excellence \\he admiration impression insipidity so\\. \n\tscale ought who terms after own
#    quick since. Servants margaret husbands to screened in throwing. Imprudence oh an collecting partiality. Admiration
#    gay difficulty unaffected how."""
#
#
# print(big_string)

"""
2. Написати скрипт, який до перемінної 'default_var' добавить інший 'second_def_var' і в результаті буде виведено:

   2.1. ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE', ['Ukraine', 'USA', 'Greate Britain', 'Poland', 'Canada', 'Brazil']]
   2.2. ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE', 'Ukraine', 'USA', 'Greate Britain', 'Poland', 'Canada', 'Brazil']
   2.3.* ['Kyiv', 'Odessa', ['Ukraine', 'USA', 'Greate Britain', 'Poland', 'Canada', 'Brazil'], 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
   
   Перемінні:
   default_var = ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
   second_def_var = ['Ukraine', 'USA', 'Greate Britain', 'Poland', 'Canada', 'Brazil'] 
"""
# default_var = ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
# second_def_var = ['Ukraine', 'USA', 'Greate Britain', 'Poland', 'Canada', 'Brazil']
# default_var.append(second_def_var)
# print(default_var)
#
# default_var = ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
# second_def_var = ['Ukraine', 'USA', 'Greate Britain', 'Poland', 'Canada', 'Brazil']
# default_var.extend(second_def_var)
# print(default_var)
#
# default_var = ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
# second_def_var = ['Ukraine', 'USA', 'Greate Britain', 'Poland', 'Canada', 'Brazil']
# default_var.insert(2, second_def_var)
# print(default_var)

"""
3. З перемінної "default_var" потрібно перенести весь список до перемінної 'list_of_variabeles' після чого з 
   "default_var":
   3.1. видалити всі дані;
   3.2. видалити міста 'Dnipro', 'Odessa', 'Kharkiv', 'Washington' ;
   3.3. видалити міста під індексом 0, 5, 7, 9 ;
   
   В консолі дані мають бути виведені в такому вигляді:
   ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
   []
   ['Kyiv', 'Lviv', 'Bila Cherkva', 'London', 'Bohuslav', 'OAE']
   ['Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'London', 'Washington']
   
   Перемінні:
   default_var = ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
   list_of_variabeles
"""
# default_var = ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
# list_of_variabeles = default_var.copy()
# default_var.clear()
#
# print(list_of_variabeles, default_var, sep='\n')
#
# list_of_variabeles.remove('Dnipro')
# list_of_variabeles.remove('Odessa')
# list_of_variabeles.remove('Kharkiv')
# list_of_variabeles.remove('Washington')
# print(list_of_variabeles)
#
# default_var = ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
# list_of_variabeles = default_var.copy()
# list_of_variabeles.pop(0)
# list_of_variabeles.pop(5)
# list_of_variabeles.pop(7)
# list_of_variabeles.pop(5)
# print(list_of_variabeles)
"""
4. Написати скрипт, який в перемінній "default_var":
   4.1. відсортує дані в алфавітному порядку ;
   4.2. зробить так, щоб дані відображались в зворотньому порядку ;
   4.3.* відсортує список в алфавітному порядку і виведе його в зворотньому порядку
   
   В консолі дані мають бути виведені в такому вигляді:
   ['Bila Cherkva', 'Bohuslav', 'Dnipro', 'Kharkiv', 'Kyiv', 'London', 'Lviv', 'OAE', 'Odessa', 'Washington']
   ['OAE', 'Washington', 'Bohuslav', 'London', 'Kharkiv', 'Dnipro', 'Bila Cherkva', 'Lviv', 'Odessa', 'Kyiv']
   ['Washington', 'Odessa', 'OAE', 'Lviv', 'London', 'Kyiv', 'Kharkiv', 'Dnipro', 'Bohuslav', 'Bila Cherkva']
   
    Перемінна:
    default_var = ['Kyiv', 'O
    dessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
"""
# default_var = ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
# default_var.sort()
# print(default_var)
#
# default_var = ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
# default_var.reverse()
# print(default_var)
#
# default_var = ['Kyiv', 'Odessa', 'Lviv', 'Bila Cherkva', 'Dnipro', 'Kharkiv', 'London', 'Bohuslav', 'Washington', 'OAE']
# default_var.sort(reverse=True)
# print(default_var)
