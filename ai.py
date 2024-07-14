import numpy as np
import numpy.typing as npt

np.random.seed(0)

class LayerDense:
    weights: npt.NDArray[np.float32]
    biases: npt.NDArray[np.float32]
    output: npt.NDArray[np.float32]

def create_layer(n_inputs: int, n_neurons) ->LayerDense:
    layer = LayerDense()
    layer.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
    layer.biases = np.zeros((1, n_neurons))

    return layer

def forward(layer: LayerDense, inputs: npt.NDArray[np.float32]) ->None:
    layer.output = np.dot(inputs, layer.weights) + layer.biases