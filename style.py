class colors:
    def __init__(self):
        self.colorScheme = self.simple
        self.colorSchemes = [
            self.simple,
            self.stripy,
            self.rainbow,
        ]

    def get(self, mandelbrotgetal, max=100):
        return self.colorScheme(mandelbrotgetal, max)

    def simple(self, mandelbrotgetal, max):
        if mandelbrotgetal == max:
            return "#000"
        else:
            return "#fff"

    def stripy(self, mandelbrotgetal, max):
        if mandelbrotgetal == max:
            return "#000"
        elif mandelbrotgetal % 2 == 0:
            return "#000"
        else:
            return "#FFF"

    def rainbow(self, mandelbrotgetal, max):
        if mandelbrotgetal == max:
            return "#000"
        else:
            colors = ["#ff0000", "#ff4000", "#ff8000", "#ffbf00", "#ffff00", "#bfff00", "#80ff00", "#40ff00", "#00ff00",
                      "#00ff40", "#00ff80", "#00ffbf", "#00ffff", "#00bfff", "#0080ff", "#0040ff", "#0000ff", "#4000ff",
                      "#8000ff", "#bf00ff", "#ff00ff", "#ff00bf", "#ff0080", "#ff0040", "#ff0000"]
            return colors[(mandelbrotgetal -1)% len(colors)]
