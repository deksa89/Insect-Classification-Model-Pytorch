Insect classification model made using pytorch

INTRO
This is my first model which is actually the result of my experience in forestry and completed a course in the field of artificial intelligence.
The project is just a basis for creating a much bigger model that would be actually useful for those unexperienced in entomology. 
Creating the model wasn't a big deal as much as collecting insect images which I got help from Faculty of Forestry in Zagreb.

During this project I learned a lot what is going on "under the hood" when model is using training images and setting up its weights in order to be able
to recognize given insect, how to use image augmentation in order to expand my dataset, plot images and confusion matrix using matplotlib and 
scikit-learn or using tensorboard to track model's curve to tell whether model is overfitting or underfitting.

It's just a beginning :D

Project Description:
 - this is a small and demonstrative project that classifies 12 different insects and returns their latin names
 - image classification is done by using torch 1.10.2, matplotlib 3.5.1 for visualization and scikit-learn 1.0.2 for making a confusion matrix
 - project itself was fed with 5200 images of 12 different insects splited in 3 folders: training, validation and test
 - final model was trained using resnet18 which showed high accuracy on test images >94%
 
 



![results matplotlib](https://user-images.githubusercontent.com/89583742/161552413-ddb8f95c-5269-4dbb-9ff2-d4b3b277215a.png)
![confusion_matrix](https://user-images.githubusercontent.com/89583742/161552455-6b93fc1c-bc71-45a7-ae16-f0f643652d4d.png)
![successfully returned ping](https://user-images.githubusercontent.com/89583742/161728619-eb8bc9f1-ae12-4c6f-bfc1-9eadab20139e.jpg)
