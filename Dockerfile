#use an official light weight python image

FROM python:3.10-slim

#set a working directory inside the container
WORKDIR /app

# Copy ONLY the requirements file first
COPY requirements.txt .

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt


#Now, copy the rest of your application code
#(app.py, model.pkl, scaling.pkl, templates folder, etc.)
COPY . .

#Expose ports
EXPOSE 5000

#Run Flask app by defualt
CMD [ "python","app.py" ]
