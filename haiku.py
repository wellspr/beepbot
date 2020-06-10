# https://examples.yourdictionary.com/examples-of-haiku-poems.html
def haiku_info(info):

    intro_to_haiku = [
        "A haiku is traditionally a Japanese poem consisting of three short lines that do not rhyme. The origins of haiku poems can be traced back as far as the 9th century.",

        "A haiku is considered to be more than a type of poem; it is a way of looking at the physical world and seeing something deeper, like the very nature of existence. It should leave the reader with a strong feeling or impression. Take a look at the following examples of traditional and modern haiku poems to see what we mean."
        ]

    haiku_masters = [
        "There were four master haiku poets from Japan, known as \"the Great Four:\" Matsuo Basho, Kobayashi Issa, Masaoka Shiki, and Yosa Buson. Their work is still the model for traditional haiku writing today. We have also included examples from Natsume Soseki here, a famed novelist and contemporary of Shiki, who also wrote haiku.",

        "Reviewing examples of haiku poems is an excellent way to become familiar with this form of poetry and the sensory language it uses, and gain some inspiration.",

        "In Japanese, there are five \"moras\" in the first and third line, and seven in the second, following the standard 5-7-5 structure of haiku. A mora is a sound unit, much like a syllable, but is not identical to it. This rhythm is often lost in translation, as not every English word has the same number of syllables, or moras, as its Japanese counterpart. For example, haiku has two syllables in English and in Japanese, it has three moras."
        ]

    Matsuo_Basho = {

        "intro" : "Here are three examples of haiku poems from Matsuo Basho (1644-1694), considered the greatest haiku poet.",

        "haikus" : [
            [
                "An old silent pond...",
                "A frog jumps into the pond,",
                "splash! Silence again."
            ],

            [
                "Autumn moonlight-",
                "a worm digs silently",
                "into the chestnut."
            ],

            [
                "In the twilight rain",
                "these brilliant-hued hibiscus -",
                "A lovely sunset."
            ]
        ]
    }

    Yosa_Buson = {
        "intro" : "Here are three examples of haiku poems from Yosa Buson (1716-1784), a haiku master poet and painter.",

        "haikus" : [
            [
                "A summer river being crossed",
                "how pleasing",
                "with sandals in my hands!"
            ],

            [
                "Light of the moon",
                "Moves west, flowers' shadows",
                "Creep eastward."
            ],

            [
                "In the moonlight,",
                "The color and scent of the wisteria",
                "Seems far away."
            ]
        ]
    }

    Kobayashi_Issa = {
        "intro" : "Here are three examples of haiku from Kobayashi Issa (1763-1828), a renowned haiku poet.",

        "haikus" : [
            [
                "O snail",
                "Climb Mount Fuji,",
                "But slowly, slowly!"
            ],

            [
                "Trusting the Buddha, good and bad,",
                "I bid farewell",
                "To the departing year."
            ],

            [
                "Everything I touch",
                "with tenderness, alas,",
                "pricks like a bramble."
            ]
        ]
    }

    Masaoka_Shiki = {
        "intro" : "Here are seven examples of haiku poems from Masaoka Shiki (1867-1902), credited with reviving the haiku and developing its modern format.",

        "haikus" : [
            [
                "I want to sleep",
                "Swat the flies",
                "Softly, please."
            ],

            [
                "After killing",
                "a spider, how lonely I feel",
                "in the cold of night!"
            ],

            [
                "For love and for hate",
                "I swat a fly and offer it",
                "to an ant."
            ],

            [
                "A mountain village",
                "under the piled-up snow",
                "the sound of water."
            ],

            [
                "Night; and once again,",
                "the while I wait for you, cold wind",
                "turns into rain."
            ],

            [
                "The summer river:",
                "although there is a bridge, my horse",
                "goes through the water."
            ],

            [
                "A lightning flash:",
                "between the forest trees",
                "I have seen water."
            ]
        ]
    }

    Natsume_Soseki = {
        "intro" : "Natsume Soseki (1867-1916) was a widely respected novelist who also had many fairy tales and haiku published. Here are three examples of his haikus.",

        "haikus" : [
            [
                "The lamp once out",
                "Cool stars enter",
                "The window frame."
            ],

            [
                "Plum flower temple:",
                "Voices rise",
                "From the foothills"
            ],

            [
                "The crow has flown away",
                "swaying in the evening sun,",
                "a leafless tree."
            ]
        ]
    }

    modern_haiku = {

        "intro" : [
            "Many modern western poets do not subscribe to the 5-7-5 pattern. The Academy of American Poets recognizes this evolution, but maintains that several core principles remain woven into the tapestry of modern haiku. That is, a haiku still focuses on one brief moment in time, employs provocative, colorful imagery, and provides a sudden moment of illumination.",

            "Here are seven examples of 20th-century haiku poems:"
        ],

        "haikus" : [

            [
                [
                    "From across the lake,",
                    "Past the black winter trees,",
                    "Faint sounds of a flute."
                ],

                [ "Richard Wright" ]
            ],

            [
                [
                    "Lily:",
                    "out of the water",
                    "out of itself"
                ],

                [ "Nick Virgilio" ]
            ],

            [
                [
                    "ground squirrel",
                    "balancing its tomato",
                    "on the garden fence"
                ],

                [ "Don Eulert" ]
            ],

            [
                [
                    "Nightfall,",
                    "Too dark to read the page",
                    "Too cold."
                ],

                [ "Jack Kerouac" ]
            ],

            [
                [
                    "Just friends:",
                    "he watches my gauze dress",
                    "blowing on the line."
                ],

                [ "Alexis Rotella" ]
            ],

            [
                [
                    "A little boy sings",
                    "on a terrace, eyes aglow.",
                    "Ridge spills upward."
                ],

                [ "Robert Yehling" ]
            ],

            [
                [
                    "meteor shower",
                    "a gentle wave",
                    "wets our sandals"
                ],

                [ "Michael Dylan Welch" ]
            ]
        ]
    }

    masters = {
        "Matsuo Basho" : Matsuo_Basho,
        "Yosa Buson" : Yosa_Buson,
        "Kobayashi Issa" : Kobayashi_Issa,
        "Masaoka Shiki" : Masaoka_Shiki,
        "Natsume Soseki" : Natsume_Soseki
    }

    if info == "intro_to_haiku":
        return intro_to_haiku
    elif info == "haiku_masters":
        return haiku_masters
    elif info == "modern_haiku":
        return modern_haiku
    elif info == "masters":
        return masters

