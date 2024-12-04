from clickbait.clickbait_utils import BaitHeadlineGenerator
from unittest.mock import patch

# Тест для generateAreMillennialsKillingHeadline


def test_generateAreMillennialsKillingHeadline():
    with patch('random.choice', return_value="Plastic Straw"):
        generator = BaitHeadlineGenerator()
        result = generator.generateAreMillennialsKillingHeadline()
        assert result == "Are Millennials Killing the Plastic Straw Industry?"

# Тест для generateWhatYouDontKnowHeadline


def test_generateWhatYouDontKnowHeadline():
    with patch('random.choice', side_effect=["Plastic Straw", "Shovels", "RIGHT NOW"]):
        generator = BaitHeadlineGenerator()
        result = generator.generateWhatYouDontKnowHeadline()
        assert result == "Without This Plastic Straw, Shovels Could Kill You RIGHT NOW"


# Тест для generateBigCompaniesHateHerHeadline


def test_generateBigCompaniesHateHerHeadline():
    with patch('random.choice', side_effect=["Her", "Texas", "Plastic Straw", "Athlete"]):
        generator = BaitHeadlineGenerator()
        result = generator.generateBigCompaniesHateHerHeadline()
        assert result == "Big Companies Hate Her! See How This Texas Plastic Straw Invented a Cheaper Athlete"

# Тест для generateYouWontBelieveHeadline


def test_generateYouWontBelieveHeadline():
    with patch('random.choice', side_effect=["California", "Athlete", "His", "Bank Deposit Box"]):
        generator = BaitHeadlineGenerator()
        result = generator.generateYouWontBelieveHeadline()
        assert result == "You Won't Believe What This California Athlete Found in His Bank Deposit Box"

# Тест для generateDontWantYouToKnowHeadline


def test_generateDontWantYouToKnowHeadline():
    with patch('random.choice', side_effect=["Plastic Straws", "Athletes"]):
        generator = BaitHeadlineGenerator()
        result = generator.generateDontWantYouToKnowHeadline()
        assert result == "What Plastic Straws Don't Want You To Know About Athletes"

# Тест для generateGiftIdeaHeadline


def test_generateGiftIdeaHeadline():
    with patch('random.randint', return_value=10), patch('random.choice', side_effect=["Athlete", "California"]):
        generator = BaitHeadlineGenerator()
        result = generator.generateGiftIdeaHeadline()
        assert result == "10 Gift Ideas to Give Your Athlete From California"

# Тест для generateReasonsWhyHeadline


def test_generateReasonsWhyHeadline():
    with patch('random.randint', side_effect=[10, 5]), patch('random.choice', return_value="Plastic Straw"):
        generator = BaitHeadlineGenerator()
        result = generator.generateReasonsWhyHeadline()
        assert result == "10 Reasons Why Plastic Straws Are More Interesting Than You Think (Number 5) Will Surprise You!"

# Тест для generateJobAutomatedHeadline


def test_generateJobAutomatedHeadline():
    # Патчим случайные значения, чтобы гарантировать корректный вывод
    with patch('random.choice', side_effect=["Texas", "Plastic Straw", "Her", "She"]), patch('random.randint', return_value=0):
        generator = BaitHeadlineGenerator()
        result = generator.generateJobAutomatedHeadline()
        # Ожидаем, что pronoun1 будет "Her", а pronoun2 будет "She", и итоговая строка будет с "Was"
        assert result == "This Texas Plastic Straw Didn't Think Robots Would Take Her Job. She Was Wrong."
