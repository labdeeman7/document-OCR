# Document OCR

This is a project that deals with scanned documents. It aims to classify scanned documents, read text on the document and generate inferences.

## 1. Abstract
I have had problems retrieving my certificates back when I go back to my old schools, so I said why not build something that helps with that. 
Many organizations process registration and application forms such as universities during the intake of new students, or government ministries and private entities during procurement processes. They usually require supporting documents along with the various applications such as driving licences, certificates, passports etc. Manpower must be spent by organizations to process these application forms and get useful information from them.

This project aims to use computer vision and machine learning methodologies to give our registration and application systems the ability to

i. Recognize and classify images. Specifically documents like ID cards and certificates
ii. Extract and identify information from these documents such as the name, certificate number, scores etc.

## 2. What I plan to do

i.  The pictures of the documents would be fed into an optical character recognition(OCR) software called tesseract to get the text from the documents.
ii. Text gotten from the picture would be used to classify the documents using SVMs. Since the documents are generally things like certificates and ID cards, with classes having very similar features, I expect a very good classification
ii. Store the extracted information in an orderly manner.

### 2.1 Note.
Need to figure out how to get tesseract OCR to work better or scrap it entirely as it is not recognizing text that are not in standard fonts or with another colour

### 2.2 Other uses

The project can also be used to aid in digitization of paper records. We have problem of digital data in Nigeria, but we actually have a lot of paper data. So I plan to explore this too

## 3. Implementation
I made fake ID cards and certificates and plan to work with that, till maybe I gert something real.
