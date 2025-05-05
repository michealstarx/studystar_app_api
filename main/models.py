from django.db import models

class Home(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    quote = models.CharField(max_length=7000, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    
    # images
    imageOne = models.TextField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    linkOne = models.TextField(blank=True, null=True)
    numberOne = models.IntegerField(blank=True, null=True)
    
    imageTwo = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    linkTwo = models.TextField(blank=True, null=True)
    numberTwo = models.IntegerField(blank=True, null=True)
    
    imageThree = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    linkThree = models.TextField(blank=True, null=True)
    numberThree = models.IntegerField(blank=True, null=True)
    
    imageFour = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    linkFour = models.TextField(blank=True, null=True)
    numberFour = models.IntegerField(blank=True, null=True)
    
    imageFive = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    linkFive = models.TextField(blank=True, null=True)
    numberFive = models.IntegerField(blank=True, null=True)
    
    imageSix = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    linkSix = models.TextField(blank=True, null=True)
    numberSix = models.IntegerField(blank=True, null=True)
    
    imageSeven = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    linkSeven = models.TextField(blank=True, null=True)
    numberSeven = models.IntegerField(blank=True, null=True)
    
    imageEight = models.TextField(blank=True, null=True)
    textEight = models.TextField(blank=True, null=True)
    linkEight = models.TextField(blank=True, null=True)
    numberEight = models.IntegerField(blank=True, null=True)
    
    imageNine = models.TextField(blank=True, null=True)
    textNine = models.TextField(blank=True, null=True)
    linkNine = models.TextField(blank=True, null=True)
    numberNine = models.IntegerField(blank=True, null=True)
    
    imageTen = models.TextField(blank=True, null=True)
    textTen = models.TextField(blank=True, null=True)
    linkTen = models.TextField(blank=True, null=True)
    numberTen = models.IntegerField(blank=True, null=True)
    
    imageEleven = models.TextField(blank=True, null=True)
    textEleven = models.TextField(blank=True, null=True)
    linkEleven = models.TextField(blank=True, null=True)
    numberEleven = models.IntegerField(blank=True, null=True)
    
    imageTwelve = models.TextField(blank=True, null=True)
    textTwelve = models.TextField(blank=True, null=True)
    linkTwelve = models.TextField(blank=True, null=True)
    numberTwelve = models.IntegerField(blank=True, null=True)
    
    imageThirteen = models.TextField(blank=True, null=True)
    textThirteen = models.TextField(blank=True, null=True)
    linkThirteen = models.TextField(blank=True, null=True)
    numberThirteen = models.IntegerField(blank=True, null=True)
    
    imageFourteen = models.TextField(blank=True, null=True)
    textFourteen = models.TextField(blank=True, null=True)
    linkFourteen = models.TextField(blank=True, null=True)
    numberFourteen = models.IntegerField(blank=True, null=True)
    
    imageFifteen = models.TextField(blank=True, null=True)
    textFifteen = models.TextField(blank=True, null=True)
    linkFifteen = models.TextField(blank=True, null=True)
    numberFifteen = models.IntegerField(blank=True, null=True)
    
    imageSixteen = models.TextField(blank=True, null=True)
    textSixteen = models.TextField(blank=True, null=True)
    linkSixteen = models.TextField(blank=True, null=True)
    numberSixteen = models.IntegerField(blank=True, null=True)
    
    imageSeventeen = models.TextField(blank=True, null=True)
    textSeventeen = models.TextField(blank=True, null=True)
    linkSeventeen = models.TextField(blank=True, null=True)
    numberSeventeen = models.IntegerField(blank=True, null=True)
    
    imageEighteen = models.TextField(blank=True, null=True)
    textEighteen = models.TextField(blank=True, null=True)
    linkEighteen = models.TextField(blank=True, null=True)
    numberEighteen = models.IntegerField(blank=True, null=True)
    
    imageNineteen = models.TextField(blank=True, null=True)
    textNineteen = models.TextField(blank=True, null=True)
    linkNineteen = models.TextField(blank=True, null=True)
    numberNineteen = models.IntegerField(blank=True, null=True)
    
    imageTwenty = models.TextField(blank=True, null=True)
    textTwenty = models.TextField(blank=True, null=True)
    linkTwenty = models.TextField(blank=True, null=True)
    numberTwenty = models.IntegerField(blank=True, null=True)

    
    def __str__(self):
        return self.screen
    
    
class Books(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    free = models.CharField(max_length=120, blank=True, null=True)
    
        
    extraTwo = models.TextField(blank=True, null=True)
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class Podcasts(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    dimensionx = models.IntegerField(blank=True, null=True)
    dimensiony = models.IntegerField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class Videos(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    dimensionx = models.IntegerField(blank=True, null=True)
    dimensiony = models.IntegerField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.screen
    

class Biology(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    specificGrade = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    
    price = models.IntegerField(blank=True, null=True)
    imageLink = models.TextField(blank=True, null=True)
    imagedimensionx = models.IntegerField(blank=True, null=True)
    imagedimensiony = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    fileLink = models.TextField(blank=True, null=True)
    brainBoosterText = models.TextField(blank=True, null=True)
    brainBoosterLink = models.TextField(blank=True, null=True)
    practiceTestText = models.TextField(blank=True, null=True)
    practiceTestLink = models.TextField(blank=True, null=True)
    practiceTestAnswerText = models.TextField(blank=True, null=True)
    practiceTestAnswerLink = models.TextField(blank=True, null=True)
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class Chemistry(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    specificGrade = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    
    price = models.IntegerField(blank=True, null=True)
    imageLink = models.TextField(blank=True, null=True)
    imagedimensionx = models.IntegerField(blank=True, null=True)
    imagedimensiony = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    fileLink = models.TextField(blank=True, null=True)
    brainBoosterText = models.TextField(blank=True, null=True)
    brainBoosterLink = models.TextField(blank=True, null=True)
    practiceTestText = models.TextField(blank=True, null=True)
    practiceTestLink = models.TextField(blank=True, null=True)
    practiceTestAnswerText = models.TextField(blank=True, null=True)
    practiceTestAnswerLink = models.TextField(blank=True, null=True)
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class English(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    specificGrade = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    
    price = models.IntegerField(blank=True, null=True)
    imageLink = models.TextField(blank=True, null=True)
    imagedimensionx = models.IntegerField(blank=True, null=True)
    imagedimensiony = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    fileLink = models.TextField(blank=True, null=True)
    brainBoosterText = models.TextField(blank=True, null=True)
    brainBoosterLink = models.TextField(blank=True, null=True)
    practiceTestText = models.TextField(blank=True, null=True)
    practiceTestLink = models.TextField(blank=True, null=True)
    practiceTestAnswerText = models.TextField(blank=True, null=True)
    practiceTestAnswerLink = models.TextField(blank=True, null=True)
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class Mathematics(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    specificGrade = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    
    price = models.IntegerField(blank=True, null=True)
    imageLink = models.TextField(blank=True, null=True)
    imagedimensionx = models.IntegerField(blank=True, null=True)
    imagedimensiony = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    fileLink = models.TextField(blank=True, null=True)
    brainBoosterText = models.TextField(blank=True, null=True)
    brainBoosterLink = models.TextField(blank=True, null=True)
    practiceTestText = models.TextField(blank=True, null=True)
    practiceTestLink = models.TextField(blank=True, null=True)
    practiceTestAnswerText = models.TextField(blank=True, null=True)
    practiceTestAnswerLink = models.TextField(blank=True, null=True)
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class Physics(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    specificGrade = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    
    price = models.IntegerField(blank=True, null=True)
    imageLink = models.TextField(blank=True, null=True)
    imagedimensionx = models.IntegerField(blank=True, null=True)
    imagedimensiony = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    fileLink = models.TextField(blank=True, null=True)
    brainBoosterText = models.TextField(blank=True, null=True)
    brainBoosterLink = models.TextField(blank=True, null=True)
    practiceTestText = models.TextField(blank=True, null=True)
    practiceTestLink = models.TextField(blank=True, null=True)
    practiceTestAnswerText = models.TextField(blank=True, null=True)
    practiceTestAnswerLink = models.TextField(blank=True, null=True)
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
    
class BiNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class ChNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class CsNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class LaNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class MaNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class PhNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class AnatomyOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

class AnatomyOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class BiochemistryOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

class BiochemistryOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class ClinicalScienceOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class ClinicalScienceOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

    
class DiagnosticsOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

class DiagnosticsOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class LabScienceOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

class LabScienceOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class PathologyOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

class PathologyOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class PhysiologyOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class PhysiologyOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class PublicHealthOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class PublicHealthOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class SocietyAndMedicineOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class SocietyAndMedicineOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class TherapeuticsOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class TherapeuticsOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class AnatomyTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

class AnatomyTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class BiochemistryTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

class BiochemistryTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class ClinicalScienceTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class ClinicalScienceTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

    
class DiagnosticsTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

class DiagnosticsTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class LabScienceTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

class LabScienceTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class PathologyTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title

class PathologyTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class PhysiologyTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class PhysiologyTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class PublicHealthTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class PublicHealthTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class SocietyAndMedicineTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class SocietyAndMedicineTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class TherapeuticsTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
class TherapeuticsTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    
    
    extraThree = models.TextField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title
    
