import cv2
import numpy as np

class Filters:
    # TODO: Image kernels
    Kernels = {
        'Original': [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        'Blur': np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9,
        'Gaussian blur': np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16,
        'Sharpen': [[0, -1, 0], [-1, 5, -1], [0, -1, 0]],
        'Sobel (x)': [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]],
        'Sobel (y)': [[-1, -2, -1], [0, 0, 0], [1, 2, 1]],
        'Edge detection': [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]],
        'emboss': [[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]
    }

    def __init__(self, kernels=Kernels):
        self.kernels = kernels
        self.current_filter = list(self.kernels.keys())
        self.count = 0
        # TODO: Implement internal variables

    def apply_filter(self, frame, filter_name) -> np.array:
        # TODO: Apply the selected filter kernel to the frame
        kernel = self.kernels[filter_name]
        return cv2.filter2D(frame, -1, kernel)


    def get_current_filter_name(self) -> str:
        # TODO: Return currently set kernels's name
        # self.current_filter = list(self.kernels.keys())
        # print(self.current_filter)
        return self.current_filter[self.count]

    def switch_next_filter(self):
        # TODO: Update currently selected kernel to the next
        self.count += 1
        if self.count >= len(self.current_filter):
            self.count = self.count % len(self.current_filter)
        # self.kernels[self.current_filter[self.count]]

    def switch_previous_filter(self):
        # TODO: Update currently selected kernel to the previous
        self.count -= 1
        self.kernels[self.current_filter[self.count]]
        if self.count < len(self.current_filter):
            self.count = self.count % len(self.current_filter)
