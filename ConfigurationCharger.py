import io


class ChargeConfigurationClass():    

    def __init__(self):
        self.WIDTH_SCREEN = 0
        self.HEIGHT_SCREEN = 0
        self.TOTAL_BACKGROUND_STARS = 0
        self.__listConfiguration = []
        
        self.ChargeConfiguration()

    def ChargeConfiguration(self):
        configurationFile = io.open('configurationGame', 'r')
        x = configurationFile.read().split('\n')

        for i in x: 
            self.__listConfiguration.append(i)

        self.extractWidthScreen()
        self.extractHeightScreen()
        self.extractStarsBackground()

    def extractWidthScreen(self):
        for x in self.__listConfiguration:
            if str(x).startswith('WIDTH'):
                self.WIDTH_SCREEN = int(x.split(':')[1])

    def extractHeightScreen(self):
        for x in self.__listConfiguration:
            if str(x).startswith('HEIGHT'):
                self.HEIGHT_SCREEN = int(x.split(':')[1])

    def extractStarsBackground(self):
        for x in self.__listConfiguration:
            if str(x).startswith('TOTAL_BACKGROUND_STARS'):
                self.TOTAL_BACKGROUND_STARS = int(x.split(':')[1])

    def GetHeightScreen(self):
        return self.HEIGHT_SCREEN

    def GetWidthScreen(self):
        return self.WIDTH_SCREEN

    def GetTotalBackgroundStars(self):
        return self.TOTAL_BACKGROUND_STARS