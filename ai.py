import numpy as np
import numpy.typing as npt

np.random.seed(0)

class LayerDense:
    weights: npt.NDArray[np.float32]
    biases: npt.NDArray[np.float32]

def create_layer(n_inputs: int, n_neurons) ->LayerDense:
    layer = LayerDense()
    layer.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
    layer.biases = np.zeros((1, n_neurons))

    return layer

def forward(layer: LayerDense, inputs: npt.NDArray[np.float32]) ->npt.NDArray[np.float32]:
    result = np.dot(inputs, layer.weights) + layer.biases
    return result

def relu_forward(input: npt.NDArray[np.float32])->npt.NDArray[np.float32]:
   result = np.maximum(0, input)
   return result

def softmax_forward(input: npt.NDArray[np.float32])->npt.NDArray[np.float32]:
    exp_values = np.exp(input - np.max(input, axis=1, keepdims=True))
    probabilities = exp_values / np.sum(exp_values, axis=1,keepdims=True)
    return probabilities