# Document OCR

This is a project that deals with scanned documents. It aims to classify scanned documents, read text on the document and generate inferences.

## 1. Abstract

Many organizations process registration and application forms such as universities during the intake of new students, or government ministries and private entities during procurement processes. They usually require supporting documents along with the various applications such as driving licences, certificates, passports etc. Manpower must be spent by organizations to process these application forms and get useful information from them.

This project aims to use computer vision and deep learning methodologies to give our registration and application systems the ability to

i. Recognize and classify images. Specifically documents like ID cards and certificates using convolutional neural networks
ii. Extract and identify information from these documents such as the name, certificate number, scores etc.

## 2. What I plan to do

i. Do image classification first, using transfer learning on an already trained network. Keras would be majorly used in this project, for deep learning and pre-processing, scikit learn for some machine learning and calculation of accuracy, as well as other standard python libraries like pandas, numpy and Pillow.
ii. The classified document would be fed into an optical character recognition(OCR) software called tesseract to get the text from the documents.
iii. Store the extracted information in an orderly manner in google firebase.

### 2.1 Note.

I realized that CNN may not be the best way to go, I have seen some implementations with Deep-CNN and, it also makes sense to use some form of NLU to better ensure that the classification is done more effectively. This are things which I plan to try out as soon as I first finish what I have in mind.

### 2.2 Other uses

The project can also be used to aid in digitization of paper records. We have problem of digital data in Nigeria, but we actually have a lot of paper data. So I plan to explore this too

## 3. Implementation

I first tried to get scanned documents from friends, I guessed that at least I could start with litle amount of data, when I have a proof of concept, I would approach big organizations liek universities, but everyone was reluctant to give their data. So i went looking for data, and I found the tobacco_3842 data set which I would be using to prototype.
