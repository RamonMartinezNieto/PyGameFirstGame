import io
from os import execlp
from pygame import Surface
from pygame import SRCALPHA
class ChargeConfigurationClass():    

    def __init__(self):
        self.__listConfigurationParameters = []

        #Init with default values
        self.WIDTH_SCREEN = 600
        self.HEIGHT_SCREEN = 800
        self.TOTAL_BACKGROUND_STARS = 20
        self.STARS_PER_SURFACE = 4
        self.RESERVED_SURFACES = 5;
        
        self.LIST_SURFACES = []

        self._chargeConfiguration()
        self._createAllSurfaces()

    def _chargeConfiguration(self):
        try:
            configurationFile = io.open('resources\configurationGame', 'r')
            x = configurationFile.read().split('\n')

            for i in x: 
                self.__listConfigurationParameters.append(i)
            
            self.WIDTH_SCREEN = self._extractAttributeInt('WIDTH_SCREEN')
            self.HEIGHT_SCREEN = self._extractAttributeInt('HEIGHT_SCREEN')
            self.TOTAL_BACKGROUND_STARS = self._extractAttributeInt('TOTAL_BACKGROUND_STARS')
            self.STARS_PER_SURFACE = self._extractAttributeInt('STARS_PER_SURFACE')
        except:
            pass




    def _extractAttributeInt(self,string_attribute):
        parameter = 0
        
        for x in self.__listConfigurationParameters:
            if str(x).startswith(string_attribute):
                try:
                    value = int(x.split(':')[1])
                    return value
                except:
                    return eval('self.'+string_attribute)
                    


    def _createAllSurfaces(self):
        
        total_surfaces = (self.TOTAL_BACKGROUND_STARS//self.STARS_PER_SURFACE) + self.RESERVED_SURFACES;  

        if total_surfaces > 30: 
            raise Exception('No more than 30 surfaces is allowed')
    
        for i in range(total_surfaces):
            self.LIST_SURFACES.append(Surface((self.WIDTH_SCREEN,self.HEIGHT_SCREEN), SRCALPHA))


    ### GETTERS 
    def GetHeightScreen(self):
        return self.HEIGHT_SCREEN

    def GetWidthScreen(self):
        return self.WIDTH_SCREEN

    def GetTotalBackgroundStars(self):
        return self.TOTAL_BACKGROUND_STARS

    def GetStarsPerSurface(self):
        return self.STARS_PER_SURFACE

    def GetTotalReservedSurfaces(self):
        return self.RESERVED_SURFACES

    def GetTotalSurfaces(self):
        return self.LIST_SURFACES

    # Surfaces
    def GetStarsSurfaces(self): 
        return self.LIST_SURFACES[self.RESERVED_SURFACES:]

    def get_principal_surface(self):
        return self.LIST_SURFACES[0]