# Functions
def display_authors(authors):
    count = 0;
    print("")
    for author in authors:
        print(str(count) + " : " + author)
        count+=1
    print("")

def display_haiku(haiku):
    print("")
    for line in haiku:
        print("     " + line)
    print("")

def display_haiku_author(author):
    if type(author) == str:
        print("     - " + author)
    print("")

def display_haiku_and_author(haiku,author):
    display_haiku(haiku)
    display_haiku_author(author)

def random_index(range):
    import random
    return random.randrange(range)

def create_list_of_authors_from(source_of_authors):
    authors = []
    for item in source_of_authors.keys():
        authors.append(item)
    return authors

def get_classic_haiku():
    authors_source = haiku_info("masters")
    # Get a list of authors and display to user
    authors = create_list_of_authors_from(authors_source)
    # Total of Authors
    total_of_authors = len(authors)
    # Choose a random index from authors list
    author_index = random_index(int(total_of_authors))
    # Set chosen author from Dictionary
    my_author = authors_source.get(authors[int(author_index)])
    my_author_name = authors[author_index]
    # Get Haikus from selected author
    haikus = my_author.get("haikus")
    # Total of haikus
    total_of_haikus = len(haikus)
    # Choose a random index of Haikus
    haiku_index = random_index(int(total_of_haikus))
    # Choose a random Haiku
    my_haiku = haikus[haiku_index]
    return [my_haiku,my_author_name]

def get_modern_haiku():
    modern_haiku_source = haiku_info("modern_haiku")
    modern_haikus = modern_haiku_source.get("haikus")
    modern_haiku_index = random_index(len(modern_haikus))
    modern_haiku = modern_haikus[modern_haiku_index][0]
    modern_haiku_author = modern_haikus[modern_haiku_index][1][0]
    return [modern_haiku,modern_haiku_author]

def display_classic_haiku():
    haiku = get_classic_haiku()
    my_haiku = haiku[0]
    my_author_name = haiku[1]
    display_haiku_and_author(my_haiku, my_author_name)

def display_modern_haiku():
    haiku = get_modern_haiku()
    my_haiku = haiku[0]
    my_author_name = haiku[1]
    display_haiku_and_author(my_haiku, my_author_name)

def get_random_haiku():
    import random
    choice = random.randint(0,1)
    if choice == 0:
        return get_classic_haiku()
    else:
        return get_modern_haiku()

def display_random_haiku():
    import random
    choice = random.randint(0,1)
    if choice == 0:
        display_classic_haiku()
    else:
        display_modern_haiku()
