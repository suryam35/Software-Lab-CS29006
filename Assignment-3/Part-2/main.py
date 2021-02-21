#Imports
from torch_package import ObjectDetectionModel
from torch_package import Dataset
from torch_package import plot_boxes
from torch_package import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image

def experiment(annotation_file, detector, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        detector: The object detector
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    '''

    #Create the instance of the dataset.
    data = Dataset(annotation_file , transforms)

    #Iterate over all data items.
    # image = Image.open('./data/imgs/2.jpg')
    # im = np.array(image) 
    # print(im.shape)
    # blur = RotateImage(45)
    # im = blur(im)
    # img = Image.fromarray(im)
    # img.save('rotate.jpg')
    # im = im/255.0
    # im = np.transpose(im,(2,0,1))
    # print(im.shape)
    # pred_boxes , pred_class , pred_score = detector(im) 
    # # print("pred_boxes : " , pred_boxes , len(pred_boxes))
    # # print("pred_clas : " , pred_class , len(pred_class))
    # # print("pred_score : " , pred_score , len(pred_score)) 
    # plot_boxes(im,pred_boxes,pred_class,'./output/crop.jpg')
    # image.save('saved.jpg')   

    #Get the predictions from the detector.
    names = ['normal','horizontal_flip' , 'blur' , '2Xrescaled' , '0.5Xrescaled' , '90rotate' , '45rotate']
    for i in range(len(data)):
        images , annotation_list = data[i]
        if i == 0:
            count = 0
            for img in images:
                img = img/255.0
                img = np.transpose(img,(2,0,1))
                pred_boxes,pred_class,pred_score = detector(img)
                plot_boxes(img , pred_boxes , pred_class , outputs + "/0_" + names[count]+".jpg")
                count = count+1
        else:
            img = images[0]
            img = img/255.0
            img = np.transpose(img , (2,0,1))
            pred_boxes,pred_class,pred_score = detector(img)
            plot_boxes(img , pred_boxes , pred_class , outputs + "/" + str(i) + ".jpg")


    #Draw the boxes on the image and save them.


    #Do the required analysis experiments.
    


def main():
    detector = ObjectDetectionModel()
    experiment('./data/annotations.jsonl', detector, [FlipImage(),BlurImage(1),RescaleImage(956),RescaleImage(239),RotateImage(-90),RotateImage(45)], './output') # Sample arguments to call experiment()



if __name__ == '__main__':
    main()