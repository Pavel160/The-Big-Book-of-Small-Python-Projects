import random


class BaitHeadlineGenerator:
    def __init__(self):
        self.OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
        self.POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
        self.PERSONAL_PRONOUNS = ['She', 'He', 'They']
        self.STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
                       'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
        self.NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
                      'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
        self.PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
                       'Workplace', 'Donut Shop', 'Apocalypse Bunker']
        self.WHEN = ['Soon', 'This Year',
                     'Later Today', 'RIGHT NOW', 'Next Week']

    def generateAreMillennialsKillingHeadline(self):
        noun = random.choice(self.NOUNS)
        return 'Are Millennials Killing the {} Industry?'.format(noun)

    def generateWhatYouDontKnowHeadline(self):
        noun = random.choice(self.NOUNS)
        # Use already plural noun from list
        pluralNoun = random.choice(self.NOUNS)
        when = random.choice(self.WHEN)
        return ('Without This {}, {} Could Kill You {}').format(noun, pluralNoun, when)

    def generateBigCompaniesHateHerHeadline(self):
        pronoun = random.choice(self.OBJECT_PRONOUNS)
        state = random.choice(self.STATES)
        noun1 = random.choice(self.NOUNS)
        noun2 = random.choice(self.NOUNS)
        return ('Big Companies Hate {}! See How This {} {} Invented a Cheaper {}').format(pronoun, state, noun1, noun2)

    def generateYouWontBelieveHeadline(self):
        state = random.choice(self.STATES)
        noun = random.choice(self.NOUNS)
        pronoun = random.choice(self.POSSESIVE_PRONOUNS)
        place = random.choice(self.PLACES)
        return ('You Won\'t Believe What This {} {} Found in {} {}').format(state, noun, pronoun, place)

    def generateDontWantYouToKnowHeadline(self):
        pluralNoun1 = random.choice(self.NOUNS)  # Don't add 's' here
        pluralNoun2 = random.choice(self.NOUNS)  # Don't add 's' here
        return ('What {} Don\'t Want You To Know About {}').format(pluralNoun1, pluralNoun2)

    def generateGiftIdeaHeadline(self):
        number = random.randint(7, 15)
        noun = random.choice(self.NOUNS)
        state = random.choice(self.STATES)
        return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)

    def generateReasonsWhyHeadline(self):
        number1 = random.randint(3, 19)
        noun = random.choice(self.NOUNS)

        # Удостоверимся, что существительное во множественном числе
        pluralNoun = noun if noun.endswith('s') else noun + 's'

        number2 = random.randint(1, number1)
        return ('{} Reasons Why {} Are More Interesting Than You Think '
                '(Number {}) Will Surprise You!').format(number1, pluralNoun, number2)

    def generateJobAutomatedHeadline(self):
        state = random.choice(self.STATES)
        noun = random.choice(self.NOUNS)
        i = random.randint(0, 2)
        pronoun1 = self.POSSESIVE_PRONOUNS[i]
        pronoun2 = self.PERSONAL_PRONOUNS[i]
    
        # Убедимся, что для "Their" используем "They Were", а для "Her" - "She Was"
        if pronoun1 == 'Their':  # Для "Their" используется "They Were"
            return ('This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.').format(state, noun, pronoun1, pronoun2)
        else:  # Для других местоимений используется "Was" и "Her"
            return ('This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.').format(state, noun, pronoun1, pronoun2)
