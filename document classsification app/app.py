import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from flask import Flask, render_template, jsonify, url_for, request, redirect
import pickle
import pytesseract
from PIL import Image
import os
from pathlib import Path
from nltk import word_tokenize, pos_tag, ne_chunk

import nltk
print('NTLK version: %s' % nltk.__version__)


app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

#
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        comment = request.form['comment']

        f.save(f.filename)

        classes = ["School_ID", "Letter", "Memo"]

        extracted_text = pytesseract.image_to_string(Image.open(f.filename))
        extracted_text_class = model.predict([extracted_text])
        extracted_class = classes[extracted_text_class[0]]
        print(extracted_text)
        print(extracted_class)

        def fn_preprocess(art):
            art = nltk.word_tokenize(art)
            art = nltk.pos_tag(art)
            return art

        art_processed = fn_preprocess(extracted_text)

        grammar = r"""
            NP: {<DT|PP\$>?<JJ>*<NN>}   
            {<NNP>+}                
        """
        cp = nltk.RegexpParser(grammar)
        result = cp.parse(art_processed)

        terms = []
        for e in result:
            if isinstance(e, tuple):
                terms.append([e[0]])
            else:
                terms.append([w for w, t in e])

        returnData = {
            "fileName": f.filename,
            "filePhysicalLocation": comment,
            "class": extracted_class,
            "keywords":terms
        }

        return render_template('home.html', prediction=returnData)


if __name__ == '__main__':
    app.run(debug=True)