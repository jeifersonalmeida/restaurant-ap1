class Utils():

    @staticmethod
    def getUserOption(min, max):
        option = int(input("\n -> "))
        if(option < min or option > max):
            return -1
        return option