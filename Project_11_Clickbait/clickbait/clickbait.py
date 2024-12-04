
import random
from clickbait.clickbait_utils import BaitHeadlineGenerator
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

class Game:

    def __init__(self):
        self.generator = BaitHeadlineGenerator()

    def main(self):
        print('Clickbait Headline Generator')
        print('By Al Sweigart al@inventwithpython.com')
        print()
        print('Our website needs to trick people into looking at ads!')
        while True:
            print('Enter the number of clickbait headlines to generate:')
            response = input('> ')
            if not response.isdecimal():
                print('Please enter a number.')
            else:
                number_Of_headlines = int(response)
                break  
        for i in range(number_Of_headlines):
            clickbaitType = random.randint(1, 8)
            headline = ''
            if clickbaitType == 1:
                headline =  self.generator.generateAreMillennialsKillingHeadline()
            elif clickbaitType == 2:
                headline =  self.generator.generateWhatYouDontKnowHeadline()
            elif clickbaitType == 3:
                headline =  self.generator.generateBigCompaniesHateHerHeadline()
            elif clickbaitType == 4:
                headline =  self.generator.generateYouWontBelieveHeadline()
            elif clickbaitType == 5:
                headline = self.generator.generateDontWantYouToKnowHeadline()
            elif clickbaitType == 6:
                headline = self.generator.generateGiftIdeaHeadline()
            elif clickbaitType == 7:
                headline = self.generator.generateReasonsWhyHeadline()
            elif clickbaitType == 8:
                headline = self.generator.generateJobAutomatedHeadline()
            print(headline)
        print()
        website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                                 'Facesbook', 'Tweedie', 'Pastagram'])
        when = random.choice(WHEN).lower()
        print('Post these to our', website, when, 'or you\'re fired!')