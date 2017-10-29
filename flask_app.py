#!/usr/bin/env python
import os
import pandas as pd
from flask import Flask, request,render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from pandas.io.common import EmptyDataError



# create app
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/home/Firiyuu77/mysite/uploads'
app.config['ALLOWED_EXTENSIONS'] = set(['csv','xlsx'])

def allowed_file(filename, filename1, filename3):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def main():
    return render_template('index.html')

# Route that will process the file upload
@app.route('/upload', methods=['GET','POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    file1 = request.files['file1']
    file2 = request.files['file2']
    # Check if the file is one of the allowed types/extensions
    if file and file1 and allowed_file(file.filename, file1.filename, file2.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)

        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
        file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))

        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file',
                                filename=filename, filename1=filename1, filename2=filename2))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an csv , that csv  is going to be returned after the eupload then evaluation.
@app.route('/uploads/evaluation/<filename>/<filename1>/<filename2>', methods=['GET','POST'])
def uploaded_file(filename, filename1, filename2):
    if __name__ == '__main__':
      app.run(
      host="0.0.0.0",
      port=int("80"),
      debug=True
         )


    pathto_csv = os.path.join('mysite/uploads/',filename)
    pathto_csv1 = os.path.join('mysite/uploads/',filename1)
    pathto_resultxls = os.path.join('mysite/uploads/',filename2)
    #filename = os.path.abspath(dire)
    #filename1 = os.path.abspath(dire)



    if request.method == 'GET':
    # show html form

       try:
          data_df = pd.read_csv(pathto_csv, delimiter=',', encoding="utf-8-sig" )
          data_df1 = pd.read_csv(pathto_csv1, delimiter=',', encoding="utf-8-sig")
          data_dfres = pd.read_csv(pathto_resultxls, delimiter=',', encoding="utf-8-sig")

          for i, row in data_df.iterrows() :
             equityC = data_df.iloc[i]['OWNER 1 FIRST NAME']
             data_dfres.set_value([i], ['OWNER 1 FIRST NAME'], equityC)
             equityB = data_df.iloc[i]['OWNER 1 LAST NAME']
             data_dfres.set_value([i], ['OWNER 1 LAST NAME'], equityB)
             equityH = data_df.iloc[i]['OWNER 2 FIRST NAME']
             data_dfres.set_value([i], ['OWNER 2 FIRST NAME'], equityH)
             equityG = data_df.iloc[i]['OWNER 2 LAST NAME']
             data_dfres.set_value([i], ['OWNER 2 LAST NAME'], equityG)
             equityAK = data_df.iloc[i]['EQUITY (%)']
             data_dfres.set_value([i], ['EQUITY (%)'], equityAK)
             equityT = data_df.iloc[i]['PROPERTY ADDRESS']
             data_dfres.set_value([i], ['PROPERTY ADDRESS'], equityT)
             equityAD = data_df.iloc[i]['PROPERTY CITY']
             data_dfres.set_value([i], ['PROPERTY CITY'], equityAD)
             equityAE = data_df.iloc[i]['PROPERTY STATE']
             data_dfres.set_value([i], ['PROPERTY STATE'], equityAE)
             equityAF = data_df.iloc[i]['PROPERTY ZIP CODE']
             data_dfres.set_value([i], ['PROPERTY ZIP CODE'], equityAF)
             equityL = data_df.iloc[i]['MAIL ADDRESS']
             data_dfres.set_value([i], ['MAIL ADDRESS'], equityL)
             equityQ = data_df.iloc[i]['MAIL CITY']
             data_dfres.set_value([i], ['MAIL CITY'], equityQ)
             equityN = data_df.iloc[i]['MAIL STATE']
             data_dfres.set_value([i], ['MAIL STATE'], equityN)


             data_dfres.to_csv(pathto_resultxls)

          for i, row in data_df1.iterrows() :
             vortexName = data_df1.iloc[i]['Name']
             data_dfres.set_value([i], ['Name'], vortexName)
             vortexName2 = data_df1.iloc[i]['Name 2']
             data_dfres.set_value([i], ['Name 2'], vortexName2)
             vortexPhone = data_df1.iloc[i]['Phone']
             data_dfres.set_value([i], ['Phone'], vortexPhone)
             vortexPhone2 = data_df1.iloc[i]['Phone 2']
             data_dfres.set_value([i], ['Phone 2'], vortexPhone2)
             vortexPhone3 = data_df1.iloc[i]['Phone 3']
             data_dfres.set_value([i], ['Phone 3'], vortexPhone3)
             vortexPhone4 = data_df1.iloc[i]['Phone 4']
             data_dfres.set_value([i], ['Phone 4'], vortexPhone4)
             vortexPhone5 = data_df1.iloc[i]['Phone 5']
             data_dfres.set_value([i], ['Phone 5'], vortexPhone5)
             vortexPhone6 = data_df1.iloc[i]['Phone 6']
             data_dfres.set_value([i], ['Phone 6'], vortexPhone6)
             equityAP = data_df1.iloc[i]['Bedrooms']
             data_dfres.set_value([i], ['Bedrooms'], equityAP)

             equityAQ = data_df1.iloc[i]['Bathrooms']
             data_dfres.set_value([i], ['Bathrooms'], equityAQ)

             equityAS = data_df1.iloc[i]['Square Footage']
             data_dfres.set_value([i], ['Square Footage'], equityAS)
             equityAT = data_df1.iloc[i]['Year Built']
             data_dfres.set_value([i], ['Year Built'], equityAT)
             equityBK = data_df1.iloc[i]['Folders']
             data_dfres.set_value([i], ['Folders'], equityBK)

             data_dfres.to_csv(pathto_resultxls)



       except EmptyDataError:
          pass


       path = os.path.join(app.root_path, 'uploads')
       assert os.path.exists (path)
       return send_from_directory (path, filename2)

    else:
       return render_template('success.html')







