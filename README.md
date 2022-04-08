Insect classification model made using pytorch

# INTRO
This is my first model which is actually the result of my experience in forestry and completed a course in the field of artificial intelligence.
The project is just a basis for creating a much bigger model that would be actually useful for those unexperienced in entomology. 
Creating my first model was a big deal to me but collecting insect images was strenuous but I got help from Faculty of Forestry in Zagreb and google.

During this project I learned a lot what is going on "under the hood" when model is using training images and setting up its weights in order to be able
to recognize given object, how to use image augmentation in order to expand my dataset, plot images and confusion matrix using matplotlib and 
scikit-learn or using tensorboard to track model's curve to tell whether model is overfitting or underfitting.

It's just a beginning :D

## Project Description:
 - this is a small and demonstrative project that classifies 12 different insects and returns their latin names
 - those insects are: Adalia bipunctata, Calliteara pudibunda, Cerambyx cerdo, Gryllotalpa gryllotalpa, Lucanus cervus, Mantis religiosa, Melolontha melolontha, Phyrrochorus apterus, Rhaphigaster nebulosa, Sesia apiformis, Tettigonia viridissima, Xylocopa violacea
 - image classification is done by using `torch 1.10.2`, `matplotlib 3.5.1` for visualization and `scikit-learn 1.0.2` for making a confusion matrix
 - model was fed with 5200 images of 12 different insects splited in 3 folders: training, validation and test
 - final model was trained using pretrained resnet18 which showed high accuracy on test images >94% after just 4 epochs
 - I have also tried model from https://github.com/rwightman/pytorch-image-models but built-in resnet18 did its job

to run the model:
 - clone the repository
 - install `requirements.txt`
 - run `pytorch_insect_classification_model.ipynb`
 
 
![results matplotlib](https://user-images.githubusercontent.com/89583742/161552413-ddb8f95c-5269-4dbb-9ff2-d4b3b277215a.png)
![confusion_matrix](https://user-images.githubusercontent.com/89583742/161552455-6b93fc1c-bc71-45a7-ae16-f0f643652d4d.png)
![successfully returned ping](https://user-images.githubusercontent.com/89583742/161728619-eb8bc9f1-ae12-4c6f-bfc1-9eadab20139e.jpg)


## FRONTEND part of the project

to install frontend:
 - install NodeJS and NPM
 - install dependencies in frontend folder `cd Desktop/Insects/frontend` by typing `npm install --from-lock-json` and then `npm audit fix`
 - copy and rename `.env.example` to `.env` and change REACT_APP_API_URL to API URL if needed

to run frontend:
 - first run `fast.py` and `model.py`
 - go to frontend folder in cmd, e.g. C:\Users\User\Desktop\torch_model\frontend>
 - run the frontend by typing `npm run start` in cmd
 
![Screenshot](https://user-images.githubusercontent.com/89583742/161758722-7c66f494-c27d-4f99-a1bd-1d9c8e5eef51.jpg)

<!--
<img src="https://user-images.githubusercontent.com/89583742/161758722-7c66f494-c27d-4f99-a1bd-1d9c8e5eef51.jpg" width=250px />
-->

