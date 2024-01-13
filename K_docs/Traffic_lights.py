#!/usr/bin/env python
from samplebase import SampleBase
import time


class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        while True:
            for x in range(0, self.matrix.width):
                for y in range(0, self.matrix.height):
                    # offset_canvas.Clear()
                    offset_canvas.SetPixel(x, y, 255, 0, 0)
                    # time.sleep(0.2)
                    
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)


# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if (not simple_square.process()):
        simple_square.print_help()
