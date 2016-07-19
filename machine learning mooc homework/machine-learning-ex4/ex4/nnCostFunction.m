function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%



% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

h1 = sigmoid([ones(m, 1) X] * Theta1');
h2 = sigmoid([ones(m, 1) h1] * Theta2');


y_vec = zeros(size(h2));

for inval = [1:length(y);y']
      y_vec(inval(1),inval(2))=1;
endfor

J = sum(sum(-y_vec.*log(h2)-(1-y_vec).*log(1-h2)))/m + (sum(sum(Theta1(:,2:end).^2))+sum(sum(Theta2(:,2:end).^2)))*lambda/(2*m);







% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];

DELTA1 = zeros(size(Theta1_grad));
DELTA2 = zeros(size(Theta2_grad));

for t=1:m
%Step one
  a_1 = [1,X(t,:)];
  z_2 = a_1 * Theta1';
  a_2 = [1,sigmoid(z_2)];
  z_3 = a_2 * Theta2';
  a_3 = sigmoid(z_3);
  
%Step two
  yvec = zeros(size(h2,2),1);
  yvec(y(t))=1;

  delta_3 = a_3-yvec';

%Step three
  delta_2 = (delta_3*Theta2)(2:end).*sigmoidGradient(z_2);
  
%Step four
  DELTA1 = DELTA1 + delta_2'*a_1;
  DELTA2 = DELTA2 + delta_3'*a_2;

endfor

tempTheta1 = Theta1;
tempTheta1(:,1)=0;
tempTheta2 = Theta2;
tempTheta2(:,1)=0;

Theta1_grad = DELTA1/m+tempTheta1*lambda/m;
Theta2_grad = DELTA2/m+tempTheta2*lambda/m;


grad = [Theta1_grad(:) ; Theta2_grad(:)];
end

